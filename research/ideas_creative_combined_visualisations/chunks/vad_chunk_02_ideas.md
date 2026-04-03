# [agent_17] Visualization Analysis and Design — pages 51-100

## Theoretical Grounding for This Chunk

This chunk introduces three key conceptual layers that directly inform creative combination:

1. **Data abstraction:** the dataset can and should be transformed. Deriving new attributes (e.g. differences, ratios, rankings) before encoding enables richer visualization. "Don't just draw what you're given." (p.76)
2. **Task abstraction:** user goals have three levels — analyze (discover/present/enjoy), search (lookup/locate/browse/explore), and query (identify/compare/summarize). Each idiom combination should support a specific goal at each level.
3. **Nested validation model:** every design choice must be justified against (a) what the user actually needs, (b) whether the abstraction is correct, (c) whether the encoding works perceptually, (d) whether the implementation is fast enough.

These concepts imply that the most powerful visualization ideas for the coffee dataset will involve: (a) deliberate data derivation before encoding; (b) multi-level task support (overview + detail + compare); and (c) multiple coordinated views linked by shared color or selection.

---

### Idea: Yield-Biodiversity Trade-off Corridor Map (inspired by p.76–78, p.87–89)
- **Basic visuals combined:** Scatterplot (yield vs. total species richness) + color-coded site markers + linked site map or bar chart of management variables.
- **What the combination adds:** The scatterplot alone shows the trade-off; adding the linked management-variable panel allows the user to immediately ask "which management practices sit in the 'sweet spot' — high yield AND moderate richness?" and identify which variables distinguish those sites. Neither view alone answers this question.
- **Data manipulation applied:** Derive a new attribute: "trade-off score" = normalized_yield − normalized_biodiversity_loss (or alternatively: yield / species_loss_rate). This derived variable directly encodes the efficiency of each site and can be encoded as color or sorted as an axis.
- **Marks:** Circles (sites) in scatterplot; bars (management variables) in linked panel.
- **Channels:** Position x = yield (quantitative); Position y = total species richness (quantitative); Color hue = cluster assignment (categorical); Size = Strahler-analog: relative trade-off score; linked color highlight shared across views.
- **User task supported:** Explore (find pattern in trade-off space) → Compare (compare management profiles of sites in different quadrants) → Identify (call out specific top-performing sites).
- **What it shows for our data:** Directly visualizes the core tension: are high-yield sites always low-biodiversity? Do clusters reveal distinct management strategies? Are there outlier sites that beat the trade-off?
- **Persona it serves:** Elena (scientist) — sees full correlation structure; Sofia (conservationist) — can identify and argue for the "sweet spot" sites as conservation priority.
- **Interaction if needed:** Brushing sites in the scatterplot highlights their management bar profile in the linked panel. Filter by cluster.
- **Page reference:** p.76–78 (derive), p.87–89 (linked derived spaces with shared color highlighting).

---

### Idea: Multi-Scale Species Richness Hierarchy Browser (inspired by p.59, p.85–87)
- **Basic visuals combined:** Treemap or sunburst (species richness hierarchically nested: total → woody/herbaceous/bryophyte → individual species) + bar chart of yield per site, sorted to match selection.
- **What the combination adds:** The treemap reveals the *composition* of biodiversity (which functional group dominates?); the linked bar chart reveals whether sites richer in a *particular group* also achieve higher or lower yields. Neither chart alone answers this.
- **Data manipulation applied:** Aggregate species counts per functional group per site. Derive a "group diversity ratio" attribute (e.g. woody species % of total). Hierarchical aggregation of species data mirrors Munzner's hierarchical attribute discussion (p.59).
- **Marks:** Nested rectangles (treemap); bars.
- **Channels:** Area = species richness magnitude; Color hue = functional group type (categorical: woody/herbaceous/bryophyte); Bar length = yield; shared color highlight on selection.
- **User task supported:** Browse (explore which plant groups are represented at each site) → Compare (compare functional group composition across sites) → Summarize (see distribution of group proportions across all sites).
- **What it shows for our data:** Does the biodiversity-yield trade-off differ by functional group? Are woody-species-dominated sites higher or lower yield? Does bryophyte presence correlate with site quality?
- **Persona it serves:** Sofia (conservationist) — community composition across management gradient; Elena (scientist) — group-level correlation structure.
- **Interaction if needed:** Click a functional group in the treemap to filter the bar chart to only show sites where that group is dominant. Hover for species count tooltips.
- **Page reference:** p.59 (hierarchical attributes), p.85–87 (deriving derived attributes for filter/summarize tasks).

---

### Idea: Site Trajectory Dashboard — "What-Why-How" for Farmers (inspired by p.68–76, p.82–83)
- **Basic visuals combined:** Small multiples line graph (3-year yield trend per site) + dot strip plot (yield distribution across all sites, showing current year) + site-level detail panel (spider/radar chart of 5 shrub structure variables).
- **What the combination adds:** The line graph shows temporal trend (is this site improving or declining?); the strip plot shows where this site sits relative to all others (rank context); the radar chart shows the structural profile underlying performance. Together they answer: "Is my site improving? Am I above average? What drives my performance?"
- **Data manipulation applied:** Derive year-over-year yield change attribute (delta); derive percentile rank across all sites for each year. Normalize the 5 shrub structure variables for radar chart display.
- **Marks:** Lines (yield trends per site); points (strip plot positions); polygon fill (radar chart).
- **Channels:** Position x = time (sequential quantitative); Position y = yield; Color hue = cluster (site management group, categorical); Point position on strip = current rank; Radar area = structural profile shape.
- **User task supported:** Identify (look up my site's trend) → Compare (compare my site to cluster average and to overall distribution) → Discover (find whether my structural profile matches high-yield profiles).
- **What it shows for our data:** Whether yield is changing over the 3 years and whether that change is structurally explained. Which cluster a site belongs to, and whether it is performing above or below cluster average.
- **Persona it serves:** Hana (farmer) — wants to compare her site to top performers and understand what to change; can spot whether she is above average and see which structural variables distinguish top sites from hers.
- **Interaction if needed:** Clicking a site on the strip plot populates the line trend and radar chart with that site's data. Toggle to show cluster average overlay on radar.
- **Page reference:** p.68–71 (task abstraction: discover, compare, identify), p.76 (derive new attributes), p.82–83 (how: encode, facet, manipulate preview).

---

### Idea: Species × Yield Heat Matrix with Hierarchical Sorting (inspired by p.61, p.78–80)
- **Basic visuals combined:** Heatmap matrix (species × sites) + dendrogram on both axes (cluster similar species together; cluster similar sites together) + marginal bar charts (total species richness per site, average yield per species).
- **What the combination adds:** The raw presence/absence matrix is too large and complex to read without ordering. Hierarchical clustering of both axes groups sites with similar species composition together AND groups species that co-occur together. Marginal bars show at a glance which sites are richest and which species are associated with high yield. This is a classic double-dendrogram heatmap (bicluster matrix).
- **Data manipulation applied:** Hierarchical clustering of the 60-site × 407-species presence/absence matrix to derive a dendrogram ordering for both axes. Compute per-species average yield across all sites where it occurs (column marginal). Compute per-site total species richness (row marginal).
- **Marks:** Filled cells (presence = colored, absence = white/grey); lines (dendrogram branches); bars (marginals).
- **Channels:** Cell color saturation = presence/abundance magnitude; dendrogram position = cluster membership; bar length = richness or average yield.
- **User task supported:** Explore (find clusters of species that co-occur) → Compare (compare species composition between site clusters) → Identify (which individual species are associated with high-yield sites).
- **What it shows for our data:** Whether there are species guilds that consistently appear together; whether high-yield sites form a distinct species composition cluster; which indicator species predict either high yield or high biodiversity.
- **Persona it serves:** Elena (scientist) — sees full correlation structure and methodological rigour; Sofia (conservationist) — identifies biodiversity hotspot clusters in the site dendrogram.
- **Interaction if needed:** Hover on a cell for site name + species name + yield. Click dendrogram branch to isolate a cluster of sites. Filter to show only woody / herbaceous / bryophyte species using a toggle.
- **Page reference:** p.61 (multidimensional tables with multiple keys), p.78–80 (browse + explore search), p.87–89 (linked views with shared color).

---

### Idea: Management Gradient Narrative Strip (inspired by p.72–74, p.82–83)
- **Basic visuals combined:** Horizontally sorted parallel-coordinates-style strip (sites ordered left to right by management intensity index) + color-coded density ribbons per variable (yield, structure index, species richness) + annotations marking cluster boundaries.
- **What the combination adds:** Standard parallel coordinates show attribute profiles but don't carry narrative. Sorting the x-axis by management intensity and adding density ribbons (rather than individual lines) reveals the *direction of change across the management gradient* — which variables rise, which fall, and where the crossover point is. This makes the biodiversity-yield trade-off not just visible but persuasive as a narrative.
- **Data manipulation applied:** Sort sites by management intensity (density or structure index). Compute rolling average for each variable across the gradient. Derive "crossover points" where yield and richness curves intersect.
- **Marks:** Ribbons/density bands (one per variable); point markers for cluster boundaries; annotation arrows.
- **Channels:** Position x = management gradient (ordered quantitative); Position y = value of each variable (quantitative); Color hue = variable identity (categorical); Ribbon width = variability across sites at that gradient position.
- **User task supported:** Present (tell the trade-off story) → Compare (how do yield and richness move relative to each other along the gradient) → Identify (where is the crossover / sweet spot).
- **What it shows for our data:** Directly embeds the core scientific narrative: as management intensity increases, yield rises but biodiversity falls. Ribbon width shows whether this is consistent or variable. Annotations mark where the two curves cross and where clusters transition.
- **Persona it serves:** Sofia (conservationist) — trade-off visible and persuasive, compelling for advocacy; can be used as a "present" goal visualization for communicating to policy audiences.
- **Interaction if needed:** Minimal — designed for presentation. Optional: hover to reveal individual site identities along the gradient.
- **Page reference:** p.72–73 (present goal: succinct communication, story with data), p.82–83 (encode: order + align; map: color hue for categories).

---

### Idea: Derived Difference Map — "What Changes When You Trade Off?" (inspired by p.77–78)
- **Basic visuals combined:** Two side-by-side bar charts (one sorted by yield rank, one sorted by species richness rank) with lines connecting the same site's position in each ranking + a derived "rank divergence" bar chart below showing the magnitude of rank change.
- **What the combination adds:** Directly applies Munzner's trade balance example (p.77): instead of requiring users to judge relative positions across two charts, the derived "rank divergence" attribute (yield_rank − richness_rank) is encoded directly as a signed bar, making sites that achieve both above-average yield AND above-average richness immediately visible as outliers.
- **Data manipulation applied:** Derive rank attributes for each site on both yield and species richness. Compute derived divergence = yield_rank − richness_rank. Positive = better at yield than richness; negative = better at richness than yield. Sites near zero are the "sweet spot."
- **Marks:** Bars (rank positions); connecting lines (same site across two orderings); signed bars (divergence).
- **Channels:** Bar length = rank position; Line connections = identity across views; Bar color saturation = magnitude of divergence; Bar color hue = direction of divergence (yield-favoring vs. richness-favoring).
- **User task supported:** Compare (which sites perform consistently well on both?) → Identify (which specific sites are outliers that beat the trade-off?) → Summarize (what is the overall distribution of the divergence?).
- **What it shows for our data:** Directly reveals whether the yield-biodiversity trade-off is universal across all 60 sites or whether some sites genuinely escape it.
- **Persona it serves:** Elena (scientist) — methodological interest in the distribution of divergence and outlier detection; Hana (farmer) — can identify which sites near her cluster achieve the best combination.
- **Interaction if needed:** Click a connecting line to highlight the site and show its management profile in a popup.
- **Page reference:** p.77–78 (derived difference attribute preferable to raw comparison for comparison tasks; trade balance = exports − imports example).

---

### Idea: Cyclic/Temporal Yield Pattern Viewer (inspired by p.59, p.63–64)
- **Basic visuals combined:** Radial/circular bar chart (one spoke per year, 3 years of yield per site) + cluster-colored background sectors + small multiple version showing all 60 sites simultaneously.
- **What the combination adds:** Treating the 3-year measurement as a short cyclic or sequential temporal dataset and using a radial layout makes year-over-year stability vs. variability visible. Sites with consistent radial symmetry are stable; asymmetric spokes show directional change. Cluster coloring on background sectors immediately shows whether variability is cluster-specific.
- **Data manipulation applied:** Normalize yield per site across the 3 years (so the radial length encodes relative within-site change, not absolute value). Compute coefficient of variation across years as a derived stability attribute. Arrange sites as small multiples grouped by cluster.
- **Marks:** Spokes/bars (yield per year per site); circular sectors (cluster background).
- **Channels:** Length = yield (quantitative); Angle = year (ordinal/cyclic with only 3 values — sequential better); Color hue = cluster (categorical).
- **User task supported:** Compare (is year-to-year yield stable within a cluster?) → Summarize (how consistent is yield across all sites?) → Identify (which sites changed most?).
- **What it shows for our data:** Whether high-yield sites are consistently high or fluctuating; whether the 3-year average is a reliable proxy for individual year performance.
- **Persona it serves:** Hana (farmer) — wants to know if top performers are reliably top or just lucky in one year; Elena (scientist) — temporal variability as methodological concern.
- **Interaction if needed:** Click a small multiple to expand it; toggle between normalized (relative change) and absolute (actual yield) radial scale.
- **Page reference:** p.59 (cyclic and hierarchical temporal attributes), p.63–64 (temporal semantics, time-varying data, time-series dataset definition).
