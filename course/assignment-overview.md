# Assignment Overview — [G0R72A] Data Visualisation

## Core Goal in One Sentence

**Design creative, combined visualisations** of the coffee/biodiversity dataset that provide deeper insight through visuals. Document the full design process (diverge → emerge → converge), implement 3 custom interactive visuals in marimo, and report what you found in the data.

The emphasis is on **creative combination**: not bar charts in isolation, but multiple "basic" ideas fused into one rich visual. The bar chart is the floor, not the ceiling.

---

## What "Creative Combined" Actually Means

The key insight the assignment stresses: take two or more individually interesting (but standalone) visuals and merge them into a single, more informative one. You must track which basic designs went into the final combined design.

**Concrete example from the assignment brief:**

| Basic design 1 | Basic design 2 | Combined |
|---|---|---|
| Each site = a circle; smaller circles inside show energy per building type; size = relative energy share | Sankey-style: cities on left, energy-use types on right, line width = energy going to that type | Left = cities, right = building types. Instead of a line, a **rotated bar** connects them. Bar width = total energy; bar is subdivided by energy type (colour). So 90% red = 90% heating in that building type in that city. |

Applied to our data: you might combine a **species richness bar per site** with a **coffee yield encoding** (e.g. circle size or colour) — so each "bar" tells you both biodiversity and productivity at once.

---

## The Design Process: Diverge → Emerge → Converge

This is the core methodology. Repeat the cycle at least once; more cycles = higher score.

```
DIVERGE                    EMERGE                   CONVERGE
──────────────────         ──────────────────        ──────────────────
Generate many ideas        Cluster sketches          Pick 2–3 to implement
independently              by theme or form          Explain why (theory!)
No constraints             Combine & critique        Document gaps vs ideal
Sketches: hand-drawn       SCAMPER techniques        NUF test: New-Useful-
or digital                 Card sorting              Feasible
```

**SCAMPER** (a tool for emerge phase):
- **S**ubstitute — replace a standard mark with something domain-specific
- **C**ombine — merge two sketches
- **A**dapt — take a visual from another domain and adapt it
- **M**odify / **M**agnify — change scale, emphasis, proportion
- **P**ut to another use — repurpose a visual type (e.g. network to show geography)
- **E**liminate — strip away noise
- **R**everse — flip the representation (lines for nodes, circles for links)

**Critique checklist** (use this at each emerge/converge step):
- What are the dimensions displayed?
- What are the marks? What are the channels?
- What is good / bad?
- How could the message be made stronger?
- Which additional dimensions would help?
- 2 things to keep + 2 things to change

---

## What You Must Submit (Report Structure)

### Part 1 — Metadata
Version (Design / Implementation), student names, dataset name.

### Part 2 — Project description *(~1 page)*
1. Short description of the data and the **persona** (who is the user of this visualisation, and what do they need to know?).
2. Description of selected features — what variables are interesting and why.
3. **2–3 guiding questions** that drive the rest of the project. Everything in Parts 3–5 should connect back to these.

**The three official personae (choose one, or design for more than one):**

| Persona | Role | Core need |
|---|---|---|
| **Hana Abebe** | Coffee producer managing an agroforest | Wants to increase yield. Needs to compare sites, identify strong/weak performers, and understand which site conditions, management practices, and biodiversity characteristics are associated with higher production. Wants practical, actionable insights. |
| **Sofia Almeida** | Biodiversity conservation activist | Concerned that yield pressure reduces species richness and erodes ecological value. Wants to know where biodiversity is highest, how different species groups respond to management intensity, and whether high-yield sites systematically cost conservation. |
| **Elena Novak** | Agroecology scientist planning a new field study | Wants to know which yield variable to measure in future studies, how strongly the available yield measures agree, and which environmental/management variables should be prioritised. Needs interpretable evidence about dataset structure and variable usefulness. |

**The core tension in this dataset** (from the source paper): tropical agroforests are both productive for farmers *and* refuges for biodiversity — but there is a **trade-off between managing for yield versus managing for biodiversity**. This tension is the story the visualisations should tell.

*For our data, candidate guiding questions per persona:*

*Hana (yield-focused):*
- Which sites are the top/bottom performers, and what distinguishes them (management, biodiversity, shrub structure)?
- Is yield stable across years, or are some sites consistently variable?
- Which plant species or management conditions predict high yield?

*Sofia (biodiversity-focused):*
- Do high-yield sites have lower species richness — and is this true for all plant groups?
- Which species groups (woody / herbaceous / bryophytes) are most sensitive to management intensity?
- Are there sites that achieve both high yield and high biodiversity, or is the trade-off unavoidable?

*Elena (methods-focused):*
- How correlated are the three yearly yield measurements? Is the mean a reliable proxy?
- Which management variables (density, dominance, structure index) most strongly co-vary with yield?
- What is the structure of the shrub clusters, and do they segment the data usefully?

### Part 3 — Visual design *(max 3 pages)*
1. Description of **how** you designed (process, collaboration tools like Miro/Excalidraw).
2. **5–10 sketches** (mix of diverge, emerge, converge). Each sketch must be annotated: explain the encoding (marks + channels) and why you chose it.
3. **2–3 reworked/converged designs** you would implement. Explain encoding, interaction, and how they help answer the guiding questions.

**What graders look for:**
| Score | What it means |
|-------|---------------|
| +0 | Designs are all very similar (only explored a tiny corner of the design space) |
| +1 | Different chart types explored, but all standard (bar, scatter, line) |
| +2 | Novel, non-standard designs explored — or standard types used in a semantically novel way |

A network diagram is standard. A network diagram where nodes are *sites* and links encode *species co-occurrence* is not standard — same visual type, different semantic use.

### Part 4 — Implementation *(max 5 pages)*
Describe **3 custom interactive visualisations** built in **marimo** (Python). For each:

1. **Intended design** — sketch/mock-up of what you aimed for (hand-drawn is fine).
2. **Actual design** — what you built. Explain every mark and channel. Annotated screenshot recommended.
3. **Interactions** — what can the user do (hover, filter, zoom, select)?
4. **Gap analysis** — what is in the intended design but not yet implemented? What would a skilled programmer add?
5. **Link to running marimo instance** (e.g. HuggingFace deployment).
6. **Link to 4–6 min YouTube video** (public or unlisted) demonstrating the visuals and how they answer the guiding questions.

> The implementations **do not have to come from Part 3**. They can be new designs. But they must be relevant to the guiding questions from Part 2.

### Part 5 — Findings *(max 2 pages)*
Answer: *"What interesting things can you tell about the data?"*

Use a storytelling arc:
- What did you expect to find?
- What initial patterns appeared?
- Where did that lead you (which part of the data did you zoom in on)?
- What was surprising or unexpected?

Include annotated screenshots for every finding.

---

## Grading Criteria (Scoresheet Summary)

| Criterion | Poor (+0) | Sufficient (+1) | Good (+2) |
|---|---|---|---|
| Design space explored | Very limited, similar designs | Different but all standard charts | Novel / semantically unusual designs |
| Designs well-annotated | No or useless annotations | Some labels, limited context | Clear encoding + design rationale explained |
| Designs reworked meaningfully | No emerge/converge at all | One diverge→emerge→converge cycle | Multiple cycles, each building on the last; connection to research question explained |
| Design decisions explained (final converge) | No explanation given | Explanation given | Explanation grounded in **visualisation theory** |

**"Grounded in visualisation theory"** means referencing concepts from the course/textbook: marks vs channels, expressiveness, effectiveness, pre-attentive features, Gestalt principles, etc.

---

## Technology

- **marimo** — interactive Python notebook for implementation (required)
- Deployment: HuggingFace or similar (link required in report)
- Sketching tools: hand-drawn, Miro, Figma, Excalidraw (all acceptable; link is supplementary only)

---

## Common Pitfalls to Avoid

- Submitting only standard charts (bar, pie, scatter) with no creative combination → maximum +1 on design space
- Sketches without annotations explaining marks/channels → +0 on annotation criterion
- Skipping the emerge phase (jumping straight from diverge to implementation) → +0 on rework criterion
- Justifying design choices without referencing visual encoding theory → +1 instead of +2 on final decision criterion
- Guiding questions that are vague or disconnected from the visualisations built
- A YouTube video that just shows the visuals without explaining how they answer the questions
