# Ecommerce Prompt Template Library

## Purpose

This library contains 10 reusable AI prompts for common ecommerce content-writing tasks. Each template is designed to produce channel-appropriate, conversion-focused content while protecting against invented facts, unsupported claims, and inconsistent brand voice.

## How to Use This Library

1. Select the prompt template that matches the content you need.
2. Replace every uppercase placeholder in square brackets with accurate information.
3. Remove optional inputs that do not apply.
4. Paste the completed prompt into an AI writing tool.
5. Review the result for factual accuracy, brand fit, and platform requirements before publishing.

Never provide a claim, review, policy, certification, discount, or scarcity statement unless it is verified.

## Shared Placeholder Key

| Placeholder | What to provide |
|---|---|
| `[BRAND NAME]` | Store or brand name |
| `[PRODUCT NAME]` | Exact product name |
| `[PRODUCT CATEGORY]` | Product type or category |
| `[TARGET CUSTOMER]` | Specific intended customer |
| `[CUSTOMER SITUATION]` | Moment, problem, or use case |
| `[DESIRED OUTCOME]` | Result the customer wants |
| `[VERIFIED FEATURES]` | Confirmed product specifications or capabilities |
| `[VERIFIED PROOF]` | Supported test results, certifications, ratings, or other evidence |
| `[DIFFERENTIATOR]` | Credible reason to choose this product |
| `[CUSTOMER OBJECTIONS]` | Main concerns that may prevent purchase |
| `[OFFER DETAILS]` | Verified price, promotion, bundle, guarantee, or shipping terms |
| `[BRAND VOICE]` | Observable tone and style rules |
| `[CALL TO ACTION]` | Desired next action |
| `[CHANNEL]` | Store page, marketplace, email, social platform, or ad platform |
| `[CONSTRAINTS]` | Word limit, character limit, banned terms, or required details |
| `[BLOG TOPIC]` | Specific subject of the article |
| `[TARGET KEYWORD]` | Primary search phrase the article should address |
| `[SEARCH INTENT]` | What the searcher wants to learn, compare, or accomplish |
| `[TARGET READER]` | Intended reader of an article |
| `[READER PROBLEM]` | Immediate question or challenge bringing the reader to the article |
| `[ARTICLE PROMISE]` | Useful knowledge or outcome the article will provide |
| `[EMAIL GOAL]` | Primary action or result intended from the email |
| `[EMAIL CONTENT]` | Accurate summary of what the email contains |
| `[AUDIENCE SEGMENT]` | Defined group receiving the email |
| `[AWARENESS STAGE]` | Unaware, problem-aware, solution-aware, product-aware, or most aware |
| `[SUBJECT CHARACTER LIMIT]` | Maximum permitted email-subject length |
| `[AD PLATFORM]` | Advertising platform where the headline will run |
| `[HEADLINE CHARACTER LIMIT]` | Maximum permitted ad-headline length |
| `[SOCIAL PLATFORM]` | Social network where the post will appear |
| `[CONTENT ASSET]` | Photo, video, carousel, article, or other media accompanying the caption |
| `[POST GOAL]` | Awareness, engagement, traffic, conversion, education, or community goal |
| `[KEY MESSAGE]` | Single main idea the post should communicate |
| `[VERIFIED PRODUCT FACTS]` | Confirmed facts available for FAQs or social content |
| `[EMOJI PREFERENCE]` | Whether and how emojis should be used |
| `[HASHTAG PREFERENCE]` | Number, style, or restrictions for hashtags |
| `[CUSTOMER QUESTIONS]` | Actual questions requiring FAQ answers |
| `[VERIFIED POLICIES]` | Confirmed shipping, return, warranty, or service rules |
| `[IMPORTANT LIMITATIONS]` | Relevant exclusions, risks, compatibility notes, or restrictions |
| `[CALL TO ACTION OR SUPPORT PATH]` | Appropriate next step or customer-support route |
| `[CUSTOMER NAME]` | Public customer name, or blank when unavailable |
| `[REVIEW TEXT]` | Customer's original review |
| `[VERIFIED POLICY OR RESOLUTION OPTIONS]` | Confirmed actions support may offer for a complaint |
| `[SUPPORT CONTACT METHOD]` | Private channel for account-specific help |
| `[BRAND PURPOSE]` | Reason the brand exists beyond selling products |
| `[POSITIONING]` | Distinct place the brand aims to own in the customer's mind |
| `[BRAND VALUES]` | Principles guiding brand decisions and behavior |
| `[DESIRED PERSONALITY]` | Human qualities the brand should express |
| `[EXISTING CONTENT EXAMPLES]` | Approved examples showing the current or desired voice |
| `[COMPETITOR OR CATEGORY CONTEXT]` | Relevant market conventions and differentiation context |
| `[WORDS TO USE]` | Preferred vocabulary and phrases |
| `[WORDS TO AVOID]` | Banned, overused, or off-brand vocabulary |

---

## 1. Short Product Description Prompt

**Purpose:** Create a concise product description that communicates the strongest customer benefit and supports a purchase decision.

**Best used for:** Collection pages, marketplace listings, quick-view panels, product cards, and short product-page summaries.

**Required inputs:** `[BRAND NAME]`, `[PRODUCT NAME]`, `[TARGET CUSTOMER]`, `[CUSTOMER SITUATION]`, `[DESIRED OUTCOME]`, `[VERIFIED FEATURES]`, `[DIFFERENTIATOR]`, `[BRAND VOICE]`, `[CALL TO ACTION]`, `[CHANNEL]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are an ecommerce conversion copywriter.

Create a short product description for the following product:

- Brand: [BRAND NAME]
- Product: [PRODUCT NAME]
- Target customer: [TARGET CUSTOMER]
- Customer situation or problem: [CUSTOMER SITUATION]
- Desired outcome: [DESIRED OUTCOME]
- Verified features: [VERIFIED FEATURES]
- Main differentiator: [DIFFERENTIATOR]
- Brand voice: [BRAND VOICE]
- Call to action: [CALL TO ACTION]
- Publishing channel: [CHANNEL]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Identify the single strongest value proposition for this customer.
2. Lead with the desired outcome, then connect one or two verified features to practical benefits.
3. Make the differentiator clear without attacking competitors.
4. End with a natural call to action.
5. Use only the supplied facts. Do not invent proof, results, awards, urgency, or product capabilities.
6. If a critical fact is missing, use a clearly labeled placeholder instead of guessing.
7. Silently revise the description if it is generic, repetitive, or unsuitable for the channel.

Output format:
- One finished product description
- 40-80 words unless [CONSTRAINTS] specifies otherwise
- One optional headline of no more than 8 words
```

---

## 2. Long Product Description Prompt

**Purpose:** Create a detailed, scannable product description that explains value, supports claims, handles objections, and encourages conversion.

**Best used for:** Ecommerce product pages, Shopify stores, marketplace enhanced content, and landing pages.

**Required inputs:** `[BRAND NAME]`, `[PRODUCT NAME]`, `[PRODUCT CATEGORY]`, `[TARGET CUSTOMER]`, `[CUSTOMER SITUATION]`, `[DESIRED OUTCOME]`, `[VERIFIED FEATURES]`, `[VERIFIED PROOF]`, `[DIFFERENTIATOR]`, `[CUSTOMER OBJECTIONS]`, `[OFFER DETAILS]`, `[BRAND VOICE]`, `[CALL TO ACTION]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are a senior ecommerce product-page copywriter.

Write a long-form product description using this verified brief:

- Brand: [BRAND NAME]
- Product: [PRODUCT NAME]
- Category: [PRODUCT CATEGORY]
- Target customer: [TARGET CUSTOMER]
- Customer situation or problem: [CUSTOMER SITUATION]
- Desired outcome: [DESIRED OUTCOME]
- Verified features and specifications: [VERIFIED FEATURES]
- Verified proof: [VERIFIED PROOF]
- Main differentiator: [DIFFERENTIATOR]
- Customer objections: [CUSTOMER OBJECTIONS]
- Offer details: [OFFER DETAILS]
- Brand voice: [BRAND VOICE]
- Call to action: [CALL TO ACTION]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Create one clear value proposition based on the customer's desired outcome.
2. Translate verified features into practical benefits without exaggerating results.
3. Explain the product's differentiator and support it with the supplied proof.
4. Address the most important objections, limitations, compatibility notes, care instructions, or risks where relevant.
5. Make the description easy to scan with useful headings and bullets.
6. Use only supplied facts. Clearly label missing proof or policy details rather than inventing them.
7. Avoid generic superlatives, fake scarcity, unsupported comparisons, and repetitive claims.
8. Audit and revise the draft for specificity, credibility, readability, and conversion logic before returning it.

Output format:
1. Product headline
2. Value-proposition paragraph
3. Three to five benefit-led sections
4. Key features or specifications list
5. Objection-handling or "Good to know" section
6. Offer and call-to-action section

Target length: 350-600 words unless [CONSTRAINTS] specifies otherwise.
```

---

## 3. Blog Introduction Prompt

**Purpose:** Write a focused introduction that matches search intent, establishes relevance, and encourages the reader to continue.

**Best used for:** Ecommerce blog posts, buying guides, educational articles, gift guides, and search-focused content.

**Required inputs:** `[BLOG TOPIC]`, `[TARGET KEYWORD]`, `[SEARCH INTENT]`, `[TARGET READER]`, `[READER PROBLEM]`, `[ARTICLE PROMISE]`, `[BRAND NAME]`, `[BRAND VOICE]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are an ecommerce content strategist and SEO copywriter.

Write the introduction for this article:

- Blog topic: [BLOG TOPIC]
- Primary target keyword: [TARGET KEYWORD]
- Search intent: [SEARCH INTENT]
- Target reader: [TARGET READER]
- Reader's immediate problem or question: [READER PROBLEM]
- Useful promise of the article: [ARTICLE PROMISE]
- Brand: [BRAND NAME]
- Brand voice: [BRAND VOICE]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Match the reader's search intent in the opening sentence.
2. Make the problem recognizable and explain why the article will be useful.
3. Preview what the reader will learn without summarizing the whole article.
4. Use the primary keyword naturally, without keyword stuffing.
5. Do not open with a dictionary definition, a broad history lesson, "In today's world," or an unsupported statistic.
6. Do not make product claims or promises that are not supported by the brief.
7. Silently revise the introduction if it is slow, generic, or overly promotional.

Output format:
- One finished introduction
- Two or three short paragraphs
- 90-150 words unless [CONSTRAINTS] specifies otherwise
- No heading unless requested
```

---

## 4. Email Subject Lines Prompt

**Purpose:** Generate strategically different subject lines and preheaders that accurately represent an ecommerce email.

**Best used for:** Promotional campaigns, product launches, abandoned-cart emails, welcome flows, win-back emails, and educational newsletters.

**Required inputs:** `[EMAIL GOAL]`, `[EMAIL CONTENT]`, `[AUDIENCE SEGMENT]`, `[AWARENESS STAGE]`, `[OFFER DETAILS]`, `[BRAND VOICE]`, `[SUBJECT CHARACTER LIMIT]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are an ecommerce email strategist specializing in ethical, high-performing subject lines.

Create subject lines and preheaders for this email:

- Email goal: [EMAIL GOAL]
- What the email actually contains: [EMAIL CONTENT]
- Audience segment: [AUDIENCE SEGMENT]
- Customer awareness stage: [AWARENESS STAGE]
- Verified offer details: [OFFER DETAILS]
- Brand voice: [BRAND VOICE]
- Subject-line character limit: [SUBJECT CHARACTER LIMIT]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Create 10 subject lines built around distinct strategic angles: benefit, curiosity, specificity, direct offer, problem, desired outcome, social proof, objection, timely relevance, and brand personality.
2. Pair every subject line with a preheader that adds information instead of repeating it.
3. Match the audience's awareness stage and the email's actual content.
4. Do not use fake urgency, misleading claims, deceptive "Re:" or "Fwd:", invented personalization, or unsupported scarcity.
5. Keep every subject line within the supplied character limit.
6. Audit the set and replace any repetitive or cosmetic variations.

Output format:
Create a table with these columns:
1. Number
2. Strategic angle
3. Subject line
4. Character count
5. Preheader
```

---

## 5. Ad Headlines Prompt

**Purpose:** Generate concise, distinct ad headlines based on credible customer and offer angles.

**Best used for:** Meta ads, Google ads, TikTok ads, display ads, marketplace ads, and creative testing.

**Required inputs:** `[AD PLATFORM]`, `[PRODUCT NAME]`, `[TARGET CUSTOMER]`, `[CUSTOMER SITUATION]`, `[DESIRED OUTCOME]`, `[DIFFERENTIATOR]`, `[VERIFIED PROOF]`, `[OFFER DETAILS]`, `[AWARENESS STAGE]`, `[BRAND VOICE]`, `[HEADLINE CHARACTER LIMIT]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are a direct-response ecommerce advertising copywriter.

Generate ad headlines using this brief:

- Ad platform: [AD PLATFORM]
- Product: [PRODUCT NAME]
- Target customer: [TARGET CUSTOMER]
- Customer situation or problem: [CUSTOMER SITUATION]
- Desired outcome: [DESIRED OUTCOME]
- Main differentiator: [DIFFERENTIATOR]
- Verified proof: [VERIFIED PROOF]
- Verified offer details: [OFFER DETAILS]
- Customer awareness stage: [AWARENESS STAGE]
- Brand voice: [BRAND VOICE]
- Headline character limit: [HEADLINE CHARACTER LIMIT]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Create 12 headlines across distinct angles: problem, outcome, use case, differentiator, proof, objection, offer, convenience, identity, comparison without naming competitors, curiosity, and direct response.
2. Express only one main idea in each headline.
3. Make each headline clear without relying on the image or body copy.
4. Follow the platform and character-limit requirements.
5. Do not invent proof, guarantees, scarcity, or results. Avoid personal-attribute targeting and unsupported superlatives.
6. Replace any headline that is merely a synonym-based variation of another.
7. Audit the final set for clarity, strategic variety, credibility, and platform fit.

Output format:
Create a table with these columns:
1. Number
2. Strategic angle
3. Headline
4. Character count
5. Supporting fact used
```

---

## 6. Social Media Captions Prompt

**Purpose:** Create platform-appropriate social captions that support a defined content and business goal.

**Best used for:** Instagram, TikTok, Facebook, Pinterest, LinkedIn, and other organic social posts.

**Required inputs:** `[SOCIAL PLATFORM]`, `[CONTENT ASSET]`, `[POST GOAL]`, `[TARGET CUSTOMER]`, `[KEY MESSAGE]`, `[VERIFIED PRODUCT FACTS]`, `[BRAND VOICE]`, `[CALL TO ACTION]`, `[EMOJI PREFERENCE]`, `[HASHTAG PREFERENCE]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are an ecommerce social media copywriter.

Create captions for this social post:

- Platform: [SOCIAL PLATFORM]
- Content asset or visual: [CONTENT ASSET]
- Post goal: [POST GOAL]
- Target customer: [TARGET CUSTOMER]
- Key message: [KEY MESSAGE]
- Verified product facts: [VERIFIED PRODUCT FACTS]
- Brand voice: [BRAND VOICE]
- Call to action: [CALL TO ACTION]
- Emoji preference: [EMOJI PREFERENCE]
- Hashtag preference: [HASHTAG PREFERENCE]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Write a hook that fits the platform and complements the visual.
2. Build the caption around one clear message and the requested post goal.
3. Use only verified product facts and avoid unsupported results or urgency.
4. Make the call to action appropriate for the audience and platform.
5. Use emojis and hashtags intentionally according to the supplied preferences.
6. Produce meaningfully different caption approaches, not minor rewrites.
7. Audit the captions for clarity, brand consistency, and platform fit.

Output format:
Provide three caption versions:
1. Short direct-response caption
2. Story-led caption
3. Educational or community-focused caption

For each version, include:
- Angle label
- Finished caption
- Suggested call to action
- Suggested hashtags, if requested
```

---

## 7. FAQ Answers Prompt

**Purpose:** Turn real customer questions and verified business information into clear, trustworthy FAQ answers.

**Best used for:** Product pages, help centers, shipping pages, return pages, marketplace listings, and customer-support macros.

**Required inputs:** `[CUSTOMER QUESTIONS]`, `[VERIFIED PRODUCT FACTS]`, `[VERIFIED POLICIES]`, `[IMPORTANT LIMITATIONS]`, `[BRAND VOICE]`, `[CALL TO ACTION OR SUPPORT PATH]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are an ecommerce customer-experience writer.

Write FAQ answers using only the following information:

- Customer questions: [CUSTOMER QUESTIONS]
- Verified product facts: [VERIFIED PRODUCT FACTS]
- Verified shipping, return, warranty, or service policies: [VERIFIED POLICIES]
- Important limitations, exclusions, or compatibility details: [IMPORTANT LIMITATIONS]
- Brand voice: [BRAND VOICE]
- Call to action or support path: [CALL TO ACTION OR SUPPORT PATH]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Preserve each customer's question and answer it directly in the first sentence.
2. Add only the context, caveats, instructions, and next steps needed to prevent confusion.
3. Use calm, plain language and make each answer easy to scan.
4. Never invent policy details, timelines, compatibility, safety guidance, or product capabilities.
5. If the supplied information cannot answer a question, write: "Needs confirmation:" followed by the missing information.
6. Keep related answers consistent and remove repetitive wording.
7. Audit the final set for accuracy, clarity, and customer usefulness.

Output format:
For each FAQ, provide:
- Question
- Short answer
- Important details or limitations
- Next step, when relevant

Keep each complete answer under 120 words unless [CONSTRAINTS] specifies otherwise.
```

---

## 8. Positive Review Response Prompt

**Purpose:** Write personalized, appreciative responses to positive customer reviews without sounding automated or overly promotional.

**Best used for:** Store reviews, marketplaces, Google Business profiles, social comments, and post-purchase reputation management.

**Required inputs:** `[CUSTOMER NAME]`, `[REVIEW TEXT]`, `[PRODUCT NAME]`, `[BRAND NAME]`, `[BRAND VOICE]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are a thoughtful ecommerce community manager.

Write a response to this positive customer review:

- Customer name, if public: [CUSTOMER NAME]
- Review text: [REVIEW TEXT]
- Product: [PRODUCT NAME]
- Brand: [BRAND NAME]
- Brand voice: [BRAND VOICE]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Thank the customer naturally.
2. Reference one specific detail from the review so the response feels personal.
3. Reinforce the benefit or experience the customer mentioned without adding unsupported claims.
4. Keep the response warm and concise.
5. Do not copy the review back to the customer, reveal private information, overuse exclamation marks, or turn the response into a hard sell.
6. Do not invent a customer name when one is not provided.
7. Silently revise the response if it sounds generic or scripted.

Output format:
- One finished public response
- 40-80 words unless [CONSTRAINTS] specifies otherwise
```

---

## 9. Negative Review Response Prompt

**Purpose:** Respond to negative reviews with empathy, specificity, and a practical resolution path while protecting customer privacy.

**Best used for:** Store reviews, marketplaces, social comments, and public reputation-management channels.

**Required inputs:** `[CUSTOMER NAME]`, `[REVIEW TEXT]`, `[PRODUCT NAME]`, `[VERIFIED POLICY OR RESOLUTION OPTIONS]`, `[SUPPORT CONTACT METHOD]`, `[BRAND NAME]`, `[BRAND VOICE]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are an experienced ecommerce reputation and customer-support manager.

Write a public response to this negative customer review:

- Customer name, if public: [CUSTOMER NAME]
- Review text: [REVIEW TEXT]
- Product: [PRODUCT NAME]
- Verified policy or available resolution options: [VERIFIED POLICY OR RESOLUTION OPTIONS]
- Private support contact method: [SUPPORT CONTACT METHOD]
- Brand: [BRAND NAME]
- Brand voice: [BRAND VOICE]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Acknowledge the customer's specific experience and frustration without arguing or blaming them.
2. Apologize for the experience when appropriate, but do not admit unsupported legal liability.
3. State only verified resolution options or policies.
4. Offer a clear next step and move order-specific details to the private support channel.
5. Do not request or reveal order numbers, addresses, payment details, or other private information publicly.
6. Do not invent a refund, replacement, guarantee, policy exception, or investigation outcome.
7. Keep the tone calm, respectful, and concise.
8. Silently revise the response if it sounds defensive, dismissive, or scripted.

Output format:
- One finished public response
- 60-120 words unless [CONSTRAINTS] specifies otherwise
- One internal note listing any missing information the support team should confirm
```

---

## 10. Brand Voice Guide Prompt

**Purpose:** Create an actionable brand voice guide that keeps ecommerce content consistent across sales, education, and customer support.

**Best used for:** New brands, rebrands, content teams, AI writing systems, freelancers, agencies, and multi-channel ecommerce operations.

**Required inputs:** `[BRAND NAME]`, `[BRAND PURPOSE]`, `[TARGET CUSTOMER]`, `[POSITIONING]`, `[BRAND VALUES]`, `[DESIRED PERSONALITY]`, `[EXISTING CONTENT EXAMPLES]`, `[COMPETITOR OR CATEGORY CONTEXT]`, `[WORDS TO USE]`, `[WORDS TO AVOID]`, and `[CONSTRAINTS]`.

**Copy-ready prompt:**

```text
You are a senior brand strategist and ecommerce editorial director.

Create an actionable brand voice guide using this brief:

- Brand: [BRAND NAME]
- Brand purpose: [BRAND PURPOSE]
- Target customer: [TARGET CUSTOMER]
- Positioning and differentiator: [POSITIONING]
- Brand values: [BRAND VALUES]
- Desired personality: [DESIRED PERSONALITY]
- Existing content examples: [EXISTING CONTENT EXAMPLES]
- Competitor or category context: [COMPETITOR OR CATEGORY CONTEXT]
- Words or phrases to use: [WORDS TO USE]
- Words or phrases to avoid: [WORDS TO AVOID]
- Additional constraints: [CONSTRAINTS]

Instructions:
1. Translate the brief into observable writing rules, not personality adjectives alone.
2. Define the brand's role in the customer's life and the relationship it should create.
3. Create three to five voice pillars. For each pillar, explain what it means, how it appears in writing, and what to avoid.
4. Explain how tone should adapt across product pages, advertising, educational content, positive interactions, and complaints.
5. Define vocabulary, sentence rhythm, formatting, humor, emoji, urgency, and call-to-action rules.
6. Provide before-and-after examples that demonstrate the voice.
7. Do not imitate a competitor or invent brand facts that are not supplied.
8. Identify contradictions or missing inputs, then create clearly labeled provisional guidance where necessary.
9. Audit the guide for clarity, distinctiveness, and practical usability.

Output format:
1. Brand voice summary
2. Audience relationship and brand role
3. Voice pillars table
4. "We sound like / We do not sound like" table
5. Tone-by-situation table
6. Vocabulary and writing-mechanics rules
7. Five before-and-after examples
8. Final do-and-don't checklist
```

---

## Quality-Control Checklist

Before using or submitting AI-generated ecommerce content, confirm:

- All placeholders were replaced or intentionally marked for confirmation.
- Every factual, product, policy, review, certification, and offer claim is verified.
- The content is specific to the product, customer, channel, and goal.
- Features are connected to practical customer benefits without exaggeration.
- The message fits the customer's awareness stage.
- The output follows the requested word count, character count, structure, and number of variants.
- The brand voice is consistent and observable.
- Headline, subject-line, and caption variants use genuinely different strategic angles.
- Compatibility details, limitations, safety notes, and exclusions are included where relevant.
- The call to action is clear and appropriate.
- The final content has been reviewed by a human before publication.
