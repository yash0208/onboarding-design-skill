# Repository observations

Checked 2026-10-27 using public GitHub README/license files and selected source/example sections at the commits below. This is **not** a full code, security, accessibility, or maintenance audit. No code is vendored. Recheck the version you actually adopt.

## Driver.js

Repository: [nilbuild/driver.js](https://github.com/nilbuild/driver.js); the former `kamranahmedse/driver.js` URL redirected here.

Snapshot: `1c77160392e1e2ade13c2d9edf646c75ce098aad`.

Read: [README](https://github.com/nilbuild/driver.js/blob/1c77160392e1e2ade13c2d9edf646c75ce098aad/README.md), [MIT license](https://github.com/nilbuild/driver.js/blob/1c77160392e1e2ade13c2d9edf646c75ce098aad/license), and the opening tour examples in [tour.ts](https://github.com/nilbuild/driver.js/blob/1c77160392e1e2ade13c2d9edf646c75ce098aad/apps/playground/src/examples/tour.ts).

The selected examples cover progress/navigation, disabled animation and manually advanced asynchronous steps. Candidate for framework-independent highlights or optional contextual tours. It does not decide which task matters, own server-side onboarding state, or establish conversion benefit. Verify missing-target and cancellation behavior in the intended layout.

## React Joyride

Repository: [gilbarbara/react-joyride](https://github.com/gilbarbara/react-joyride).

Snapshot: `1fe55f1aedcf6d1fe0bceaf1418c0d5ad9a65bbb`.

Read: [README](https://github.com/gilbarbara/react-joyride/blob/1fe55f1aedcf6d1fe0bceaf1418c0d5ad9a65bbb/README.md), [MIT license](https://github.com/gilbarbara/react-joyride/blob/1fe55f1aedcf6d1fe0bceaf1418c0d5ad9a65bbb/LICENSE), and opening control implementations in [useControls.ts](https://github.com/gilbarbara/react-joyride/blob/1fe55f1aedcf6d1fe0bceaf1418c0d5ad9a65bbb/src/hooks/useControls.ts).

The README demonstrates component and hook APIs; the inspected control logic separates running state and controlled navigation. Candidate for a React application needing an optional guided interaction. Do not mix API versions when copying examples, equate tour completion with activation, or assume a library's accessibility claims verify the composed app.

## Shepherd

Repository: [shipshapecode/shepherd](https://github.com/shipshapecode/shepherd).

Snapshot: `7f25ce5db4fb3f809fc9ab10e5d9cef8fbde732d`.

Read: [README](https://github.com/shipshapecode/shepherd/blob/7f25ce5db4fb3f809fc9ab10e5d9cef8fbde732d/README.md), [license](https://github.com/shipshapecode/shepherd/blob/7f25ce5db4fb3f809fc9ab10e5d9cef8fbde732d/LICENSE.md), and initial setup/events/options in [usage guide](https://github.com/shipshapecode/shepherd/blob/7f25ce5db4fb3f809fc9ab10e5d9cef8fbde732d/docs-src/src/content/docs/guides/usage.md).

The guide exposes attached steps, lifecycle events, cancellation and escape configuration. Candidate for structured contextual guidance. Its license file describes AGPL-3.0/commercial licensing and additional usage guidance; do not treat it as MIT or automatically install it into a proprietary product. Review the exact terms with the appropriate owner. This note reports upstream material, not legal advice.

## Selection rule

First decide whether a tour is needed at all. Native forms, useful empty states and inline help may solve the task without another library. If a tour is justified, compare framework fit, license, size against project constraints, focus/keyboard behavior, reduced motion, route transitions, lazy targets, nested scroll areas, cancellation and testability. Pin the chosen version and test the integrated flow. None of these libraries supplies the entire onboarding strategy, consent model, pricing policy or persistence contract.
