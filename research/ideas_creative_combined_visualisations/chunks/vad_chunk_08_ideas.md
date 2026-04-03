# [agent_23] Visualization Analysis and Design — pages 351-400

## Creative Combined Visualization Ideas for the Ethiopian Coffee Dataset

Dataset reminder: 60 sites, coffee yield (3-year mean), species richness (woody/herbaceous/bryophytes/total), species composition (407 species), shrub structure index (7 variables + cluster), management variables (density, dominance), per-species site count + average yield. Core tension: higher yield tends to lower biodiversity.

---

### Idea: Yield-Relevance Spiral — Sites as Dense Pixels Ranked by Yield (inspired by p. 347–350)

- **Basic visuals combined:** VisDB-style dense pixel/area mark display + spiral spatial ordering + small-multiple views per variable group
- **What the combination adds:** Turning the 60 sites into a spatially arranged set of colored marks, ordered by yield in a spiral from center outward, immediately shows which sites are high-yield vs. low-yield without requiring bar charts. A second spiral can show species richness, making the trade-off instantly visible as color divergence between the two spirals.
- **Data manipulation applied:** Derive a per-site relevance score for each variable group (yield percentile rank, richness percentile rank, structure index score). Normalize across all 60 sites. Arrange sites in rank order, spiraling outward from the median.
- **Marks:** Square area marks (one per site × one per variable group view)
- **Channels:** Color (multi-hue sequential: dark red → purple → cyan → yellow for yield percentile); spatial position in spiral = yield rank; size uniform
- **User task supported:** Identify top/bottom performing sites; see how richness co-varies with yield rank at a glance; characterize distributions
- **What it shows for our data:** The "biodiversity penalty" of high yield: as the spiral moves outward (higher yield), the richness color in the parallel spiral cools down (lower richness), making the core tension a visible color gradient divergence.
- **Persona it serves:** Hana (compare sites by yield, spot top performers); Elena (distribution characterization across all 60 sites)
- **Interaction if needed:** Hover on any site mark to show a popup with exact values; click to highlight the site across all small-multiple spirals simultaneously (linked highlighting)
- **Page reference:** p. 347–350

---

### Idea: Scagnostics-Inspired "Relationship Fingerprint" — Which Variables Tell the Same Story? (inspired by p. 342–345)

- **Basic visuals combined:** Scagnostics shape measures applied to all pairwise combinations of continuous site-level variables → shown in a compact SPLOM-of-SPLOMs; clicking any cell opens the full scatterplot with sites labeled
- **What the combination adds:** The 60-site dataset has ~15 continuous variables (yield, total richness, woody richness, herbaceous richness, bryophyte richness, structure index, density, dominance, 7 shrub structure variables). That is 105 scatterplots. The standard approach is to try to read all of them. Scagnostics computes monotonic/outlying/clumpy/stringy scores for each pair and shows them as a meta-display, directing attention to the most interesting relationships automatically.
- **Data manipulation applied:** Compute 9 scagnostics measures for each of the 105 pairwise combinations of site-level variables. Display in a 9×9 scagnostics SPLOM (each axis = one scagnostics measure, each point = one variable pair). Color code points by variable category (yield vs. richness vs. management). Clicking a point opens the original scatterplot.
- **Marks:** Points (in scagnostics SPLOM, each = one variable pair); point marks in detail scatterplot (each = one site)
- **Channels:** Position (scagnostics measure values on X/Y); color hue (variable category — yield, richness, structure, management); size (can encode one additional measure like outlying score)
- **User task supported:** Identify which variable pairs have strong monotonic, clustered, or outlier relationships; guide systematic exploration of correlations; discover which variables are collinear and which are independent
- **What it shows for our data:** Reveals whether yield-richness is truly the dominant monotonic pattern, or whether shrub structure variables show stronger/weaker relationships; identifies potential confounders
- **Persona it serves:** Elena (correlation structure, methodological rigor, discovering dataset structure)
- **Interaction if needed:** Click any point in the scagnostics SPLOM to open the full scatterplot; linked highlighting to see which variable pair is selected across all views
- **Page reference:** p. 342–345

---

### Idea: Biodiversity Trade-Off PivotGraph — Site Groups as Aggregate Nodes (inspired by p. 355–358)

- **Basic visuals combined:** PivotGraph roll-up aggregation applied to the site×species network + size and color encoding of aggregate group properties
- **What the combination adds:** Instead of showing all 60 sites as individual nodes, roll up sites by two categorical attributes simultaneously (e.g., yield tertile × cluster assignment from shrub structure). The resulting aggregate nodes show how many sites share each combination, and aggregate links between groups show how many species are shared between site groups. This transforms a 60-node × 407-species bipartite network into a compact ~9-node (3 yield groups × 3 clusters) summary.
- **Data manipulation applied:** Derive yield tertile (low/medium/high) per site. Use existing cluster assignments (from shrub structure index). Compute species co-occurrence between groups as aggregate link weights. Derive average yield and average total species richness per aggregate group.
- **Marks:** Aggregate nodes (sized by number of sites in group); curved links (width = species overlap between groups); optional color on nodes
- **Channels:** Node size = number of sites; link width = shared species count; node color = average yield (diverging: blue=low, red=high); node position = 3×3 grid (yield tertile × cluster)
- **User task supported:** Cross-attribute comparison — do high-yield clusters share fewer species with low-yield clusters? Which cluster-yield combinations exist? Are some combinations empty?
- **What it shows for our data:** Shows whether yield level and structural cluster are independent or correlated, and whether species assemblages differ systematically across these groups
- **Persona it serves:** Sofia (trade-off visible and persuasive; composition changes); Elena (dataset structure, methodology)
- **Interaction if needed:** Click aggregate node to see the constituent sites; animated transition when changing the roll-up attributes (e.g., swap yield tertile for richness tertile)
- **Page reference:** p. 355–358

---

### Idea: Site Explorer with Guaranteed Visibility — Species Importance Never Hidden (inspired by p. 356–358)

- **Basic visuals combined:** Stretch and squish navigation (rubber sheet) + guaranteed visibility of rare/keystone species + site ordering by yield
- **What the combination adds:** Display all 60 sites as a horizontal array, ordered by yield. Each site column contains a compressed representation of its 407-species presence/absence vector. When the user stretches a site column (focus), all species become readable. Guaranteed visibility ensures that species marked as "rare" (occurring in ≤3 sites) always show a visible mark even in compressed columns — analogous to TreeJuxtaposer's high-importance marks.
- **Data manipulation applied:** Derive "species importance" = inverse of site frequency (rarer species get higher importance values). Derive a binary presence/absence matrix (60 sites × 407 species). Order sites by yield (left=low, right=high). Apply sub-pixel aggregation that always renders marks for high-importance (rare) species as visible colored pixels.
- **Marks:** Colored pixels/cells per species per site; stretched detail columns show full species labels
- **Channels:** Spatial position (horizontal = yield rank, vertical = species category); color (presence=colored, absence=gray; rare species in a distinct hue like orange); size (varies by stretch factor)
- **User task supported:** Identify where rare/keystone species occur across the yield spectrum; compare site compositions; see whether rare species cluster at low- or high-yield sites
- **What it shows for our data:** Whether biodiversity loss at high-yield sites is uniform (all species disappear proportionally) or disproportionately affects rare species (the most critical conservation concern)
- **Persona it serves:** Sofia (hotspot identification; trade-off visible); Hana (species associations per site)
- **Interaction if needed:** Click/drag a site column to stretch it; slider to adjust what counts as "rare" (importance threshold); hover on a species mark for the species name and its average yield context
- **Page reference:** p. 356–358

---

### Idea: Hierarchical Clustering Explorer for Species × Site — Systematic Cluster Comparison (inspired by p. 351–354)

- **Basic visuals combined:** HCE-style cluster heatmap (overview + detail) applied to the species×site presence/absence matrix + rank-by-feature idiom for site variables + linked scatterplot for yield vs. richness
- **What the combination adds:** The HCE idiom scales precisely to the problem: 407 species × 60 sites is analogous to HCE's genes × conditions. The overview heatmap shows all 60 sites in a single aggregated row set, ordered by species similarity. A dendrogram reveals site clusters. Dragging the Minimum Similarity slider partitions sites into distinct composition groups. A linked scatterplot immediately shows where each composition cluster falls on the yield-richness trade-off curve.
- **Data manipulation applied:** Compute hierarchical clustering of 60 sites based on species composition (Bray-Curtis or Jaccard distance). Reorder species by frequency across sites. Derive cluster assignments at multiple dendrogram cut levels. Compute within-cluster average yield and average richness for the linked scatterplot.
- **Marks:** Heatmap cells (presence/absence); dendrogram line marks; scatterplot points (one per site, colored by composition cluster)
- **Channels:** Color in heatmap (presence=dark, absence=light; diverging for cluster membership); vertical position = site (ordered by clustering); horizontal position = species (ordered by frequency or clustering); scatterplot: X=yield, Y=richness, color=cluster identity
- **User task supported:** Find site clusters with similar composition; identify which species define each cluster; verify whether composition clusters correspond to yield/richness groupings
- **What it shows for our data:** Whether sites group by composition in ways that align with yield levels — if yes, species assemblages predict yield performance
- **Persona it serves:** Elena (cluster structure, methodological rigor); Sofia (composition changes; hotspot identification)
- **Interaction if needed:** Minimum Similarity slider to adjust cluster granularity; click a cluster in the heatmap to highlight those sites in the scatterplot; rank-by-feature view for sorting site variables
- **Page reference:** p. 351–354

---

### Idea: Focus+Context Lens for Species Richness Maps — Neighborhood Highlighting Without Distortion (inspired by p. 361–362)

- **Basic visuals combined:** Neighborhood highlighting lens (opacity-based, no spatial distortion) applied to a site-similarity network + yield color coding
- **What the combination adds:** Draw 60 sites as nodes in a 2D layout where spatial position is determined by species composition similarity (MDS or UMAP embedding). Color nodes by yield level. A hoverable neighborhood lens highlights all sites within a chosen species similarity threshold of the selected site, fading out all others. Unlike fisheye, this doesn't distort positions — it simply reveals the local neighborhood structure through opacity, making it easy to trace which sites are compositionally similar and whether they share yield properties.
- **Data manipulation applied:** Compute pairwise Bray-Curtis dissimilarity between all 60 sites on species composition. Embed in 2D using MDS or UMAP. Derive "similarity neighborhood" for each site (e.g., top 10 most similar sites). Yield is a color attribute on nodes.
- **Marks:** Circular nodes (one per site); connection lines (for similar pairs within threshold); opacity overlay for dimmed non-neighborhood items
- **Channels:** Spatial position = species composition similarity (from MDS); color hue = yield level (diverging: blue=low yield, red=high yield); opacity = in/out of current lens neighborhood; size = total species richness
- **User task supported:** Path tracing in similarity space — find sites compositionally similar to high-yield sites but with different yield; identify outlier sites; verify whether similar compositions lead to similar yields
- **What it shows for our data:** Whether yield correlates with composition-space position (a cluster of high-yield sites in MDS space) or whether yield varies independently of composition
- **Persona it serves:** Hana (compare sites, spot top performers, species associations); Sofia (biodiversity hotspots, composition changes)
- **Interaction if needed:** Hover any site node to trigger neighborhood highlighting; slider for similarity threshold; click to pin a comparison site; toggle link overlay on/off
- **Page reference:** p. 361–362

---

### Idea: Semantic Zoom across Three Scales — Site → Species Group → Species (inspired by p. 363–366)

- **Basic visuals combined:** Constellation-inspired semantic zooming with three discrete viewing levels applied to a site × species composition treemap/sunburst
- **What the combination adds:** At the highest zoom level, 60 sites are shown as proportional blocks sized by total richness and colored by yield. Zooming into a site reveals a breakdown of richness by plant group (woody/herbaceous/bryophyte). Zooming further reveals the individual species present. At each level, the space allocation changes (semantic zooming): more space goes to the currently zoomed item; sibling sites compress gracefully. This is a "site explorer" where all three levels of biodiversity data are accessible without switching views.
- **Data manipulation applied:** Aggregate species into plant groups. Compute per-site richness totals and group breakdowns. Use yield as a sorting/coloring criterion. Derive a Constellation-like curvilinear grid: sites ordered left-to-right by yield; groups ordered within each site by richness contribution.
- **Marks:** Rectangular containment blocks (site → group → species); label text at each level; connection lines between same species appearing in multiple sites (in zoomed species view)
- **Channels:** Block area = richness count; color = yield level (site level) or group type (species level, categorical hue); horizontal position = yield rank; vertical position = richness proportion
- **User task supported:** Drill into specific sites and their composition; compare composition structure across yield levels; identify which plant groups drive richness differences
- **What it shows for our data:** Whether the yield-richness trade-off plays out differently across plant groups — e.g., does high yield mainly suppress woody diversity, or does it equally reduce all groups?
- **Persona it serves:** Hana (multiple variables simultaneously; top performers); Sofia (composition changes; persuasive trade-off visualization); Elena (detailed composition structure)
- **Interaction if needed:** Click any site block to zoom in (animated transition); double-click to return to overview; slider to sort sites by different criteria (yield / total richness / woody richness)
- **Page reference:** p. 363–366
