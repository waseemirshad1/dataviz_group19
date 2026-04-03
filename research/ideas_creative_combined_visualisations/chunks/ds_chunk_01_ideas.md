# [agent_06] Data Sketches — pages 1-50

## Creative Combined Visualization Ideas

Inspired by the Loom and Strings (custom chord diagram) and Film Flowers (flower glyph per item) visualizations from pages 28-50 of Data Sketches.

---

### Idea: Site Flowers — Multi-Channel Glyph per Coffee Site (inspired by p.44-50)

- **Basic visuals combined:** Flower glyph (Film Flowers) + bar chart (species richness breakdown per group embedded in petal structure)
- **What the combination adds:** A plain scatterplot could show yield vs. total species richness. A plain bar chart shows species group breakdown per site. The combination answers: *What does the full biodiversity profile of each site look like, and how does it relate to that site's yield?* — both simultaneously per site.
- **Data manipulation applied:** Compute species richness per plant group (woody / herbaceous / bryophyte) per site. Normalize richness values within each group to enable comparable petal sizing. Compute mean yield per site. Discretize mean yield into 4-5 bins to assign a discrete petal shape (or color).
- **Marks:** One flower glyph per site (60 flowers total). Each flower has 3 petal groups (one per plant species group). Petal length encodes species richness within that group. Petal shape or color encodes the plant group type.
- **Channels:**
  - Petal length / radius → species richness per plant group (quantitative)
  - Petal color hue → plant group (woody = brown/green, herbaceous = light green, bryophyte = blue-grey)
  - Number of petals per group → optionally encodes number of individual species present (discretized count)
  - Overall flower size (base radius) → mean coffee yield (quantitative)
  - Layout position (x-axis) → sites ranked by mean yield (left = low, right = high)
- **User task supported:** Compare biodiversity profiles across sites; spot trade-off between yield and richness; identify which plant group drives biodiversity variation
- **What it shows for our data:** Which sites have high yield but low richness (small flower, short petals), which have low yield but rich biodiversity (large flower, long petals), and which plant group is most sensitive to the yield gradient
- **Persona it serves:** Sofia Almeida — answers "Do high-yield sites have lower species richness?" and "Which plant group is most sensitive to management intensity?" The gallery layout makes the trade-off visible across all 60 sites. Also serves Hana Abebe — she can see which plant group co-varies most with high yield.
- **Interaction if needed:** Hover over a flower to reveal site name, exact yield, and species counts per group. Filter by management intensity cluster to focus on a subset. Click to drill into species composition.
- **Page reference:** p.48-50

---

### Idea: Loom-and-Strings for Species-Site Connections (inspired by p.28-43)

- **Basic visuals combined:** Custom Loom-and-Strings chord diagram + outer arc magnitude encoding
- **What the combination adds:** A standard presence/absence heatmap shows which species occur at which sites. A simple bar chart shows yield per site. The Loom-and-Strings combination answers: *Which species groups are most strongly connected to high-yield vs. low-yield sites, and how does each site's connection profile look across species groups?* — the flow structure of the species-site relationship.
- **Data manipulation applied:** Aggregate presence/absence data from individual species up to plant group level (woody / herbaceous / bryophyte) per site. Compute total number of species per group per site. Group sites into yield quartiles (4 yield bands = 4 "characters" in the center). String thickness = number of species from that group found at sites in that yield band.
- **Marks:** Curved strings flowing from outer arcs (plant groups or species clusters) to inner sections (yield quartiles). Outer arcs per plant group. Inner positions per yield band.
- **Channels:**
  - String thickness → number of species connections (quantitative)
  - Color → plant group identity (categorical)
  - Arc length (outer) → total species richness of that group across all sites
  - Inner position → yield quartile (ordinal)
- **User task supported:** Spot which plant groups are concentrated in low-yield sites vs. widespread; identify which yield quartile has the richest connections overall
- **What it shows for our data:** Whether high-yield sites are connected to fewer plant groups (thinner strings), whether bryophytes are disproportionately concentrated in low-yield sites
- **Persona it serves:** Sofia Almeida — makes the yield-biodiversity trade-off visible through the flow structure. The visual argument: high-yield inner sections receive thin strings, low-yield sections receive thick strings.
- **Interaction if needed:** Hover over a yield-band section to highlight all strings connected to it and show mean species richness. Hover over a plant group arc to isolate its connection profile across yield bands.
- **Page reference:** p.28-43

---

### Idea: Yield-Biodiversity Trade-off Scatterplot with Embedded Site Profiles (inspired by p.44-50)

- **Basic visuals combined:** Scatterplot + small flower/radial glyph per point
- **What the combination adds:** A plain scatterplot of yield vs. total species richness shows the trade-off as a trend. A plain glyph shows which species groups contribute to richness. Combined, it answers: *Where does each site sit on the yield-diversity trade-off, AND what is the species composition driving that site's richness?* — the scatterplot reveals the trend; the glyph reveals the within-site structure that explains position on the trend.
- **Data manipulation applied:** Compute mean yield and total richness per site. Compute proportion of richness from each plant group per site. Optionally compute a management index composite score for a third encoding.
- **Marks:** 60 points in a scatterplot. Each point is replaced by a small radial glyph (3 wedges, like a pie but with variable radius per wedge).
- **Channels:**
  - x-position → mean coffee yield (quantitative — most important variable, highest accuracy channel)
  - y-position → total species richness (quantitative)
  - Wedge angle (fixed 120° each) → plant group identity (categorical: woody / herbaceous / bryophyte)
  - Wedge radius → species richness contribution of that group (quantitative)
  - Overall glyph color saturation → management intensity (coffee structure index) (quantitative)
- **User task supported:** Spot trade-off pattern (downward slope left to right); identify which plant group drives richness in low-yield sites; find outliers (sites with both high yield and high richness)
- **What it shows for our data:** The central tension: as yield increases, total richness decreases — and the radial glyphs reveal whether this is driven by loss of woody species, herbaceous species, or bryophytes
- **Persona it serves:** Sofia Almeida (primary) — the trade-off is the visual argument. Elena Novak — can inspect which species group correlates most with the y-axis variable. Hana Abebe — can spot outlier sites that achieved both goals.
- **Interaction if needed:** Hover on a glyph to show site name, exact yield, richness per group, management variables. Filter to highlight sites in the same shrub cluster group.
- **Semantic novelty:** The scatterplot is standard when points are uniform dots. It becomes semantically novel when each point is itself a species composition profile — the position shows where the site sits on the trade-off; the glyph shows why it sits there.
- **Page reference:** p.48-50

---

### Idea: Ranked Site Gallery with Shrub Structure Small Multiples (inspired by p.44-50)

- **Basic visuals combined:** Ranked bar chart (sites by yield) + small polar/radar glyph per bar (shrub morphological profile)
- **What the combination adds:** A ranked bar chart shows yield ranking across 60 sites. A radar chart shows the 7 shrub morphological variables per site. Combined, it answers: *Do the highest-yield sites share a distinctive shrub structure profile?* — the bar shows rank; the glyph shows the structural fingerprint at that rank.
- **Data manipulation applied:** Compute mean yield per site and rank sites 1-60. Average the 7 shrub morphological variables across 16 shrubs per site. Normalize each variable to [0,1] for radar comparability. Color-code sites by cluster group from cluster analysis.
- **Marks:** 60 bars arranged horizontally by yield rank. Each bar topped by a small polar/radar glyph (7 axes, one per morphological variable). Bar height = yield. Glyph shape = shrub structure.
- **Channels:**
  - Bar height → mean coffee yield (quantitative)
  - Bar / glyph color → shrub cluster group (categorical: 4-5 groups)
  - Radar axis extent → value of each morphological variable (quantitative)
  - Position (x-axis) → yield rank (ordinal)
- **User task supported:** Rank sites by yield; compare shrub profiles of top vs. bottom performers; identify which cluster groups dominate high-yield positions
- **What it shows for our data:** Whether specific shrub structure clusters are consistently associated with top-yield sites, giving Hana actionable insight about which shrub characteristics to cultivate
- **Persona it serves:** Hana Abebe — directly answers "Which site conditions are associated with higher production?" and specifically addresses shrub structure clusters. Also serves Elena Novak for validating the cluster analysis.
- **Interaction if needed:** Hover for exact values per site. Filter by cluster group to isolate each cluster's position in the yield ranking. Toggle between viewing mean vs. year-by-year yield (to assess stability).
- **Page reference:** p.48-50

---

### Idea: Species Gradient Strip — Presence/Absence Heatmap Sorted by Yield (inspired by p.28-43, data manipulation logic)

- **Basic visuals combined:** Heatmap (species × site matrix) + yield gradient axis
- **What the combination adds:** A standard heatmap of species presence by site shows composition. A bar chart shows yield. Sorted together they answer: *Which individual species are consistently found only at low-yield, biodiverse sites, and which are found everywhere?* — the sort order reveals the ecological gradient hidden in the matrix.
- **Data manipulation applied:** Sort sites (columns) by mean yield (low to high). Sort species (rows) by the mean yield of sites where each species occurs (provided directly as a variable in the dataset). Optionally cluster rows into groups (indicator species, generalists, etc.)
- **Marks:** Rectangles in a grid (site × species). Each cell filled or empty depending on presence/absence.
- **Channels:**
  - Cell fill (binary) → species presence at site (presence/absence)
  - Cell color (when present) → optionally encode abundance or frequency (quantitative, using color saturation)
  - Column order → site yield rank (ordinal, low to high)
  - Row order → species mean-yield association (ordinal: species found only at low-yield sites at top; widespread species at bottom)
  - Row color strip on left margin → plant group identity (categorical)
- **User task supported:** Identify species only present at low-yield sites (indicator species for biodiversity); spot generalist species present across the yield gradient; explore community composition change
- **What it shows for our data:** The 407-species × 60-site matrix is the richest data in the dataset. Sorted by yield, it visually reveals which species track the low-yield / high-biodiversity end of the gradient
- **Persona it serves:** Sofia Almeida — "Which specific species are only found at low-yield biodiverse sites?" This visual makes the ecological argument: as you move right (toward high yield) rows disappear from the top, showing species loss. Elena Novak — can inspect structure in the composition data.
- **Interaction if needed:** Hover to see species name, plant group, number of sites it occurs in, and mean yield of those sites. Filter rows to show only woody species, or only bryophytes. Click on a column (site) to highlight that site across the gallery.
- **Semantic novelty:** A heatmap is standard when rows and columns are arbitrary. It becomes semantically novel when columns are sorted by yield gradient and rows by species-yield association — the sorting transforms a matrix into a biodiversity gradient story.
- **Page reference:** p.28-43 (manual variable addition and aggregation logic)
