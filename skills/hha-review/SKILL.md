---
name: hha-review
description: Review a stable project checkpoint against its README and SPEC without editing. Use in a fresh session or read-only subagent to find requirement gaps, logic bugs, state-boundary failures, misleading UI behavior and unsupported completion claims.
---

# Read-only project review

Read [AGENTS.md](../../AGENTS.md) and the target README, SPEC, generated verification skill and relevant source. You are a reviewer. Do not edit files, update the plan, commit, install dependencies or push. If you helped write the reviewed code or inherited its authoring conversation, label the result same-context rather than independent.

## Fix the review target

Prefer a local checkpoint commit. Record its SHA and inspect `git status`, the diff from the baseline or prior checkpoint, and changed files. If there is no commit, list the exact files and record that the target is an unfrozen working tree. A moving working tree invalidates the review; ask the writer to pause before retrying.

## Review from requirements to behavior

Build a small coverage map from required README items and SPEC acceptance IDs to actual implementation and verification evidence. Focus on observable defects:

- a required path absent, incomplete or implemented only in UI copy;
- incorrect state transitions, authorization/exposure boundaries or persistence;
- external failures that crash unrelated paths or masquerade as success;
- input matching, filtering, fallback or feedback behavior that contradicts the requirement;
- tests that exercise a proxy instead of the user's path, or evidence that does not prove the claimed criterion;
- UI states or copy that imply saved, published, generated or personalized behavior the code did not complete.

Trace one important request through its real input, server validation, handler, data source and query conditions, processing, response and consumer where those layers exist. Check that the evidence identifies the intended instance and distinguishes real data or services from fixtures and mocks. Treat comments, commit messages, SPEC checkboxes and the author's completion report as claims. Run existing relevant checks when permitted; do not create a different easy test to replace a failing required check. For UI work, read [hha-ui](../hha-ui/SKILL.md). Visual quality needs the rendered surface or allowed screenshots; code-only review must say it did not verify rendering.

For an integrated result, inspect shared contracts and rerun the core path on the combined checkpoint. A writer's isolated PASS or a conflict-free merge does not prove integration. Review invalid input, data changes, restart behavior or concurrent writes only when they are required or plausible risks for this project; report unsupported guarantees instead of demanding unnecessary architecture.

Avoid speculative architecture advice, broad refactors and style nits without user impact. Verify a suspected issue against source or a reproducible run before calling it confirmed. If evidence is unavailable, label it inferred and state the missing check.

## Return one review record

Start with `PASS`, `ISSUES`, or `BLOCKED`, followed by `independent` or `same-context` and the reviewed SHA/file state. List findings by impact, each with requirement ID, file/line or runtime evidence, observed behavior, expected behavior and the smallest useful reproduction. Then list checks actually run and remaining unverified areas. Do not modify the project.
