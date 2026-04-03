# [agent_15] examples from class (dutch) — pages 1-3

The source document presents visualization examples for energy consumption data. The ideas below adapt those forms to the 60 Ethiopian coffee agroforest sites dataset.

---

### Idea: Site Flower Grid — Species Composition as Petals, Yield as Stem (inspired by p.2)

- **Basic visuals combined:** Flower diagram (Bloemen-diagram) + small-multiples grid layout.
- **What the combination adds:** Each site becomes its own "flower." Petals encode the composition of biodiversity (woody species richness, herbaceous richness, bryophyte richness, total richness) by size. The central circle or stem height encodes coffee yield. A grid of 60 flowers allows simultaneous comparison of all sites. The viewer can instantly see whether "full-petalled" (biodiverse) flowers tend to have small or large central yield circles — directly visualizing the yield–biodiversity trade-off.
- **Data manipulation applied:** Normalize petal sizes within each plant group category across all sites so sizes are comparable. Scale central circle area proportionally to 3-year mean yield. Arrange flowers in a grid sorted by yield (high to low) so the trade-off pattern reads left-to-right.
- **Marks:** Petals (custom shapes per species group); Central circle (yield); Grid cells (site identity).
- **Channels:** Petal size/area (richness per group); Central circle area (coffee yield); Color hue per petal (species group — woody/herbaceous/bryophyte/total); Position in grid (rank by yield).
- **User task supported:** Pattern detection (does high yield correlate with small petals?); comparison across sites; identify biodiversity hotspots vs. high-yield sites.
- **What it shows for our data:** Directly embodies the core tension: high yield = smaller/fewer petals. Sites in the upper-left of the grid (highest yield) should visually appear as "thin-petalled flowers with large centers."
- **Persona it serves:** Sofia (sees the trade-off spatially and persuasively); Elena (structure of the full 60-site dataset at once); Hana (spot her site and compare to top performers).
- **Interaction if needed:** Hover to reveal exact values per petal and yield; click to filter by cluster assignment from shrub structure data.
- **Page reference:** p.2 (Bloemen-diagram)

---

### Idea: Yield–Biodiversity Climate Stripes — Sites Ranked, Deviation Color-Coded (inspired by p.2)

- **Basic visuals combined:** Climate stripes + ranked bar ordering.
- **What the combination adds:** Each vertical stripe = one of the 60 sites, ordered left-to-right by coffee yield (low to high). Stripe color encodes deviation of total species richness from the mean: dark green = far above average richness, dark brown = far below. This creates a single image that answers the question: "As yield increases, does biodiversity systematically fall?" If the trade-off is real, the stripes should transition from green (left, low yield) to brown (right, high yield).
- **Data manipulation applied:** Rank 60 sites by mean coffee yield. Compute deviation of total species richness from the dataset mean. Map deviation to a diverging color scale (green–white–brown). No axes needed.
- **Marks:** Vertical rectangles (one per site).
- **Channels:** Position on x-axis (yield rank); Color hue (direction of richness deviation: green = above, brown = below mean); Color saturation (magnitude of deviation).
- **User task supported:** Identify trend (does richness fall as yield rises?); spot outliers (high yield AND high biodiversity); communicate the trade-off to non-technical audiences.
- **What it shows for our data:** A single striking image that either confirms or complicates the yield–biodiversity trade-off narrative.
- **Persona it serves:** Sofia (persuasive advocacy visual — the trade-off in one image); general public communication.
- **Interaction if needed:** Click a stripe to reveal site details (name, cluster, management variables).
- **Page reference:** p.2 (Klimaatstrepen / climate stripes)

---

### Idea: 60-Site Matrix Heatmap with Hierarchical Clustering — Species Groups × Sites (inspired by p.1)

- **Basic visuals combined:** Matrix heatmap + hierarchical clustering on both axes.
- **What the combination adds:** Rows = plant species groups (or individual dominant species); Columns = 60 sites. Cell color = abundance or presence. Hierarchical clustering reorders both axes so that sites with similar species compositions cluster together and species that co-occur cluster together. Overlaid on the column dendrogram: a color strip encoding coffee yield per site. This answers: "Do sites that cluster together by species composition also share similar yields?"
- **Data manipulation applied:** Build a species-by-site presence/absence or abundance matrix from the Total_species_composition.xlsx data (407 species). Compute a distance matrix (Bray-Curtis or Jaccard) and apply Ward hierarchical clustering. Annotate column dendrogram with yield as a color strip.
- **Marks:** Rectangles (cells); Dendrogram lines; Color strip bar.
- **Channels:** Color saturation/hue (species abundance or presence); Position (species × site identity after clustering); Color of annotation strip (yield magnitude).
- **User task supported:** Identify species composition clusters; link composition clusters to yield levels; find indicator species for high-yield sites.
- **What it shows for our data:** Whether the 60 sites form natural groups by plant community — and whether those groups map onto the yield gradient. Elena's primary question.
- **Persona it serves:** Elena (methodological structure, correlation across dimensions); Sofia (which communities are associated with high vs. low yield?).
- **Interaction if needed:** Expand/collapse dendrogram branches; filter to show only woody/herbaceous/bryophyte rows; hover for species name and site metadata.
- **Page reference:** p.1 (Matrix heatmap with hierarchical clustering)

---

### Idea: Shrub Structure Flower × Yield Node-Matrix (inspired by p.2 + p.2–3)

- **Basic visuals combined:** Flower diagram (per site) + node-matrix layout (JA9 concept).
- **What the combination adds:** Sites are arranged in a matrix layout (rows = management cluster, columns = yield quartile). Each cell contains a small flower diagram encoding the 7 shrub structure variables as petals. The cell background color encodes mean yield. This answers: "Within each management cluster, how does shrub structure vary, and does that variation predict yield?"
- **Data manipulation applied:** Assign sites to cluster and yield-quartile bins. Aggregate the 7 shrub structure variables (from Coffee_structure_index_variables.xlsx) per site. Normalize petal sizes across all sites for comparability.
- **Marks:** Petals (7 per flower, one per structure variable); Rectangles (cell backgrounds); Grid lines (matrix).
- **Channels:** Petal size (shrub structure variable magnitude); Cell background color saturation (yield level); Matrix position (cluster × yield quartile identity).
- **User task supported:** Compare how shrub structure profiles differ by management cluster and by yield level simultaneously.
- **What it shows for our data:** Whether management clusters correspond to distinct shrub structure profiles, and whether any profile is systematically associated with higher yield.
- **Persona it serves:** Elena (multivariate structure analysis); Hana (which cluster/profile produces the highest yield?).
- **Interaction if needed:** Hover on flower to see exact variable values; click to isolate one cluster row.
- **Page reference:** p.2 (Bloemen-diagram); p.2–3 (JA9 node-matrix concept)

---

### Idea: Cumulative Species Accumulation Curve × Yield Quartile (inspired by p.1)

- **Basic visuals combined:** Cumulative line chart + multi-group overlay (one line per yield quartile).
- **What the combination adds:** X-axis = sites added one by one (ordered within each quartile by species richness). Y-axis = cumulative total species count. Four lines (one per yield quartile: low/medium-low/medium-high/high). The slope of each line reveals how quickly new species appear as more sites are added in that yield group — i.e., how species-rich and how compositionally diverse each yield group's sites are.
- **Data manipulation applied:** Divide 60 sites into four yield quartiles using mean coffee yield. Within each quartile, order sites by total species richness (ascending). Compute cumulative unique species count as sites are added (species accumulation curve).
- **Marks:** Lines (four, one per quartile).
- **Channels:** Position x (number of sites added); Position y (cumulative unique species); Color hue (yield quartile — light to dark for low to high yield); Line slope (implied rate of new species per site added).
- **User task supported:** Compare species turnover rate across yield groups; identify whether low-yield sites hold disproportionate biodiversity; support conservation prioritization.
- **What it shows for our data:** If low-yield sites are also more compositionally unique, their conservation value is high even though they underperform agriculturally. Key argument for Sofia.
- **Persona it serves:** Sofia (biodiversity argument for low-yield site conservation); Elena (methodological — species accumulation curves are a standard ecological analysis tool).
- **Interaction if needed:** Toggle individual quartile lines on/off; hover to see which site is being added at each step.
- **Page reference:** p.1 (Geaccumuleerde Verbruikslijnen / cumulative consumption lines)

---

### Idea: Home vs. Field Comparison — Yield and Richness Profiles Across Day-Analog (Site Index) (inspired by p.2)

- **Basic visuals combined:** Dual-area mirror chart (JA7-inspired diverging layout) + site index axis.
- **What the combination adds:** X-axis = sites ordered by a composite management intensity index (from low-shade/high-intensity farming to high-shade/low-intensity). Upper area = coffee yield (above center line). Lower area = total species richness (below center line, mirrored). This directly shows the trade-off as a visual divergence: where the upper area is tallest, the lower is shortest, and vice versa. The mirroring makes the tension unmissable.
- **Data manipulation applied:** Compute a management intensity index by combining structure index, density, and dominance variables. Rank 60 sites by this index. Plot yield (up) and richness (down) as mirror areas, normalized to the same visual scale for drama.
- **Marks:** Area (two bands, mirrored above and below a central axis).
- **Channels:** Position x (management intensity rank); Height above center (yield magnitude); Depth below center (species richness); Color hue (green for richness area, amber/gold for yield area).
- **User task supported:** See the yield–biodiversity trade-off as a continuous function of management intensity; find sites near the center where both values are relatively high (best-of-both-worlds candidates).
- **What it shows for our data:** Whether the trade-off is linear or whether there is a "sweet spot" of management intensity where reasonable yield and reasonable richness coexist.
- **Persona it serves:** Sofia (trade-off argument, visually persuasive); Hana (find the sweet spot for her farming decisions); Elena (ecological gradient analysis).
- **Interaction if needed:** Brush to select sites in the sweet-spot zone; overlay individual site dots to identify them.
- **Page reference:** p.1 (JA7 mirror chart); p.2 (Vergelijking thuis versus kantoor)
