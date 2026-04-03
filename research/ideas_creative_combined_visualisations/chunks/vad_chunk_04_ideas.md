# [agent_19] Visualization Analysis and Design — pages 151-200

## Creative Combined Visualization Ideas
### Dataset: 60 Ethiopian coffee agroforest sites
### Core tension: Higher yield ↔ Lower biodiversity

---

### Idea: Yield-Biodiversity Scatterplot with Cluster Heatmap Companion (inspired by p.146–161)
- **Basic visuals combined:** Scatterplot (primary) + Cluster Heatmap (companion view)
- **What the combination adds:** The scatterplot reveals the macro trade-off (yield vs. total species richness), identifying outlier sites that achieve BOTH high yield AND high diversity. The cluster heatmap companion then shows those same 60 sites × 7 shrub structure variables, matrix-reordered by hierarchical clustering — connecting the site positions in the scatter to their structural profiles. Neither visual alone answers: "WHY do some sites escape the trade-off?"
- **Data manipulation applied:** Derive yield z-score and species richness z-score; compute Euclidean distance matrix for site × shrub-structure clustering; log-transform yield if skewed (following p.147 example with diamond data)
- **Marks:** Point marks in scatterplot; area marks in heatmap cells
- **Channels:** Scatterplot: H position = mean yield, V position = total species richness, color hue = cluster assignment from heatmap (shared), size = site dominance index; Heatmap: color diverging from mean per variable (saturation = deviation from mean), position = matrix rows (sites) and columns (structure variables)
- **User task supported:** Find outliers (scatterplot), summarize and find clusters (heatmap), explore why outliers differ (heatmap rows highlighted for outlier sites)
- **What it shows for our data:** Which sites beat the trade-off, and whether they share a structural profile; whether high-yield/high-diversity sites form a distinct structural cluster
- **Persona it serves:** Elena (scientist): correlation structure, methodology; Sofia (conservationist): trade-off visibility; Hana (farmer): identify top-performer sites
- **Interaction if needed:** Linked highlighting — selecting a site in the scatterplot highlights it in the heatmap and vice versa; brushing yield/diversity range filters visible sites
- **Page reference:** p.146–161

---

### Idea: Parallel Coordinates for Multi-Variable Site Profiling (inspired by p.163–166)
- **Basic visuals combined:** Parallel coordinates (main) + Scatterplot (linked detail for two selected axes)
- **What the combination adds:** Parallel coordinates shows all management/structure variables simultaneously across all 60 sites. The linked scatterplot then provides accurate position-based comparison for any selected pair of axes. This answers: "Which combination of management variables consistently appears in high-yield sites?" — impossible to answer by comparing individual bar charts
- **Data manipulation applied:** Normalize all axes to 0–1 scale per variable; sort sites by mean yield for initial axis ordering; compute correlation between all axis pairs to suggest optimal axis ordering (most correlated neighboring axes)
- **Marks:** Polylines (one per site, connecting all axes); point marks in linked scatterplot
- **Channels:** Vertical position on each axis (normalized variable value); horizontal position (which variable); color hue (yield quartile — 4 colors from low to high); opacity (reduce to ~40% for non-selected sites on hover)
- **User task supported:** Overview of all attributes; find ranges; outlier detection; select subsets by brushing axis ranges
- **What it shows for our data:** Whether high-yield sites share a similar management profile visible as a "bundle" of parallel lines; whether low-diversity sites are outliers on specific structure variables
- **Persona it serves:** Elena (scientist): correlation structure, range exploration, dataset overview; Hana (farmer): profiling top-performing sites
- **Interaction if needed:** Interactive axis reordering (drag axes); brushing on individual axes to filter sites; clicking a site to highlight its polyline and cross-link to scatterplot; color by different attributes (yield, diversity, cluster)
- **Page reference:** p.163–166

---

### Idea: Streamgraph of Species Composition Over Yield Rank (inspired by p.153–155)
- **Basic visuals combined:** Streamgraph + Bar chart (yield axis)
- **What the combination adds:** Sites sorted by ascending mean yield form the horizontal axis. The streamgraph shows how plant group composition (woody/herbaceous/bryophyte proportions) flows across the yield gradient — revealing whether specific groups systematically shrink as yield rises. The bar chart beneath provides the actual yield magnitudes. Neither alone shows: "Does the composition shift gradually or suddenly as yield increases?"
- **Data manipulation applied:** Sort 60 sites by mean yield (derived ranking); compute species group proportions per site as a percentage (normalized); use streamgraph layer ordering by "onset" of group dominance across the yield axis — semantically novel use of onset-ordering (designed for time, used here for yield rank)
- **Marks:** Area marks (species group streams); line marks (yield bar chart below)
- **Channels:** Stream height (species group proportion); horizontal position (site yield rank); color hue (plant group — woody/herbaceous/bryophyte/other); bar height (actual yield value)
- **User task supported:** Find trends in composition as yield changes; characterize distribution of species group contributions; identify yield thresholds where composition shifts
- **What it shows for our data:** Whether high-yield sites consistently show lower herbaceous/bryophyte proportions; whether the trade-off is gradual or abrupt; which plant groups drive the diversity-yield relationship
- **Persona it serves:** Sofia (conservationist): makes trade-off visible and persuasive (composition changes visible); Elena (scientist): correlation structure between composition and yield
- **Interaction if needed:** Hover to highlight one species group stream; click on a site in the x-axis to cross-link to a detail card; toggle between absolute species counts and proportions (streamgraph vs. bar chart mode)
- **Page reference:** p.153–155 (semantic novelty: onset-ordering principle applied to yield rank instead of time)

---

### Idea: Small Multiples of Site Scatterplots — Cluster × Year Faceting (inspired by p.133 small multiples reference, p.158–162)
- **Basic visuals combined:** Small multiples (grid of scatterplots, one per cluster) + Normalized stacked bar (cluster composition summary)
- **What the combination adds:** Each cluster (from shrub structure clustering) gets its own scatterplot panel showing yield × diversity for the sites in that cluster across all 3 years. Side-by-side panels allow direct visual comparison without relying on memory (per the "eyes beat memory" rule, p.131). The normalized stacked bar alongside shows what proportion of sites belong to each cluster, serving as a navigational overview. This answers: "Does the yield-diversity trade-off operate differently in different structural clusters?"
- **Data manipulation applied:** Cluster 60 sites by shrub structure variables (7 variables); facet by cluster; for each cluster compute year-over-year yield trajectories; normalize stacked bar shows cluster size proportions
- **Marks:** Point marks (sites, one per year per site per panel); area marks (stacked bar sub-components)
- **Channels:** V position = yield, H position = diversity within each panel; color hue = year (3 colors); panel position = cluster identity; bar length = cluster size proportion; shape = optional (distinguishing sites within cluster)
- **User task supported:** Compare yield-diversity trade-off patterns across structural clusters; identify which cluster types decouple yield from biodiversity loss
- **What it shows for our data:** Whether specific structural clusters consistently achieve better yield:diversity ratios; year-to-year stability within clusters
- **Persona it serves:** Elena (scientist): methodological rigor; variability across years and clusters; Hana (farmer): which management cluster type to aspire to
- **Interaction if needed:** Clicking a cluster panel zooms it full-screen for detail; hovering a point shows site name and full variable profile; toggling which year's data is highlighted
- **Page reference:** p.131 (eyes beat memory), p.133 (small multiples over animation), p.158–162 (matrix alignment)

---

### Idea: Linked Calendar + Yield Overview (inspired by p.126–128 linked 2D views)
- **Basic visuals combined:** Calendar/matrix view (sites × year organized spatially) + Overview bar chart (sorted by yield)
- **What the combination adds:** The calendar view arranges 60 sites as rows and 3 years as columns (small matrix), with each cell colored by yield value. The companion sorted bar chart ranks sites by mean yield. Linked color coding means that when the user identifies a yield cluster in the bar chart, those exact sites light up in the matrix — immediately showing whether high-yield sites are geographically/structurally clustered. Inspired directly by the van Wijk & van Selow example (p.126) — they used calendar for temporal context; here the "calendar" structure is site × year for agricultural context.
- **Data manipulation applied:** Compute mean yield across 3 years (derived); compute year-over-year yield change (derived); cluster sites by 3-year yield trajectory for color coding
- **Marks:** Area marks (matrix cells); line marks (bar chart)
- **Channels:** Cell color (yield value per site-year, sequential colormap); horizontal position (year); vertical position (site); bar height (mean yield); color hue in bar chart (yield trajectory cluster, same as matrix)
- **User task supported:** Summarize yield patterns across 60 sites × 3 years; identify consistent top performers vs. volatile ones; spot anomalous years for specific sites
- **What it shows for our data:** Whether high-yield sites are consistently high across all 3 years (stable performers) or show year-to-year variation; which sites had one exceptional year vs. sustained performance
- **Persona it serves:** Hana (farmer): compare sites, spot top performers across years; Elena (scientist): year-over-year variability and consistency
- **Interaction if needed:** Brush to select a yield range in the bar chart, highlighting corresponding matrix cells; hover on a matrix cell to show full variable profile; sort matrix rows by different derived attributes (mean yield, yield variance, diversity)
- **Page reference:** p.126–128 (linked 2D views with calendar; shared color coding)

---

### Idea: Species Presence × Average Yield Scatter with Annotation Layer (inspired by p.146–148 scatterplots)
- **Basic visuals combined:** Scatterplot (species × yield) + Density layer + Bar chart (site count)
- **What the combination adds:** The dataset provides, for each of 407 species, the number of sites where it occurs and the average yield of those sites. A scatterplot of these two variables (site count × average yield of co-occurring sites) answers: "Which species are diagnostic indicators of high-yield AND common enough to be useful indicators?" A density overlay shows where the species cluster. The companion bar chart shows the distribution of site counts to contextualize rare vs. common species.
- **Data manipulation applied:** Derive "yield-association score" = average yield of sites where species occurs (already in dataset); derive rarity = number of sites; compute density of points for overlay; log-transform site count axis to spread rare species; color code by plant group (woody/herbaceous/bryophyte)
- **Marks:** Point marks (one per species); density contour marks (overlay); line marks (companion bar)
- **Channels:** H position = average yield of co-occurring sites; V position = number of co-occurring sites (log scale); color hue = plant group; size = optional (no clear mapping needed — keep simple); density contour = visual channel for cluster density
- **User task supported:** Find species that are both common and associated with high yield (top-right quadrant); identify plant groups that disproportionately associate with high yield; outlier species
- **What it shows for our data:** Which specific species could serve as ecological indicators of productive agroforests; whether woody vs. herbaceous species tend to associate with higher or lower yield sites
- **Persona it serves:** Sofia (conservationist): identifies which species are "good news" indicators for both yield and biodiversity; Elena (scientist): correlation structure, species × yield associations
- **Interaction if needed:** Hover for species name and full profile; brush to select species in a yield-association range; toggle between plant groups; lasso selection of quadrant
- **Page reference:** p.146–148 (scatterplot effectiveness for correlation and outlier finding)

---

### Idea: Radial Site Profile — Yield + Diversity + Structure in Polar (inspired by p.166–170)
- **Basic visuals combined:** Polar area chart (per-site radial profile) arranged as small multiples + Cluster color coding from SPLOM
- **What the combination adds:** Each site gets a polar area chart with 5–7 axes (yield, total diversity, woody richness, herbaceous richness, structure index, density, dominance). Sites are arranged in a grid sorted by cluster. This answers: "What does a 'complete' high-performing site look like compared to a specialist or low performer?" — a profile question that single-variable charts cannot answer. The polar form is justified here because the variables have no natural ordering and the "completeness" metaphor maps to filling the circle.
- **Data manipulation applied:** Normalize all variables to 0–1 scale; assign cluster labels; arrange grid by cluster; within cluster, sort by mean yield
- **Marks:** Area marks (wedges in each polar chart = one variable each)
- **Channels:** Length from center (normalized variable value); angle (which variable — consistent across all charts); color hue (cluster identity, consistent across grid); area (not used for comparison — only within a single site's profile)
- **User task supported:** Compare profiles across sites and clusters; identify which structural dimensions distinguish clusters
- **What it shows for our data:** Whether high-yield sites have uniformly large profiles or are specialists; whether conservation-valuable sites (high diversity) tend to have deflated yield wedges
- **Persona it serves:** Hana (farmer): visual "score card" for each site; Sofia (conservationist): trade-off visible in profile shape; Elena (scientist): multi-variable structure per cluster
- **Interaction if needed:** Click on individual polar chart to expand; select a cluster to highlight all its sites in the grid; toggle which variables to show as axes
- **Page reference:** p.168–170 (polar area charts; length channel more accurate than angle in radial form), p.133 (small multiples for side-by-side comparison)

---

### Idea: Dense Overview of Species Composition Matrix (inspired by p.172–174)
- **Basic visuals combined:** Dense layout (sites × species presence/absence matrix) + Bar chart sorted marginals
- **What the combination adds:** The 60×407 species × site presence/absence matrix is visualized as a dense pixel matrix — one dot per cell. Sites are sorted horizontally by yield (derived rank); species are sorted vertically by frequency of occurrence. Color encodes whether the species occurs (present/absent) AND, for present cells, the site's yield (sequential color from low to high yield). This answers: "Which species systematically appear only at high-yield sites, and which appear across all yield levels?" — a question requiring a simultaneous view of all 407 species.
- **Data manipulation applied:** Sort sites by mean yield (derived ranking); sort species by frequency of occurrence across sites; compute per-species yield-association score for color intensity of present cells
- **Marks:** Point marks (1 pixel per cell = 60 × 407 cells)
- **Channels:** H position = site (sorted by yield); V position = species (sorted by frequency); color hue (present = blue–yellow spectrum representing site yield; absent = white/gray)
- **User task supported:** Identify patterns of species co-occurrence with high/low yield; find rare species associated with specific yield ranges; provide complete overview of the 407-species × 60-site matrix
- **What it shows for our data:** Whether the species × site matrix shows a nested structure (high-yield sites are subsets of low-yield site species), or a replacement structure (high-yield sites have completely different species); visual signature of the biodiversity–yield trade-off at the species level
- **Persona it serves:** Elena (scientist): complete dataset structure view; Sofia (conservationist): which species are at risk when moving to higher-yield sites
- **Interaction if needed:** Hover over row/column to highlight; linked bar charts showing species richness per site and site count per species (marginals); click species row to see its yield distribution across sites
- **Page reference:** p.172–174 (dense layouts; position and color are the only available channels at pixel scale)
