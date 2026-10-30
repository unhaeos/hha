---
name: hha-create-verification
description: Generate or refresh a project-specific verification skill from the task README, checklist SPEC and actual code. Create an honest draft for an empty app, then validate executable procedures once it runs.
---

# Create project verification

Read [working guidance](../../guidance.md) if not loaded. Adapted from pstack; see [attribution](../../THIRD_PARTY.md). This version adds requirements coverage and a draft stage, and removes mandatory UI automation, parallel agents and shipping steps.

## Establish coverage first

Read the source requirements, SPEC and code. Compare README requirements against SPEC; surface missing or contradictory items before treating the plan as complete. Every required acceptance check gets a stable ID in the feature map, including behavior not yet implemented. Optional behavior is explicitly optional.

Inspect the real entry points, launch commands, data prerequisites, existing test tools and allowed interaction methods. Never invent routes, commands, selectors or expected output. If there is no working app, create a DRAFT with unresolved execution details listed as NOT RUN. Do not install a stack just to generate the draft.

Where relevant to the requirements, include state and integration boundaries: unpublished data must not appear on a published surface; invalid transitions must not persist; unavailable external dependencies must produce the specified visible state; feedback must change the subsequent outcome, not merely be stored. Derive expected behavior from the task, not these examples. Preserve a failed check's inputs and expected result, and rerun that same check after the fix before marking it resolved. Other passing tests are not a substitute.

## Generate in the target workspace

Default to `hha-work/verification/SKILL.md` and a compact sibling `features.md`. Read and update existing files rather than replacing user edits. Use [the verifier template](../../templates/verification.md), filling it with project facts. The generated frontmatter needs a valid `verify-projectname` name and an app-specific description. Direct file reading is the supported invocation path; do not depend on automatic registration.

The generated skill must specify:

- **Scope and status:** source README/SPEC paths, project root, DRAFT or READY, and unresolved details. READY means the procedure was smoke-tested, not that all requirements passed.
- **Launch:** exact working directory and startup command, readiness including needed data, and prerequisites. Short-lived programs need no server. Do not treat an open port alone as application readiness.
- **Doctor:** a read-only check of the intended build/instance and its inputs. Avoid accidentally testing a different checkout or an unrelated running server.
- **Drive:** actual public entry points and allowed interaction procedures, mapped to acceptance IDs. Test externally visible behavior and relevant side effects, not just internal setters or compilation.
- **Evidence:** project-local destination, inputs, expected and observed results, status, and tested file/build identity. Capture only what the environment allows. Do not send artifacts elsewhere.
- **Cleanup:** remove only scratch state and processes this run owns; retain evidence. Do not kill by generic process name or alter the user's running instance.
- **Feature map:** criterion ID, source, preconditions, action, expected end state, evidence, latest status. Implementation gaps stay listed.

Use existing tools first. Add a helper only when repeatable execution benefits from it; document and actually run it. Keep templates out of READY procedures. Realistic test fixtures are fine but label fixtures and mocks, and do not present a mock integration as proof of a live integration.

## Validate the procedure

When the smallest app path exists, resolve its execution details and run launch, doctor, one mapped feature, evidence capture and cleanup. Confirm the evidence remains. Fix procedure errors and repeat the affected check. A blocked or unexecuted procedure remains DRAFT with a concrete reason.

During implementation, run the generated verifier for changed criteria. Mark PASS only for the behavior actually observed. An API test cannot prove screen layout; source inspection cannot prove runtime behavior. Prohibited UI automation leaves visual checks NOT RUN or BLOCKED, even if nonvisual checks pass.

## Refresh without hiding regressions

When code or requirements change, reconcile README, SPEC, map and actual entry points. Update outdated commands and rerun them. If a requirement still applies but behavior breaks, keep the expected result and report FAIL. Change acceptance only for a genuine requirement change, recording its source. Invalidate affected earlier evidence; preserve useful history without duplicating full logs.
