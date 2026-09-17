"""Artifact regressions use isolated copies and never run agents or ERP tools."""

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_agent_artifacts import validate_agent_artifacts

ROOT = Path(__file__).resolve().parents[1]


class AgentArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in (".agents/skills", ".codex/agents", "workflows"):
            shutil.copytree(ROOT / name, self.root / name)

    def test_current_contract(self):
        validate_agent_artifacts(self.root)

    def test_duplicate_legacy_layout_is_rejected(self):
        for name in ("skills", "agents"):
            with self.subTest(directory=name):
                path = self.root / name
                path.mkdir()
                with self.assertRaisesRegex(ValueError, "Legacy consumer directory"):
                    validate_agent_artifacts(self.root)
                path.rmdir()

    def test_role_markdown_is_not_an_agent_registration(self):
        agent = self.root / ".codex/agents/operator.toml"
        agent.rename(agent.with_suffix(".md"))
        with self.assertRaisesRegex(ValueError, "Invalid custom-agent path"):
            validate_agent_artifacts(self.root)

    def test_mismatched_agent_name_is_rejected(self):
        path = self.root / ".codex/agents/operator.toml"
        path.write_text(path.read_text().replace('name = "operator"', 'name = "different"'))
        with self.assertRaisesRegex(ValueError, "Custom-agent name mismatch"):
            validate_agent_artifacts(self.root)

    def test_empty_agent_instructions_are_rejected(self):
        path = self.root / ".codex/agents/operator.toml"
        path.write_text('name = "operator"\ndescription = "Role"\ndeveloper_instructions = ""\n')
        with self.assertRaisesRegex(ValueError, "Missing agent developer_instructions"):
            validate_agent_artifacts(self.root)

    def test_flat_workflow_is_rejected(self):
        path = self.root / "workflows/legacy.md"
        path.write_text("# Old workflow\n")
        with self.assertRaisesRegex(ValueError, "Invalid workflow directory"):
            validate_agent_artifacts(self.root)

    def test_unresolved_workflow_dependency_is_rejected(self):
        path = self.root / "workflows/versat-operation/workflow.md"
        path.write_text(
            path.read_text().replace(".agents/skills/versat-mcp/", ".agents/skills/missing/")
        )
        with self.assertRaisesRegex(ValueError, "Unresolved workflow Skill"):
            validate_agent_artifacts(self.root)

    def test_missing_recovery_contract_is_rejected(self):
        path = self.root / "workflows/versat-operation/workflow.md"
        path.write_text(path.read_text().split("## Failure and recovery")[0])
        with self.assertRaisesRegex(ValueError, "Missing workflow section: Failure and recovery"):
            validate_agent_artifacts(self.root)

    def test_missing_skill_frontmatter_is_rejected(self):
        path = self.root / ".agents/skills/versat-mcp/SKILL.md"
        path.write_text("# Missing frontmatter\n")
        with self.assertRaisesRegex(ValueError, "Invalid frontmatter"):
            validate_agent_artifacts(self.root)
