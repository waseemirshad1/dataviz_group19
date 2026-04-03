# [agent_03] Cool Infographics — pages 101-150

## Creative Combined Visualization Ideas

These ideas are inspired by visualizations seen in pages 101–150 of Cool Infographics (primarily Chapter 4 on Infographic Resumes). The resume examples in this section are an unusually rich source of inspiration because they solve the same problem our assignment faces: showing multiple variables about 60 individual "items" (sites, not people) in ways that allow comparison, ranking, and pattern discovery.

---

### Idea: The Career Timeline Becomes a Site Trajectory — Stacked Area Chart of Biodiversity Over a Yield Gradient (inspired by p.138–140)

- **Basic visuals combined:** Stacked area chart (from Randall Knapp / Mike Wirth resume designs) + ranked bar chart
- **What the combination adds:** The stacked area chart alone shows composition; the ranked bar chart alone shows a single variable. Combined: sites are sorted along the x-axis by yield (low to high), and for each site position a stacked bar of species richness by group (woody / herbaceous / bryophytes / total) rises from the baseline. The viewer reads both the yield gradient AND the simultaneous change in biodiversity composition as a continuous "wave" from left to right.
- **Data manipulation applied:** Sites ranked by mean coffee yield (continuous quantitative → ordinal position). Species richness aggregated per plant group per site (four summary counts). No individual species shown — group-level abstraction prevents overload.
- **Marks:** Stacked vertical bars (one per site, 60 total), color bands within each bar for each plant group
- **Channels:** Horizontal position = yield rank (low → high); bar height = total species richness; color hue = plant group (woody / herbaceous / bryophytes); stacked segment height = species richness per group
- **User task supported:** Spot trade-off, compare, identify pattern
- **What it shows for our data:** Whether total and group-specific biodiversity systematically declines as yield increases; whether any plant group is more sensitive to management than others
- **Persona it serves:** Sofia Almeida — directly answers "Do high-yield sites have lower species richness?" and "Which plant group is most sensitive?" Also useful for Elena Novak: "Which management gradient shows the strongest biodiversity response?"
- **Interaction if needed:** Hover over a bar to see site ID, exact species counts per group, and management variable values. Filter by plant group to isolate one color band.
- **Page reference:** p.138–140

---

### Idea: The Butterfly Spine — Yield vs. Biodiversity as a Mirrored Bar Chart Along a Management Gradient (inspired by p.141, Duncan McKean)

- **Basic visuals combined:** Butterfly / spine chart (education/employment mirrored around central axis) + scatter of management variables
- **What the combination adds:** The butterfly chart shows two opposing variables on the same time/gradient axis. Here: central spine = management intensity (coffee structure index, low to high, as vertical axis). Bars extend LEFT = species richness (declining as management intensity rises). Bars extend RIGHT = coffee yield (rising as management intensity rises). The opposing directions make the trade-off physically visible — the chart literally splits apart toward the ends.
- **Data manipulation applied:** Sites sorted by management intensity (coffee structure index) along the vertical axis. Mean yield and total species richness both normalized to 0–100% of their respective ranges for visual comparability. Each site = one row.
- **Marks:** Horizontal bars (left = biodiversity, right = yield), central spine line (management intensity scale)
- **Channels:** Vertical position = management intensity (low → high); left bar length = species richness; right bar length = mean yield; color hue = left (green, biodiversity) vs. right (amber, yield)
- **User task supported:** Spot trade-off, compare, rank
- **What it shows for our data:** The yield-biodiversity trade-off as a mirror structure. High-management sites have long right bars (yield) and short left bars (biodiversity) — visually the design tears apart at the extremes.
- **Persona it serves:** Sofia Almeida — most persuasive visualization of the trade-off; "hard to deny" because the opposing bar directions make the relationship spatially undeniable. Also answers: "Are there any sites that manage both high yield and high biodiversity?" (sites where both bars are moderately long)
- **Interaction if needed:** Color-code sites that are in the top quartile of BOTH yield and biodiversity (anomaly sites) — highlight in a distinct color to answer "are trade-off exceptions possible?"
- **Page reference:** p.141 (Duncan McKean butterfly spine)

---

### Idea: The Glyph Portfolio — Each Site as a Multi-Dimensional Mini-Profile (inspired by p.132, Michael Anderson dual-dimension donut)

- **Basic visuals combined:** Donut/pie chart with dual dimensions (angle + height from Anderson resume) + small multiples grid
- **What the combination adds:** A small multiples grid of 60 site glyphs. Each glyph is a small radial chart (like Anderson's skill donut): segments = plant groups (woody / herbaceous / bryophytes), angle = relative species richness of that group, height/radius = management intensity. Color of the glyph border = yield quartile (dark amber = highest yield, light yellow = lowest yield). The viewer can scan all 60 sites simultaneously and identify visual patterns.
- **Data manipulation applied:** Species richness per group normalized within each site to show composition (not absolute count). Management intensity mapped to glyph radius. Yield mapped to 4 color classes (quartiles). Sites arranged in a grid sorted by mean yield.
- **Marks:** 60 small radial glyphs (one per site), each with 3–4 segments
- **Channels:** Glyph segment angle = relative species richness per plant group; glyph overall size/radius = management intensity; glyph border color = yield quartile; grid position = yield rank
- **User task supported:** Compare (sites), identify (outliers), explore (patterns across the grid)
- **What it shows for our data:** At a glance: do high-yield (dark border) sites systematically show smaller, more uniform glyphs (lower biodiversity)? Do low-yield (light border) sites show larger, more varied glyphs? Are there any anomalies?
- **Persona it serves:** Elena Novak — reveals dataset structure and cluster patterns across all 60 sites simultaneously; supports methodological decisions about which sites are representative. Also useful for Sofia Almeida to identify biodiversity hotspots visually.
- **Interaction if needed:** Click on any glyph to expand to a full site profile showing all management variables, individual species lists, shrub cluster membership, and year-by-year yield stability.
- **Page reference:** p.132 (Anderson dual-dimension donut)

---

### Idea: The Mountain Slope of Yield — Sites Positioned on a "Difficulty Gradient" (inspired by p.105, Google PageRank mountain metaphor)

- **Basic visuals combined:** Metaphor-driven slope/gradient chart (PageRank mountain) + labeled scatter plot
- **What the combination adds:** The mountain metaphor maps naturally to the coffee yield context: "climbing toward higher yield requires effort (management investment) but at a cost (biodiversity loss)." A diagonal slope from lower-left (low yield, high biodiversity) to upper-right (high yield, low biodiversity) positions all 60 sites. Each site is a circular dot, sized by total species richness and colored by management intensity tier.
- **Data manipulation applied:** X-axis = mean coffee yield; Y-axis = total species richness. Management intensity mapped to color tier (4 classes). Species richness as a circle size channel. Background illustration: a coffee plant that grows larger toward the lower-left (high biodiversity) and smaller toward the upper-right (high yield, less shade).
- **Marks:** Circular dots (sites), diagonal gradient line, background coffee-plant illustration
- **Channels:** Horizontal position = mean yield; vertical position = total species richness; dot size = management intensity (larger = more intensively managed); color hue = management tier
- **User task supported:** Spot trade-off, identify outliers, compare
- **What it shows for our data:** The negative correlation between yield and biodiversity. Sites in the upper-left are high-biodiversity, low-yield. Sites in the lower-right are high-yield, low-biodiversity. Sites near the diagonal are "on the trade-off curve." Outliers above or below the trend line are the most interesting sites.
- **Persona it serves:** Sofia Almeida — the trade-off is the central visual message; metaphor-driven design makes it persuasive and emotionally legible. Hana Abebe — she can locate her sites on the slope and see whether there is a practical path to higher yield (moving right on the gradient).
- **Interaction if needed:** Hover over any dot to see site name, exact yield values (3 years), species counts per group, shrub cluster. Color toggle between management intensity tiers and plant group dominance.
- **Page reference:** p.105 (mountain metaphor chart)

---

### Idea: The Overlapping Timeline of Yield Stability — Area Chart of 3-Year Yield per Site (inspired by p.132, p.138)

- **Basic visuals combined:** Overlapping area chart (Anderson/Knapp timeline style) + small multiples
- **What the combination adds:** 60 small overlapping area charts arranged in a grid, each showing 3-year yield as an area profile. Year 1, Year 2, Year 3 on the x-axis; yield value on y-axis. The area fill shows whether yield is stable (flat top) or volatile (rising/falling shape). Sites sorted by mean yield. The viewer can scan all 60 sites and immediately see which are reliable producers vs. volatile ones.
- **Data manipulation applied:** Each site's 3 yearly yield values normalized to a common y-scale. Sites grouped into quartiles by mean yield and arranged left-to-right within quartile groups. The range (max − min) computed per site as a volatility index — sites with high range get a colored border highlight.
- **Marks:** Small area charts (one per site), colored border around volatile sites
- **Channels:** X position within glyph = year (1, 2, 3); area height = yield value; area shape = stability vs. volatility; grid position = mean yield rank; border color = volatility flag
- **User task supported:** Identify (reliable vs. unreliable producers), compare, rank
- **What it shows for our data:** Which sites deliver consistent yield year-over-year vs. which fluctuate. High-mean but high-volatility sites may be risky investments for Hana. Are the most stable high-yield sites also the most intensively managed?
- **Persona it serves:** Hana Abebe — directly answers "Is yield stable across years, or are some sites unreliable?" Elena Novak — "How strongly do the 3 yearly yield measurements agree? Is the mean a reliable proxy?"
- **Interaction if needed:** Click on any small area chart to expand to full-size with management variable overlays showing whether volatility correlates with management intensity changes.
- **Page reference:** p.132, p.138

---

### Idea: The Connection Matrix of Species × Yield — Which Species Track High Yield Environments? (inspired by p.122, Wine & Food connection matrix)

- **Basic visuals combined:** Connection matrix / flow lines (Pairing Wine & Food) + heatmap
- **What the combination adds:** The wine-food matrix uses lines to connect two sets of categorical items. Here: rows = plant species (or grouped by family/type), columns = yield quartile bins (Q1 low yield → Q4 high yield). A heatmap cell shows how frequently each species appears in sites of each yield tier. Dark cells = species strongly associated with that yield tier. Lines connect species with the strongest cross-quartile associations (appearing in all 4) vs. specialist species (only Q1 or only Q4).
- **Data manipulation applied:** For each of the 407 species: compute average site yield and number of sites it occurs in (already in the dataset). Bin species into "low-yield specialists," "high-yield specialists," and "generalists" based on mean yield of occurrence sites. Show top 30–40 species (enough for pattern, not overwhelming).
- **Marks:** Heatmap cells (species × yield quartile), optional connecting lines for strongest associations
- **Channels:** Cell color saturation = frequency of species occurrence at that yield level; row position = species identity; column position = yield quartile; optional line = cross-quartile pattern
- **User task supported:** Identify (yield-indicator species), explore, find outliers
- **What it shows for our data:** Which specific species are strongly associated with high-yield sites (potential indicator species for management intensity) vs. which species are found only at low-yield, biodiverse sites (biodiversity indicator species worth protecting).
- **Persona it serves:** Sofia Almeida — "Which specific species are only found at low-yield (biodiverse) sites?" This answers the most granular biodiversity question. Elena Novak — "Which species would be the best indicators to measure in a new field study?"
- **Interaction if needed:** Filter by plant group (woody/herbaceous/bryophytes). Hover over a cell to see species name, occurrence count, and site list. Sort rows by "yield association score" (mean yield of occurrence sites) to move high-yield specialists to top and low-yield specialists to bottom.
- **Page reference:** p.122

---

### Idea: The Viral Sharing Network as a Species Co-Occurrence Network — Which Sites Share Rare Species? (inspired by p.109, viral sharing radial network)

- **Basic visuals combined:** Radial/network diagram (viral sharing tree) + proximity-based clustering
- **What the combination adds:** The viral network shows connections between nodes through shared links. Here: nodes = 60 sites, link strength = number of shared rare species (species occurring in 5 or fewer sites). Sites that share many rare species are pulled close together; sites with no rare species in common are far apart. Node size = total species richness. Node color = yield quartile.
- **Data manipulation applied:** From the species-composition presence/absence matrix, compute a pairwise site-similarity matrix based on Jaccard index (shared species / union of species). Filter to rare species only (occurring in ≤5 sites). Run a force-directed layout to position sites. Sites form clusters of shared rare species.
- **Marks:** Circular nodes (sites), lines/edges (shared rare species), node size = species richness, node color = yield quartile
- **Channels:** Position (proximity) = similarity in rare species composition; node size = total species richness; node color hue = yield quartile; edge thickness = number of shared rare species
- **User task supported:** Explore, identify (biodiversity hotspot clusters), spot outliers
- **What it shows for our data:** Which groups of sites form rare-species communities (ecological clusters). Whether high-yield sites (dark colored nodes) cluster separately from low-yield sites (light colored nodes) — if so, the network makes the ecological segregation visible as spatial separation.
- **Persona it serves:** Sofia Almeida — reveals where biodiversity hotspots are concentrated and whether they form a coherent group of sites that could be targeted for conservation. Elena Novak — reveals underlying ecological structure of the dataset that purely statistical analyses may miss.
- **Interaction if needed:** Hover over a node to see site name, yield, and list of rare species. Click a node to highlight all connected edges. Filter by minimum edge weight (showing only connections with 3+ shared rare species).
- **Page reference:** p.109

---

### Idea: The Shrub Cluster Glyph — Each Shrub Cluster Group as a Multi-Variable Morphological Portrait (inspired by p.132, Anderson dual-dimension donut)

- **Basic visuals combined:** Radar / spider chart (implicit from multi-variable glyphs) + grouped dot plot
- **What the combination adds:** The four shrub cluster groups (from cluster analysis of 7 morphological variables) are shown as four large radar glyphs — one per cluster. Each axis of the radar = one morphological variable (e.g., stem diameter, canopy height, branch count, etc.). Overlaid dots on each axis show the distribution of values within the cluster (not just the mean). Beside each radar, a small bar shows the mean yield of sites in that cluster.
- **Data manipulation applied:** Cluster assignments already computed. For each cluster: compute mean and range of all 7 morphological variables per cluster. Normalize all variables to 0–1 scale for radar comparability. Compute mean yield per cluster as a bar annotation.
- **Marks:** Radar polygon (mean cluster profile), shaded band (range of values), bar (mean yield per cluster)
- **Channels:** Radar axis = morphological variable; polygon vertex distance = mean variable value; shaded band width = within-cluster variation; bar length = mean yield
- **User task supported:** Identify (cluster identity), compare (clusters to each other), explore (which morphological traits associate with higher yield)
- **What it shows for our data:** The internal structure of each shrub cluster — what makes cluster 1 different from cluster 2 morphologically, and whether the highest-yield cluster also has distinctive morphological traits.
- **Persona it serves:** Elena Novak — "What is the internal structure of the shrub cluster groups?" and "Which variables would she prioritize measuring?" Hana Abebe — "Which shrub cluster type is associated with higher production?" — if one cluster consistently shows higher yield, she has an actionable target for shrub management.
- **Interaction if needed:** Hover over each radar axis to see the variable description and distribution histogram for that variable within the cluster.
- **Page reference:** p.132
