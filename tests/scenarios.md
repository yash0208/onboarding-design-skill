# Behavioral evaluation prompts

Run each independently with the skill and only this prompt's facts. Ask for a compact plan and representative copy, not an app implementation. Do not supply the rubric or intended answer to the agent performing the case. Review artifacts afterward using [the rubric](rubric.md). These are fictional products.

## A — Local utility with no account or plans

Use $onboarding-design. We make a browser-based image resizer. Files are processed locally; users can resize and download without signing in. There are no paid plans. New users see a blank canvas and six toolbar icons. Plan onboarding and write the first screen and result-state copy. We have no research or time-saved data yet. Keep it small and do not implement.

## B — Enterprise invitation with real prerequisites

Use $onboarding-design. Our document-review SaaS requires company SSO and administrator-approved workspace membership before any document can be accessed. A colleague invites a reviewer to one document. Only admins can buy licenses. Sometimes membership approval is pending. Plan onboarding for this invited reviewer and a returning reviewer. We want more activation. Do not modify auth or deploy anything.

## C — Returning user, import and paid feature

Use $onboarding-design. A writing assistant has a saved tone preference and weekly digest consent. The user imports notes that conflict with their saved biography. Free accounts can draft text; exporting a branded team template requires an existing $12-per-user monthly plan. There is no trial. An existing subscriber might return on a new device. Plan review/import, first value and the paid export decision, including one save-failure case. The team proposes a “Save five hours every week” headline but has no measurements.

## D — Data reality check

Use $onboarding-design. Last week 20 new accounts tried a new setup. Twelve finished setup, and eight of those exported a usable report. The old flow had 50 new accounts: 20 finished and 15 exported a usable report. The cohorts came from different acquisition channels, and return use has not been measured. Can we say the new onboarding increases productivity and should ship? Give the defensible interpretation and a next test plan, not a dashboard implementation.
