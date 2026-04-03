# [agent_02] Cool Infographics — pages 51-100

---

### Idea: Site Comparison Table with Per-Row Glyph Columns (inspired by p.95–96)

- **Basic visuals combined:** Ranked data table + icon glyph columns + color pixel mosaic for species composition
- **What the combination adds:** A plain ranked table shows yield order but cannot show WHY sites differ. Adding glyph columns for management intensity, shrub cluster group, and a small color-encoded species bar per row shows simultaneously how a site ranks AND what its profile looks like. The combination answers: "Which sites perform best AND what do they have in common?"
- **Data manipulation applied:** Sites ranked by mean coffee yield (descending). Each row = one site. Columns = yield (bar), coffee density (bar or dot), coffee structure index (dot size), shrub cluster (color badge), species richness (stacked mini-bar of plant group counts). Species composition of all 407 species condensed to a color pixel strip (one pixel per species, colored by plant group, sorted by species frequency across sites — presence = colored, absence = grey). This strip is the "color mosaic" technique from the Honda Accord visual.
- **Marks:** Table rows (sites), horizontal bars (yield, density), colored badge (cluster group), stacked mini-bar (species richness by group), pixel strip (species composition)
- **Channels:** Row position (yield rank), bar length (yield value), color hue of badge (cluster: 4 groups), stacked bar color (plant group identity), pixel strip color (species present), pixel strip grey (absent)
- **User task supported:** Compare sites, rank, identify what distinguishes top performers from bottom
- **What it shows for our data:** Yield rank × management variables × shrub cluster × biodiversity profile simultaneously per site. Reveals whether top-yield sites share a cluster group or management pattern.
- **Persona it serves:** Hana Abebe — directly answers "which of my sites are strong vs. weak, and what do top performers look like?"
- **Interaction if needed:** Hover over pixel strip to see species name; click column header to re-sort by any variable; filter by cluster group to isolate one archetype
- **Page reference:** p.95–96 (Honda Accord multi-column generation table)

---

### Idea: Side-by-Side Two-Column Trade-Off Comparison (inspired by p.93–94)

- **Basic visuals combined:** Two-column comparison layout + per-dimension mini-charts (bar, dot, area) + a scatterplot teaser in the header
- **What the combination adds:** The two-column structure makes the trade-off between high-yield and high-biodiversity sites the literal structure of the page. Neither a scatterplot alone nor a bar chart alone makes this as confrontational and clear. The combination answers: "Is the trade-off real, and how does it manifest across every dimension I care about?"
- **Data manipulation applied:** Sites divided into two groups: top tercile by mean yield ("High Yield") and bottom tercile ("High Biodiversity" — verified by checking these sites' actual richness scores). For each of 5–6 dimensions (total species richness, woody species count, herbaceous species count, bryophyte frequency, coffee density, coffee structure index), compute group mean. Display each dimension as one row, with left column = high-yield group value, right column = high-biodiversity group value. Central divider column names the dimension. Header: small scatterplot showing yield vs. total species richness for all 60 sites, color-coded by group membership.
- **Marks:** Horizontal bars (group means per dimension), dots (individual sites in header scatterplot), two-column layout (group identity)
- **Channels:** Bar length (group mean), color (left = orange/yield, right = green/biodiversity), position in column (group identity), dot color in scatterplot (group membership), dot position (yield × richness)
- **User task supported:** Spot trade-off, compare, identify which plant group is most sensitive
- **What it shows for our data:** The yield–biodiversity trade-off made visible across all plant groups and management variables simultaneously. Shows which dimension diverges most between groups.
- **Persona it serves:** Sofia Almeida — makes the trade-off hard to deny; persuasive structure mirrors the SoNice infographic format; ideal for an activist making a case
- **Interaction if needed:** Click on a dimension row to expand to a full dot plot showing all 60 sites rather than just group means
- **Page reference:** p.93–94 (SoNice "Making an Organic Choice" side-by-side format)

---

### Idea: Scrolling Scale Infographic — "If This Site Were a Forest" (inspired by p.52–53)

- **Basic visuals combined:** Proportional scale scrolling + annotated plant icon accumulation
- **What the combination adds:** The Mars distance infographic shows that making the viewer work (scroll) to reach a value IS the encoding of that value. Applied to species richness: as the viewer scrolls down, plant species icons accumulate one by one. At the point where a high-yield site's species count is reached (e.g., 45 species), the scroll stops with a marker. The viewer must continue scrolling much further to reach a high-biodiversity site's count (e.g., 110 species). The scrolling effort conveys the magnitude difference experientially. A plain bar chart of "45 vs. 110 species" does not create the same impact.
- **Data manipulation applied:** The two comparison values are total species richness for the median high-yield site vs. median high-biodiversity site. Species icons accumulate as abstract generic plant silhouettes (not identified), colored by group (green = woody, yellow = herbaceous, teal = bryophyte). The ratio of colors reflects actual species group composition.
- **Marks:** Plant silhouette icons (species), scroll axis (accumulation), colored groups
- **Channels:** Scroll position (total species count), icon color (plant group), icon accumulation rate (density of biodiversity)
- **User task supported:** See magnitude, feel trade-off, emotional legibility
- **What it shows for our data:** The sheer difference in species richness between high-yield and high-biodiversity sites, made visceral through scroll distance
- **Persona it serves:** Sofia Almeida — persuasive and emotionally legible; communicates scale of biodiversity loss not achievable with a bar chart
- **Interaction if needed:** Optional: hover over accumulated icons at any point to see which species group they represent; milestone markers at each site's richness value
- **Page reference:** p.52–53 ("How Far is it to Mars?" scrolling scale)

---

### Idea: Radial Site Wheel with Petals per Plant Group (inspired by p.67, flower/petal chart)

- **Basic visuals combined:** Radial petal/wedge chart + small multiples (one per site) + color encoding of management intensity
- **What the combination adds:** Each site is shown as a small radial petal chart: 4 petals (woody richness, herbaceous richness, bryophyte richness, total) where petal length encodes the richness value. 60 of these mini-charts arranged in a grid, ordered by yield (left to right, top to bottom). The combination answers: "Do high-yield sites have consistently shorter petals (lower richness) across all plant groups, or only for some?"
- **Data manipulation applied:** Normalize each richness dimension to a 0–1 scale so petals are comparable across sites. Color of the center dot = management intensity (coffee structure index, continuous color scale from light to dark). Sort sites by mean yield.
- **Marks:** Petal/wedge areas (one per plant group per site), center dot (management intensity)
- **Channels:** Petal length (richness value per plant group), petal color hue (plant group identity: green/yellow/teal), center dot color saturation (management intensity), position in grid (yield rank)
- **User task supported:** Explore, identify pattern across yield gradient, compare plant groups
- **What it shows for our data:** How the species richness profile (shape of the petal chart) changes across the yield gradient; whether one plant group consistently shrinks while others stay stable
- **Persona it serves:** Sofia Almeida (sees which group is most sensitive) and Elena Novak (sees structure of the dataset — which variable co-varies most with yield)
- **Interaction if needed:** Hover over any mini-chart to see site ID and exact values; click to expand to full detail view
- **Page reference:** p.67 (Mobile Youth communication wheel / petal chart)

---

### Idea: Monroe's Motivated Sequence Persuasive Infographic for Sofia (inspired by p.85–86)

- **Basic visuals combined:** Structured narrative layout (persuasive sections) + choropleth-style site map + trade-off scatterplot + species richness bar breakdown
- **What the combination adds:** The Monroe's Motivated Sequence structure (Key message → Problem → Danger → Solution → Call to action) is a design skeleton that organizes multiple chart types into a persuasive narrative. No single chart type creates a call to action alone. The structure turns data visualizations into an argument.
- **Data manipulation applied:** The argument is structured as: (1) KEY MESSAGE — "High-yield sites have fewer plant species"; a single large number (e.g., "42% fewer species at high-yield sites"). (2) PROBLEM — scatterplot of yield vs. total species richness, 60 dots. (3) DANGER — breakdown by plant group showing which group loses most (horizontal bars for each group, comparing top vs. bottom tercile). (4) SPECIES AT RISK — top 10 species found only at low-yield sites (list + site count). (5) CALL TO ACTION — "These sites need protection" with policy recommendation.
- **Marks:** Large number callout, scatterplot dots, horizontal bars, species list
- **Channels:** Dot position (yield × richness), dot color (management intensity tercile), bar length (species count per group), bar color (plant group), bold text (key numbers)
- **User task supported:** Follow argument, identify at-risk species, be persuaded to act
- **What it shows for our data:** The full trade-off narrative from headline fact to species-level evidence to policy implication
- **Persona it serves:** Sofia Almeida — she uses visuals to argue a case; this is built for presentation to an advocacy audience
- **Interaction if needed:** Static format preferred for this use case — meant to be printed or shared as image
- **Page reference:** p.85–86 ("Can Soap Make You Sick?" Monroe's Motivated Sequence structure)

---

### Idea: Growth Trajectory Bundles for Yield Stability Analysis (inspired by p.59)

- **Basic visuals combined:** Multi-series line chart (one line per site) + color-coded clustering by growth archetype + linked data table
- **What the combination adds:** The "Tale of 100 Entrepreneurs" shows that grouping trajectories by archetype makes patterns readable even with many overlapping lines. Applied to yield: each site is a line across 3 years, color-coded by shrub cluster group (4 colors). The combination answers: "Are high-yield sites also stable producers, or do some sites swing dramatically year to year?"
- **Data manipulation applied:** Normalize year-1 yield to a common starting point for each cluster to compare trajectory shape (not absolute level). Alternatively, show raw values with a % deviation from 3-year mean to highlight instability. Cluster group assignments from the existing cluster analysis become the color encoding.
- **Marks:** Lines (one per site), one line = 3 data points (year 1, year 2, year 3)
- **Channels:** Color hue (shrub cluster group: 4 groups), line position y (yield value), line slope (year-to-year change), position x (year 1 / year 2 / year 3), opacity (individual lines semi-transparent to show bundle shape)
- **User task supported:** Compare stability, identify unreliable sites, find which cluster groups are consistent
- **What it shows for our data:** Whether the 4 shrub cluster groups differ not just in mean yield but in yield stability; whether some clusters are more volatile than others
- **Persona it serves:** Hana Abebe — wants to know if yield is stable across years and which sites are reliable; Elena Novak — wants to know whether year-mean is a reliable proxy and how clusters differ internally
- **Interaction if needed:** Hover over a line to highlight that site's trajectory and see its ID; filter by cluster group checkbox to isolate one group; toggle between raw values and % deviation from mean
- **Page reference:** p.59 (Tale of 100 Entrepreneurs multi-series line chart with archetype grouping)

---

### Idea: Species × Site Heatmap with Yield Gradient Sorting (inspired by p.79, Lifespan bar chart ordering)

- **Basic visuals combined:** Presence/absence heatmap + yield-sorted site axis + species-frequency sorting
- **What the combination adds:** A plain presence/absence matrix of 407 species × 60 sites is unreadable. Sorting sites by yield (left = low yield, right = high yield) and sorting species by their correlation with yield (top = species associated with high yield, bottom = species associated with low yield) reveals structure: a diagonal gradient showing which species track high-yield environments and which track low-yield environments. This answers: "Which specific species are exclusively found at biodiverse, low-yield sites vs. which ones persist everywhere?"
- **Data manipulation applied:** Compute per-species mean yield of sites where it occurs (this is directly available in the dataset). Sort species by this value. Sort sites by mean coffee yield. Color cells: presence = colored (by plant group), absence = grey. Add a thin header row above the matrix showing yield value per site (color gradient from yellow to dark brown). Add a thin left margin showing plant group of each species (color strip).
- **Marks:** Filled cells (presence), empty cells (absence), header bar (yield), side strip (plant group)
- **Channels:** Cell color (presence/absence + plant group hue), cell position x (site, sorted by yield), cell position y (species, sorted by yield association), header bar color saturation (yield level), side strip color (plant group)
- **User task supported:** Find outliers, spot pattern, identify species sensitive to yield gradient
- **What it shows for our data:** The full community composition gradient across the yield spectrum; species that only occur at biodiverse sites form a visible cluster at the bottom-left of the matrix
- **Persona it serves:** Sofia Almeida (which species are at risk at high-yield sites); Elena Novak (correlation structure of species × yield, which variables to prioritize in a new study)
- **Interaction if needed:** Hover over a cell to see species name, site ID, yield value, and species occurrence count; click species row to highlight that species across all sites; filter by plant group to reduce to one group
- **Page reference:** p.79 (Lifespan of Storage Media — ordered rows make pattern appear; concept of sorting items to reveal structure)

---

### Idea: Isometric Scene with Color-Coded Site Icons (inspired by p.54–55)

- **Basic visuals combined:** Isometric scene illustration + color-coded categorical icons + size encoding
- **What the combination adds:** The Royksopp video uses an isometric cityscape where crowds are colored by employment type, embedding categorical data into a scene. Applied to the coffee dataset: an overhead isometric view of 60 agroforest sites arranged as a landscape. Each site is represented as a coffee farm icon. Color of the site = shrub cluster group. Size of the icon = mean yield. Density of tree symbols around the farm icon = species richness. This is semantically novel — the mark is a farm, and the forest density around it IS the biodiversity data.
- **Data manipulation applied:** Place 60 sites in a 2D grid or along a yield gradient. Icon size scaled to mean yield (3 size categories for visual clarity). Tree density around icon derived from total species richness (binned into 3–4 levels). Icon color = shrub cluster group (4 colors).
- **Marks:** Farm icon glyph (site), tree symbols (biodiversity proxy), colored icon hue (cluster)
- **Channels:** Icon size (yield magnitude), icon color (cluster group), tree density (richness level), position in layout (optional: management gradient)
- **User task supported:** Identify patterns spatially, compare sites, see co-occurrence of high yield and low biodiversity
- **What it shows for our data:** Whether high-yield sites (large icons) consistently appear in sparse tree environments (low density) — the trade-off made visible in a single scene
- **Persona it serves:** Hana Abebe — intuitive scene-based representation of her farms; also works as an overview for Sofia
- **Interaction if needed:** Click a farm icon to see full site profile; toggle tree density layer on/off; filter by cluster group
- **Page reference:** p.54–55 (Royksopp isometric crowd scene with color-coded categorical icons)

---

### Idea: Chord Diagram of Species Co-occurrence Across Sites (inspired by p.98–99)

- **Basic visuals combined:** Chord diagram + radial bar chart + color-encoded yield gradient
- **What the combination adds:** The Hockey Stanley Cup chord diagram shows team matchups as connections. Applied to species: each arc segment on the circle represents a plant species (or species group). A chord between two species means they frequently co-occur at the same sites. Chord thickness = number of shared sites. Radial bars show each species' association with yield (bar extending inward = associated with LOW yield; bar extending outward = associated with HIGH yield). This is semantically novel: species are normally not compared as "opponents" but this structure reveals which species communities hang together and whether those communities align with high or low yield.
- **Data manipulation applied:** Compute a co-occurrence matrix (how many of the 60 sites do species A and B both appear in?). Threshold to top 50–100 most connected species to avoid hairball. Compute per-species mean yield. Sort species by yield association on the circle arc.
- **Marks:** Arc segments (species), curved chords (co-occurrence), radial bars (yield association)
- **Channels:** Chord thickness (number of shared sites), bar length (yield association strength), bar direction (inward = low-yield association, outward = high-yield), arc color (plant group)
- **User task supported:** Explore community structure, identify species clusters, find which co-occurring communities align with high vs. low yield
- **What it shows for our data:** Whether there are distinct co-occurring species communities, and whether those communities map onto yield performance — the biological mechanism behind the trade-off
- **Persona it serves:** Elena Novak — reveals dataset structure and species co-occurrence patterns that inform field study design; Sofia Almeida — shows which species communities are at risk together
- **Interaction if needed:** Hover over an arc segment to highlight all chords for that species; filter by plant group; adjust co-occurrence threshold slider to show more or fewer chords
- **Page reference:** p.98–99 (Hockey Stanley Cup chord diagram with radial bar encoding)

---

### Idea: Persuasive "State of the Sites" Poster (inspired by p.83)

- **Basic visuals combined:** Map-style site overview + three-panel trade-off visual + call to action section
- **What the combination adds:** The "Most Polluted Cities" infographic ends with three clear calls to action after presenting data evidence. The structure: (1) establish scope with a map/overview, (2) present the damning data in two or three compact charts, (3) end with actionable recommendations. A single chart doesn't create a call to action; the structure does.
- **Data manipulation applied:** (1) Overview panel: 60 sites shown as dots on a coordinate plane (or abstract grid if no real geography), colored by yield tercile (low/medium/high). (2) Evidence panel: split scatter (yield vs. richness), one dot per site, large and clear, color = yield tercile. (3) Danger panel: horizontal bars showing mean richness per yield tercile for each plant group — showing that bryophytes and herbaceous plants lose most. (4) Action panel: "These X sites are high yield AND low biodiversity — they need management intervention."
- **Marks:** Dots (sites), scatter position (yield × richness), bars (mean per group), color (yield tercile)
- **Channels:** Dot color (yield tercile), bar length (mean richness), bar color (plant group), position (yield × richness in scatter)
- **User task supported:** Be persuaded, identify at-risk sites, follow narrative to conclusion
- **What it shows for our data:** A complete persuasive narrative from overview to evidence to species-level detail to actionable recommendation
- **Persona it serves:** Sofia Almeida — uses visuals to argue a case to policy makers or funders
- **Interaction if needed:** Static preferred; if interactive, hover on scatter dots to see site name
- **Page reference:** p.83 ("Most Polluted Cities" persuasive infographic with call-to-action structure)
