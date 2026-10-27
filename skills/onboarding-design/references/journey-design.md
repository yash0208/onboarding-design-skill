# Journey design

## Inspect before prescribing

Trace the actual entry paths: marketing, invitation, deep link, extension, imported account, and return visit where applicable. Inspect authentication, profile schema, import/parser, preference saves, feature flags, billing/entitlements, existing UI tokens, and current analytics. Use targeted files, not a whole-repository dump. Record contradictions between docs and implementation.

State the user's job as a situation and desired outcome: “When X happens, I need Y so I can Z.” Identify the obstacle the product removes. A feature list is not a user journey. Verify business restrictions instead of quietly removing gates in the name of conversion.

Choose a first-value event that includes quality: a usable export, a relevant shortlist the user can act on, or a correctly configured test workflow. A sample output can explain value but must not count as the user's completed real task.

## Select the shape

| Situation | Candidate pattern | Watch out for |
| --- | --- | --- |
| Useful action needs little context | Start in the task with a helpful empty state | Do not add a questionnaire just to collect data |
| Several true prerequisites | Short, logically grouped setup with resumable progress | State blockers honestly; allow optional steps to wait |
| Long independent setup tasks | Checklist or hub, with dependencies and progress | Do not force an order that the product does not require |
| Unfamiliar interaction | Optional practice or contextual instruction | Teach while doing; let users reopen help |
| Team invitation | Join the correct workspace and perform the invited task | Avoid owner-only billing/setup for ordinary members |
| Existing user, new personalization | Review known facts and ask only missing/stale items | No repeated signup, lost work, or automatic consent |
| Account required before value | Explain why; minimize identity inputs | Do not introduce an unauthorized guest bypass |

These are hypotheses to test, not rankings. No universal ideal step count, time limit, or “aha” threshold exists in this package.

## Budget the effort

For each field, permission, import, invitation or integration, record:

`requested item → user-visible benefit → actual consumer → needed now/later/not needed → required/optional → source/confidence → correction/deletion path`

Remove items with no defensible consumer. Include integration setup, document finding, verification and decision effort—not just typing. Offer “Not sure” when it is a valid state; an empty field is not automatically “no.” Distinguish hard requirements from preferences. Avoid defaulting every preference to a hard filter.

Give users a useful output as early as the prerequisites allow. Follow it with one relevant next action. Additional context should improve an outcome the user can recognize. Reuse known information instead of asking it again [R05, R08 in the source ledger](research.md).

## Returning and interrupted users

Track onboarding version separately from profile completeness and activation. Candidate states are `not_started`, `in_progress`, `deferred`, `completed`, and `needs_review`; adapt to the existing model rather than prescribing a new schema unnecessarily.

- Resume the last meaningful unfinished task, or the first missing prerequisite.
- Explain what changed since the previous setup. Confirm stale preferences instead of silently refreshing them.
- Preserve previous values on skip. Provide clear/replace as explicit choices, not an ambiguous empty PATCH.
- Respect dismissed optional prompts; use a relevant re-entry point instead of prompting on every login.
- Keep current work accessible unless a documented security, safety or contractual change actually requires a gate.

## Imports and saves

Treat imports and AI extractions as proposed facts. Show source and freshness, distinguish unknown from confirmed, and allow correction before persistence. For conflicts, show existing versus proposed values and preserve unrelated fields. An import failure should offer retry or manual entry where supported.

For implementation, inspect merge semantics, ownership, authorization, version/concurrency checks and retry/idempotency. Specify draft vs committed state, durable save acknowledgment, retention, deletion and cross-device behavior. Do not store sensitive uploads or credentials in a prototype or casually in browser storage. “Saved” appears only after the relevant store acknowledges success; failed saves retain recoverable input.

Permission requests occur when their feature needs access, with a purpose and a denial path. Keep service notifications distinct from optional marketing. Existing choices carry forward; new consent is not inferred from continuing onboarding.

## Exit condition

The user should know what is ready, what is missing, and the next useful action. A completion celebration should not obscure those facts. Use the brief template to record deliberate deferrals and the later trigger for each one.
