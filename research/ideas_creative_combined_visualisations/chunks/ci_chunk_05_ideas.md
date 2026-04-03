# [agent_05] Cool Infographics — pages 201-249

## Overview

Pages 201–249 are heavy on design principles and tools, with fewer gallery-style visuals than earlier chapters. However, several specific design techniques inspire directly applicable ideas: the vertical graduated scale (Caffeine Poster), inline icon replacement of legends, the ranked-pie + extended legend-line hybrid, area-based bubble sizing, and the character-flow path diagram. Ideas below are drawn from these.

---

### Idea: The Yield Ladder — Graduated Site Ranking with Embedded Biodiversity Profiles (inspired by p.210)

- **Basic visuals combined:** Vertical graduated scale (like the Caffeine Poster) + small horizontal stacked bar glyphs embedded at each site's position on the scale.
- **What the combination adds:** The scale alone ranks sites by yield. The stacked bar glyph at each position adds the biodiversity breakdown (woody / herbaceous / bryophyte species counts) without requiring a separate chart. The question "which sites rank highest in yield AND what is their biodiversity profile?" can be answered in a single glance — something neither the ranked list nor the stacked bar alone could provide.
- **Data manipulation applied:** Sites sorted by mean yield (continuous scale); biodiversity counts normalized to proportions within each site's total species richness so the stacked bar is a constant visual width regardless of absolute species count. This focuses on composition rather than absolute count.
- **Marks:** Vertical scale bar (color-graded from dark green at top = high yield, to pale yellow at bottom = low yield); small horizontal stacked bar attached to each site's position on the scale; site labels.
- **Channels:** Position on vertical axis (mean coffee yield — most accurate channel for the primary variable); color saturation of scale bar (yield level at a glance); stacked bar segment width (proportion of total species richness from each plant group — woody / herbaceous / bryophyte, color-coded); label text (site identifier).
- **User task supported:** Rank sites by yield; simultaneously identify biodiversity composition at each rank position; spot trade-off (do top-yield sites show a consistent shift toward one plant group?).
- **What it shows for our data:** Mean yield per site (y-axis position), species richness composition breakdown per site (stacked bar glyph), the 60 sites compared all at once.
- **Persona it serves:** Hana Abebe — she can see which of her sites are top/bottom performers AND immediately see whether high-yield sites share a biodiversity pattern she could act on. Also Sofia Almeida — the trade-off becomes visible as a gradient: do the stacked bars change systematically as you move down the ladder from high to low yield?
- **Interaction if needed:** Hovering on a site's glyph reveals full species count per group and the three annual yield values (to show year-to-year stability). Click to filter: highlight only sites within a selected yield band.
- **Page reference:** p.210

---

### Idea: The Biodiversity Cost Bubble Map — Yield vs. Total Species Richness with Area-Correct Management Bubbles (inspired by p.203–205)

- **Basic visuals combined:** Scatterplot (yield × total species richness) + area-sized bubble (encoding management intensity — coffee structure index) overlaid on each point.
- **What the combination adds:** The scatterplot alone shows the yield–biodiversity trade-off. The correctly area-sized bubble at each point encodes how intensively managed the site is. This answers a question neither chart alone could answer: "Is the yield–biodiversity trade-off driven primarily by management intensity, and do high-management sites cluster at high-yield / low-biodiversity?" All three variables visible simultaneously.
- **Data manipulation applied:** Coffee structure index used as the bubble area variable (must be correctly calculated: area proportional to index value, radius derived from area). Sites without extreme values could be slightly alpha-blended to reduce occlusion in the cluster center.
- **Marks:** Circles (one per site), positioned on a 2D scatterplot.
- **Channels:** X-axis position (mean coffee yield — quantitative, primary trade-off axis); Y-axis position (total species richness — quantitative); circle area (coffee structure index = management intensity — sized by area formula, not diameter); color hue (optional: shrub cluster group from cluster analysis, as categorical identity).
- **User task supported:** Spot trade-off (yield vs. biodiversity); identify whether management intensity mediates the trade-off; find outlier sites that combine high yield with high richness.
- **What it shows for our data:** The core trade-off between coffee productivity and plant diversity, modulated by management intensity, across all 60 sites.
- **Persona it serves:** Sofia Almeida — makes the trade-off undeniable and shows whether it is driven by management. Elena Novak — shows the correlation structure of three key variables simultaneously and helps her decide which variables to prioritize in a new study.
- **Interaction if needed:** Hover on a bubble to show site ID, yield values for all 3 years, species richness per group, and management variable values. Filter by shrub cluster group to see whether cluster membership predicts position in the trade-off space.
- **Page reference:** p.203–205

---

### Idea: The Species Sensitivity Flow Diagram — Which Plant Groups Track the Yield Gradient (inspired by p.213)

- **Basic visuals combined:** Flow/path diagram (inspired by the Star Wars character path structure) + color-coded species group "streams" flowing across a yield gradient axis.
- **What the combination adds:** A standard grouped bar chart would show richness by plant group per site in isolation. A flow diagram shows how each plant group's richness rises and falls continuously as sites are ordered along the yield gradient — making which group "collapses" first at high yield immediately apparent. The combination answers: "As yield increases, do woody plants, herbaceous plants, and bryophytes decline together or at different rates?"
- **Data manipulation applied:** Sites sorted along the x-axis by mean yield (continuous gradient). For each of the three plant groups (woody / herbaceous / bryophyte), a smoothed trend line (rolling average or LOESS) is calculated across the yield gradient. The width or thickness of each stream encodes species richness at that point — wide = high richness, narrow = low richness. This is a streamgraph-style approach applied to ecological sensitivity.
- **Marks:** Three flowing ribbon/stream shapes (one per plant group), positioned on a shared yield-gradient x-axis.
- **Channels:** X-axis position (site's mean yield — the gradient dimension); stream width/thickness at each x-position (species richness of that plant group — the sensitivity signal); color hue (plant group identity: e.g., brown for woody, green for herbaceous, grey-blue for bryophytes); stream overlap (showing relative dominance at each yield level).
- **User task supported:** Spot trade-off; identify which group is most sensitive to yield intensity; find threshold points where richness drops sharply.
- **What it shows for our data:** Species richness of each plant group across the yield gradient — making differential sensitivity between plant groups visible.
- **Persona it serves:** Sofia Almeida — directly answers "which plant group is most sensitive to management intensity?" and allows her to build a persuasive argument about which ecological community is most threatened. Elena Novak — helps her decide which plant group to prioritize measuring in a new field study.
- **Interaction if needed:** Hover on any point along a stream to see the specific sites at that yield level with their actual species counts. Toggle smoothing on/off to see raw site-level variation vs. trend.
- **Page reference:** p.213

---

### Idea: The Site Portrait Grid — Small Multiple Radar Glyphs Sorted by Yield (inspired by p.215 inline icon embedding)

- **Basic visuals combined:** Small multiple grid layout + radar/spider chart glyph per site (each showing 5–7 key variables simultaneously).
- **What the combination adds:** A single radar chart per site shows multiple dimensions. Arranging all 60 sites as small multiples sorted by mean yield creates a visual that allows pattern recognition across the full dataset — do the shapes visually shift as you move from high-yield to low-yield sites? Neither the radar alone nor a simple ranked list can answer this. The combination shows "what does the full profile of a top-yield site look like vs. a low-yield site?" across all 60 at once.
- **Data manipulation applied:** Variables normalized to a 0–1 scale within the dataset so all axes are comparable. Variables shown on each radar: mean yield (or excluded from radar and used as sort key), total species richness, coffee density, coffee dominance, coffee structure index, shrub cluster group (encoded as background color rather than radar axis). Sites arranged in a grid sorted left-to-right and top-to-bottom by descending mean yield.
- **Marks:** Small radar/spider chart polygons (one per site), arranged in a 10×6 or 12×5 grid.
- **Channels:** Position in grid (yield rank — leftmost/top = highest yield); polygon shape (profile of the 5–6 variables — the "fingerprint" of each site); color fill of polygon (optional: hue intensity proportional to yield for quick visual reinforcement); background cell color (shrub cluster group — categorical).
- **User task supported:** Identify site profiles; spot which variables distinguish top-yield sites from low-yield sites; explore whether cluster group membership correlates with yield rank position in the grid.
- **What it shows for our data:** The full multivariate profile of each site, ranked by yield, allowing comparison of profile shapes across the yield spectrum.
- **Persona it serves:** Hana Abebe — can see whether her highest-yield sites share a consistent "shape" (e.g., consistently high coffee density + low species richness) suggesting actionable site conditions. Elena Novak — can use this to identify which variables show the strongest visual differentiation between high and low yield sites, informing variable prioritization.
- **Interaction if needed:** Hover to reveal site label and all raw variable values. Click to isolate and enlarge a single site's radar. Filter by shrub cluster group to see whether cluster members share visual profile shapes.
- **Page reference:** p.215

---

### Idea: The Species × Yield Ranked Fan Chart — Which Species Predict High or Low Yield (inspired by p.208–209 ranked pie with leader lines)

- **Basic visuals combined:** Ranked horizontal bar chart + leader-line annotation + threshold divider line separating high-yield from low-yield associated species.
- **What the combination adds:** A standard list of species sorted by associated yield would be a ranked table — not visually legible for 407 species. The ranked bar chart makes the distribution of yield associations immediately visible. The leader-line technique (from the ranked pie chart) solves the crowding problem by pulling out the extreme high and low performers for explicit annotation. The combination answers: "Which specific species are most strongly associated with high yield vs. low yield, and what is the distribution shape?"
- **Data manipulation applied:** For each of the 407 species, use the pre-existing "average yield of sites where species occurs" metric. Sort species by this average yield. Filter to show only species occurring in at least 3 sites (to exclude noise from rare species). Display as a horizontal ranked bar chart with a vertical threshold line at the overall mean yield. Leader lines from extreme species (top 10 / bottom 10) extend to annotation boxes naming the species and their occurrence count.
- **Marks:** Horizontal bars (one per species), threshold line, leader lines, annotation text boxes for top/bottom performers.
- **Channels:** Bar length (average yield of sites where species occurs); color hue (above/below mean yield threshold — green vs. red, or two-tone diverging); bar opacity (occurrence count — more frequent species are more opaque, rarer species more transparent); position on vertical axis (yield rank).
- **User task supported:** Identify species most associated with high/low yield; spot whether high-yield sites share a set of "indicator species"; explore rarity vs. association strength.
- **What it shows for our data:** Per-species average site yield and occurrence frequency — the "species × yield link" dataset.
- **Persona it serves:** Sofia Almeida — can identify which species are found only at low-yield (biodiverse) sites, making the case for specific conservation priorities. Hana Abebe — can identify positive indicator species associated with high yield sites.
- **Interaction if needed:** Hover on any bar to see species name, number of sites it occurs in, and average yield. Filter by plant group (woody / herbaceous / bryophyte) to see whether the association with yield differs by ecological group.
- **Page reference:** p.208–209

---

### Idea: The Yield Stability Strip Chart — Three Years of Yield per Site with Management Gradient Background (inspired by p.210 Caffeine Poster vertical scale + p.203 area sizing)

- **Basic visuals combined:** Strip/dot plot (showing 3 annual yield measurements per site as dots on a vertical scale) + background color gradient (encoding management intensity — coffee structure index).
- **What the combination adds:** A bar chart of mean yield loses year-to-year variation. A strip chart shows all three annual values per site and their spread, revealing whether high-yield sites are reliably high (tight cluster) or unreliable (wide spread). The background color gradient adds management intensity without an additional axis. The combination answers: "Are high-yield sites reliably high year-to-year, and is yield stability associated with management intensity?" — a question neither chart type alone could answer.
- **Data manipulation applied:** Sites sorted by mean yield on the y-axis. For each site, three dots are plotted at their annual yield values. A connecting line between the three dots shows the range. The background of each site's row is colored by coffee structure index (light to dark) to encode management intensity.
- **Marks:** Dots (3 per site = 3 annual yield measurements), connecting lines between dots (showing year-to-year range), horizontal row backgrounds (management color).
- **Channels:** Y-axis position (site sorted by mean yield); x-axis position within each row (annual yield value); dot spread (year-to-year variability — narrow = stable, wide = unreliable); background color saturation (coffee structure index / management intensity).
- **User task supported:** Compare sites by yield; assess yield stability; spot whether stable high-yield sites also show high or low management intensity.
- **What it shows for our data:** Three annual yield values per site, mean yield rank, and management intensity — all in one view.
- **Persona it serves:** Hana Abebe — she can identify which of her sites are reliable vs. variable producers and whether stability is linked to management approach. Elena Novak — she can assess whether the 3-year mean is a reliable proxy for true yield (do sites with high variability need longer measurement periods?).
- **Interaction if needed:** Hover to show all three year values, mean, and coefficient of variation. Click to highlight all sites in the same shrub cluster group.
- **Page reference:** p.210
