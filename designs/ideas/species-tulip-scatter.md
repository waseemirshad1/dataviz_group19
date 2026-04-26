# Species Tulip Scatter

**Type:** Combined visualization — scatterplot + domain-semantic tulip glyph  
**Status:** Idea / pre-sketch  
**Semantic novelty:** [SEMANTICALLY NOVEL] — standard scatter, but points are plant-shaped glyphs encoding yield-tier presence profiles; the mark IS the domain object  
**Personas:** Sofia Almeida (primary), Elena Novak (primary), Hana Abebe (secondary)  
**Related ideas:** species-signature-glyph-scatter.md, S-02, S-05, E-04 in `combined-viz-ideas.md`

---

## Concept

Each of the ~407 plant species is a **tulip glyph** positioned in a yield-association × biodiversity-association space. The tulip's shape encodes how that species distributes across yield tiers. The color encodes which plant group it belongs to. The scatter position encodes its ecological role.

The mark is the metaphor: plant species drawn as plants.

---

## Scatterplot Axes

| Axis | Variable | How to derive |
|------|----------|---------------|
| **y** | Yield association | `avg_yield_at_sites` from `Plant_species_and_average_coffee_yield_in_sites_where_the_species_occurs.xlsx` — directly available |
| **x** | Biodiversity association | Average `richness_total` of sites where this species occurs — join species presence matrices with `Plant_species_richness.xlsx` per site |

**Quadrant meaning:**
- Upper-right → species found at both high-yield AND high-richness sites → sweet-spot indicator species
- Upper-left → high yield, low biodiversity → management-tolerant specialists
- Lower-right → low yield, high biodiversity → undisturbed agroforest indicators
- Lower-left → weak signal both ways → generalist / low-information species

---

## The Tulip Glyph

### Structure
- **x within glyph** = yield tier (1–5, left = lowest yield, right = highest yield; 60 sites ÷ 12 = 5 tiers)
- **y within glyph** = presence/abundance in that tier:
  - Presence/absence species: count of sites in tier where species occurs (0–12)
  - Woody/herbaceous: mean abundance per tier
  - Bryophyte: mean frequency per tier
- **Top line** = smoothed curve connecting the 5 tier values (loess or cubic spline)
- **Bottom** = flat baseline at y = 0
- **Fill** = area between curve and baseline → the tulip body

### Shape encodes ecology
```
Left-heavy tulip:   ╭╮___   biodiversity indicator — absent at high yield
Right-heavy tulip:  ___╭╮   management-tolerant — appears at high yield
Symmetric/round:    _╭──╮_  generalist — present across all tiers
Sharp peak:         __╭╮__  narrow niche species
Flat/absent:        ______   too rare to show (filtered out)
```

### Color = plant group (fill + stroke)
- Woody plants → dark green
- Herbaceous plants → golden yellow
- Bryophytes → steel blue

Color makes the distribution of plant groups across the scatter space immediately readable — e.g. "do bryophytes cluster in the lower-right (biodiversity) corner?"

### Size of glyph
- Proportional to `n_sites` — widespread species get a larger tulip, rare species smaller
- Minimum size threshold: species with `n_sites < 5` rendered as tiny dots only (too noisy for a reliable smoothed line)

---

## Filter & Overplotting Strategy

407 species in a scatter = severe overplotting. Two complementary approaches:

### Option A — Non-overlapping selection
Show only the subset of species whose glyphs do not overlap at the current zoom level. Selection priority:
1. Species at the extremes of each quadrant (most informative positions)
2. Largest `n_sites` within each quadrant (most reliable signal)
3. One per plant group per quadrant region (ensures color diversity)

This gives a curated, clean view — a gallery of representative species across the ecological space.

### Option B — Dots at rest, tulip on demand
- All species shown as colored dots (color = plant group, size = n_sites) at rest
- Hover over any dot → tulip glyph expands in place, overlaying the scatter
- Click to pin a tulip; click again to release
- Pin multiple species for side-by-side shape comparison

### Recommended: combine both
- Default view = Option A (non-overlapping, ~30–50 representative tulips visible)
- Toggle "show all as dots" → Option B mode
- Both allow hover-to-expand

---

## Marks & Channels Summary

| Element | Mark | Channel | Variable |
|---------|------|---------|----------|
| Species position | Glyph center | x-position | Biodiversity association (avg richness of host sites) |
| Species position | Glyph center | y-position | Yield association (`avg_yield_at_sites`) |
| Tier profile | Area (tulip body) | Shape of top curve | Presence/abundance across 5 yield tiers |
| Plant group | Fill color hue | Color hue | Woody / herbaceous / bryophyte |
| Species prevalence | Glyph size | Size | `n_sites` |
| Tier distribution | Curve left-vs-right lean | Asymmetry of shape | Whether species favors low- or high-yield tiers |

---

## What the combination uniquely answers

| Component alone | Question answered |
|----------------|-------------------|
| Scatterplot position | What is this species' average yield and biodiversity association? |
| Tulip shape | How does presence distribute across the yield gradient — smooth, threshold, or peaked? |
| **Combined** | **Are sweet-spot species (upper-right) found broadly across productive sites, or only at specific yield tiers? And which plant group contains them?** |

Neither component alone can answer this. The scatter gives the average association; the tulip reveals its structure.

---

## Interaction Detail

| Interaction | What it does |
|-------------|--------------|
| Hover | Expand tulip to legible size; show species name, n_sites, avg_yield, avg_richness of host sites |
| Click to pin | Keep tulip expanded for comparison; up to 4 pinned simultaneously |
| Filter by plant group | Toggle woody / herbaceous / bryophyte layers on/off |
| Zoom into quadrant | Upper-right quadrant zoom → shows only sweet-spot candidate species in full detail |
| "Show all as dots" toggle | Switches from curated non-overlapping view to full 407-species dot cloud |

---

## Strengths

- **Domain-semantic mark**: plant species drawn as plant-like shapes — the metaphor is intrinsic, not decorative
- **Tulip asymmetry is immediately readable**: a right-leaning tulip = yield-tolerant; a left-leaning tulip = biodiversity-only species. No legend needed for this dimension.
- **Color distribution across scatter**: shows whether one plant group dominates the sweet-spot quadrant — answering "which group is most compatible with decent yield?"
- **The smoothed line handles sparse tier data gracefully**: a species present at only 3 of 12 sites in a tier produces a low smooth value, not a jagged spike
- **Visually compelling for Sofia's advocacy use case**: a field of tulips that withers toward the high-yield corner is a persuasive image

## Weaknesses / risks

- **Smoothed line on 5 points**: loess on 5 data points is borderline — consider cubic interpolation instead, or just connect dots with a rounded bezier curve
- **Asymmetry is confounded**: a right-leaning tulip could mean the species loves high yield, OR that it's simply a common species present everywhere and the highest-yield tier just has more sites (all 12) included. Normalize by tier size (always 12) before computing presence rate.
- **x-axis derivation is a computation step**: needs a join of species presence matrices with site-level richness — not in raw files directly
- **407 species, 3 plant groups**: the scatter could still show strong color clustering (e.g. all bryophytes at lower-right). That's informative but risks making the view look like a color separation chart rather than a species landscape

---

## Simplification path

1. Reduce to top 50 species by `|yield_association - global_mean|` — the most informative species only
2. Replace smooth curve with 5 connected dots (no fill) — simpler but loses tulip metaphor
3. Remove size encoding (n_sites) — all glyphs same size, reduces visual complexity
4. Show only 3 "archetype" tulips per quadrant with labels — purely illustrative / editorial

---

## Sketch direction

```
high yield assoc.
    │   ╭──╮        ╭╮ ╭─╮
    │  ╭╯  ╰─╮    ╭─╯╰─╯ ╰╮   <- right-leaning = yield-tolerant species
    │──────────────────────────  avg yield line
    │  ╭─╮        ╭──╮
    │ ╭╯  ╰╮    ╭─╯  ╰─╮        <- left-leaning = biodiversity-only species
    │
low yield assoc.
    └──────────────────────────
      low biodiv assoc.    high biodiv assoc.
```

Upper-right = tulips that are full AND right-leaning (or symmetric) = sweet-spot species.

---

## Related files

- `designs/ideas/species-signature-glyph-scatter.md` — companion idea; sites as glyphs instead of species
- `research/ideas_creative_combined_visualisations/combined-viz-ideas.md` — S-02 (heatmap), S-05 (radial wheel), E-04 (trade-off scatter with clusters)
