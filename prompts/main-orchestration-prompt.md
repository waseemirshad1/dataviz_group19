# Main Orchestration Prompt — Book Extraction via MapReduce

## Overview

Extract knowledge from all books in `books/` to serve four simultaneous goals:
1. **Summaries** — data visualization theory, principles, and best practices → `research/summaries/chunks/`
2. **Visualization catalogue** — specific visualization types with examples → `research/data_visualisations/chunks/`
3. **Creative combined ideas** — inspiration for the assignment's combined visualizations → `research/ideas_creative_combined_visualisations/chunks/`
4. **Infographic CV ideas** — creative ways to visualize personal/professional data → `research/cv/chunks/`

READ prompts/agent-prompt.md for info about all the four goals!

All folders and chunk subfolders already exist.

---

## Book Inventory and Chunk Assignments

| Agent ID | Book | Pages | Chunk file prefix |
|---|---|---|---|
| agent_01 | `books/Cool Infographics.pdf` | 1–50 | `ci_chunk_01` |
| agent_02 | `books/Cool Infographics.pdf` | 51–100 | `ci_chunk_02` |
| agent_03 | `books/Cool Infographics.pdf` | 101–150 | `ci_chunk_03` |
| agent_04 | `books/Cool Infographics.pdf` | 151–200 | `ci_chunk_04` |
| agent_05 | `books/Cool Infographics.pdf` | 201–249 | `ci_chunk_05` |
| agent_06 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 1–50 | `ds_chunk_01` |
| agent_07 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 51–100 | `ds_chunk_02` |
| agent_08 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 101–150 | `ds_chunk_03` |
| agent_09 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 151–200 | `ds_chunk_04` |
| agent_10 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 201–250 | `ds_chunk_05` |
| agent_11 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 251–300 | `ds_chunk_06` |
| agent_12 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 301–350 | `ds_chunk_07` |
| agent_13 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 351–400 | `ds_chunk_08` |
| agent_14 | `books/Data Sketches (AK Peters Visualization Series)_nodrm.pdf` | 401–428 | `ds_chunk_09` |
| agent_15 | `books/examples from class (dutch).pdf` | 1–3 | `ec_chunk_01` |
| agent_25 | `course/example_reports/example_report_1.pdf` (p.1–15) + `course/example_reports/example_report_2.pdf` (p.1–14) | all pages | `er_chunk_01` |
| agent_16 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 1–50 | `vad_chunk_01` |
| agent_17 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 51–100 | `vad_chunk_02` |
| agent_18 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 101–150 | `vad_chunk_03` |
| agent_19 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 151–200 | `vad_chunk_04` |
| agent_20 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 201–250 | `vad_chunk_05` |
| agent_21 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 251–300 | `vad_chunk_06` |
| agent_22 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 301–350 | `vad_chunk_07` |
| agent_23 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 351–400 | `vad_chunk_08` |
| agent_24 | `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` | 401–430 | `vad_chunk_09` |

---

## Execution Plan

### Phase 1 — Parallel Reading (3 batches, max 10 agents at a time)

**Batch 1 (launch in parallel):** agents 01–10  
**Batch 2 (launch in parallel, after batch 1 completes):** agents 11–20  
**Batch 3 (launch in parallel, after batch 2 completes):** agents 21–25

Each agent receives the **agent prompt** (see `prompts/agent-prompt.md`) with its specific `AGENT_ID`, `BOOK_PATH`, `PAGES`, and `CHUNK_PREFIX` filled in.

> **Exception — agent_25 (example reports):** This agent reads two real student reports instead of a book. Use the agent prompt but with the **adapted extraction instructions** listed below. Read both files sequentially (the tool allows max 20 pages per call, so read each report in one call).

agent_25 reads `course/example_reports/example_report_1.pdf` (15 pages) and `course/example_reports/example_report_2.pdf` (14 pages). These are real graded student submissions for this exact course. Adapt each goal as follows:

### Phase 2 — Synthesis (4 parallel synthesis agents, after all Phase 1 agents complete)

Launch 4 synthesis agents in parallel, one per goal. Each synthesis agent:
1. **Reads `prompts/agent-prompt.md`** — this is the authoritative definition of what each goal extracts and how output should be structured. Use the relevant Goal section as the blueprint for the synthesized output.
2. **Reads all chunk files** for its goal — these are the raw extractions from individual agents.
3. **Produces one final synthesized document** — same structure and fields as defined in the agent prompt, but merged, deduplicated, and organized across all sources.
```
research/summaries/chunks/{CHUNK_PREFIX}_summary.md
research/data_visualisations/chunks/{CHUNK_PREFIX}_visuals.md
research/ideas_creative_combined_visualisations/chunks/{CHUNK_PREFIX}_ideas.md
research/cv/chunks/{CHUNK_PREFIX}_cv.md
```
---

**Synthesis agent 1 — Data Visualization Knowledge**
- Reads: `prompts/agent-prompt.md` (see **Goal 1** for output structure and extraction criteria)
- Reads: all `research/summaries/chunks/*.md` (25 files)
- Writes: `research/summaries/dataviz-knowledge.md`
- Synthesize thematically across all books — not by book, not by chunk. Deduplicate overlapping content, merge complementary points. This is a **general-purpose reference**, not tied to any dataset. Add one dedicated section at the end: **"What good reports look like in practice"** synthesized exclusively from `er_chunk_01_summary.md`.

**Synthesis agent 2 — Visualization Catalogue**
- Reads: `prompts/agent-prompt.md` (see **Goal 2** for the per-entry field structure)
- Reads: all `research/data_visualisations/chunks/*.md` (25 files)
- Writes: `research/data_visualisations/visualization-catalogue.md`
- Compile every visualization type found across all sources into one **general catalogue**, not scoped to any dataset. Deduplicate entries for the same chart type (merge fields, keep the richest description). Group by data type (quantitative, categorical, relational, temporal, spatial). Mark entries from student reports with `[from student report]`.

**Synthesis agent 3 — Creative Combined Ideas for Assignment**
- Reads: `prompts/agent-prompt.md` (see **Goal 3** for the idea card fields, persona descriptions, dataset context, and theoretical framework)
- Reads: all `research/ideas_creative_combined_visualisations/chunks/*.md` (25 files)
- Also reads: `research/summaries/assignment-overview.md` and `research/summaries/conceptual-data-map.md`
- Writes: `research/ideas_creative_combined_visualisations/combined-viz-ideas.md`
- Synthesize all idea cards into one document. Deduplicate similar ideas (keep the most complete version). Group by persona (Hana / Sofia / Elena). Preserve all idea card fields exactly as defined in the agent prompt. Add a dedicated section **"Ideas from real student submissions"** from `er_chunk_01_ideas.md`.

**Synthesis agent 4 — Infographic CV Ideas**
- Reads: `prompts/agent-prompt.md` (see **Goal 4** for output structure and CV context)
- Reads: all `research/cv/chunks/*.md` (25 files — skip `er_chunk_01_cv.md` which is N/A)
- Writes: `research/cv/cv-ideas.md`
- Synthesize all CV idea cards into one document. Group by CV section (education, skills, work experience, growth over time, character traits). Preserve all idea card fields. Deduplicate similar ideas.

---