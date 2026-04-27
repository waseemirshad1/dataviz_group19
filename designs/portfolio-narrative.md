# Design Portfolio Narrative

> **Purpose:** Explain *why this set of designs* — what question each one answers, and how together they cover the dataset's main axes without redundancy.

This portfolio is built around the central tension of the Ethiopian coffee-agroforest dataset: **higher yield comes at a cost to biodiversity**, but that trade-off is mediated by management and changes over time. No single chart can answer that fully, so we use three complementary designs, each anchored to a distinct question.

---

## The three designs at a glance

| # | Design | Core question | Unit | Files used |
|---|---|---|---|---|
| 1 | **Comet Chart** (yield × richness scatter with management vectors) | *Where does each site sit in the yield–biodiversity trade-off, and which way is management pulling it?* | Site (60) | `Coffee_yield`, `Plant_species_richness`, `Environmental_and_management_variables` |
| 2 | **Hexagon Map** (gridded hex small-multiples, color/hatch = trend, size = density) | *Which sites are on a declining trajectory over the 3-year study, and how does plot density relate?* | Site (60) — gridded layout, not positioned by yield | `Coffee_yield` (3 yearly columns), `Environmental_and_management_variables` |
| 3 | **Species Tulip Field** (plants as flower glyphs in yield-association × biodiversity-association space, with a tier-curve shape per species) | *Which species are sweet-spot indicators, which are bridge candidates, and how is their presence distributed across yield tiers?* | Species (199 after the `n_sites >= 5` filter; 407 in source) | `Total_species_composition`, species-level summary, `Plant_species_richness`, `Coffee_yield` |

Together they answer the dataset's three biggest questions:

1. **Where are we in the trade-off?** → Comet
2. **Are we stable or drifting?** → Hexagon Map
3. **Which species can live in the sweet-spot, and which can bridge the trade-off?** → Tulip

---

## Why these three, not four

We considered a fourth design — a "site signature glyph scatter" placing sites as radial-bar glyphs on the same yield × richness axes used by the Comet. We dropped it because:

- The Comet already occupies the yield × richness canvas with a clear payload (management vectors). Stacking another site-level glyph design on the same axes creates redundancy without adding a distinct question.
- Reconciling three different abundance scales (woody counts vs. herbaceous Braun-Blanquet ordinal vs. bryophyte frequency) into a single comparable spoke length is a methods burden the report would have to defend, with no commensurate insight gain.
- The species-level question is more cleanly answered at the species unit (Tulip) than by a per-site fingerprint.

---

## What each design uniquely contributes

### 1. Comet Chart — the trade-off diagnosis
Standard scatter (richness on x, yield on y) shows *position* in the trade-off. The novelty is the **vector tail** drawn from each point, whose length and direction encode how the management variables (coffee structure index × density) pull the site. A long tail leaning down-and-left signals a site whose management is pulling it out of the Pareto-optimal zone; a short tail signals a stable/balanced site.

**Reads:** position (where), management state (why), trade-off shape (regression direction).

**Does not read:** time, species composition.

### 2. Hexagon Map — the stability diagnosis
Sixty hexagons in a 10×6 grid (not positioned by yield/richness — layout is gridded for legibility, identity-only). Each hexagon's color + hatch encodes the 3-year yield trend (red `///` = declining, green `\\\\` = safe), and its size encodes coffee density.

This is the **only** design in the set that uses the longitudinal structure of `Coffee_yield.xlsx` (`CC_Yield_2017`, `_2018`, `_2019`). It answers "is this site getting better or worse?" — a question the cross-sectional Comet and Tulip cannot.

**Reads:** trajectory (declining/safe), density (size), site identity (label).

**Does not read:** trade-off position, biodiversity, species.

### 3. Species Tulip Field — the species sweet-spot AND bridge-species diagnosis
Each plant species is drawn as a tulip-shaped glyph on a scatter where x = average biodiversity of host sites and y = average yield of host sites. The mark is split into two encodings:

- **Position** = the species' *averages* (yield, biodiversity).
- **Tulip shape** = the *distribution* of its presence across five yield tiers (low → high). The wavy top of the cup is a smoothed curve over those five counts; the rounded cup beneath is a fixed silhouette so every glyph stays visually anchored.

This split is what the design buys over a plain scatter: position alone cannot distinguish a narrow specialist (peaked in one tier) from a generalist (mass at both ends). Two species can sit at the same medium-medium point with completely different tier curves.

Color encodes plant group (woody `#374`, non-woody `#da2`, bryophyte `#38f`); the global **size slider** scales every tulip; **biodiversity-range** and **yield-range** sliders define the visible window, and overlap selection re-runs against that window so zooming in reveals more glyphs as the visible region depopulates. The Plotly chart's full body is hoverable for species metadata; up to four species can be pinned into a side-by-side detail panel for comparison.

The design surfaces two distinct species categories:

- **Sweet-spot indicators** — upper-right tulips, thriving at both higher yield and higher biodiversity.
- **Bridge candidates** — mid-position tulips whose tier curves nonetheless reach into high-yield tiers. Their averages are unremarkable, but their distribution shows tolerance for productive, intensively managed sites. These are exactly the species worth flagging when looking for "balanced solution" recommendations between yield and conservation.

The mark *is* the metaphor: plants drawn as plants.

**Reads:** species ecological role (quadrant), distribution of presence across the yield gradient (curve asymmetry / bimodality), plant group composition of each region (color clustering), bridge-species candidates (mid-position with right-shifted curve).

**Does not read:** site-level state, time, management variables.

---

## Mapping to the conceptual data map

The four numbered questions in `data/conceptual-data-map.md` map onto the portfolio as follows:

| Question (from data map) | Answered by |
|---|---|
| 1. Biodiversity–yield relationship — does richer = lower yield? Driven by which group? | Comet (overall shape) + Tulip (per-group color clustering) |
| 2. Species-level associations — which species track high or low yield, and which bridge the trade-off? | **Tulip (primary)** — position answers the average, the tier curve answers the distribution, together they expose bridge candidates |
| 3. Structural clusters / cluster predicts yield? | Comet (color/size by management variables); cluster overlay possible as a future extension |
| 4. Spatial/management gradient — does management mediate the trade-off? | **Comet (primary)** — the vector payload is exactly this |

Question 1 is shared between two designs by intention: Comet shows the *aggregate* trade-off, Tulip shows *which species* are responsible for it. They reinforce rather than repeat.

A fifth question we surface that isn't explicit in the data map: **temporal stability** — answered uniquely by the Hexagon Map.

---

## Persona alignment

| Persona | Primary design | Reason |
|---|---|---|
| **Hana Abebe** (coffee producer) | Hexagon Map → Comet | Wants to know "is my site declining, and what's pulling it?" — actionable site-level diagnosis |
| **Sofia Almeida** (conservation activist) | Tulip → Comet | Wants to identify species worth protecting and to argue management can preserve them — sweet-spot species + bridge candidates + the trade-off shape they sit in |
| **Elena Novak** (scientist) | Comet → Tulip → Hex | Wants the full multivariate picture; reads all three as a chain |

No persona is left without a primary entry point.

---

## Why this set passes the rubric

- **Distinct questions, no canvas collision** — three designs answer three non-overlapping questions; only Q1 is shared, and intentionally so.
- **Different units of analysis** — site (60), site-over-time (60×3), species (199 after `n_sites >= 5` filter, 407 in source). The dataset is exercised across all three of its natural axes.
- **Different visual languages** — Cartesian scatter with vectors (Comet), gridded categorical small-multiples (Hex), domain-semantic glyph scatter with split position/shape encoding (Tulip). No design is a re-skin of another.
- **Marks-and-channels variety** — point + vector (Comet), polygon + hatch + size (Hex), filled cup-and-petal polygon + position + tier-curve shape + color + size (Tulip). Every chart introduces a non-trivial channel.
- **Interactive layer** — the Tulip Field adds reactive widgets (size slider, plant-group filter, biodiversity/yield range sliders for zoom-driven overlap selection, species pin for the detail panel) on top of the static Comet and Hex views. All three render in one marimo notebook.
- **Coverage of the data files** — the three together touch all 9 raw files; Comet alone touches 3.
