# Reusable Ecommerce Prompt Engineering

## Prompt Architecture

Use this structure for reusable prompts:

```text
PROMPT NAME

Purpose:
[What business task this prompt completes and when to use it]

Inputs:
- [BRAND]
- [PRODUCT]
- [TARGET CUSTOMER]
- [VERIFIED FEATURES]
- [VERIFIED PROOF]
- [OFFER]
- [BRAND VOICE]
- [CHANNEL]
- [CONSTRAINTS]

Prompt:
You are [RELEVANT EXPERT ROLE].

Objective:
[Specific business and communication outcome]

Context:
[Audience, funnel stage, channel, product, and voice information]

Instructions:
1. Analyze the supplied inputs and identify the primary message.
2. Use only verified facts. Mark missing information rather than inventing it.
3. [Task-specific writing steps]
4. Audit the draft against the constraints and revise it before returning.

Constraints:
- [Length and formatting]
- [Required elements]
- [Banned or risky patterns]

Output format:
[Exact output contract]
```

## Design Rules

- Use uppercase square-bracket variables consistently: `[PRODUCT NAME]`.
- Define every variable used in the prompt.
- Separate inputs from instructions so users can update the prompt safely.
- Specify the output's count, fields, order, and length.
- Ask for distinct strategic variants, not cosmetic rewrites.
- Include a non-fabrication rule in prompts involving facts, proof, policies, reviews, scarcity, or claims.
- Tell the model to flag missing critical inputs and continue with placeholders when possible.
- Avoid asking for hidden chain-of-thought. Request a brief rationale, checklist, or score only when useful.
- Keep prompts portable across mainstream text-generation models unless the user requests platform-specific syntax.

## Advanced Prompt Patterns

Use these only when they improve the task:

- **Brief normalization:** First convert messy inputs into a structured brief, flagging missing or contradictory details.
- **Angle matrix:** Generate distinct concepts across audience pain, desired outcome, differentiator, proof, use case, and objection before drafting variants.
- **Generate-critic-revise:** Draft, score against a task-specific rubric, then silently revise weak areas before returning the final.
- **Constraint-first drafting:** Put non-negotiable claims, policy, length, or platform restrictions before stylistic preferences.
- **Few-shot calibration:** Include one or two short examples when a precise house style or format is difficult to describe. Explain what each example demonstrates.
- **Batch consistency:** Require a shared voice and non-repeating angle labels when generating a content set.
- **Conditional behavior:** State what to do when evidence, policy details, or brand guidance is missing.

Do not add elaborate multi-stage instructions to simple tasks. More prompt text is useful only when it removes ambiguity or improves repeatability.

## Evaluation Strategy

For high-value prompts, test with at least three different products or scenarios:

1. A product with complete facts and strong proof
2. A product with missing inputs and claim-sensitive benefits
3. A different category, channel, or audience than the original example

Check whether the prompt:

- Preserves facts and flags unknowns
- Produces genuinely different angles
- Follows exact counts and formatting
- Adapts to channel and awareness stage
- Remains useful outside the original product category

## Assignment Workflow: 10-Prompt Library

For an assignment requesting 10 reusable prompts across the listed categories, use this exact coverage:

1. Short product description
2. Long product description
3. Blog introduction
4. Email subject lines
5. Ad headlines
6. Social captions
7. FAQ answers
8. Positive review response
9. Negative review response
10. Brand voice guide

Treat positive and negative review responses as separate templates because their risks, tone, and resolution goals differ.

## Prompt Library Document Structure

Build the submission-ready document in this order:

1. Title
2. Purpose and usage instructions
3. Placeholder key
4. Ten numbered prompt templates
5. Quality-control checklist

Each template must include:

- Purpose
- Best-use context
- Required inputs
- Copy-ready prompt
- Explicit output format
- At least one safety or quality constraint relevant to the task

Do not fill the document with sample outputs unless the assignment requests them. The deliverable is a reusable prompt library.

## Task-Specific Requirements

### Product Descriptions

Require audience, verified features, benefits, proof, objections, channel, CTA, voice, and limits. Short and long versions must be separate prompts with different output contracts.

### Blog Introduction

Require topic, search intent, reader, article promise, target keyword, voice, and length. Ban generic dictionary openings and unsupported statistics.

### Email Subject Lines

Require email goal, offer, segment, awareness level, voice, and character limit. Request variants across distinct angles and prohibit misleading urgency.

### Ad Headlines

Require platform, audience, product, differentiator, proof, offer, awareness level, and character limit. Request angle labels and distinct concepts.

### Social Captions

Require platform, content asset, goal, audience, voice, CTA, length, emoji, and hashtag preferences. Ensure the hook fits the platform.

### FAQ Answers

Require real questions plus verified policy or product facts. Instruct the model to answer first, stay concise, and flag missing policy information.

### Review Responses

Positive prompt: personalize gratitude, reinforce the mentioned benefit, and avoid hard selling.

Negative prompt: acknowledge specifics, avoid defensiveness and invented resolutions, protect private data, and offer a practical next step.

### Brand Voice Guide

Require brand purpose, audience, positioning, values, personality, examples, competitors, and banned language. Output observable rules and before-and-after examples, not adjectives alone.

## Prompt QA Checklist

- Does the prompt have one clear task?
- Are all placeholders defined and consistently formatted?
- Can it work for a different product without rewriting the instructions?
- Does it specify audience, channel, and commercial goal?
- Does it prevent invented facts and unsafe claims?
- Does it produce a predictable, usable output format?
- Does it demand meaningful strategic variation where needed?
- Does it include a final quality check?
