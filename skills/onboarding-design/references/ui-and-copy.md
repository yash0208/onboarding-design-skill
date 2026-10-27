# UI, copy and prototype review

## Composition

Use the project's existing type, color, spacing, radius and component tokens. For a new project, propose a small explicit token set rather than copying a brand from this package. Prioritize a clear heading, a short reason, the relevant control/output, and a distinct next action. Avoid nested cards and equal visual weight for everything.

Related fields can share a screen; difficult decisions can deserve a screen of their own. Choose based on cognitive and interaction effort, not a fixed “one field per screen” rule. An optional advanced area can reduce clutter, but costs and requirements stay visible. On mobile, make action order and content order coherent; avoid sticky footers covering fields or keyboard focus.

## Screen contract

For every screen specify:

- User question, useful outcome, and the minimum input.
- Primary action and what actually happens; back/skip/exit where applicable.
- Required/optional status, default values, and why those defaults are appropriate.
- Empty, selected, invalid, loading, failed, succeeded, and resumed states.
- Source of displayed data and exact persistence semantics.

Say “Choose the roles you want to see” rather than “Configure personalization parameters.” Explain the immediate use of a field. Use labels instead of placeholder-only inputs. Avoid unexplained “AI magic,” inflated promises, fake social proof, and shame-based dismissal text. Name actions after their outcome: “Review imported details,” “Save preferences,” or “Compare plans” when those are true.

## Interaction and accessibility

Use native controls and semantic groups where possible: labels, fieldsets/legends, links for navigation, buttons for actions. Selection cannot rely only on color. Preserve values during navigation and connect validation messages to the relevant fields. Identify the correction needed, not merely “invalid.” Move focus intentionally after a step transition or submit error, without repeatedly stealing it while typing.

Test keyboard order, visible/unobscured focus, zoom/reflow, screen-reader names and announcements, and contrast in supported themes. Loading changes need a status announcement, not an indefinitely spinning screen. Authentication must support password-manager/autofill and paste, including codes [R09](research.md).

Use appropriately sized, separated touch controls. WCAG 2.2 AA SC 2.5.8 specifies 24×24 CSS pixels or qualifying exceptions; a larger project touch target (often 44×44) is a usability choice, not that exact AA minimum [R10](research.md). Test at 320 CSS-pixel width and with long/localized content; do not assume one desktop screenshot proves responsiveness. Honor reduced motion; never make a decorative animation necessary to understand or complete a step.

Progress must reflect the real branching journey. Do not show “almost done” before undisclosed requirements. For long or variable workflows use stage labels or an honest approximate indicator. A save-and-return promise requires actual persistence, not just in-memory state [R04](research.md).

## Prototype boundaries

When asked for a simple HTML draft, prefer a dependency-light local artifact with fictional fixtures. Make flows usable: selection, back, validation, correction, skips, and empty/failure examples. Mark sample output and simulated imports clearly. Do not read real selected file contents, send network requests, charge credits or persist personal data unless explicitly in scope. Clearly separate demo controls from product UI.

Include both fresh and returning-user scenarios without polluting one with the other's state. Store no real personal information in fixture data. If the product app is not being changed, say so. Keep the prototype source and a short run instruction for future review.

## Acceptance exercise

1. Complete the shortest valid path and verify a meaningful next action.
2. Leave optional fields empty; confirm no misleading default or accidental consent.
3. Go back, edit, and return to review without redoing unrelated steps.
4. Interrupt an import/save; verify clear recovery and no false success.
5. Resume an existing account; preserve data, preferences and entitlements.
6. Exercise keyboard, narrow screen, zoom, long copy, supported themes and reduced motion.
7. Confirm no unintended requests, uploads, purchases or analytic collection in review mode.

Record the actual tested dimensions and remaining gaps. An automated accessibility scan is useful but does not establish full accessibility conformance or real-user usability.
