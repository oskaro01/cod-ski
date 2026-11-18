# Prompt 2 v1.2 revision notes

## What changed

The prior method made missing search and local social access affect both the Demand Index and overall coverage. v1.2 separates observed demand, availability of demand channels, sample-stage research coverage and commercial confidence.

| Measure | v1.1 | v1.2 |
|---|---|---|
| GCC Demand Index | Marketplace 40%, search 30%, social 30%; missing component meant INCOMPLETE | Marketplace 60%, search 20%, GCC social 20%; explicit FULL/PROVISIONAL/INSUFFICIENT EVIDENCE with demand coverage |
| Search access | Multiple tools requested without a bounded first pass | Optional accessible tools, bounded queries and documented access gaps |
| Commercial weights | Demand 25, creative 20, economics 25, competition 10, supplier/execution 20 | Demand 20, creative 15, economics 30, competition 10, supplier/execution 25 |
| Evidence coverage | Search/social counted within required dossier evidence | Fixed 15 core items across six dimensions; 80% minimum plus required entry checks; supplemental search/social reported separately |
| Global UGC | Supporting context | Can support relevant creative demonstration/feasibility; cannot establish local demand |
| Sample decision | General coverage and gate rules | Explicit required core items, A/B confidence, positive plausible base case after CAC and stage-specific dependencies |

Weights are operating preferences for prioritizing research and sample spending. They have not been calibrated against actual product sales. A higher score after reweighting is not new market evidence.

## Examples of the revised calculations

Illustrative inputs below are invented solely to check arithmetic and decision logic. They are not product research, sales predictions or investment recommendations.

| Assessed inputs | Demand result | Coverage | Interpretation |
|---|---|---:|---|
| M=80, S=40, L=60 | FULL 68/100 | 100% | 48 + 8 + 12 |
| M=80, S unavailable, L=60 | PROVISIONAL 75/100 | 80% | (48 + 12) / 0.80; disclose missing search |
| M=80, S and L unavailable | PROVISIONAL 80/100 | 60% | 48 / 0.60; marketplace-only, not equivalent to FULL 80 |
| M unavailable, S=80, L=80 | INSUFFICIENT EVIDENCE | 40% | No composite; marketplace assessment is required |
| M=80, assessed S=20, L=60 | FULL 64/100 | 100% | Include the weak observed search value; never remove it to get 75 |

Core coverage of 12 supported items out of 15 applicable items is 80%. This describes the core checklist only, not full demand coverage. If a mandatory sample-entry item is missing, the same 80% does not qualify for SAMPLE.

For a provisional Demand Index of 75, the commercial demand rating is 3.75/5, worth 15/20 points. If the other four ratings are each 3/5, their points are 9 + 18 + 6 + 15, giving a PROVISIONAL commercial score of 63/100. The score does not independently grant SAMPLE. If a commercial dimension is UNKNOWN, show assessed points/weight and the missing weight rather than rescaling to 100.

## Decision checks

- Strong independent local demand evidence, a relevant global demonstration, sourced plausible economics, adequate supplier/specification evidence and satisfied sample-entry requirements can support SAMPLE despite unavailable search/local social. Label demand and commercial scores provisional, disclose coverage and use confidence B at best.
- A single listing plus international views cannot pass the two-signal local demand requirement. Return RESEARCH MORE if further evidence can resolve it.
- Missing Trends or creator metrics is an access/evidence gap. It is not a negative sales finding, an invented zero or an automatic DROP.
- A verified critical pre-sample safety/identity/import failure or nonviable base case overrides a high score. Unresolved critical dependencies prevent SAMPLE.
- Physical sample quality and later shipment inspection stay PENDING until the appropriate Stage 3 evidence exists. The earlier SAMPLE decision is a validation step, not payment or inventory authorization.

## Using existing research

Reuse the same Product ID, original/current URLs, source records and historical decisions. Keep old scores labelled v1.1, then reassess the evidence under v1.2. Identify which changes came from methodology and which came from newly captured facts. Preserve original currencies, quote dates and uncertain costs.

The optional tools follow v1.2. Earlier screening stages keep their existing criteria; they do not retrospectively become sample approvals. Stage 3 retains supplier/payment verification, physical testing, pilot-order and shipment-release gates.

The exact previous Prompt 2 is backed up under `archive/2026-11-18-before-prompt-2-demand-revision/`. Unit-economics formulas are preserved. Validation of this revision covers document consistency, arithmetic examples and illustrative decision cases; it does not establish reliable live model execution or validate a real product.
