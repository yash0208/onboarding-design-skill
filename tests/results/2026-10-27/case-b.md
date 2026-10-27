# B — Invited and returning document reviewers

Bring reviewers back to the document that prompted their visit after the real access requirements are met. Activation means useful review work, so do not turn an invitation into workspace creation, profile collection or a license purchase journey.

## Invitation journey

1. **Identify the required sign-in.** Keep the destination through authentication using the existing secure invitation mechanism. Before authorization, show only invitation metadata the current system permits; do not expose protected document contents or assume its title is public.

   > **Open your document invitation**
   > Sign in with your company account. Access also requires administrator-approved workspace membership.
   > **Continue with company SSO**

   Company identity is necessary for authorization. Reuse the identity returned by SSO; ask for a company identifier only if the existing SSO routing actually needs one. No job-title, interests, marketing consent or payment fields are needed for this task. Support existing SSO recovery and account switching without discarding the intended destination.

2. **Resolve membership from the authoritative status.** If approved, proceed to the invited document and recheck document authorization. If pending, show an honest blocked state:

   > **Workspace approval is pending**
   > An administrator needs to approve your membership before you can access this document. Return to this invitation to check your access.
   > **Check access again** · **Sign out**

   Include the verified workspace name after it is safe to display. Provide an existing administrator contact route if available, but do not invent an automated approval request or promise an email. A status lookup failure must say “We couldn’t check your access. Try again,” not imply approval is pending. A declined or revoked membership needs its own accurate state and the supported admin route.

3. **Begin the assigned work.** Once both membership and document access are valid, open the document in the existing review UI, with its actual review controls and any existing review instructions. Keep optional help next to unfamiliar actions. Show no billing offer: only administrators may purchase licenses. If a verified license restriction blocks review, explain that exact restriction and route through the supported administrator process.

   > **Review {authorized document title}**
   > {Existing review instruction, if supplied by the invitation}

   Do not manufacture a deadline, requested review type or “review submitted” status. A completion message must match the product’s actual, acknowledged review operation.

## Returning and interrupted reviewers

An authorized returning reviewer follows the invitation directly into its document. Require SSO again only under the existing session policy. A pending reviewer resumes at the live approval status; once approved, the same invitation continues to its destination. Do not restart account setup when the onboarding version changes.

Preserve existing review work through supported saving and resume behavior. Draft persistence has not been specified, so do not promise cross-device recovery. Expired, revoked and wrong-account invitations should offer the existing recovery or account-switch path without leaking document data. Every access is still subject to authorization; “returning” is not an access bypass.

## Activation hypothesis and next validation

Candidate first value is the first meaningful review action on the invited document acknowledged by the service. Confirm the product’s review operation and its quality criterion before choosing the event; opening a document shell or completing SSO does not prove review value. Reading the intended document is a useful intermediate milestone.

Report invitation-to-first-value completion and elapsed time, including admin waiting time, with a second diagnostic view for users already approved at entry. Separate new and returning reviewers and pending/approved status; never remove pending users from the overall funnel to imply activation improved. Guardrails include authorization failures, exposed content, lost work and support requests.

Review wrong-account SSO, pending-to-approved return, lookup failure, revoked access, back navigation, keyboard access and a narrow screen. No flow, auth, analytics or experiment has been changed or tested here. Evidence consists only of the fictional scenario and the skill’s journey, UI and measurement guidance; review operations, invitation expiry, license rules and persistence remain unverified.
