# [agent_20] Visualization Analysis and Design — pages 201-250

## Creative Combined Visualization Ideas

### Dataset context
60 Ethiopian coffee agroforest sites. Variables: coffee yield (3-year mean + annual), species richness (woody/herbaceous/bryophytes/total), species composition (407 species presence/absence), management variables (structure index, density, dominance), shrub structure (7 variables + cluster), species × yield link.

**Core tension:** Higher yield = lower plant biodiversity.

---

### Idea: Site Adjacency Matrix Ordered by Yield × Biodiversity (inspired by p. 208–212)

- **Basic visuals combined:** Adjacency matrix view (network) + color encoding of yield + row/column reordering by derived rank
- **What the combination adds:** Transforms species co-occurrence data (sites sharing species, or species co-occurring across sites) into a spatial relational view. Reordering by yield reveals whether high-yield sites form a visual cluster (diagonal block) vs. scatter randomly — answering "do sites with similar yields have similar species compositions?"
- **Data manipulation applied:** Derive a site×site similarity matrix from species composition (Jaccard or Bray-Curtis similarity). Reorder rows/columns by coffee yield rank. Optionally by species richness rank. Fill cells = similarity value encoded with sequential colormap (luminance/saturation).
- **Marks:** Area marks (cells in 2D matrix alignment).
- **Channels:** Spatial position (site × site matrix; rows/columns ordered by yield); luminance/saturation (species composition similarity value, sequential colormap); optional separate color stripe along axes for yield quintile (categorical hue).
- **User task supported:** Find clusters — do high-yield sites form a distinct composition cluster? Detect anomalies — are there high-yield sites with high biodiversity (resisting the tension)?
- **What it shows for our data:** If high-yield sites cluster in the top-left diagonal block, the yield–biodiversity trade-off is systematic and spatially structured. If not, the pattern is more complex.
- **Persona it serves:** Elena (scientist) — wants correlation structure and methodological rigor. Also Sofia (conservationist) — wants to see whether the biodiversity trade-off is universal or has exceptions.
- **Interaction if needed:** Reorder rows/columns interactively by different variables (yield, richness, dominance). Hover cells to see which two sites are compared. Filter to show only top-N or bottom-N yield sites.
- **Page reference:** p. 208–212

---

### Idea: Coffee Yield Choropleth + Species Richness Contour Overlay (inspired by p. 181, 183–184)

- **Basic visuals combined:** Choropleth map (area marks, yield as color) + isocontour overlay (derived contours from interpolated species richness surface)
- **What the combination adds:** The combination shows simultaneously WHERE yield is high/low (choropleth) AND how species richness gradients align or diverge from yield patterns. If isocontour lines of equal richness cut across choropleth regions, the trade-off is spatially explicit and visible as non-aligned patterns.
- **Data manipulation applied:** Interpolate species richness values across the 60 site coordinates to create a continuous 2D scalar field (kriging or IDW interpolation). Derive isocontour lines from this field at e.g. 5 richness levels. Apply yield as a sequential colormap for site polygons (or Voronoi cells if no polygons exist).
- **Marks:** Area marks (site regions/Voronoi cells, choropleth); line marks (isocontour lines of equal species richness).
- **Channels:** Color/saturation (yield, sequential colormap, choropleth); spatial position (geographic location of sites); implicit magnitude via contour line density (richness gradient steepness).
- **User task supported:** Locate — where are high-yield sites? Identify — do richness gradients align with yield boundaries or cut across them?
- **What it shows for our data:** Regions where contour lines are dense AND yield choropleth shows high values = steep richness decline near productive sites. Visual divergence between contour alignment and yield color = local exceptions to the global trade-off.
- **Persona it serves:** Sofia (conservationist) — spatial persuasion of the trade-off. Hana (farmer) — where to farm to preserve some richness.
- **Interaction if needed:** Toggle between different plant groups (woody/herbaceous/bryophytes) as the richness surface for isocontour derivation. Slider to select contour levels.
- **Page reference:** p. 181, 183–184

---

### Idea: Species Co-occurrence Network + Yield Node Sizing (inspired by p. 204–208)

- **Basic visuals combined:** Node–link diagram (force-directed) of species co-occurrence network + node size encoding yield of sites where each species occurs + color encoding plant group (categorical hue)
- **What the combination adds:** The force-directed network reveals which species naturally cluster together (co-occurrence communities). Sizing nodes by the average coffee yield at sites where each species occurs adds a direct yield-association layer. Species that appear in high-yield sites AND cluster together form high-yield-associated communities — a combined ecological + agronomic insight.
- **Data manipulation applied:** From species×site presence/absence matrix: build species co-occurrence network (link between species A and B = they co-occur in at least N sites). Compute per-species average yield (from species × yield data file). Size each species node by this average yield. Color by plant group (woody/herbaceous/bryophyte).
- **Marks:** Point marks (species nodes); connection marks (co-occurrence links).
- **Channels:** Spatial position (force-directed layout — cluster proximity indicates co-occurrence community); size (average coffee yield at sites where species occurs); color hue (plant group: woody/herbaceous/bryophyte — categorical); line width (optional: number of sites of co-occurrence).
- **User task supported:** Identify yield-associated species clusters. Find species communities that tend to be associated with high or low yield. Distinguish plant group composition of communities.
- **What it shows for our data:** If high-yield species (large nodes) cluster together, they form a community not randomly distributed. If they scatter across the network, yield association is independent of co-occurrence community.
- **Persona it serves:** Elena (scientist) — methodological, ecological community structure. Hana (farmer) — "which species can I encourage alongside coffee?"
- **Interaction if needed:** Filter to show only species above a threshold number of sites. Highlight nodes by plant group. Hover node to see species name, yield mean, site count. L < 4N rule (p. 206) applies — restrict to species with at least k co-occurrences to reduce link density.
- **Page reference:** p. 204–208
- **Note:** Force-directed nondeterminism (p. 205) is a risk; use fixed seed for reproducibility.

---

### Idea: Treemap of Species × Site Hierarchy Colored by Yield Quartile (inspired by p. 213–215)

- **Basic visuals combined:** Treemap (containment, hierarchical structure) + sequential colormap for yield + nested structure by plant group → species
- **What the combination adds:** A treemap of species nested within plant groups (woody → species, herbaceous → species, bryophytes → species) where each leaf node (species) is sized by its site count and colored by the mean yield of sites where it occurs. This directly reveals: which plant groups harbor the most yield-associated species? Are there specific groups (e.g., bryophytes) that are predominantly low-yield or high-yield associated?
- **Data manipulation applied:** Build tree: root → plant groups (woody/herbaceous/bryophyte) → species within each group. Leaf size = number of sites where species occurs. Leaf color = mean coffee yield at those sites (sequential colormap: low yield = light; high yield = dark). Derived from species × yield data file + species composition.
- **Marks:** Area marks (nested rectangles, rectilinear layout).
- **Channels:** Area/size (site count per species — quantitative); color luminance/saturation (mean coffee yield — sequential ordered colormap); spatial nesting level (plant group → species hierarchy); spatial position within level (layout algorithm, not meaningful).
- **User task supported:** Spot outliers — which species occur in many sites with high yield? Compare plant groups — do woody species have more high-yield association than herbaceous? Identify — which species are largest in area (most widely distributed)?
- **What it shows for our data:** If the treemap shows large dark-colored cells in the woody section and small pale cells in the bryophyte section, it suggests woody species are better tolerated in productive landscapes. Or vice versa, revealing bryophytes as sensitive biodiversity indicators.
- **Persona it serves:** Sofia (conservationist) — which species are trade-off victims? Hana (farmer) — which species are "compatible" with high yields? Elena (scientist) — quantitative structure across all 407 species at once.
- **Interaction if needed:** Zoom into individual plant group subtrees. Hover for species name, yield mean, site count. Toggle color to show species richness rank vs. yield rank. Filter to show only species present in >5 sites.
- **Page reference:** p. 213–215

---

### Idea: Shrub Cluster Node–Link + Management Variable Attribute Overlays (inspired by p. 202–208, 213–215)

- **Basic visuals combined:** Node–link diagram (tree or network) of site clusters (from shrub structure cluster assignments) + color/size encoding of management variables (density, dominance, structure index) + yield as an outer ring size
- **What the combination adds:** The cluster hierarchy from shrub structure divides sites into groups with similar coffee shrub architecture. Overlaying management variables on this cluster structure reveals whether cluster membership predicts management intensity. Adding yield as a node size shows whether clusters correspond to yield bands — answering "does shrub architecture cluster define a productivity-biodiversity type?"
- **Data manipulation applied:** Site clusters from shrub structure variables (already provided). Build cluster hierarchy (3–4 levels: all sites → cluster groups → individual sites as leaves). Node size = mean coffee yield of sites in cluster. Color = structure index (sequential colormap). Optional: radial node–link or BubbleTree layout for circular visual grouping of clusters.
- **Marks:** Point marks (site nodes and cluster nodes); connection marks (cluster hierarchy links).
- **Channels:** Spatial position (hierarchy depth in radial/vertical layout); size (mean yield per cluster or per site); color saturation/luminance (structure index — ordered); color hue (cluster identity — categorical, if multiple clusters shown simultaneously).
- **User task supported:** Compare — do high-structure-index clusters have lower yield? Identify — which cluster is the outlier (high yield + high structure index)?
- **What it shows for our data:** If cluster structure closely corresponds to yield bands, shrub architecture is a strong predictor of productivity. If not, management variables (density/dominance) explain the residual variance.
- **Persona it serves:** Elena (scientist) — cluster structure and management interaction. Hana (farmer) — "which type of shrub structure should I aim for?"
- **Interaction if needed:** Expand/collapse cluster nodes. Highlight one cluster at a time. Filter to sites above/below median yield. Toggle between different management variable encodings.
- **Page reference:** p. 202–208, 213–215

---

### Idea: Bivariate Colormap Scatter — Yield vs. Richness with Luminance × Hue (inspired by p. 219–225)

- **Basic visuals combined:** Scatterplot (position encodes yield × total species richness) + bivariate colormap on site marks (luminance = management intensity / structure index; hue = dominant plant group / cluster)
- **What the combination adds:** The scatterplot position already shows the core yield–richness trade-off. The bivariate color adds a third dimension: where along the trade-off curve does management intensity sit? If highly managed sites (high structure index, shown by high luminance) cluster in the high-yield / low-richness corner, management drives the trade-off. If they're scattered, management is not the mediating variable.
- **Data manipulation applied:** Normalize yield and total richness to [0,1] for scatterplot axes. Compute a management intensity score (derived from structure index + density + dominance). Encode management intensity with luminance (sequential). Encode dominant plant group (which group contributes most species at this site) with hue (categorical). Note: bivariate colormap is safe here because hue (categorical, few levels) and luminance (ordered, few levels) are being combined — one binary/few-level categorical + one ordered (p. 225 guidance).
- **Marks:** Point marks (sites); optional line marks connecting sites in the same management cluster.
- **Channels:** Horizontal spatial position (coffee yield); vertical spatial position (total species richness); luminance (management intensity — ordered); hue (dominant plant group — categorical).
- **User task supported:** Identify trade-off outliers — sites with both high yield and reasonable richness. Find — which management type clusters in which part of the trade-off curve? Compare — does dominant plant group vary systematically along the trade-off?
- **What it shows for our data:** If high-luminance (high management) sites cluster in top-right (high yield, low richness) of the scatterplot, management drives both outcomes. Outlier sites with low luminance but high yield suggest other explanatory factors.
- **Persona it serves:** Elena (scientist) — correlation structure. Sofia (conservationist) — which management practices are most damaging to biodiversity?
- **Interaction if needed:** Hover for site details. Brush and link with a parallel coordinates view. Filter by dominant plant group.
- **Page reference:** p. 219–225

---

### Idea: Color-Coded Node–Link Species Network with Hue = Plant Group, Luminance = Yield Association (inspired by p. 224, 204–208)

- **Basic visuals combined:** Node–link network of species co-occurrence + dual color encoding (hue for plant group identity, luminance for yield association magnitude)
- **What the combination adds:** The network shows community structure; the dual color encoding makes it possible to see whether a species is (a) a woody plant (hue), and (b) associated with high yields (bright/dark luminance). This is a semantic novelty — a standard network uses hue for categories but not luminance for an ordered attribute, creating a new question: "Are yield-associated species distributed across all plant groups or concentrated in one?"
- **Data manipulation applied:** Co-occurrence network (as above). Per-species derived attribute: mean yield of sites where present. Normalize to luminance scale. Hue from plant group membership (categorical, 3–4 levels: woody/herbaceous/bryophyte/other).
- **Marks:** Point marks (species nodes); connection marks (co-occurrence links).
- **Channels:** Spatial position (force-directed cluster proximity); hue (plant group — categorical identity); luminance (mean yield association — ordered magnitude); size (optional: number of occurrence sites).
- **User task supported:** Identify — which species combine high yield association with diverse plant group membership? Find community patterns where yield-associated species (bright nodes) cluster together despite belonging to different plant groups.
- **What it shows for our data:** If bright (high-yield-associated) nodes of multiple hues (different plant groups) cluster together, yield-tolerant species cut across plant group boundaries. If bright nodes concentrate in one hue only, that plant group has a systematically higher yield association.
- **Persona it serves:** Elena (scientist) — rigorous pattern analysis. Sofia (conservationist) — which plant groups are most affected by yield pressure?
- **Interaction if needed:** Filter by minimum co-occurrence count (L < 4N constraint). Hover for species name. Highlight one plant group at a time (opacity layering, inspired by p. 193 similarity-clustered streamlines).
- **Page reference:** p. 224, 204–208
- **Semantic novelty:** Using luminance (ordered magnitude) on network nodes, in addition to standard hue (categorical), is unusual. Standard network visualization uses only categorical color or size. Luminance encodes a quantitative ecological score — a novel semantic role for this channel (+2).

---

### Idea: Contour Tree of Species Richness as Ecological "Terrain" (inspired by p. 185–186)

- **Basic visuals combined:** Simplified contour tree structure (from flexible isosurfaces concept) + visual layout of richness "landscape" levels + yield color overlay
- **What the combination adds:** Treating total species richness as a scalar field over a derived site-space (e.g., PCA of environmental variables as x-y position) allows computing a conceptual "richness terrain" with isocontour lines. The simplified contour tree structure (inspired by flexible isosurfaces, p. 185) summarizes where richness levels split, join, or disappear — analogous to mountain peaks splitting into valleys. Adding yield color to the tree nodes shows where yield sits within the richness topology.
- **Data manipulation applied:** PCA of management/environmental variables to create 2D site space. Interpolate richness to continuous surface. Extract isocontour lines at multiple richness levels. Derive simplified contour tree (merging nearby components below a minimum persistence threshold). Color tree nodes by mean yield of sites in that contour component.
- **Marks:** Line marks (contour lines); line marks (contour tree structure with vertical spatial position = richness level); point marks (sites as leaf nodes).
- **Channels:** Spatial position x-y (site positions in PCA-derived environmental space); spatial position vertical (richness level in contour tree); color luminance/saturation (mean yield at each contour component — sequential); line density (gradient of richness).
- **User task supported:** Explore — are high-richness sites always low-yield? Find topological features — are there "peaks" of richness isolated from the main high-richness region that also tolerate high yields?
- **What it shows for our data:** A simplified contour tree with 5–10 nodes would summarize the entire richness landscape and show which richness regimes correspond to which yield ranges.
- **Persona it serves:** Elena (scientist) — methodological innovation, ecology-topology crossover. Sofia — persuasive spatial narrative of where richness "collapses."
- **Interaction if needed:** Interactive slider for richness contour level (as in standard flexible isosurfaces). Select contour tree node to highlight corresponding sites on the map.
- **Page reference:** p. 185–186

---

### Idea: Small-Multiple Choropleth Grid — One Panel per Plant Group Richness (inspired by p. 181)

- **Basic visuals combined:** Small multiples of choropleth maps (one per plant group: woody, herbaceous, bryophytes, total) + aligned color scale + yield as a separate synchronized panel
- **What the combination adds:** Four synchronized choropleths allow direct visual comparison of how woody species richness, herbaceous richness, and bryophyte richness spatially vary relative to each other AND relative to yield. This is something a single combined visualization cannot show without clutter. The combination answers: "Do all plant groups respond similarly to yield gradients, or do some groups remain rich even in high-yield areas?"
- **Data manipulation applied:** Normalize each richness type to [0–1] within its own range (to enable comparison across groups with very different absolute scales). Apply identical sequential colormap (e.g., light-to-dark green) to all panels. Yield panel uses a separate sequential colormap (e.g., brown-to-orange) to visually distinguish it from richness panels.
- **Marks:** Area marks (site regions/Voronoi cells across all panels, identical spatial layout).
- **Channels:** Spatial position (identical geographic layout, aligned across panels); color luminance/saturation (richness level within plant group — normalized sequential colormap); color hue distinction between richness (green) and yield (orange) panels.
- **User task supported:** Compare — which plant group shows the strongest negative correlation with yield? Identify — are there sites where woody richness is high even where yield is high? Locate — spatial clustering of high vs. low richness by group.
- **What it shows for our data:** If the woody richness choropleth closely mirrors the yield choropleth (same spatial pattern) while bryophytes do not, it suggests woody species are the key trade-off drivers. Regional "refugia" would appear as sites with both high richness (any panel) and high yield (yield panel).
- **Persona it serves:** Sofia (conservationist) — persuasive, clear spatial trade-off across groups. Hana (farmer) — "which species groups are compatible with my yield goals?" Elena — rigorous comparison.
- **Interaction if needed:** Synchronized hover/selection across all panels. Toggle to show raw vs. normalized values. Filter sites by management cluster.
- **Page reference:** p. 181
