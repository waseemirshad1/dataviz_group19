# [agent_24] Visualization Analysis and Design — pages 401-430

## Note on Source Pages

Pages 401–430 are back matter (Bibliography, Idiom & System Examples Index, Concept Index). The ideas below are inspired by the complete idiom catalogue revealed by the index, combined with earlier chapters' principles — specifically by cross-referencing idioms listed in the index at pages 422–423 with the pages where they are taught, and seeing which combinations are novel for our coffee dataset.

---

### Idea: Species-Yield Scagnostic Explorer (inspired by p. 342–346)

- **Basic visuals combined:** SPLOM (scatterplot matrix) of all quantitative variables (yield, species richness per group, structure variables, dominance, density) + scagnostics-ranked cell highlighting + color by cluster assignment
- **What the combination adds:** Scagnostics automatically surface the most structurally interesting pairwise relationships — not just linear correlations but clumpy, outlying, monotone, striated patterns. This reveals the yield-biodiversity trade-off structure without pre-assuming linearity.
- **Data manipulation applied:** Compute scagnostics (outlying, monotone, clumpy scores) for each pair of variables; rank pairs; color SPLOM cells by most interesting score; overlay cluster assignment as point color within each cell.
- **Marks:** Points (scatterplot cells), colored rectangles for cell-level scagnostic scores
- **Channels:** Position x/y (quantitative attributes), color hue (cluster), cell background intensity (scagnostic score)
- **User task supported:** Discover correlations; identify structure; compare attribute pairs
- **What it shows for our data:** Surfaces the yield × total species richness cell as most interesting (monotone? clumpy?); reveals whether woody species vs. herbaceous species differ in how strongly they relate to yield; detects outlier sites in multi-dimensional space
- **Persona it serves:** Elena (scientist) — methodological rigor, correlation structure, dataset structure
- **Interaction if needed:** Hover cell to expand; filter to subset of attributes; click to see which sites drive the pattern
- **Page reference:** p. 342–346 (Graph-Theoretic Scagnostics), p. 160–161 (SPLOM)

---

### Idea: Biodiversity Trade-Off LineUp (inspired by p. 246–248)

- **Basic visuals combined:** LineUp (multi-attribute ranking bars) with sites as rows, ranked by coffee yield, with parallel attribute bars for woody richness, herbaceous richness, bryophyte frequency, total richness, structure index, cluster
- **What the combination adds:** Allows Hana (farmer) to see at a glance which high-yield sites sacrifice which type of biodiversity, and to interactively re-weight the ranking to ask "what if I prioritize yield AND woody species richness?"
- **Data manipulation applied:** Normalize all attributes to [0,1]; compute composite weighted score; sort by yield descending; color bars by cluster assignment; stack bars for composite ranking
- **Marks:** Horizontal bars per attribute per site
- **Channels:** Length (attribute value normalized), position (rank = y), color hue (cluster)
- **User task supported:** Compare sites by yield; spot top performers; multiple variables simultaneously
- **What it shows for our data:** Top-yield sites visually show short biodiversity bars; middle-yield sites may show longer biodiversity bars — making the trade-off viscerally visible as a visual gap pattern
- **Persona it serves:** Hana (farmer) primary; Sofia (conservationist) secondary (can see where high yield means low conservation value)
- **Interaction if needed:** Weight sliders to adjust composite score; filter by cluster; highlight Pareto-optimal sites (high yield AND high biodiversity)
- **Page reference:** p. 246–248 (LineUp)

---

### Idea: Yield-Biodiversity Horizon Graph Across Sites (inspired by p. 90–91)

- **Basic visuals combined:** Horizon graph (folded time series) adapted for site-ordered data — sites ordered by yield on x-axis, with multiple stacked horizon bands for each biodiversity metric (woody, herbaceous, bryophyte, total richness)
- **What the combination adds:** Horizon graphs use space-efficient layering — four biodiversity metrics can be shown in the vertical space of one chart, making the multi-metric decline (or rise) as yield increases directly visible in a compact space. The folding reveals amplitude at the cost of absolute position.
- **Data manipulation applied:** Order 60 sites by mean coffee yield (x-axis); for each biodiversity metric, normalize to range [0, max] and fold into horizon band layers; use a diverging approach to show above/below-median values
- **Marks:** Area (horizon bands, multiple layers)
- **Channels:** Color (layer = diverging, darker = further from median), position x (yield rank), vertical stacking (biodiversity metric identity)
- **User task supported:** Identify trend; compare multiple metrics simultaneously; spot outlier sites
- **What it shows for our data:** As yield rank increases left to right, do all biodiversity metrics decline together? Or does woody richness hold steady while herbaceous collapses first?
- **Persona it serves:** Elena (scientist) — sees multi-metric pattern; Sofia (conservationist) — sees at which yield threshold biodiversity begins to drop
- **Interaction if needed:** Click site to see detail; adjust folding threshold; reorder sites by different variable
- **Page reference:** p. 90–91 (Sizing the Horizon / horizon graphs)

---

### Idea: Focus+Context Site Map with Cluster Drill-Down (inspired by p. 323–338)

- **Basic visuals combined:** Geographic or ordination-based site map (60 sites as dots, positioned by similarity using MDS of species composition) + fisheye lens focus+context interaction + cluster color coding + linked detail panel showing species composition on hover
- **What the combination adds:** The 407-species composition matrix is too high-dimensional to show directly. MDS (from p. 316–319) places sites in 2D by overall floristic similarity. The fisheye lens lets the user focus on a local neighborhood of sites in compositional space while keeping the rest in context. This enables local comparison without losing global structure.
- **Data manipulation applied:** PCoA/MDS on Bray-Curtis dissimilarity of species × site matrix → 2D coordinates per site; color by cluster assignment (4 clusters from shrub structure variables); size by mean coffee yield; fisheye distortion on hover/click
- **Marks:** Points (sites)
- **Channels:** Position (compositional similarity), color hue (cluster), size (yield), opacity (focus weight in fisheye)
- **User task supported:** Navigate composition space; identify biodiversity hotspot clusters; locate outlier sites
- **What it shows for our data:** Are floristically similar sites also similar in yield? Do the 4 structural clusters correspond to floristic clusters? Are there sites with unique species composition?
- **Persona it serves:** Sofia (conservationist) — composition changes visible; biodiversity hotspots identifiable; Elena (scientist) — dataset structure
- **Interaction if needed:** Hover activates fisheye; click site to see species list; toggle layers (structural cluster vs. floristic cluster)
- **Page reference:** p. 316–319 (dimensionality reduction), p. 323–338 (focus+context / fisheye)

---

### Idea: Species × Site Cluster Heatmap with Yield Sidebar (inspired by p. 158–160)

- **Basic visuals combined:** Cluster heatmap of species × site presence/absence (407 species × 60 sites) with matrix reordering by hierarchical clustering on both axes + yield bar chart sidebar aligned to site columns
- **What the combination adds:** The species composition matrix becomes interpretable through biclustering — groups of species that co-occur in groups of sites emerge as rectangular blocks. The yield sidebar immediately shows whether high-yield sites form a distinct floristic block.
- **Data manipulation applied:** Hierarchical clustering of sites (columns) by Bray-Curtis dissimilarity; hierarchical clustering of species (rows) by co-occurrence; reorder both; encode presence/absence as binary color; add normalized yield bar alongside site dendrogram
- **Marks:** Area (cells in heatmap), bars (yield sidebar)
- **Channels:** Color (binary: present/absent or species abundance), length (yield), position (site and species order from clustering)
- **User task supported:** Identify species groups associated with high-yield sites; compare composition across clusters
- **What it shows for our data:** Are there indicator species for high-yield sites? Do low-yield sites have higher species richness (more filled rows)? This directly tests the biodiversity-yield trade-off at species level.
- **Persona it serves:** Sofia (conservationist) — can identify which species are at risk in high-yield sites; Elena (scientist) — can see clustering methodology at work; Hana (farmer) — can identify what makes top sites distinctive
- **Interaction if needed:** Filter by species group (woody/herbaceous/bryophyte); zoom into site clusters; click species to see which sites it occurs in
- **Page reference:** p. 158–160 (cluster heatmap), p. 288 (spatially ordered treemaps for spatial ordering variant)

---

### Idea: Geographically Weighted Boxplot Transect (inspired by p. 313–315)

- **Basic visuals combined:** Geographically weighted boxplots adapted for a yield-richness transect — sites arranged on x-axis by elevation or management intensity gradient, with boxplots of species richness per group smoothed geographically (a sliding window of neighboring sites)
- **What the combination adds:** Instead of treating 60 sites as independent points, this shows how the distribution of biodiversity metrics varies across an environmental gradient. The sliding window reveals spatial autocorrelation and non-stationarity — does the yield-biodiversity trade-off get stronger at higher elevations?
- **Data manipulation applied:** Order sites by management intensity variable; compute sliding-window boxplot statistics for each biodiversity metric (window = nearest 10 sites on gradient); plot as connected boxplots
- **Marks:** Box (Q1-Q3), whisker, point (outliers)
- **Channels:** Position x (gradient/management intensity), position y (species richness), length (IQR), color (biodiversity metric type)
- **User task supported:** Identify trends in distribution along gradient; detect outlier sites; compare spread vs. median
- **What it shows for our data:** Does the variance in species richness increase or decrease at high-yield sites? Are there threshold effects — a point along the management intensity axis where richness suddenly drops?
- **Persona it serves:** Elena (scientist) — statistical distribution visualization; Sofia (conservationist) — sees where the biggest biodiversity losses concentrate along the gradient
- **Interaction if needed:** Adjust sliding window width; switch between richness groups; overlay raw data points
- **Page reference:** p. 313–315 (geographically weighted boxplots)

---

### Idea: Coordinated Treemap + Parallel Coordinates for Structure Clusters (inspired by p. 213–214, p. 162–166)

- **Basic visuals combined:** Treemap (60 sites, area = coffee yield, color = cluster) linked to parallel coordinates (7 shrub structure variables + yield + total richness per site), with brushing connecting both views
- **What the combination adds:** The treemap gives an immediate visual weight to yield (bigger area = more yield) and cluster structure (color = cluster). The parallel coordinates lets users see what pattern of structural variables defines each cluster and whether yield-rich clusters have lower richness.
- **Data manipulation applied:** Treemap: sites as leaves, area = mean coffee yield, color hue = cluster (4 levels); parallel coordinates: one polyline per site, axes = 7 shrub structure variables + yield + species richness groups; brushing in treemap highlights lines in PCP and vice versa
- **Marks:** Area (treemap cells), lines (polylines in PCP)
- **Channels:** Area (yield — treemap), color hue (cluster — both views), position y per axis (variable value — PCP)
- **User task supported:** Compare cluster yield distributions; identify structural profile of high-yield clusters; spot outlier sites
- **What it shows for our data:** Do the 4 structural clusters form coherent profiles in PCP? Which structural variables most discriminate high-yield from low-yield clusters? Directly supports the core research question about structure × yield interactions.
- **Persona it serves:** Hana (farmer) — spot top performers; Elena (scientist) — correlation structure; Sofia (conservationist) — can see which cluster types support most biodiversity
- **Interaction if needed:** Brush in either view; filter to one cluster; reorder PCP axes; normalize PCP axes
- **Page reference:** p. 213–214 (treemaps), p. 162–166 (parallel coordinates), p. 267 (linked views)

---

### Idea: Animated Transition Species Accumulation Across Yield Groups (inspired by p. 248–249)

- **Basic visuals combined:** Bar chart (species richness per group) that animates as the user drags a yield threshold slider — bars update with smooth animated transitions showing how species richness changes as sites above/below threshold are included
- **What the combination adds:** Animated transitions maintain object constancy — the viewer tracks how individual bars grow or shrink as the threshold moves, making the trade-off feel dynamic and causal rather than static.
- **Data manipulation applied:** Partition sites dynamically by yield threshold; aggregate species richness per group (woody, herbaceous, bryophyte, total) for sites above and below threshold; animate bar heights on slider move
- **Marks:** Bar
- **Channels:** Length (species richness), color hue (species group: woody/herbaceous/bryophyte/total), position (group on x-axis)
- **User task supported:** Identify threshold effects; compare biodiversity between high- and low-yield site groups
- **What it shows for our data:** Is there a specific yield threshold above which certain plant groups disappear? Does total richness decline linearly with yield or step-wise?
- **Persona it serves:** Sofia (conservationist) — trade-off visible and persuasive; Hana (farmer) — understands the cost of pushing for higher yield
- **Interaction if needed:** Yield threshold slider (core); toggle between above/below/both groups; show site count per group
- **Page reference:** p. 248–249 (animated transitions), p. 149–153 (bar charts)
