---
name: hha-create-verification
description: Generate or refresh a project-specific verification skill from the task README, checklist SPEC and actual code. Create an honest draft for an empty app, then validate executable procedures once it runs.
---

# Create project verification

Read [working guidance](../../AGENTS.md) if not loaded. Adapted from pstack; see [attribution](../../THIRD_PARTY.md). This version adds requirements coverage and a draft stage, and removes mandatory UI automation, parallel agents and shipping steps.

## Establish coverage first

Read the source requirements, SPEC and code. Compare README requirements against SPEC; surface missing or contradictory items before treating the plan as complete. Every required acceptance check gets a stable ID in the feature map, including behavior not yet implemented. Optional behavior is explicitly optional.

Use the coordinator's shared SPEC as the acceptance source. Generate the DRAFT after that SPEC exists and before FE/BE or other work slices diverge. Do not create separate competing verifiers for implementation roles; update the shared verifier as real entry points become available.

Inspect the real entry points, launch commands, data prerequisites, existing test tools and allowed interaction methods. Never invent routes, commands, selectors or expected output. If there is no working app, create a DRAFT with unresolved execution details listed as NOT RUN. Do not install a stack just to generate the draft.

Separate proof levels: source inspection, unit or command checks, fixture/mock integration, connection to the intended data/service, and the user's real end-to-end path. Record which level each check establishes. A mock response, open port or successful build must not be reported as live application proof.

Include a proportional service baseline: launch and readiness on the intended instance, one required end-to-end path without an unhandled failure, rejected invalid input without prohibited state change, and visible non-success behavior for a required dependency failure when that failure can be exercised safely. Do not invent availability, load or recovery targets that the task does not require.

Where relevant to the requirements, include state and integration boundaries: unpublished data must not appear on a published surface; invalid transitions must not persist; unavailable external dependencies must produce the specified visible state; feedback must change the subsequent outcome, not merely be stored. Derive expected behavior from the task, not these examples. Preserve a failed check's inputs and expected result, and rerun that same check after the fix before marking it resolved. Other passing tests are not a substitute.

## Generate in the target workspace

Default to `hha-work/verification/SKILL.md` and a compact sibling `features.md`. Read and update existing files rather than replacing user edits. Use [the verifier template](../../templates/verification.md), filling it with project facts. The generated frontmatter needs a valid `verify-projectname` name and an app-specific description. Direct file reading is the supported invocation path; do not depend on automatic registration.

The generated skill must specify:

- **Scope and status:** source README/SPEC paths, project root, DRAFT or READY, and unresolved details. READY means the procedure was smoke-tested, not that all requirements passed.
- **Launch:** exact working directory and startup command, readiness including needed data, and prerequisites. Use an existing declared container or compose path when it is the project's real run path; do not add containerization only for verification. Short-lived programs need no server. Do not treat an open port alone as application readiness.
- **Doctor:** a read-only check of the intended build/instance and its inputs. Avoid accidentally testing a different checkout or an unrelated running server.
- **Static:** exact existing lint, typecheck, build, test or schema checks that apply. State what each proves; static success does not prove the running service.
- **Drive:** actual public HTTP, CLI or permitted UI entry points, mapped to acceptance IDs. Follow at least one required input through validation, data access, processing, response and visible result when those layers exist. Test externally visible behavior and relevant side effects, not just internal setters or compilation.
- **Evidence:** project-local destination, inputs, expected and observed results, exit status/output, relevant logs or state before and after, and tested file/build/container identity. Capture only what the environment allows. Do not send artifacts elsewhere.
- **Cleanup:** remove only scratch state and processes this run owns; retain evidence. Do not kill by generic process name or alter the user's running instance.
- **Feature map:** criterion ID, source, preconditions, action, expected end state, evidence, latest status. Implementation gaps stay listed.

Use existing tools first. Add a helper only when repeatable execution benefits from it; document and actually run it. Keep templates out of READY procedures. Realistic test fixtures are fine but label fixtures and mocks, and do not present a mock integration as proof of a live integration.

## Validate the procedure

When the smallest app path exists, resolve its execution details and run launch, doctor, applicable static checks, one mapped feature through the public entry point, evidence capture and cleanup. Confirm the evidence remains. Fix procedure errors and repeat the affected check. A blocked or unexecuted procedure remains DRAFT with a concrete reason.

Scale each run to the checkpoint. Use a broader early baseline to validate the intended environment, data and core path. In the implementation loop, run changed acceptance IDs, adjacent contracts and the exact failure condition; at integration run the core smoke path; before finish cover all required IDs with missing or stale evidence. Reuse unaffected evidence only when its code, dependencies, inputs and environment identity remain valid. Do not spend a deadline rerunning expensive unchanged checks or exploring failure combinations unrelated to the requirements and current diff.

Select failure and change cases from the actual requirements and risks rather than creating a universal checklist. Relevant cases may include invalid input that must not persist, empty or missing data, a connection failure, changed source rows or schema, duplicate initialization, or a retry that could repeat a write. For a selected failure, verify both the visible error/fallback and the state or side effect that must not change; an error response alone does not prove that a partial write was avoided. Preserve the exact failing condition and rerun it after the fix. When server startup or persistence is part of the task and a restart is safe, restart only the run-owned instance and repeat the core check; otherwise record why it was not run.

During implementation, run the generated verifier for changed criteria. Mark PASS only for the behavior actually observed. An API test cannot prove screen layout; source inspection cannot prove runtime behavior. Prohibited UI automation leaves visual checks NOT RUN or BLOCKED, even if nonvisual checks pass.

## Refresh without hiding regressions

When code or requirements change, reconcile README, SPEC, map and actual entry points. Update outdated commands and rerun them. If a requirement still applies but behavior breaks, keep the expected result and report FAIL. Change acceptance only for a genuine requirement change, recording its source. Invalidate affected earlier evidence; preserve useful history without duplicating full logs.
