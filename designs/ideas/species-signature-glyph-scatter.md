# Species Signature Glyph Scatter

**Type:** Combined visualization — scatterplot + embedded coxcomb/radial bar glyph  
**Status:** Idea / pre-sketch  
**Personas:** Elena Novak (primary), Sofia Almeida (secondary), Hana Abebe (weak)  
**Related idea cards:** H-04, S-13, E-04, E-06 in `combined-viz-ideas.md`

---

## What it shows

A scatterplot of all 60 sites where:
- **x-axis** = total species richness (`richness_total`) — biodiversity
- **y-axis** = mean coffee yield (`yield_mean`) — productivity

Each site is rendered as a **coxcomb/radial bar glyph** instead of a plain dot. The glyph encodes a site's species signature: which yield-correlated species are distinctively abundant there.

**The combination answers a question neither component alone can:**
- Scatterplot alone: where does each site sit in the trade-off space?
- Glyph alone: which species dominate this site?
- Combined: *for sites that beat or follow the trade-off, what species signature explains their position?*

This directly addresses the sweet-spot question: sites in the upper-right quadrant (high yield AND high richness) — if any exist — will show a distinctive glyph pattern that identifies which species co-occur with that unusual combination.

---

## Data & Derived Metric

### Input data
| File | Variable used |
|------|---------------|
| `Coffee_yield.xlsx` | `yield_mean` (y-axis position) |
| `Plant_species_richness.xlsx` | `richness_total` (x-axis position) |
| `Woody_species_abundance.xlsx` | Quantitative abundance per woody species per site |
| `Herbaceous_vegetation_Abundance.txt` | Quantitative abundance per herbaceous species per site (ordinal scale: 1/5/9) |
| `Bryophyte_frequency.txt` | Frequency per bryophyte species per site |
| `Plant_species_and_average_coffee_yield_in_sites_where_the_species_occurs.xlsx` | `avg_yield_at_sites` per species (used to derive yield correlation) |

### Yield correlation per species
For each species *i*, compute a yield association score:

```
yield_lift_i = avg_yield_at_sites_i - overall_mean_yield
```

`avg_yield_at_sites` is already provided in the species-level summary file.  
Filter: only include species with `n_sites >= 5` to avoid noise from rare species.

### Relative abundance per site
For each species *i* at site *j*:

```
relative_abundance_ij = abundance_ij / mean(abundance_i across all sites where species i occurs)
```

- Value > 1 → this species is overrepresented at this site vs. its typical abundance
- Value < 1 → present but below average
- Value = 0 → absent

> Note: herbaceous abundance uses a 1/5/9 ordinal scale (likely Braun-Blanquet classes). Check the paper's methods before deciding whether to treat as ordinal or map to cover percentages.

### Spoke length (composite metric)
```
spoke_ij = yield_lift_i × relative_abundance_ij
```

Positive spoke → species associated with high yield, overrepresented here  
Negative spoke (if shown) → species associated with low yield, overrepresented here

---

## Fixed Global Axes & Concentric Rings (critical design decision)

**Every glyph uses the same N axes (one per selected species), and species are ordered radially by their yield association.** Outer rings of the glyph correspond to species clusters associated with **high yield**; inner rings correspond to species associated with **low yield**.

### Ring structure (radius encodes yield-tier of the species)
1. Rank all species (across plant groups, after the `n_sites >= 5` filter) by `yield_lift_i`.
2. Bin species into ordered tiers — e.g. 3 tiers (low / mid / high yield association) or finer.
3. Map tier → radial band:
   - **Outer band** = species with highest `yield_lift` (high-yield-associated)
   - **Middle band(s)** = neutral / mid yield association
   - **Inner band** = species with lowest (or most negative) `yield_lift` (low-yield-associated)
4. Within each band, each selected species occupies a fixed angular slot, identical across all 60 site glyphs.

This means a glyph that is **bright/full on its outer ring and faint inside** is a site whose species mix leans toward high-yield indicators; a glyph **full on the inside** leans toward low-yield indicators.

### What the spoke encodes within a ring
Spoke length within its band = `relative_abundance_ij` (capped at the band's outer radius). The yield direction is now carried by the ring (radial position), not the spoke length, so spokes can stay positive-only and remain comparable across rings.

### Selecting the species
- Keep the count manageable (≈12–18 axes total) by taking the top species per yield tier by `n_sites × |yield_lift|` (informativeness × reliability).
- Fixed axes + fixed ring assignment make all 60 glyphs directly comparable.

**Ghost ring at relative-abundance = 1.0 within each band** shows the species' typical abundance — deviation from mean is still immediately readable.

---

## Marks & Channels

| Element | Mark | Channel | Variable |
|---------|------|---------|----------|
| Site position | Point (glyph center) | x-position | `richness_total` |
| Site position | Point (glyph center) | y-position | `yield_mean` |
| Species yield-tier | Radial band (ring position) | Radial position | `yield_lift_i` (binned: outer = high, inner = low) |
| Species presence at site | Radial bar arc within band | Arc length | `relative_abundance_ij` |
| Site management | Glyph fill / stroke color | Color hue or sequential ramp | Management indicator from `Environmental_and_management_variables.xlsx` (e.g. coffee structure index, density, or dominance — pick one as the lead channel) |
| Reference | Ghost ring within each band | Opacity (faint) | Mean relative abundance = 1.0 |

---

## Layout

```
high yield │  [sparse glyphs]      [sweet-spot sites — upper right]
           │
           │
           │
           │
low yield  │  [low-yield low-richness]    [rich biodiverse sites]
           └────────────────────────────────────────────────────
              low richness                         high richness
```

- Annotate the four quadrants (low/low, high/low, low/high, high/high)
- Label sites in the upper-right quadrant by name — these are the sweet-spot candidates
- Draw a regression line through the point cloud to show the trade-off direction

---

## Interaction (manages overplotting)

Overplotting is likely: sites cluster in the low-richness/high-yield and high-richness/low-yield regions.

| Interaction | What it manages |
|-------------|-----------------|
| **Hover** | Expand glyph to full legible size; show site ID, exact yield, richness values |
| **Click to pin** | Keep up to 4 glyphs expanded side by side for comparison |
| **Filter by shrub cluster** | Highlight only sites in a selected cluster; grey out others |
| **Rest state** | Show small glyphs or plain dots; glyphs expand on demand |

---

## Strengths

- Uses position (x/y) for the two most important variables — the most accurate perceptual channel for comparison
- Concentric ring structure (outer = high-yield species, inner = low-yield species) lets you read a site's yield-association profile by where its glyph "lights up" radially — no per-spoke math needed by the viewer
- Fixed axes + fixed ring assignment make all 60 glyphs directly comparable
- Color carries the management context, so the link between management practice and observed species pattern is visible at a glance — supports interaction/discussion of management as a driver
- Sweet-spot diagnostic: upper-right quadrant sites' glyphs identify indicator species for sites that beat the trade-off
- Quantitative abundance data (not just presence/absence) makes `relative_abundance` a true ratio, not a workaround

## Weaknesses / risks

- **Many axes at glyph scale**: at full scatter view, 60 glyphs compete for space; interaction (hover to expand) is essential
- **Ring binning is a judgement call**: tier boundaries on `yield_lift` need to be chosen (quantile vs. equal-width); poor cuts can hide gradients
- **Plant-group signal is demoted**: with color reassigned to management, plant-group identity must be carried by axis labels or angular sector — risk of losing the woody/herbaceous/bryophyte read-out
- **Choosing one management indicator**: `Environmental_and_management_variables.xlsx` carries structure index, density, and dominance — pick the one with the strongest behavioural meaning for the audience, or offer a toggle
- **Ordinal scale**: if herbaceous 1/5/9 values are Braun-Blanquet classes, averaging them may not be meaningful — verify against paper methods
- **Noise at n_sites threshold**: the `n_sites >= 5` filter is a judgement call; too low = noisy correlations; too high = loses rare-but-informative species

---

## Simplification path (if too complex)

1. Remove ghost ring — reduces visual noise
2. Collapse to 2 rings instead of 3 (just high-yield band vs. low-yield band)
3. Replace coxcomb with a simpler 2-bar stacked mini-chart (outer = high-yield species sum, inner = low-yield species sum), still colored by management — loses species detail but keeps the inside-vs-outside pattern
4. Show glyphs only for the 10 highest and 10 lowest yield sites — reduces overplotting to a manageable gallery

---

## Related ideas (for sketching comparison)

- **H-04** — same glyph scatter concept, broader biodiversity profile
- **S-13** — the four-quadrant annotation layer (can be merged directly into this view)
- **E-06** — rank divergence as an alternative x-axis (yield rank minus richness rank)
- **S-02** — the heatmap answers the same species question but for all species, not just the top 12
