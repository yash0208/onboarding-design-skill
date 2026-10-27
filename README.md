# Onboarding Design Skill

Help people understand a product, reach a useful result, and decide whether it belongs in their workflow.

A research-informed agent skill for onboarding **journey, UI, copy, activation, returning-user setup, and paid-plan fit**. It works with an existing product's constraints and design tokens—not a prescribed six-screen wizard or a tooltip tour pasted onto every app.

## What you get

- A reasoned route from product promise to first useful outcome.
- A field-by-field decision about what to ask now, later, or not at all.
- New, invited, returning, and interrupted-user paths.
- Clear screens, accessible forms, recovery states, and consent choices.
- Concrete benefits without invented time-savings or productivity figures.
- Contextual upgrades when paid plans actually exist, with clear costs and alternatives.
- Measurement and acceptance criteria that distinguish completion from value.

The package contains instructions and templates, not an application, analytics SDK, billing integration, or promised conversion increase. It has no runtime dependencies. Research is curated, not exhaustive; its applicability and limits are recorded in the [source ledger](skills/onboarding-design/references/research.md). Three [public repositories](skills/onboarding-design/references/repositories.md) are reviewed as implementation references, not bundled dependencies.

## Install

Clone this repository into a new directory:

```sh
git clone https://github.com/yash0208/onboarding-design-skill.git
```

Copy the **whole** `skills/onboarding-design` directory, including references and assets, into your agent's skill directory. If a skill with that name already exists, review it before replacing anything.

| Agent | Common user-level location | Usage |
| --- | --- | --- |
| Codex | `~/.codex/skills/onboarding-design/` | `$onboarding-design` |
| Claude Code | `~/.claude/skills/onboarding-design/` | `/onboarding-design` |
| Other SKILL.md-compatible tools | The tool's documented skill directory | Use its skill invocation mechanism |

Project-scoped installation is also possible where your tool supports it. `agents/openai.yaml` is optional Codex UI metadata; the instructions do not require OpenAI-specific tools. For tools without skill discovery, provide [SKILL.md](skills/onboarding-design/SKILL.md) and the relevant linked references as context. Verify installation behavior against your tool version; other runtimes have not been execution-tested here.

The Claude Code path and invocation follow its [official skills documentation](https://code.claude.com/docs/en/skills). No agent configuration, permissions, or billing settings need to be changed by this package.

## Try it

```text
Use $onboarding-design to audit our existing signup and first-use journey.
Inspect the product docs and relevant code. Identify the first useful user
outcome and the three highest-impact friction hypotheses. Do not edit code yet.
```

```text
Use $onboarding-design to plan onboarding for new and existing users.
Use our design tokens. Create a local HTML prototype with fictional data,
working back/skip/review states, and no real uploads, analytics, or charges.
We will review it before app integration.
```

```text
Use $onboarding-design to improve trial-to-paid onboarding. Use only the
plans and prices in this repository. Explain who should upgrade and when;
preserve the existing free path. Propose a test, not guaranteed lift.
```

## Package map

Start at [the skill](skills/onboarding-design/SKILL.md). It routes to journey design, UI/copy, value/plans, measurement, and source/library references as needed. Adapt the [brief](skills/onboarding-design/assets/onboarding-brief.md) and [screen specification](skills/onboarding-design/assets/screen-spec.md) rather than filling every section mechanically.

For maintainers: `python3 scripts/validate_package.py` checks packaging, relative links, metadata and accidental private-path/credential patterns. [Behavioral cases](tests/scenarios.md) and [the rubric](tests/rubric.md) test judgment, not keywords. They do not prove usability or commercial outcomes. See [validation notes](tests/VALIDATION.md) for the evidence actually available.

## Contribute

Open an issue or PR with a specific user problem, product constraints, evidence, and the smallest useful change. For source updates, record the retrieval date and scope. Include fictional examples, not real profiles, screenshots, tokens, customer data, or private repository details. Avoid universal rules inferred from a single successful product.

MIT for this package's original work. Linked articles and projects retain their own copyrights and licenses; no third-party source or article text is vendored. No endorsement by the cited organizations is implied.
