# [agent_10] Data Sketches — pages 201-250

## Source context
Pages 201–250 cover three completed projects: DDR spiral visualization, Dragon Ball Z fight network, and Harry Potter fanfiction timeline. The key techniques available for inspiration are: spiral layouts for compact sequential data, stacked dot histograms with color-as-secondary-variable, Bézier connector lines between nodes with varying thickness, swoosh direction as alignment encoding, character relationship networks doubling as navigation, small-multiple genre timelines, and hover-expand interaction for detail-on-demand.

---

### Idea: Site Journey Spiral — Yield Path Through the Year (inspired by p.209–211)

- **Basic visuals combined:** Spiral layout (from DDR project) + color-encoded dot sequence
- **What the combination adds:** A spiral shows the three yearly yield measurements for each site as three dots placed along the spiral arms, plus the mean. Neither a bar chart (which would compare sites but lose the year-to-year trajectory) nor a line chart (which would show trajectory but not compactness for many sites) alone achieves the dual goal. The spiral makes 60 sites comparable in one panel while preserving the within-site temporal trajectory.
- **Data manipulation applied:** Each site has 3 yearly yield values → compute mean, compute year-to-year change. Normalize yields to a 0–1 scale for spiral arm length (so the spiral size encodes relative yield, not absolute kg). Place year 1 at inner ring, year 2 at middle, year 3 at outer ring.
- **Marks:** One spiral glyph per site (small multiples of 60 spirals). Each spiral has 3 dots (years) + 1 center dot (mean).
- **Channels:**
  - Spiral arm length (how far out each dot sits) = yield value for that year
  - Color hue of the entire spiral = management intensity group (low / medium / high coffee dominance)
  - Dot size = could encode species richness total
  - Arrangement of 60 spirals in a grid = spatial grouping by cluster type
- **User task supported:** Spot yield stability across years; compare across sites; identify unreliable producers (spirals with dots spread far apart across arms).
- **What it shows for our data:** Yearly yield variability per site, plus management intensity as context, plus optional biodiversity layer.
- **Persona it serves:** Hana — "Is yield stable across years? Which sites are reliable producers?" Elena — "How strongly do the 3 yearly measurements agree? Is the mean a reliable proxy?"
- **Interaction if needed:** Hover over a spiral to reveal site name, exact yield values, shrub cluster group, and species richness breakdown. Filter by management intensity level to isolate one management category.
- **Page reference:** p.209–211

---

### Idea: The Swoosh Gradient — Sites Ordered by Yield, Connected by Biodiversity Threads (inspired by p.219–226)

- **Basic visuals combined:** Ranked dot plot (sites ordered by yield) + Bézier connector lines encoding biodiversity
- **What the combination adds:** A ranked list of sites by yield answers "which site produces most" but says nothing about biodiversity. A biodiversity chart alone says nothing about yield. The combination — sites arranged vertically by yield, with colored threads connecting sites that share species — answers: "Do high-yield sites share species with each other, or are they ecologically isolated from biodiverse sites?" This is the core trade-off question.
- **Data manipulation applied:** Sites ranked 1–60 by mean yield (y-position). For each pair of sites sharing a species, draw a connector. To avoid clutter, only draw connectors for species that appear in 3–10 sites (not too rare, not ubiquitous). Color connectors by the plant group of the shared species (woody / herbaceous / bryophyte).
- **Marks:** Circles (one per site on the vertical axis), Bézier arcs connecting site-pairs, colored by plant group.
- **Channels:**
  - y-position = mean coffee yield (rank)
  - Arc color = plant group of shared species (woody=green, herbaceous=yellow, bryophyte=blue)
  - Arc thickness = number of shared species between the pair
  - Node size = total species richness of the site
- **User task supported:** Spot trade-off between yield and biodiversity connectivity; identify which plant group creates most biodiversity overlap across the yield gradient.
- **What it shows for our data:** Species co-occurrence network projected onto a yield gradient — revealing whether biodiverse and productive sites are connected or isolated communities.
- **Persona it serves:** Sofia — "Is the trade-off real and which plant group is most sensitive?" Shows the structural separation between high-yield and biodiverse sites visually.
- **Interaction if needed:** Hover over a species thread to reveal which species it represents and how many sites it links. Filter by plant group to focus on woody vs. herbaceous vs. bryophyte connectivity separately.
- **Page reference:** p.219–226

---

### Idea: Good Guys vs. Bad Guys — Management Intensity as Alignment Encoding (inspired by p.226)

- **Basic visuals combined:** Sorted scatter plot + directional swoosh encoding for a binary variable
- **What the combination adds:** In the DBZ visualization, swoosh direction (left vs. right) encodes alignment (good vs. bad) — a purely spatial binary encoding that requires no legend. Applied to our data: sites are arranged along a yield axis, and their management intensity is encoded by which side their biodiversity profile "leans" — intensively managed sites lean right, shade-diverse sites lean left. This encodes the trade-off without requiring a separate color channel.
- **Data manipulation applied:** Compute a management score (composite of coffee density, coffee dominance, coffee structure index). Assign each site to "high management" or "low management" binary. Compute species richness profile (breakdown by group). Represent each site as a node on a vertical yield axis with a swooshing profile leaning left (biodiverse) or right (managed).
- **Marks:** Nodes (circles) on a vertical yield scale; diverging bar-like swoosh shapes extending left (species richness) or right (management variables) from each node.
- **Channels:**
  - y-position = mean yield
  - Swoosh direction = management regime (left = biodiversity-rich, right = intensively managed)
  - Swoosh width/area = magnitude of the respective variable
  - Node color = shrub cluster group (categorical)
- **User task supported:** Spot trade-off visually; identify sites that defy the pattern (high yield + leftward swoosh = both productive and biodiverse).
- **What it shows for our data:** The yield–management–biodiversity triangle in one visual for 60 sites.
- **Persona it serves:** Sofia — "Is the trade-off unavoidable? Are there sites on both sides?" Hana — "Which management style is associated with my yield level?"
- **Interaction if needed:** Hover reveals site details. Filter to highlight only sites where the swoosh direction contradicts the expected pattern (outliers).
- **Page reference:** p.226

---

### Idea: Dot Histogram of Species × Yield — Which Species Track High-Yield Sites? (inspired by p.236–237)

- **Basic visuals combined:** Stacked dot plot (dot histogram) + color-as-secondary-variable
- **What the combination adds:** A plain dot plot of species by yield association shows association strength. A heatmap shows which species appear at which sites. The combination — species stacked along a yield axis (x = average yield of sites where the species occurs), with dot color encoding the number of sites the species occupies — answers the new question: "Are high-yield associated species also widespread, or are they rare specialists?" Neither chart alone answers this.
- **Data manipulation applied:** For each of the 407 species: compute (1) average yield of sites where it occurs (from the species×yield dataset), (2) number of sites it occurs in. Bin species by average yield into 20 bins. Stack dots within each bin. Color each dot by site count (sequential scale: light = rare / dark = widespread).
- **Marks:** Dots (one per species).
- **Channels:**
  - x-position = average yield of sites where species occurs (quantitative)
  - y-position (stacking height) = count of species in that yield bin
  - Color = number of sites the species occurs in (sequential color scale)
  - Dot shape = plant group (circle=woody, triangle=herbaceous, square=bryophyte)
- **User task supported:** Identify species most strongly associated with high yield; distinguish widespread vs. rare high-yield associates.
- **What it shows for our data:** The full spectrum of 407 species arrayed by yield association, with rarity encoded in color.
- **Persona it serves:** Hana — "Which species are associated with my highest-yielding sites?" Sofia — "Are the species at high-yield sites rare or common? What is at risk?" Elena — "Which species are the strongest predictors to measure in a new study?"
- **Interaction if needed:** Hover over a dot to reveal species name, exact average yield, and site count. Click to highlight all sites where that species occurs in an accompanying site map.
- **Page reference:** p.236–237

---

### Idea: Canon vs. Non-Canon — Yield vs. Biodiversity Stacked Area by Plant Group (inspired by p.239–241)

- **Basic visuals combined:** Stacked area chart + color gradient encoding a secondary variable
- **What the combination adds:** A stacked area chart of biodiversity by plant group along a yield gradient shows total biodiversity and its composition simultaneously. Adding color-as-secondary-variable (management intensity) within each area reveals whether high-biodiversity areas are associated with low management. The combination answers: "As yield increases across sites, how does the composition of plant groups change, and is that change driven by management?"
- **Data manipulation applied:** Sort 60 sites by mean yield (x-axis). For each site, compute species richness per plant group (woody, herbaceous, bryophyte) — these become the stacked areas. Color each segment of the area by the management intensity score of that site.
- **Marks:** Stacked filled areas (one layer per plant group), step-curve style for cleaner boundaries.
- **Channels:**
  - x-position = sites ranked by mean yield (1–60)
  - y-position (area height per group) = species richness for that plant group
  - Stack order = plant group (woody bottom, herbaceous middle, bryophyte top)
  - Color gradient within each layer = management intensity (low management = green, high = brown/orange)
- **User task supported:** Spot how biodiversity composition shifts as yield increases; see which plant group declines first as management intensifies.
- **What it shows for our data:** The yield–biodiversity–composition–management relationship in one integrated view.
- **Persona it serves:** Sofia — "Which plant group is most sensitive to management? Where is biodiversity highest?" Elena — "Which variables co-vary most strongly? Which plant group to prioritize measuring?"
- **Interaction if needed:** Hover over a site's column to reveal site name, exact richness per group, yield, and management scores. Filter to show only one plant group to see its gradient in isolation.
- **Page reference:** p.239–241

---

### Idea: Character Graph as Navigation — Species Network as Persona Navigation (inspired by p.241)

- **Basic visuals combined:** Network graph (nodes = sites or species, edges = co-occurrence) + linked timeline/detail view that updates on node click
- **What the combination adds:** A plain species co-occurrence network is exploratory but has no natural focal point. Linking it to a site-detail panel that shows yield, management, and shrub cluster data for whichever site is selected turns the network into a structured exploration tool. The new question answered: "If I click on a high-biodiversity site in the network, what yield and management profile does it have?"
- **Data manipulation applied:** Build a species co-occurrence network at the site level (two sites are connected if they share more than N species). Size nodes by total species richness. Color nodes by yield quintile. Compute network layout. The click on any node triggers a sidebar update.
- **Marks:** Nodes (circles, sized by species richness, colored by yield quintile), edges (lines, thickness = number of shared species), sidebar bar charts for the selected site.
- **Channels:**
  - Node size = species richness
  - Node color = yield quintile
  - Edge thickness = number of shared species
  - Sidebar: y-position and length = variable values for selected site
- **User task supported:** Explore relationship between network position (ecological similarity), biodiversity, and yield; identify outlier sites that are ecologically isolated.
- **What it shows for our data:** Ecological similarity network of 60 sites, with yield and management overlaid.
- **Persona it serves:** Elena — "What is the internal structure? Which sites cluster together ecologically?" Sofia — "Are high-yield sites ecologically isolated from biodiverse sites?" Hana — "Which sites are most like my own — what do they look like?"
- **Interaction if needed:** Click a node to load that site's full profile in the sidebar. Filter edges by minimum shared species threshold to de-clutter the network. Toggle node color between yield, management, and species richness.
- **Page reference:** p.241

---

### Idea: Mini-Map for Yield Gradient Scroll — Managing a Long Heatmap (inspired by p.225)

- **Basic visuals combined:** Species × site heatmap (407 rows × 60 columns) + persistent mini-map overview panel
- **What the combination adds:** A full heatmap of 407 species × 60 sites is too tall to view at once. A standalone mini-map shows the full heatmap at reduced scale. Together they allow the user to scroll through the detail view while always knowing their position in the full gradient — answering: "What proportion of total species are these rows? Where am I in the yield gradient?"
- **Data manipulation applied:** Sort sites (columns) by mean yield. Sort species (rows) by their average yield of occurrence (from the species×yield dataset) — this creates a diagonal pattern if species track yield. Apply presence/absence fill.
- **Marks:** Small rectangles (heatmap cells), viewport indicator rectangle on mini-map.
- **Channels:**
  - x-position (columns) = sites sorted by yield
  - y-position (rows) = species sorted by yield association
  - Fill color = presence (1) / absence (0), or abundance value
  - Mini-map: same encoding at 1/10 scale; viewport rectangle shows current scroll position
- **User task supported:** Find which species track the yield gradient; spot clusters of co-occurring species; use mini-map to navigate by saga/group.
- **What it shows for our data:** Full compositional structure of the 407-species × 60-site matrix sorted to reveal yield-tracking species.
- **Persona it serves:** Elena — "Dataset structure, clusters, species that track yield." Sofia — "Which species are only at low-yield sites?"
- **Interaction if needed:** Click on mini-map to jump to that section of the heatmap. Hover on a cell to reveal species name, site name, yield, management variables. Filter rows by plant group.
- **Page reference:** p.225
