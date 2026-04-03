# [agent_22] Visualization Analysis and Design — pages 301-350

## Creative Combined Visualization Ideas
### Dataset: 60 Ethiopian coffee agroforest sites

---

### Idea: Trellis Yield-Biodiversity Comparison Grid (inspired by p.307-309)

- **Basic visuals combined:** Trellis/small-multiple dot charts + color encoding of a second attribute within each panel
- **What the combination adds:** The Trellis pattern from p.307-309 (Becker et al.) reveals outliers against general trends using main-effects ordering. Adding color for cluster membership (from shrub structure clusters) within each panel answers: "Does cluster membership explain why some sites outperform expectations?" — a question neither a single dot chart nor a color scatter alone could answer
- **Data manipulation applied:** Derive median yield per management cluster; use main-effects ordering to sort both rows (by cluster median) and within-panel items (by site yield); compute residual (site yield minus cluster median) as a derived attribute
- **Marks:** Dot marks (one per site per panel)
- **Channels:** Horizontal position (yield value), vertical position (site identity within panel), panel row (management cluster), color hue (presence/absence of dominant tree species — categorical), size (species richness total, ordered)
- **User task supported:** Find outliers relative to general cluster trends; compare yields within and between clusters; identify high-yield sites within each cluster
- **What it shows for our data:** Reveals whether the yield hierarchy between clusters is consistent or whether some sites "punch above their weight"; the main-effects ordered layout makes Morris-style anomalies (anomalous sites) immediately visible
- **Persona it serves:** Elena (scientist) — correlation structure and outlier detection; Hana (farmer) — top performer identification within comparable sites
- **Interaction if needed:** Tooltip showing site name + species richness + yield when hovering dot; click to expand a single panel to full view
- **Page reference:** p.307-309

---

### Idea: Yield–Species Trade-off Superimposed Layer Map (inspired by p.313-317)

- **Basic visuals combined:** Scatterplot (yield vs. total species richness) with superimposed foreground layer highlighting a selected species group; background layer shows all 60 sites
- **What the combination adds:** A single scatterplot shows the core yield–biodiversity trade-off but cannot simultaneously highlight which specific plant groups drive the pattern. The superimposed layer (foreground: selected species group highlighted in saturated color; background: all sites in low-saturation gray) lets the user interactively explore which species groups are most associated with high-yield or low-yield sites, without losing the overall trade-off context — a question the scatterplot alone cannot answer
- **Data manipulation applied:** Compute presence/absence for each species group per site; compute species-group-specific richness; derive Pearson correlation between each group's richness and yield for ranking groups by association strength
- **Marks:** Point marks (one per site)
- **Channels:** Horizontal position (coffee yield), vertical position (total species richness), color saturation (foreground: high saturation for selected species group; background: low saturation), color hue (foreground layer: one hue per selected group), size (site-level species richness within selected group)
- **User task supported:** Identify which species groups are associated with high-yield or biodiversity-rich sites; find sites that are both high-yield and high-biodiversity for the selected group
- **What it shows for our data:** The core tension between yield and biodiversity becomes actionable: "Given that yield and total biodiversity trade off, is there a specific plant group whose presence is compatible with high yield?" — this is the conservationist's question made visual
- **Persona it serves:** Sofia (conservationist) — trade-off visibility + species composition perspective; Elena (scientist) — correlation structure per plant group
- **Interaction if needed:** Dropdown or radio buttons to select plant group (woody/herbaceous/bryophyte); animated transition between group selections highlights which sites move up/down in the foreground layer
- **Page reference:** p.313-317

---

### Idea: Dynamic Query Site Finder — FilmFinder Pattern for Coffee Sites (inspired by p.326-328)

- **Basic visuals combined:** Dynamic query scatterplot (yield vs. species richness) + multi-attribute slider panel for filtering + popup detail view per site
- **What the combination adds:** FilmFinder's (p.326-328) key insight: browsing by attribute ranges with immediate visual feedback is far better than typed queries when exploring unknown datasets. Applying this to the coffee dataset answers: "Which sites are high-yield AND have reasonable biodiversity AND have a specific shrub cluster?" — Hana's primary question, answered interactively without needing to know values in advance. Semantic novelty note: using FilmFinder's movie-browser pattern in an agricultural ecology context is novel (+2)
- **Data manipulation applied:** None special at design time — the filtering is done dynamically per user interaction; pre-compute scented widget summaries (histogram of yield distribution, histogram of species richness) for each filter widget
- **Marks:** Point marks (one per site); adaptive: auto-enlarge and label when few sites remain
- **Channels:** Horizontal position (coffee yield), vertical position (total species richness), color hue (shrub structure cluster assignment), size (adaptive: grows when fewer than ~10 sites visible)
- **User task supported:** Find sites matching multiple criteria simultaneously; identify top performers within filtered subgroup; browse unknown dataset without prior knowledge
- **What it shows for our data:** Allows Hana to ask: "Show me sites with yield above X, species richness above Y, in cluster Z" and immediately see which sites qualify — with their names auto-labeling when few remain
- **Persona it serves:** Hana (farmer) — compare sites, spot top performers, filter by multiple variables; Elena (scientist) — exploratory overview of multivariate structure
- **Interaction if needed:** Dual sliders for yield range; dual sliders for species richness range; checkbox buttons for cluster group selection; alpha sliders for management variable ranges; popup detail on click (species composition breakdown, year-by-year yield)
- **Page reference:** p.326-328

---

### Idea: Partitioned Boxplot Dashboard — Yield Distribution by Cluster and Plant Group (inspired by p.304-307, p.333-335)

- **Basic visuals combined:** Boxplot chart (yield distribution per group) + small-multiple layout partitioned by management cluster + color channel for biodiversity level
- **What the combination adds:** Partitioning (p.304-307) encodes group association via spatial proximity. Boxplots (p.333-335) show the full distributional shape per group. Combining them: one column per management cluster, one boxplot row per plant group richness quantile. This answers: "Does biodiversity level change the yield distribution shape within each management cluster?" — neither boxplots alone nor a scatterplot can answer this cleanly
- **Data manipulation applied:** Bin total species richness into 3 quantiles (low/medium/high biodiversity) as derived categorical attribute; compute 5-number boxplot summaries per (cluster × biodiversity quantile) cell; use main-effects ordering for clusters by median yield
- **Marks:** Line marks (whiskers), rectangle mark (IQR box), horizontal line (median), point marks (outlier sites with labels)
- **Channels:** Vertical position (yield value), horizontal position (biodiversity quantile within panel), panel column (management cluster, ordered by median yield), color saturation (global median reference line in background)
- **User task supported:** Characterize yield distribution; compare spread and median across clusters; find outliers; check whether high biodiversity always means lower yield or if the pattern varies by cluster
- **What it shows for our data:** Directly addresses the "higher yield = lower biodiversity" core tension — shows whether this holds uniformly across all management clusters or whether some clusters break the pattern
- **Persona it serves:** Elena (scientist) — distribution characterization and variability; Sofia (conservationist) — trade-off structure across management types
- **Interaction if needed:** Toggle between plant groups (woody/herbaceous/bryophyte) for the biodiversity binning; hover tooltip on outlier dots showing site name + species composition
- **Page reference:** p.304-307, p.333-335

---

### Idea: Recursive Subdivision — Site × Species Matrix as HiVE-Style Heatmap (inspired by p.310-313)

- **Basic visuals combined:** Recursive spatial partition (HiVE-style) applied to species-by-site presence/absence matrix, with yield encoded as color at the site level and species group as the first partitioning attribute
- **What the combination adds:** The species composition matrix (407 species × 60 sites) is too large to read directly. Applying HiVE's recursive subdivision approach (p.310-313): first partition by plant group (woody/herbaceous/bryophyte), then by presence/absence frequency class, color-encode yield of sites where each species occurs. This answers: "Which species groups most reliably co-occur with high-yield sites?" — which the raw matrix cannot show without aggregation
- **Data manipulation applied:** Derive: (1) species frequency class (occurs in 1-10, 11-30, 31-60 sites); (2) per-species average yield of sites where it occurs (already in the dataset); (3) per-plant-group yield association summary; order by average yield of co-occurring sites for within-group ordering
- **Marks:** Area marks (rectangles, color-coded)
- **Channels:** Color (sequential colormap: average yield of co-occurring sites — low=blue, high=yellow), spatial containment (plant group → frequency class → individual species), region size (proportional to number of sites where species occurs, optionally)
- **User task supported:** Identify species strongly associated with high-yield sites; compare yield associations across plant groups; find rare vs. common species with high yield association
- **What it shows for our data:** Transforms the 407-species composition matrix into a readable yield-association summary — Sofia's key question: "Which species signal conservation value AND are compatible with coffee yield?"
- **Persona it serves:** Sofia (conservationist) — species composition and yield linkage; Elena (scientist) — structural overview of high-dimensional species matrix
- **Interaction if needed:** Click on species group partition to expand into individual species; hover tooltip showing species name, site count, average yield of co-occurring sites; toggle between size-proportional and equal-size region layouts
- **Page reference:** p.310-313

---

### Idea: Hierarchical Parallel Coordinates for Multi-Variable Site Profiling (inspired by p.336-337)

- **Basic visuals combined:** Hierarchical parallel coordinates (p.336-337) + cluster-proximity coloring + interactive LOD slider
- **What the combination adds:** With 60 sites and 7 shrub structure variables + yield + species richness + management variables, standard parallel coordinates show all individual lines. The hierarchical version clusters similar sites and shows them as bands (mean ± range). This answers: "What is the typical multivariate profile of high-yield vs. low-yield clusters?" without the hairball of 60 overlapping lines. The combination of cluster coloring + LOD also reveals whether clusters have tight or loose internal variability
- **Data manipulation applied:** Compute hierarchical clustering on shrub structure variables (7 variables); derive per-cluster mean, min, max for each variable; order parallel axes by discriminative power (variables that most separate clusters); add yield and species richness as last two axes for interpretive anchoring
- **Marks:** Band marks (variable width per cluster), line marks (individual sites at finest LOD)
- **Channels:** Vertical position at each axis (variable value), width of band (min-max range within cluster at that variable), opacity (cluster population size), color hue (cluster identity / proximity in hierarchy), horizontal position (variable identity)
- **User task supported:** Compare multivariate profiles of clusters; identify which variables distinguish high-yield clusters; find whether biodiversity is consistently traded off or whether a niche exists
- **What it shows for our data:** At highest aggregation (1-2 clusters), shows the overall bivariate relationship between structure variables and yield. Zooming to finer clusters reveals within-cluster variability and niche clusters that may combine reasonable yield with higher biodiversity
- **Persona it serves:** Elena (scientist) — correlation structure and cluster profiling; Hana (farmer) — identifying the multivariate profile of top-performing clusters
- **Interaction if needed:** LOD slider (cluster granularity); axis reordering by drag; filter to show only clusters above a yield threshold
- **Page reference:** p.336-337

---

### Idea: Focus+Context Biodiversity Hotspot Navigator (inspired by p.348-350)

- **Basic visuals combined:** Overview scatterplot (yield vs. total species richness, all 60 sites) as context layer + focus detail panel (species composition breakdown + management variables) for selected site(s), using DOI function logic
- **What the combination adds:** The standard overview scatterplot positions all 60 sites but cannot simultaneously show the species composition detail for any given site. Focus+context embedding (p.348-350) lets the user keep the yield–biodiversity trade-off pattern visible as permanent context while drilling into individual site profiles. The DOI function (DOI = I(x) − D(x, y)) can be adapted so nearby sites in yield-biodiversity space get aggregated into a summary, while the clicked focus site(s) show full detail
- **Data manipulation applied:** Compute Euclidean distance in yield × total-species-richness space to define neighborhood; derive DOI scores for all sites relative to focus site; aggregate context sites within radius into a summary profile (mean yield, mean richness, modal cluster); show focus site in full detail (all 407 species + 7 shrub variables + 3-year yield)
- **Marks:** Point marks (context sites, low saturation), enlarged point marks (focus sites, high saturation), bar marks (species richness breakdown in detail panel), line marks (3-year yield trend in detail panel)
- **Channels:** Position (yield × richness in overview), saturation (focus vs. context), size (DOI score as adaptive size), color hue (cluster membership)
- **User task supported:** Identify individual sites of interest; maintain overall trade-off pattern as context during drill-down; compare focus site to its nearest neighbors in multivariate space
- **What it shows for our data:** Sofia can identify biodiversity hotspots (high richness) and see their yield context; Hana can identify top-yield sites and see their species profile to understand what conditions drive performance
- **Persona it serves:** Sofia (conservationist) — biodiversity hotspot identification with yield context; Hana (farmer) — site-specific detail with trade-off context maintained
- **Interaction if needed:** Click site to focus; hold Shift to add to multi-focus set; hover to preview; slider to control DOI distance radius; animated transition when focus changes
- **Page reference:** p.348-350

---

### Idea: Scented Widget Filter Panel for Site Explorer (inspired by p.328)

- **Basic visuals combined:** Scented filter sliders (p.328) + site scatterplot + automatic site-label pop-up when few items remain (FilmFinder pattern, p.327)
- **What the combination adds:** Standard sliders for filtering coffee sites by yield, species richness, management variables, or cluster show no information about the data distribution. Scented widgets embed a tiny histogram of the attribute's distribution inside the slider track, so the user sees where the data is concentrated before sliding. Combined with auto-labeling of remaining sites, this creates a high-information-density browser that is simultaneously guiding (the scent) and revealing (the label). The combination answers: "Where should I set the threshold to include the interesting sites?" without needing prior knowledge. Semantic novelty: scented widgets in agricultural ecology context (+2)
- **Data manipulation applied:** Compute histogram of each attribute for slider background; compute auto-label trigger threshold (e.g., fewer than 8 sites visible → show site names)
- **Marks:** Tiny bar marks within slider tracks (attribute histogram), point marks in scatterplot, text labels on auto-triggered sites
- **Channels:** Bar height in slider (count per bin = data density cue), position in scatterplot (yield × richness), color (cluster), auto-size (adaptive mark size)
- **User task supported:** Browse sites by multiple attributes; find sites meeting complex criteria; get visual guidance on where to set thresholds
- **What it shows for our data:** Makes the 60-site dataset explorable without prior knowledge of value ranges — supports Hana's comparison and top-performer identification tasks without requiring her to know what yield values are "good"
- **Persona it serves:** Hana (farmer) — guided multi-variable filtering; general audience for interactive poster/report
- **Interaction if needed:** Dual-range sliders with embedded histograms for yield, species richness, structure index, density, dominance; checkbox for cluster; auto-label when fewer than 8 sites remain
- **Page reference:** p.328
