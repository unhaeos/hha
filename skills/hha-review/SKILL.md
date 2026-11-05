---
name: hha-review
description: Execute a project verifier on a stable checkpoint, then review runtime evidence and code against README and SPEC. Use in a fresh session or source-read-only subagent to find reproducible failures, requirement gaps and unsupported completion claims.
---

# Read-only project review

Read [AGENTS.md](../../AGENTS.md) and the target README, SPEC, generated verification skill and relevant source. You are a verifier first and a code reviewer second. Do not edit product source, SPEC or verifier procedures; do not change dependencies, commit or push. You may create only the verifier's designated evidence, scratch state and run-owned processes or containers, then clean them as documented. If you helped write the reviewed code or inherited its authoring conversation, label the result same-context rather than independent.

## Fix the review target

Prefer a local checkpoint commit. Record its SHA and inspect `git status`, the diff from the baseline or prior checkpoint, and changed files. If there is no commit, list the exact files and record that the target is an unfrozen working tree. A moving working tree invalidates the review; ask the writer to pause before retrying.

## Execute before judging

Run the generated verifier against the exact checkpoint before relying on code inspection. Follow its launch, doctor, static, drive, evidence and cleanup procedures. Use the project's declared process, container or compose path when it exists and the environment permits it; do not add containerization or change the stack merely for review. Exercise an actual public API, CLI or permitted UI path, record exit status and output, and inspect relevant state or side effects. For selected failures, reproduce the condition and confirm both the visible result and what did not change.

Use current evidence from the same code, dependency, input and environment identity instead of repeating every expensive check. Prioritize changed acceptance IDs, shared contracts touched by the diff, the core integrated path and any prior failure being claimed as fixed. Before a final PASS, confirm every required criterion has current evidence; during an intermediate review, list the intentionally deferred coverage rather than blocking useful feedback.

Static analysis, lint, typecheck, build and unit tests are useful lanes, but none alone proves runtime behavior. An open port does not prove readiness, and a mocked integration does not prove the intended service. If required execution is unavailable, return BLOCKED or leave the criterion unverified rather than replacing it with an LLM opinion.

## Review from requirements to behavior

Build a small coverage map from required README items and SPEC acceptance IDs to actual implementation and verification evidence. Focus on observable defects:

- a required path absent, incomplete or implemented only in UI copy;
- incorrect state transitions, authorization/exposure boundaries or persistence;
- external failures that crash unrelated paths or masquerade as success;
- input matching, filtering, fallback or feedback behavior that contradicts the requirement;
- tests that exercise a proxy instead of the user's path, or evidence that does not prove the claimed criterion;
- UI states or copy that imply saved, published, generated or personalized behavior the code did not complete.

Also flag basic service breakage in the required path even when the README does not enumerate it: an undocumented or broken start path, unhandled runtime failure, invalid input that corrupts state, or a failed required dependency presented as success. Do not turn this into a production-readiness or scalability audit unless the task asks for one.

Check that material product and architecture decisions cite an actual task rule, responsible-person answer, observed data, user choice or clearly labeled assumption. Confirm that implementation still follows those decisions and that an unresolved README ambiguity affecting acceptance was not silently treated as agreement. Do not reopen a documented tradeoff merely because another design is possible; report it only when its basis is false, stale or contradicted by requirements or evidence.

Trace one important request through its real input, server validation, handler, data source and query conditions, processing, response and consumer where those layers exist. Check that the evidence identifies the intended instance and distinguishes real data or services from fixtures and mocks. Treat comments, commit messages, SPEC checkboxes and the author's completion report as claims. Do not create a different easy test to replace a failing required check. Use source inspection to explain executed behavior and find untested boundaries, not to substitute for execution. For UI work, read [hha-ui](../hha-ui/SKILL.md). Visual quality needs the rendered surface or allowed screenshots; code-only review must say it did not verify rendering.

For an integrated result, inspect shared contracts and rerun the core path on the combined checkpoint. A writer's isolated PASS or a conflict-free merge does not prove integration. For selected failure cases, check the visible error and confirm prohibited side effects or partial writes did not occur. Review invalid input, data changes, restart behavior or concurrent writes only when they are required or plausible risks for this project; report unsupported guarantees instead of demanding unnecessary architecture.

Avoid speculative architecture advice, broad refactors and style nits without user impact. Verify a suspected issue against source or a reproducible run before calling it confirmed. If evidence is unavailable, label it inferred and state the missing check.

## Return one review record

Start with `PASS`, `ISSUES`, or `BLOCKED`, followed by `independent` or `same-context` and the reviewed SHA/file state. List findings by impact, each with requirement ID, file/line or runtime evidence, observed behavior, expected behavior and the smallest useful reproduction. Then list checks actually run and remaining unverified areas. Do not modify the project.
