"""Validate this consumer's artifact contracts, not native discovery or execution."""

import re
import tomllib
from pathlib import Path

import yaml

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SKILL_PATH = re.compile(r"`(\.agents/skills/[^`\s]+/SKILL\.md)`")
WORKFLOW_SECTIONS = (
    "Purpose and ownership",
    "Trigger, inputs and preconditions",
    "Executor and dependencies",
    "Steps and decisions",
    "Authorization",
    "Results and evidence",
    "Failure and recovery",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_agent_artifacts(root: Path) -> None:
    for legacy in ("skills", "agents"):
        require(not (root / legacy).exists(), f"Legacy consumer directory: {legacy}")
    for directory in (".agents/skills", ".codex/agents", "workflows"):
        require((root / directory).is_dir(), f"Missing artifact directory: {directory}")

    skills = set()
    for directory in (root / ".agents/skills").iterdir():
        require(directory.is_dir(), f"Unexpected Skill artifact: {directory.name}")
        require(bool(NAME.fullmatch(directory.name)), f"Invalid Skill name: {directory.name}")
        path = directory / "SKILL.md"
        require(path.is_file(), f"Missing Skill definition: {directory.name}")
        text = path.read_text()
        parts = text.split("---", 2)
        require(text.startswith("---\n") and len(parts) == 3, f"Invalid frontmatter: {path}")
        metadata = yaml.safe_load(parts[1])
        require(isinstance(metadata, dict), f"Invalid Skill metadata: {path}")
        require(metadata.get("name") == directory.name, f"Skill name mismatch: {path}")
        description = metadata.get("description")
        require(
            isinstance(description, str) and bool(description.strip()),
            f"Missing Skill description: {path}",
        )
        skills.add(path.relative_to(root).as_posix())
    require(bool(skills), "No project Skills")

    agents = list((root / ".codex/agents").iterdir())
    require(bool(agents), "No custom agents")
    for path in agents:
        require(
            path.is_file() and path.suffix == ".toml" and bool(NAME.fullmatch(path.stem)),
            f"Invalid custom-agent path: {path.name}",
        )
        data = tomllib.loads(path.read_text())
        for field in ("name", "description", "developer_instructions"):
            value = data.get(field)
            require(isinstance(value, str) and bool(value.strip()), f"Missing agent {field}")
        require(data["name"] == path.stem, f"Custom-agent name mismatch: {path.name}")

    workflows = list((root / "workflows").iterdir())
    require(bool(workflows), "No operational workflows")
    for directory in workflows:
        require(
            directory.is_dir() and bool(NAME.fullmatch(directory.name)),
            f"Invalid workflow directory: {directory.name}",
        )
        path = directory / "workflow.md"
        require(path.is_file(), f"Missing workflow definition: {directory.name}")
        text = path.read_text()
        parts = re.split(r"^## (.+)\n", text, flags=re.MULTILINE)
        sections = dict(zip(parts[1::2], parts[2::2], strict=True))
        for heading in WORKFLOW_SECTIONS:
            require(bool(sections.get(heading, "").strip()), f"Missing workflow section: {heading}")
        dependencies = set(SKILL_PATH.findall(sections["Executor and dependencies"]))
        require(bool(dependencies), f"No bound local Skill in {path}")
        for dependency in set(SKILL_PATH.findall(text)):
            require(dependency in skills, f"Unresolved workflow Skill: {dependency}")
            require(dependency in dependencies, f"Undeclared workflow Skill: {dependency}")
