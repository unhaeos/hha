---
name: verify-project
description: Verify the target project's required behavior using its actual entry points and local evidence.
---

# Project verifier

This is a generation template, not an executable verifier. Replace project details from actual evidence. Unresolved execution details may remain only in a clearly marked DRAFT.

## Scope

- Status: DRAFT
- Project root:
- Requirements and SPEC:
- Allowed verification methods:
- Intended runtime and data source:
- Unresolved details:

## Launch

Working directory, exact command, prerequisites and usable-state signal.

## Doctor

Read-only check of the correct code, instance and input data. Identify whether inputs and integrations are real, fixture-based or mocked.

## Drive

Read `features.md`. For each relevant acceptance ID, run its documented action and compare with the expected result. Follow one required input through the real public path. Add only relevant invalid-input, missing-data, dependency-failure, data-change or restart checks. Do not omit missing features from coverage.

## Evidence

Keep local run records with date, file/build identity, criterion ID, exact command or procedure, evidence level, expected result, observed result, and PASS / FAIL / NOT RUN / BLOCKED. Do not claim fixture or mock evidence proves the intended live integration. Do not claim unexecuted checks passed. Recheck affected criteria after changes.

## Cleanup

Specify the owned processes and scratch paths to clean. Keep evidence and user data. Confirm evidence remains after cleanup.

## Procedure validation

Record which mapped feature exercised this procedure end to end. READY means the procedure works for that feature; overall completion requires every required acceptance check to pass.
