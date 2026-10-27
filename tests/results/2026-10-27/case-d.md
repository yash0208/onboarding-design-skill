# D — What these cohorts do and do not establish

No: these numbers do not establish that onboarding increases productivity or justify a broad rollout on that basis. The new cohort has a higher observed usable-export rate per new account, but the cohorts differ in acquisition channel, are small, and have no return-use measurements. A rollout decision needs stronger evidence and defined guardrails.

| Observed measure | New setup | Old flow | Descriptive difference |
| --- | ---: | ---: | ---: |
| Finished setup / new accounts | 12/20 = 60% | 20/50 = 40% | +20 percentage points |
| Usable report export / new accounts | 8/20 = 40% | 15/50 = 30% | +10 percentage points |
| Usable report export / setup finishers | 8/12 ≈ 66.7% | 15/20 = 75% | −8.3 percentage points |

These calculations assume the 15 old-flow exporters belong to its 20 setup finishers and that both flows use the same usable-export definition. If not, the conditional row needs correction. The new cohort is described as last week; the old cohort’s exposure period and equal follow-up are not specified. Reconcile those before treating the comparison as like-for-like.

More people finishing setup is not itself first value. The lower export rate among new-flow setup finishers is a useful diagnostic, but it also cannot prove that the new flow harms downstream behavior: conditioning on completion selects different people, potentially changed by the flow itself. The end-to-end outcome is the more useful primary comparison.

There is no task-time, work-quality comparison beyond the supplied “usable” label, repeated output, or retention evidence. Differences in acquisition could explain the observed gap, and sampling variation could also matter. Do not describe the +10 points as causal uplift, statistical significance, or productivity gain.

Suggested stakeholder copy:

> In these two observed cohorts, 8 of 20 new-flow accounts and 15 of 50 old-flow accounts exported a usable report. The new flow also had higher setup completion. Different acquisition channels, limited sample sizes and unconfirmed follow-up comparability prevent attributing these differences to onboarding. We recommend a controlled follow-up test; productivity and repeat-use effects remain unknown.

## Next test proposal

First confirm event definitions and exposure: one eligible new account per assignment; actual first exposure timestamp and version; authoritative export success; a consistent usability criterion; deduplicated retries; and comparable windows. Inspect missing events, bot/internal accounts, partial saves and failed exports. Do not count an export-button click as a completed usable report or silently treat missing telemetry as failure.

Hypothesis: the new setup increases the probability that an eligible new account exports a usable report within seven days of first exposure, without worsening report quality or reliability. Seven days is a proposed common window, to confirm against the product’s actual task cadence before launch.

Use concurrent, stable 1:1 assignment within acquisition-channel strata. If colleagues in a workspace influence each other’s setup, randomize by workspace and account for clustering instead. Keep features and entitlements comparable, and change only the specified onboarding experience. Analyze everyone assigned on the prespecified basis; preserve exposure failures and exclusions transparently.

Predefine:

- **Primary outcome:** accepted usable export within the common window, divided by eligible assigned accounts, with uncertainty and absolute effect size.
- **Diagnostics:** setup completion, error/failure rates and time to first usable export. Include admin/waiting/review effort where relevant; report completion and abandonment alongside time among completers.
- **Guardrails:** report correctness, lost work, access errors, support burden and accessibility failures. Predefine unacceptable deterioration and a rollback owner.
- **Return value:** a meaningful second report task in a specified later window, provisionally days 8–28; wait for both groups to mature. A login alone is not retained value.
- **Decision contract:** agree on a minimum worthwhile absolute improvement and tolerated guardrail changes, then calculate the sample requirement from an appropriate baseline and randomization unit. Set the analysis horizon, missing-data rules, safety stops and decision owner before launch; do not stop at the first encouraging result.

For limited traffic, begin with task-based sessions that exercise errors, corrections and return visits. Those can identify usability failures but cannot establish conversion uplift. To investigate productivity separately, compare equivalent baseline and assisted tasks, include setup, waiting, review and correction time, assess output quality, counterbalance task order, and report failures and distributions. Sustained weekly savings require evidence across repeated weekly use.

Evidence: arithmetic above comes only from the supplied fictional counts. The skill’s measurement and value references informed the proposed evaluation. No raw analytics, live flow, user study or experiment was inspected or run. This is a model-based interpretation and test plan, not empirical validation or authorization to ship.
