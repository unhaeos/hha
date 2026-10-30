---
name: hha-debug
description: Diagnose a failed project check or broken behavior through reproduction, a focused hypothesis, a minimal correction and re-verification. Use when implementation or verification is blocked by an error.
---

# Debug a failed check

Read [working guidance](../../guidance.md) if not loaded. Locate the failing SPEC criterion and verifier procedure, if present.

1. Capture the exact input, expected result, actual result and execution context. Reproduce on the intended code and instance. If reproduction is unavailable, say why and keep the conclusion tentative.
2. Separate product failure from a wrong test expectation, stale command, missing fixture or environment restriction. Check the evidence path before making unrelated product changes.
3. Form one concrete hypothesis and run the smallest discriminating check. Inspect relevant callers and data rather than changing several layers at once.
4. When fixes are authorized, correct the cause with the smallest relevant change. A diagnosis-only request ends with findings. Do not make tests pass by deleting requirements, swallowing errors or substituting fake success.
5. Repeat the original failed check, then relevant neighboring checks. Record failure, fix and observed result; leave remaining gaps visible in SPEC.

If two attempts fail on the same premise, test that premise directly before another patch. If blocked by unavailable permissions or services, report the precise blocker and next useful action. Do not repeatedly retry an unchanged external restriction.
