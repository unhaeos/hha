# Validation record

## Local smoke check — 2026-10-30

Environment: Windows PowerShell, Python 3.13.3. A single authoring agent followed the workflow using the synthetic [empty-project brief](../examples/empty-project/README.md) in a separate scratch directory. This was not independent agent evaluation and was not performed in a managed assessment environment.

The run produced a small SPEC, a Python CLI, a project-specific verifier and a subprocess check helper. The helper invoked the real CLI, checking stdout, stderr and exit status against literal expected values. No third-party application packages, network integration, background server or browser was used. Scratch implementation files are excluded from the public harness.

Command: `python check.py` from the scratch practice directory.

| Check | Observed stdout | Exit | Observed stderr | Result |
|---|---|---|---|---|
| R1: 2 3 0 | `5` plus newline | 0 | empty | PASS |
| R2: 0 | `0` plus newline | 0 | empty | PASS |
| R3: no arguments | empty | 2 | nonnegative-integer input instruction | PASS |
| R3: -1 | empty | 2 | nonnegative-integer input instruction | PASS |
| R3: abc | empty | 2 | nonnegative-integer input instruction | PASS |
| R3: 1.5 | empty | 2 | nonnegative-integer input instruction | PASS |

Helper summary: `6 behavioral checks passed`. No run-owned background processes or temporary data required cleanup. This record remains outside the scratch directory.

The skill-creator `quick_validate.py` validator passed for all four shipped skills and the generated example verifier. Format validation does not establish prompt quality or application correctness.

## Not yet verified

- How another agent follows these instructions without author context.
- Availability of git, runtime tools, network access or writable paths in a particular managed environment.
- Actual rendering, responsive layout and font quality of generated UI.
- Real external-service integrations or complex state transitions.
- A full task completed under a time limit.

Use the [15-minute walkthrough](try-15-minutes.md) to test the available environment. An unavailable tool is a recorded constraint, not permission to change environment settings.
