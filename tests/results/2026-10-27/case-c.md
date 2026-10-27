# C — Review imported notes, draft, then decide on branded export

Keep the saved tone and weekly digest choice. Present conflicting biography details as proposals, let the user decide which facts belong in the draft, and ask about payment only when they choose the paid branded export. Replace the unsupported headline with **“Turn your notes into a first draft you can review.”**

## Review and first value

Start with **“Review imported details”**, explaining: “Some notes differ from your saved biography. Choose what to use; your saved biography has not changed.” Show existing and proposed values side by side, stacking them in that same order on narrow screens.

Illustrative fixture, not actual account data:

| Detail | Saved biography | Imported notes | Initial choice |
| --- | --- | --- | --- |
| Current role | Researcher at Atlas | Consultant at Harbor | Keep saved |

Each imported value shows the actual filename and import time. An import timestamp does not establish when a claimed role became current. Label unresolved facts as uncertain. Offer **Keep saved**, **Use imported**, and **Edit**; imported text must not silently overwrite a confirmed fact. Preserve unrelated biography fields.

Use **“Use these details for this draft”** for the primary action. This applies the reviewed selection to the working draft without claiming that the profile was saved. **“Cancel import”** leaves the existing profile intact. Let users return and correct their choices before drafting. If generation uses account biography, the proposed implementation must explicitly pass the reviewed draft context rather than accidentally generating with the conflicting old value.

Offer a separate, unselected action **“Also update my saved biography”**, followed by a clear review of the exact changes. Existing tone remains in effect and editable through its normal control; the import has no reason to change it. Leave weekly digest consent exactly as stored, including a declined or unset value. Any later consent change belongs in an explicit preference action, independent of drafting and profile updates.

Ask only for a missing output goal that changes the draft—for example, what the text is for—if the current entry point does not already supply it. Do not require the user to complete an entire profile.

> **Your first draft**
> Review the wording and facts before using it.
> **Edit draft** · **Export branded team template**

Free accounts can draft. Candidate first value is a draft the user reviews and accepts as usable for the chosen purpose, with factual conflicts resolved. Generation completion alone is not proof of quality. A proposed **“Use this draft”** action can record acceptance where it fits the actual workflow; validate that signal against observed task success.

## Failed save and recovery

Only show **“Biography saved”** after the authoritative profile store confirms the write. On failure:

> **Your biography changes weren’t saved**
> Your previous biography is still saved. Your edits remain here while this page is open.
> **Retry save** · **Continue without updating biography**

Preserving those edits is a proposed requirement, not a claim about the current app. Retrying must not duplicate changes. If the failure leaves the write outcome uncertain, reconcile with the server before claiming the old value remains; use “We couldn’t confirm whether your changes were saved” instead. If another device changed the profile, show that conflict before replacing it. Do not use browser storage for imported personal notes merely to promise recovery. On import parsing failure, retain the existing profile, explain the failure and offer retry or manual correction where supported.

## Branded export decision

Check the signed-in account’s authoritative entitlement when **Export branded team template** is chosen. An entitled subscriber proceeds to export. On a new device, offer sign-in to the existing account; restore saved preferences and entitlement after verification instead of starting a new signup or requesting another purchase. Do not claim that an unsaved draft follows the user across devices.

For an account confirmed to lack the plan:

> **Export with your team’s branding**
> Branded team-template export requires the $12-per-user monthly plan. There is no trial. You can continue drafting on your free account.
> **Review plan and billing** · **Keep editing**
> Already subscribed? **Check your account**

Preserve the draft when leaving or returning. Do not imply an unbranded export exists. The dollar currency, seat quantity, actual total, taxes, payment-start behavior and cancellation terms are unspecified; verify them and show the complete billing summary before a purchase confirmation. The first button opens that review, not an automatic charge. If entitlement lookup fails, say so and offer retry rather than misclassifying the subscriber as free.

## Evidence and acceptance

The scenario supplies draft access, existing preference/consent, the paid capability, price cadence and absence of a trial. Journey, UI, value and measurement references informed the proposal. Profile merge behavior, import retention, draft persistence and complete billing terms remain unknown. No implementation, save, upload, paid run or billing action occurred.

Review back/cancel, each conflict choice, unchanged consent, uncertain saves, concurrent edits, new-device subscriber recovery, failed entitlement lookup, keyboard use and narrow-screen copy. No tests or user research were performed. “Save five hours every week” is unsupported; evaluating such a claim would require comparable baseline/assisted tasks, total time including setup and correction, matched quality criteria, repeat-use frequency and uncertainty. A future hypothesis is that explicit conflict review reduces factual corrections, not that this design has already improved productivity.
