# Git Standard

## Governance

- The default branch MUST be protected.
- Material changes MUST enter through Pull Requests.
- Required checks MUST pass before merge.
- Commits MUST use concise English descriptions and MUST NOT include secrets.
- Generated changes MUST remain reviewable; large mechanical changes SHOULD be isolated.
- Policy and Skill changes MUST identify reviewers through CODEOWNERS or equivalent organization rules.
- Force pushes to protected branches MUST be disabled.

## Story branch names

New branches associated with a Shortcut Story MUST use:

```text
<shortcut-id>_<story-type>_<description>
```

- `shortcut-id` is the actual numeric Story ID, without `ch` or `#`.
- `story-type` MUST match the Shortcut Story type: `bug`, `feature` or `chore`.
- `description` MUST briefly describe the Story objective in English, with words separated by underscores. Prefer lowercase words.

Examples (illustrative IDs):

```text
305319_bug_score_calculation
305400_feature_date_filter
305500_chore_update_dependencies
```

This format applies to Story work branches, not default, integration or release branches. Work with no associated Story MAY retain the repository's existing branch convention. Contributors MUST NOT invent a Story ID or infer its type from incomplete information; record missing Story context in the proposal or PR and resolve it before presenting the work as Story-linked.

## Commit messages

Commits associated with a Shortcut Story MUST begin with its marker followed by a typed description:

```text
[ch<shortcut-id>] <type>: <description>
```

The initial vocabulary and Story mapping are:

| Shortcut Story type | Commit type | Change |
|---|---|---|
| Feature (`feature`) | `feat` | New functionality |
| Bug (`bug`) | `fix` | Bug correction |
| Chore (`chore`) | `chore` | Maintenance |

Use the type that describes the logical change. The branch type continues to describe the Story; it is not renamed for an individual maintenance commit within a feature Story. Documentation, tests, refactoring and dependency maintenance can use `chore` during initial adoption. Additional types such as `refactor`, `test`, `docs`, `perf`, `revert` and `build` are deferred to a future policy revision.

Descriptions MUST be concise, specific and English, following the [Language Standard](language.md). Start with a base-form action verb, such as `fix`, `add` or `update`, rather than past tense, third-person narration or vague text such as `change`.

```text
[ch305319] fix: prevent division by zero in liquidity calculation
[ch305400] feat: add date filter
[ch305500] chore: update dependencies
```

Commits with no associated Story MUST use the same typed format without a fabricated marker, for example `chore: update Git documentation`.

### Optional scope and body

A scope is optional, never a prerequisite for committing. Prefer the simple form above; when useful, a scope MAY follow the type in parentheses, for example `[ch305319] fix(credit): prevent division by zero`.

A body MAY explain the reason, behavior or validation of the change. Separate it from the subject with a blank line and write it in English:

```text
[ch305319] fix: prevent division by zero in liquidity calculation

The calculation failed when the available balance was zero.
Add a guard and cover the zero-balance case.
```

When a change is breaking, identify it using Conventional Commits `!` syntax or a `BREAKING CHANGE:` footer. Scope and body remain optional; these markers do not introduce another commit type.

## Story, Task, commit and Pull Request traceability

- A Story represents the functional work; a Task is part of that work; a commit is a logical code or repository change; a PR delivers the work for review.
- A Story MAY contain multiple Tasks and multiple commits. There MUST NOT be a mandatory one-Task-to-one-commit mapping.
- Each commit MUST represent a logical change related to its associated Story, retaining the Story marker when applicable.
- A Story-linked PR MUST identify the Story and provide its link. Internal PR titles and descriptions remain Spanish. For example: `#305319 - Corregir el cálculo de liquidez`.
- When using squash merge, the resulting commit MUST follow the commit convention, including English text and the Story marker when applicable. Do not reuse a Spanish PR title unchanged as the squash subject.

## Compatibility and gradual adoption

The typed portion follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The leading `[ch<shortcut-id>]` marker is a Versat extension preserving the supplied Shortcut convention: the complete subject is not strict Conventional Commits syntax, which starts with the type. Before enabling commit linting, changelog generation or release inference, tooling MUST explicitly recognize the marker or remove it from parser input while preserving it in Git history and traceability output.

The branch pattern and a bare `#ID` in a PR title do not by themselves prove automatic Shortcut association. Verify branch, commit and PR linkage in the configured workspace; preserve the Story URL in the PR for explicit traceability. This policy does not change Shortcut event handlers or claim that their behavior has been tested.

Adopt these rules for new work without rewriting existing history or renaming historical branches. Keep the current delivery lifecycle and merge strategy. Initially, review the convention in PRs; the Harness structural validator does not enforce branch or commit syntax. Automated enforcement and additional commit types require subsequent governed changes.
