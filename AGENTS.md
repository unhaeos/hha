# hha agent instructions

Paths in this file are relative to this harness directory; project output paths are relative to the target project. Identify both roots before writing. The harness is reference material, not the application to build. When the user asks to maintain hha itself, edit the harness rather than starting the application workflow below; publishing is allowed only when the user requests it.

## Boundaries

- Follow the target's instructions and environment rules first. Preserve existing files and user changes. Installation may append a small reference to the project's AGENTS.md; never replace existing project instructions.
- Do not install other agents, update the agent or configure models. Additional sessions require confirmed environment support and permission. Git and commits improve checkpoints but are not prerequisites for file-based implementation or verification.
- Keep project data, generated skills and evidence in the permitted workspace. No push, PR, merge, external telemetry, personal credentials, or automated submission. Public dependency downloads must still follow the environment's rules.
- Do not add an MCP server by default. After reading the task, prefer provided files, APIs and terminal tools. Propose MCP only when a required capability is otherwise missing; identify why it is needed, what project data leaves the workspace, authentication, configuration changes and a no-MCP fallback. Do not connect it while permission or data handling is unclear.
- Do not use browser/computer automation, screenshots, external services or additional AI sessions unless the environment explicitly permits that capability. An unavailable proof stays unverified; HTTP or source checks do not establish visual correctness.
- Stop when AI assistance is no longer permitted. These instructions concern implementation work only.

## Work loop

1. Inspect local Git before editing. If Git works but HEAD does not exist, and local commits are allowed, review the original task files and create one local baseline commit. Stage explicit paths; exclude hha installation files, secrets and unrelated files. Never push. Then read [hha-plan](skills/hha-plan/SKILL.md), inspect the supplied requirements and actual files, and create or update a small SPEC. An empty app is valid.
2. For screen work, also read [hha-ui](skills/hha-ui/SKILL.md) and capture the applicable choices in the SPEC. Skip it for non-UI tasks.
   For user-visible wording, including a single button, error, label, README paragraph or result summary, read [hha-writing](skills/hha-writing/SKILL.md). Do not restrict this skill to long-form writing.
3. Read [hha-create-verification](skills/hha-create-verification/SKILL.md). Generate a requirement-based verifier, initially a draft if the app does not run yet.
4. If implementation is requested, build the smallest complete user path against the intended runtime and data source. A useful default trace is input -> server validation -> data access -> processing -> response -> rendered result, adapted to the project rather than imposed on it. Resolve the draft's executable details from actual code, then run the relevant verification. Use [hha-debug](skills/hha-debug/SKILL.md) for failures.
5. Update implementation and verification separately in SPEC. Keep evidence, decisions and the next action concise. Record material AI proposals only when they affected the work: what was proposed, what was adopted, changed, deferred or rejected, why, and what was actually observed. Do not invent disagreement or unrun evidence. After changes, mark affected earlier evidence stale until rerun; unrelated evidence need not be repeated.
   Make local checkpoint commits at coherent, tested states when Git is available. Inspect the relevant code against requirements before declaring completion. Git diff is optional: without Git, use the target file list and current source.
   When a fresh session or subagent is permitted, give it [hha-review](skills/hha-review/SKILL.md) and a stable checkpoint. During review, the coordinator is the only writer and reviewers are read-only. Do not let two sessions write the same checkout. A same-context inspection is not independent review.
6. Before finishing, compare every required criterion with its evidence, check the documented run command and required output paths, and report remaining gaps. Do not auto-submit. See [finish checklist](templates/finish.md).

While implementation assistance is permitted, explain important choices as they occur: why this approach, which real files/functions carry the input to the output, how failures propagate, and which observation confirmed it. Keep these notes in SPEC rather than generating rehearsed assessment answers. Match explanations to actual code and label simulation or fallback paths. Do not extend this assistance into a stage where AI is prohibited.

Do not pause for approval at every stage of an already authorized implementation. Ask only about material unresolved choices; continue work unaffected by those answers. A planning-only request ends with the plan, not implementation.

## Plain wording

Use concrete subjects, actions and outcomes, even for one-line UI copy. Avoid empty metaphors such as "여기서 갈린다", "무엇 위에 서 있다" or "가능성을 열다", rhetorical "X가 아니라 Y" framing, inflated slogans and middle-dot keyword chains. Preserve necessary technical distinctions and literal user content. State what happened and what the user can do; never invent an outcome to make prose sound confident.

## Verification evidence

Use PASS, FAIL, NOT RUN, or BLOCKED per check, with the actual command or procedure, expected result, observed result, and relevant file/runtime version. PASS requires observed evidence for that criterion. A generated verifier's smoke check proves only that procedure, not the whole app. Do not claim independent verification from the same session.

If a deadline is known, reserve time for verification and required deliverables. When time becomes short, prioritize required missing behavior and reproducible failures. Do not add architecture or polish that displaces those items.

## Multiple sessions

One project checkout is sufficient when one coordinator owns all edits. Fresh sessions or subagents may inspect requirements, code, UI and verification evidence in parallel, but they return findings instead of editing. Pause the writer at a local checkpoint before review so every reviewer sees one stable state. The coordinator validates findings, applies accepted fixes and reruns the exact failed check. Separate worktrees are needed only for intentionally parallel writers; that merge overhead is not part of the default hha workflow.

When parallel writers are explicitly permitted and useful, define the split in SPEC before they edit: baseline commit, owned files or directories, shared API/schema/type contracts, the single owner of shared files, server ports and processes, integration order and each writer's required check. The integration owner manages dependency files, migrations, data initialization and server lifecycle unless SPEC assigns another single owner. Writers use separate worktrees, do not change another writer's scope silently, and hand back their commit, changed files, contract changes, checks run and remaining gaps. Integrate one checkpoint at a time and rerun the smallest real end-to-end path on the combined state; a clean cherry-pick is not verification. Never stop a process by generic name or reinitialize shared data without identifying ownership and impact.
