# Validation evidence

Reviewed 2026-10-27. Status: initial package checks and model-based behavioral review completed.

## Completed checks

- Skill-creator `quick_validate.py`: passed frontmatter/name/scaffold checks.
- `python3 scripts/validate_package.py`: passed metadata, required-file, relative file-link and bounded privacy-pattern checks.
- `python3 -m unittest discover -s tests -p 'test_*.py'`: six passed, including deliberate broken/missing/escaping links, private paths and missing invocation metadata.
- Source review: 14 research/guidance entries with applicability limits, and three commit-pinned public repository observations. No third-party implementation code was copied.
- Local Codex installation: the installed directory resolves to the package skill and its supporting references. Automatic selection in a fresh session and other agent runtimes were not exercised.

## Independent forward exercise

One separate Codex agent received the skill and four fictional requests, but not the review rubric or expected answers. It produced the outputs below in one run. The package author then read the actual outputs against the rubric. This is independent from authorship, not four independently sampled runs or a comparison against a no-skill baseline.

| Case and output | Observed decision | Review |
| --- | --- | --- |
| [A — Local utility](results/2026-10-27/case-a.md) | Direct resize/download; no invented signup or paid plan; distinguishes download initiation from filesystem save | Meets case criteria |
| [B — Enterprise invitation](results/2026-10-27/case-b.md) | Preserves SSO/membership authorization, invitation intent, pending state and admin-only buying | Meets case criteria |
| [C — Import and paid export](results/2026-10-27/case-c.md) | Reviews conflicts, retains tone/consent, distinguishes uncertain saves, preserves free drafting and subscriber entitlement, refuses unsupported time claim | Meets case criteria |
| [D — Measurement](results/2026-10-27/case-d.md) | Correct 60%/40% setup and 40%/30% end-to-end export comparisons; rejects causal/productivity/retention conclusions | Meets case criteria |

No critical failures were observed. One minor usability finding was response inflation for compact plans; the entrypoint was clarified to scale deliverables and distinguish proposed checks from performed tests. The package/static tests were rerun after that clarification; the four-case agent run was not repeated. These outputs are useful samples, not required wording.

## Limits

The behavioral cases use fictional products. Automated package checks do not validate conversion, accessibility of a future implementation, or usability with real people. No live experiments or customer studies have been performed for this package.

The privacy check is a bounded pattern scan plus manual review, not an exhaustive secret detector. The link check verifies relative file targets, not remote availability or fragment anchors. Source accessibility and scope limitations are preserved in the research ledger. Future improvements should come from actual product use and measured failures.
