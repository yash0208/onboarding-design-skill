# Measurement and evidence

## Separate the milestones

| Milestone | Example definition | Interpretation |
| --- | --- | --- |
| Signup | Verified account created | Identity milestone, not proof of value |
| Setup completion | Required configuration committed | Readiness, not necessarily use |
| First value | First accepted usable output/action | Candidate activation signal |
| Activation | Defined behavior within a window, associated with future useful use | Product-specific hypothesis until supported |
| Retention | Cohort performs a meaningful return action in a stated interval | Not just opening an email |
| Paid conversion | Eligible free/trial accounts become paying within a defined window | Must be paired with fit/trust guardrails |

Specify the unit (person, workspace, account), eligible denominator, timestamp boundaries, timezone and event source. Keep invited, returning and new accounts distinguishable. Do not mix cohorts with different exposure or maturity. An activation correlation can inform hypotheses but is not a causal result [R13](research.md).

## Minimum measurement plan

Define a primary user outcome, a business outcome if relevant, guardrails, and a diagnostic funnel. Candidate events—not mandatory names—include `onboarding_started`, `step_completed`, `step_skipped`, `import_failed`, `preferences_committed`, `first_value_reached`, and `plan_offer_viewed`. Include schema/flow version, variant and coarse segment only where justified. Minimize identifiers; never log raw resumes, private message text, tokens or sensitive answers. Do not activate analytics merely because a plan mentions them.

Instrument committed events from authoritative acknowledgments, not optimistic button clicks. Dedupe retries; test reloads, multiple tabs, account switching, partial saves, missing events and bot/internal traffic. Distinguish “declined,” “unavailable” and “not asked.” A browser-only event does not prove billing succeeded.

Measure time to first value from a defined entry point. Report completion probability and failures alongside time among completers; otherwise abandonment can make the remaining users appear faster. Compare users with similar tasks and permissions. Record waiting and review effort, not only active typing.

## Experiment contract

Before launch record:

- Hypothesis, relevant user group, control and exact proposed difference.
- Assignment/exposure unit and stable allocation; avoid team contamination.
- Primary outcome, guardrails, detection threshold, sample/power plan and analysis window.
- Exclusions, missing-data handling, stopping/safety rules and decision owner.
- What evidence would reject the idea and how to roll back.

Do not repeatedly peek at ordinary fixed-horizon tests and stop when a result happens to look significant. Use an appropriate prespecified method; report uncertainty and practical effect size. Check instrumentation and allocation quality before interpreting shifts. Do not run an experiment or change feature flags without the necessary authority. Metric interpretation itself can be a failure point [R14](research.md).

For low traffic, begin with task-based usability sessions and interviews. Observe whether people understand the promise, complete the task, correct errors and can explain the paid choice. These reveal usability problems; they do not establish a conversion lift. Capture counterexamples and access needs. No fixed small participant count proves success for every audience.

## Research hygiene

Tag each statement as product fact, standard/guideline, empirical finding, vendor case, repository observation or design hypothesis. Link the supporting source and record its date/context. Prefer primary evidence; read beyond a promotional headline. Do not transfer ecommerce percentages, another company's activation threshold, or a platform guideline into a causal claim about this product.

When reporting results, separate model-based scenario review, automated tests, manual browser checks, real participant studies, and live experiments. Say exactly what each establishes and what it does not. For “saves time” claims, use the protocol in [value and plans](value-and-plans.md).
