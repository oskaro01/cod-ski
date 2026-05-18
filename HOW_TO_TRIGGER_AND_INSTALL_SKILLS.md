# How To Trigger And Install Skills

Use this as a quick reminder for how Codex skills work.

## How A Skill Gets Triggered

A skill can be triggered in two ways.

### 1. Explicit Trigger

You directly name the skill in your message.

Examples:

```text
Use the competitor-analysis-supervisor skill to make a competitor analysis.
```

```text
$competitor-analysis-supervisor
Analyze these products against competitors.
```

This is the clearest and safest method.

### 2. Natural-Language Trigger

You ask for something that matches the skill description.

For this skill, Codex should use it when you ask for things like:

```text
Make a competitor analysis for these 3 dropshipping products.
```

```text
Find 3 competitors for each product and compare price, reviews, USP, and weaknesses.
```

```text
Create a competitor-analysis-doc.md for my product research.
```

```text
Make a positioning map for these ecommerce products.
```

Simple rule:

```text
If I say "competitor analysis", this skill should wake up.
If I say the exact skill name, it definitely wakes up.
```

## What Makes A Skill Installable

When installing or creating future skills, look for these things.

### Required

A skill folder must contain:

```text
SKILL.md
```

The `SKILL.md` file should start with frontmatter like this:

```yaml
---
name: some-skill-name
description: Clear explanation of when this skill should be used.
---
```

The `name` is what you can call directly.

The `description` is what Codex uses to decide whether your request matches the skill.

### Good To Have

A good skill usually has clear sections like:

```text
Core Workflow
Required Output
Analysis Standards
References
```

It may also include support folders like:

```text
references/
scripts/
templates/
assets/
```

These are useful, but not required.

## Quick Checklist For Future Skills

Before trusting a skill, check:

```text
Does it have SKILL.md?
Does SKILL.md have name and description at the top?
Is the description specific enough to trigger the skill?
Does it explain the workflow clearly?
Does it say what output should be created?
Does it include references, scripts, or templates if needed?
```

## For This Skill Specifically

Skill name:

```text
competitor-analysis-supervisor
```

Best trigger phrase:

```text
Use competitor-analysis-supervisor to create a competitor analysis document.
```

Expected default output:

```text
competitor-analysis-doc.md
```

