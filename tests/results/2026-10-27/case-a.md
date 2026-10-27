# A — Image resizer onboarding

Start users in the resize task. Replace the unexplained blank canvas with one useful empty state and give the six toolbar icons visible, meaningful labels. The user’s job is to turn an existing image into a file with the dimensions they need; neither an account nor a tour is a prerequisite.

## Proposed journey and copy

**Empty state**

> **Resize an image**
> Choose an image, set its dimensions, then download the result. Your image is processed locally in your browser.
> **Choose image**

Use a native file picker; drag-and-drop can supplement it if supported. Do not describe this as an upload. There are no profile fields, sign-in prompts, or plan screens.

**Image selected**

Show the preview, filename and actual original dimensions. Label the controls **Width (px)** and **Height (px)**. Initialize them from the selected image; propose **Keep proportions** enabled to prevent accidental distortion, subject to confirming this option is supported. Each dimension directly controls the output. Keep the original intact when changing these settings.

> Original: {original width} × {original height} px
> **Resize image** · **Choose another image**

Explain a constraint beside the relevant field using the real accepted range: “Enter a width between {minimum} and {maximum} pixels.” Format support and size limits must come from the implementation; do not invent them in the mock.

**Processing and result**

> Resizing your image…

> **Your resized image is ready**
> {filename} · {output width} × {output height} px
> **Download image** · **Adjust dimensions**

After the browser download action, say **“Download started”**, not “Saved to your device.” Keep the result available for another download or adjustment during the current open session. “Choose another image” begins a different task; no completion celebration blocks the download.

**Recoverable error**

> We couldn’t resize this image. Your original is unchanged. Try again, or choose another image.
> **Try again** · **Choose another image**

The proposed implementation should preserve the selected image and dimension entries on a processing failure and when returning from the result. Cross-reload recovery is unknown: do not promise saved progress or add persistent file storage without deciding its privacy and retention behavior.

## Outcome and review

Candidate first value: the user initiates download of their successfully generated image, with validation that the output decodes and has the requested dimensions. A download click alone cannot establish that the file reached the user’s filesystem or met their intended use. In usability sessions, ask users to locate and inspect the result.

Before implementation acceptance, exercise keyboard-only file selection, labeled icon actions, invalid dimensions, retry, return to edit, a second download, and 320-pixel layout with zoom. Announce processing and result status accessibly; do not rely on preview appearance alone. These are proposed checks, not completed tests.

Evidence: the supplied scenario establishes local processing, account-free resizing/download and no paid plans. The skill’s journey, UI and measurement guidance informed this plan. Supported formats, limits, existing tokens and session recovery were not inspected. Reducing ambiguity is a design hypothesis; there is no measured time saving, conversion result, or real-user validation.
