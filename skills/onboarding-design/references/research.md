# Research ledger

Reviewed 2026-10-26–27. This is a curated starting library, not an exhaustive review or proof that a particular onboarding design will increase conversion. Guidance below is original synthesis; no articles are reproduced. Repository observations are recorded separately in [repository notes](repositories.md).

Evidence classes: **UX synthesis** (research-informed guidance), **standard explanation**, **design-system/platform guidance**, **provider documentation**, **vendor case**, **research publication**. They are not interchangeable. The workflow in this skill is a design synthesis to validate in each product.

## Journey and forms

### R01 — Contextual help

[NN/g, Onboarding Tutorials vs. Contextual Help](https://www.nngroup.com/articles/onboarding-tutorials/), Page Laubheimer, 2023-02-12. UX synthesis. Upfront instruction can interrupt and burden memory; assistance near the relevant task is often a better candidate. Novel interactions can still warrant a tutorial. Use this to question a tour, not categorically prohibit one. No universal conversion effect established.

### R02 — Progressive disclosure

[NN/g, Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/), Jakob Nielsen, 2006-12-03. UX guidance. Prioritize common actions while making secondary options easy to find. The primary/secondary split matters. This does not justify hiding important costs, constraints or consent.

### R03 — Account timing

[Baymard, Save Account Creation for the Confirmation Step](https://baymard.com/research-articles/delayed-account-creation), Edward Scott, 2023-09-19. Ecommerce usability findings. Optional account requests can distract from purchase completion. Applicability is checkout; do not transfer this into a requirement to bypass necessary SaaS identity or security, or reuse benchmark prevalence as conversion uplift.

### R04 — Multi-page forms

[W3C WAI, Multi-page Forms](https://www.w3.org/WAI/tutorials/forms/multi-page/). Accessibility tutorial. Group related controls, make optional stages clear, show meaningful progress, and preserve prior entries. Applicable when a long form is necessary, not evidence that every product needs one.

### R05 — Question protocol

[GOV.UK Design System, Question pages](https://design-system.service.gov.uk/patterns/question-pages/). Public-service guidance. Establish why each question is needed, explain its purpose and support correction/navigation. Optional or unknown responses need honest representation. Adapt the pattern to task complexity instead of copying an entire government-service journey into SaaS.

### R06 — Review before committing

[GOV.UK Design System, Check answers](https://design-system.service.gov.uk/patterns/check-answers/). Public-service guidance. A concise review with targeted changes can help users catch mistakes before submission. Particularly useful for consequential or imported information; a separate review screen can be unnecessary for trivial actions.

### R07 — Learning by doing

[Apple HIG, Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding). Platform guidance. Safe interactive learning and contextual tips can replace unnecessary introductory friction. Read via indexed page text; direct HTML was JavaScript-only and the linked Markdown retrieval failed during this review. Do not present this as an experimental result.

## Accessibility

### R08 — Repeated information

[W3C, Understanding SC 3.3.7: Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html). Explanation of WCAG 2.2 Level A. Reuse information within the same process, with essential/security/invalid-data exceptions. Does not authorize silent changes to a user's existing profile.

### R09 — Authentication assistance

[W3C, Understanding SC 3.3.8: Accessible Authentication (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html). Explanation of WCAG 2.2 Level AA. Password-manager assistance and paste support matter, including verification codes. Assess the complete sign-in/recovery path; passing one field check is not overall conformance.

### R10 — Target size

[W3C, Understanding SC 2.5.8: Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). Explanation of WCAG 2.2 Level AA. Specifies 24×24 CSS pixels with defined exceptions, including spacing. Larger targets may be more usable. Do not confuse a product's preferred 44-pixel target with the AA minimum. Understanding documents explain standards; they are not themselves a full audit.

## Monetization and measurement

### R11 — Relevant subscription choices

[Apple HIG, Apple In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase). Platform guidance, read via indexed page text. Explain benefits and terms; offer purchase at relevant needs, recognize existing subscribers and support management. Useful design reference, not universal web billing rules or proof of conversion uplift.

### R12 — Actual trial behavior

[Stripe, Configure trial offers on subscriptions](https://docs.stripe.com/billing/subscriptions/trials). Current provider documentation. Introductory pricing, transition behavior and integration restrictions must match what is built. Volatile: verify the project's API version, checkout support and lifecycle before implementation. No trial API or price is prescribed by this skill.

### R13 — Activation candidates

[PostHog, How we found our activation metric](https://posthog.com/product-engineers/activation-metrics), Raquel M Smith, 2024-11-28. Vendor's own methodology. Investigate early behaviors associated with retention using coherent cohorts and adequate data. Its thresholds are product-specific. Correlation can prioritize hypotheses, not prove that forcing a behavior will cause retention.

### R14 — Interpreting metrics

[Microsoft Research, A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments](https://www.microsoft.com/en-us/research/publication/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/), Dmitriev et al., KDD 2017. Research publication landing page/abstract reviewed; full paper not reviewed here. Incorrect interpretation of metric movements can undermine experiment decisions. Detailed statistical procedures in this skill are proposed evaluation practice, not a reproduction of this paper.

## How to extend this ledger

Record title/URL, author/date if available, retrieval date, evidence class, the specific finding, studied population/context, limitation, and the decision it informs. Capture disagreeing evidence too. Label a product teardown as observation, not a causal study. Keep summaries brief and linked; do not copy paywalled reports. Recheck provider docs and library licenses when implementing. When access fails, record the gap rather than inventing the missing content.
