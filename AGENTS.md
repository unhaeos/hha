# hha agent instructions

Paths in this file are relative to this harness directory; project output paths are relative to the target project. Identify both roots before writing. The harness is reference material, not the application to build. When the user asks to maintain hha itself, edit the harness rather than starting the application workflow below; publishing is allowed only when the user requests it.

## Boundaries

- Follow the target's instructions and environment rules first. Preserve existing files and user changes. Installation may append a small reference to the project's AGENTS.md; never replace existing project instructions.
- Default to one supplied agent session. Do not install other agents, update the agent or configure models. Additional sessions require confirmed environment support and permission. Git, commits and worktrees are not prerequisites for file-based implementation or verification.
- Keep project data, generated skills and evidence in the permitted workspace. No push, PR, merge, external telemetry, personal credentials, or automated submission. Public dependency downloads must still follow the environment's rules.
- Do not use browser/computer automation, screenshots, external services or additional AI sessions unless the environment explicitly permits that capability. An unavailable proof stays unverified; HTTP or source checks do not establish visual correctness.
- Stop when AI assistance is no longer permitted. These instructions concern implementation work only.

## Work loop

1. Read [hha-plan](skills/hha-plan/SKILL.md). Inspect the supplied requirements and actual files; an empty app is valid. Create or update a small SPEC in the target project.
2. For screen work, also read [hha-ui](skills/hha-ui/SKILL.md) and capture the applicable choices in the SPEC. Skip it for non-UI tasks.
   For user-visible wording, including a single button, error, label, README paragraph or result summary, read [hha-writing](skills/hha-writing/SKILL.md). Do not restrict this skill to long-form writing.
3. Read [hha-create-verification](skills/hha-create-verification/SKILL.md). Generate a requirement-based verifier, initially a draft if the app does not run yet.
4. If implementation is requested, build the smallest complete user path. Resolve the draft's executable details from actual code, then run the relevant verification. Use [hha-debug](skills/hha-debug/SKILL.md) for failures.
5. Update implementation and verification separately in SPEC. Keep evidence, decisions and the next action concise. After changes, mark affected earlier evidence stale until rerun; unrelated evidence need not be repeated.
   Inspect the relevant code against requirements before declaring completion. Git diff is optional: without Git, use the target file list and current source. This same-session inspection is not an independent code review. No fresh-review launcher or parallel orchestrator is bundled.
6. Before finishing, compare every required criterion with its evidence, check the documented run command and required output paths, and report remaining gaps. Do not auto-submit. See [finish checklist](templates/finish.md).

While implementation assistance is permitted, explain important choices as they occur: why this approach, which real files/functions carry the input to the output, how failures propagate, and which observation confirmed it. Keep these notes in SPEC rather than generating rehearsed assessment answers. Match explanations to actual code and label simulation or fallback paths. Do not extend this assistance into a stage where AI is prohibited.

Do not pause for approval at every stage of an already authorized implementation. Ask only about material unresolved choices; continue work unaffected by those answers. A planning-only request ends with the plan, not implementation.

## Plain wording

Use concrete subjects, actions and outcomes, even for one-line UI copy. Avoid empty metaphors such as "여기서 갈린다", "무엇 위에 서 있다" or "가능성을 열다", rhetorical "X가 아니라 Y" framing, inflated slogans and middle-dot keyword chains. Preserve necessary technical distinctions and literal user content. State what happened and what the user can do; never invent an outcome to make prose sound confident.

## Verification evidence

Use PASS, FAIL, NOT RUN, or BLOCKED per check, with the actual command or procedure, expected result, observed result, and relevant file/runtime version. PASS requires observed evidence for that criterion. A generated verifier's smoke check proves only that procedure, not the whole app. Do not claim independent verification from the same session.

If a deadline is known, reserve time for verification and required deliverables. When time becomes short, prioritize required missing behavior and reproducible failures. Do not add architecture or polish that displaces those items.
