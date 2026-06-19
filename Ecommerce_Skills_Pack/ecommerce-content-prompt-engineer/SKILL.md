---
name: ecommerce-content-prompt-engineer
description: Create, improve, and evaluate conversion-focused ecommerce content and reusable AI prompt systems. Use for product descriptions, landing-page copy, blog content, email subject lines, ads, social captions, FAQs, customer-review responses, brand voice guides, content calendars, prompt libraries, prompt templates, and ecommerce copy audits. Apply when content must be persuasive, brand-consistent, channel-specific, reusable, and careful about unsupported claims.
---

# Ecommerce Content Prompt Engineer

Create ecommerce content that is specific, useful, credible, and built for a clear commercial purpose. Design prompts as reusable operating instructions, not one-off requests.

## Core Workflow

1. Define the deliverable, audience, channel, buying stage, and desired action.
2. Gather or infer the minimum viable brief. Mark assumptions and unknown facts.
3. Select a copy framework and channel constraints.
4. Draft with concrete benefits, proof, objection handling, and brand voice.
5. Audit the output for specificity, claims, usability, and conversion quality.
6. Deliver in the requested format with clear placeholders where facts will vary.

For reusable prompt libraries, follow the additional workflow in `references/prompt-engineering.md`.

## Minimum Viable Brief

Collect these inputs when available:

- Brand, product, category, and offer
- Target customer, situation, pain point, and desired outcome
- Verified features, benefits, proof, differentiators, and objections
- Price, promotion, guarantee, shipping, returns, and call to action
- Channel, funnel stage, word or character limit, and number of variants
- Brand voice, banned language, regulated-claim limits, and competitor context

Do not block progress when inputs are missing. Use explicit placeholders such as `[PRODUCT]`, `[TARGET CUSTOMER]`, and `[VERIFIED PROOF]`, or state concise assumptions.

## Content Strategy

Choose the primary job before writing:

- **Discoverability:** Match search intent and make the topic easy to understand.
- **Consideration:** Explain relevance, benefits, proof, and tradeoffs.
- **Conversion:** Reduce uncertainty, answer objections, and make the next action clear.
- **Retention:** Help customers succeed, build trust, and encourage repeat purchase.
- **Reputation:** Respond calmly, acknowledge specifics, and move toward resolution.

Use one dominant message per asset. Do not crowd a short asset with every possible benefit.

## Copy Standards

- Translate features into customer-relevant benefits without inventing outcomes.
- Prefer concrete language over generic claims such as "premium," "revolutionary," or "best."
- Lead with the strongest relevant value, not company biography.
- Match awareness level: explain more to cold audiences and remove friction for warm audiences.
- Use proof only when provided or verified. Never fabricate reviews, scarcity, certifications, results, guarantees, or comparisons.
- Keep claims proportionate. For health, beauty, safety, environmental, financial, and performance claims, distinguish fact from suggestion and request evidence when needed.
- Preserve important limitations, compatibility notes, care instructions, and exclusions.
- Make the call to action natural and appropriate to the funnel stage.

Read `references/ecommerce-copy-frameworks.md` when selecting structures or writing channel-specific content.

## Prompt Engineering Standards

Build reusable prompts with these components:

1. **Role and objective:** Define the expert behavior and business outcome.
2. **Inputs:** Use clearly named placeholders for changing information.
3. **Context:** Include audience, channel, funnel stage, and brand voice.
4. **Process:** Tell the model how to reason through the task without requesting hidden chain-of-thought.
5. **Constraints:** Set length, format, claim safety, banned patterns, and required elements.
6. **Output contract:** Specify exact sections, tables, fields, or variant counts.
7. **Quality check:** Require a final audit and revision before returning the answer.

Prompts must work after placeholders are replaced by a different product or brand. Avoid vague instructions like "make it engaging" unless they are paired with observable criteria.

Read `references/prompt-engineering.md` for the reusable prompt architecture, variable conventions, and the 10-template-library specification.

## Brand Voice

Treat voice as a decision system, not a list of adjectives. Define:

- Audience relationship and brand role
- Voice pillars with observable writing behavior
- Tone shifts by situation
- Vocabulary to use and avoid
- Sentence rhythm, formatting, humor, urgency, and emoji rules
- Before-and-after examples

When no brand voice exists, create a compact provisional guide before producing a large content set.

## Quality Gate

Revise before delivery if any answer fails these checks:

- **Accuracy:** All factual and comparative claims are supported or clearly marked.
- **Specificity:** The copy could not be pasted unchanged onto most competing products.
- **Audience fit:** It reflects a real customer situation, motive, or objection.
- **Channel fit:** Length, structure, CTA, and tone suit the destination.
- **Voice consistency:** Word choice and rhythm follow the stated brand rules.
- **Conversion logic:** The asset has one clear message and next step.
- **Readability:** It is concise, scannable, and free of filler or repetition.
- **Reusability:** Prompt templates have complete placeholders and explicit outputs.

For formal audits or graded assignments, score the work using `references/quality-rubric.md`.

## Delivery Rules

- Produce finished content, not commentary about what could be written.
- For prompt libraries, include a short usage guide, consistent placeholder syntax, and one complete template per requested use case.
- Separate verified inputs from assumptions when accuracy matters.
- Explain strategic choices briefly only when they help the user apply or evaluate the work.
- If asked to create a document, use clear headings and a submission-ready structure.

## References

- `references/ecommerce-copy-frameworks.md`: Copy frameworks and format-specific requirements.
- `references/prompt-engineering.md`: Reusable prompt construction and prompt-library workflow.
- `references/quality-rubric.md`: Scoring rubric and failure-pattern checklist.
