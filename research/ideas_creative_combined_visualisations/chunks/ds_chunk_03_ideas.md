# [agent_08] Data Sketches — pages 101-150

---

### Idea: Site Constellation Map — Yield as Pull, Biodiversity as Glow (inspired by p. 119–128)

- **Basic visuals combined:** Force-layout network diagram + scatterplot with opacity-encoded secondary variable
- **What the combination adds:** A plain scatterplot shows yield vs. one management variable. A network shows species co-occurrence. The combination shows all 60 sites simultaneously as nodes in a "constellation" space where their horizontal position reflects yield gradient, their vertical position reflects species richness, their size reflects management intensity, and their opacity reflects how isolated or connected they are to other high-biodiversity sites. Hovering reveals the site's full species profile — which neither basic visual can do alone.
- **Data manipulation applied:** Sites sorted along a continuous yield axis (3-year mean); species richness normalized per plant group; management variables (coffee density, dominance, structure index) combined into a single management intensity score via simple composite (e.g., standardized average). Hop-distance concept from Royal Constellations applied as: species overlap between sites (Jaccard similarity) defines "closeness" — similar species profiles attract each other in the layout.
- **Marks:** Circles (each = one site); size encodes management intensity; opacity encodes biodiversity rank (high biodiversity = fully opaque, low = semi-transparent — the opposite of Royal Constellations' "closeness to power")
- **Channels:**
  - x-position = 3-year mean coffee yield (quantitative — the most important variable, on the most accurate channel)
  - y-position = total species richness (quantitative)
  - Size = composite management intensity score (quantitative)
  - Opacity = how many rare/low-yield specialist species the site contains (quantitative — highlights biodiversity hotspots)
  - Color hue = shrub cluster group (categorical, 4–5 clusters from cluster analysis)
- **User task supported:** Spot trade-off (yield ↑ → biodiversity ↓), identify biodiversity hotspots, find outliers (high yield AND high richness)
- **What it shows for our data:** The core yield–biodiversity tension across all 60 sites; which cluster groups tend to appear in which yield/richness quadrant; which sites manage to escape the trade-off
- **Persona it serves:** Sofia Almeida — directly answers "Is the trade-off real and visible?" and "Are there sites that manage both high yield and high biodiversity?" Also serves Elena (structure/outlier detection)
- **Interaction if needed:** Hover on a site reveals a small breakdown bar showing species richness per plant group (woody / herbaceous / bryophytes). Click on a site highlights all other sites with Jaccard similarity > 0.3 (shared species community), showing which sites are ecologically similar.
- **Page reference:** p. 119–128

---

### Idea: Species Profile Radial per Site — Biodiversity Fingerprint (inspired by p. 107–111)

- **Basic visuals combined:** Radial dot plot (like travel colors) + small-multiples layout
- **What the combination adds:** A bar chart shows species richness per group for one site. A small multiples of bars shows all 60 sites — but loses the internal structure of each site's profile. The radial version encodes each species group as an angular segment, with the radius encoding count, creating a circular "fingerprint" that makes site profiles immediately visually distinctive (like a snowflake or iris pattern). Arranged in a grid sorted by yield, the layout answers the question: "How does the shape of biodiversity change as yield increases?"
- **Data manipulation applied:** Species richness per plant group (woody / herbaceous / bryophytes / total) provides 3–4 angular segments per site; sites sorted by mean yield for left-to-right grid arrangement; each radial scaled to a common maximum so comparisons are valid.
- **Marks:** Radial sectors/arcs (each arc = one plant group); the full radial glyph = one site
- **Channels:**
  - Arc angle/segment = plant group identity (categorical — woody / herbaceous / bryophyte)
  - Arc radius = species richness for that group (quantitative)
  - Color hue = plant group (categorical, consistent palette)
  - Grid x-position = yield rank (ordinal, low yield left → high yield right)
  - Grid y-position = management cluster or other grouping variable (categorical)
- **User task supported:** Spot pattern across yield gradient, compare biodiversity profiles, identify which group is most sensitive to yield increase
- **What it shows for our data:** Whether the biodiversity "fingerprint" systematically changes shape as yield increases — e.g., bryophytes shrink first, woody plants more resilient; or whether all groups shrink proportionally
- **Persona it serves:** Sofia (which plant group is most sensitive to management intensity?) and Elena (methodological: which plant group is the best indicator variable?)
- **Interaction if needed:** Hover on any radial glyph shows the site name, exact yield value, and a list of the most distinctive/rare species present at that site.
- **Page reference:** p. 107–111

---

### Idea: Scrollytelling Yield Journey — Site Portraits Revealed in Steps (inspired by p. 137–143)

- **Basic visuals combined:** Scrollytelling narrative + small multiples that progressively reveal additional variable layers
- **What the combination adds:** A static visualization of all 60 sites with all variables visible at once overwhelms any viewer. Scrollytelling allows the designer to introduce one layer at a time: first show sites as plain circles sorted by yield (section 1); scroll reveals management intensity (size, section 2); scroll reveals species richness (opacity, section 3); scroll reveals shrub cluster group (color, section 4); scroll focuses on outlier sites that beat the trade-off (annotation layer, section 5). Each section is legible on its own; the full picture emerges only after all sections.
- **Data manipulation applied:** No transformation beyond what is used across all sections; each variable normalized to 0–1 for consistent encoding. The narrative structure is itself a form of complexity management.
- **Marks:** Circles (each = one site); consistent mark across all sections — only channels are added/changed per section
- **Channels (accumulated across scroll):**
  - x-position = mean yield (constant across all sections)
  - y-position = species richness (constant, introduced section 3)
  - Size = management intensity (added section 2)
  - Color = shrub cluster group (added section 4)
  - Opacity = whether site is an "outlier" that escapes the trade-off (added section 5)
- **User task supported:** Explore, compare, identify, spot trade-off — with guided narrative pacing
- **What it shows for our data:** The full multi-dimensional picture of 60 sites, built up one variable at a time so the viewer understands each layer before the next is added
- **Persona it serves:** Hana Abebe — she needs to see which site conditions associate with higher production, but she is not a data analyst; the scrollytelling format guides her without requiring her to interpret a complex chart cold
- **Interaction if needed:** After the narrative, final section becomes a free-exploration mode: hover for site details, filter by cluster group via legend click.
- **Page reference:** p. 137–143

---

### Idea: Shortest-Path Species Chain — Which Species Connect High and Low Yield Sites? (inspired by p. 125–128)

- **Basic visuals combined:** Network graph (species co-occurrence) + yield-sorted axis
- **What the combination adds:** A species co-occurrence network alone shows which species tend to appear together. A bar chart of species × yield shows which species associate with high yield. Combined: a network where nodes are species (not sites), positioned vertically by their average yield of co-occurring sites (high yield species at top, low yield at bottom), with edges encoding co-occurrence strength. This immediately shows which species are "bridge" species spanning high- and low-yield environments, and which species are exclusive to one end.
- **Data manipulation applied:** The dataset provides per-species: (a) how many sites it occurs in, and (b) average yield of those sites. Co-occurrence between species pairs can be calculated from the presence/absence matrix (407 species × 60 sites). To avoid hairball, filter to species occurring in at least 5 sites; only draw edges for co-occurrence strength > threshold.
- **Marks:** Circles (nodes = plant species); lines (edges = co-occurrence in shared sites)
- **Channels:**
  - y-position = average yield of sites where the species occurs (quantitative — the key axis)
  - x-position = force-layout horizontal (community clustering)
  - Node size = number of sites the species occurs in (quantitative — rarity vs. ubiquity)
  - Node color = plant group (categorical: woody / herbaceous / bryophyte)
  - Edge thickness = co-occurrence strength (quantitative)
  - Edge opacity = strength of co-occurrence (to reduce visual noise)
- **User task supported:** Identify which species are yield-associated vs. biodiversity-specialist; find bridge species; explore species communities
- **What it shows for our data:** Whether high-yield sites share a characteristic species community, and which specific species are strong indicators of high or low yield — directly from the species × yield link dataset
- **Persona it serves:** Sofia (which species are only found at low-yield biodiverse sites?) and Elena (which species would be the best biodiversity indicator variables for a new field study?)
- **Semantic novelty note:** Network diagrams are standard for species co-occurrence. Using the y-axis as a continuous yield gradient — rather than just a force-layout — makes this semantically novel: it is a bipartite-inspired layout where community structure AND environmental gradient are visible simultaneously.
- **Interaction if needed:** Hover on a species node to highlight all sites where it occurs (switching to a site-level view on hover). Click to highlight the "shortest path" through the network between two user-selected species — showing the chain of co-occurrences that connects them.
- **Page reference:** p. 125–128

---

### Idea: Site Performance Dashboard — Headshot Grid Rearranged by Management Variable (inspired by p. 139–141)

- **Basic visuals combined:** Icon/glyph grid (like the Obama headshot grid) + scroll-driven rearrangement
- **What the combination adds:** A ranked list of sites by yield is one-dimensional. Grouping sites by shrub cluster shows categorical structure. The combination uses a grid of site "portrait" icons — small circular glyphs encoding multiple variables — that rearrange under scroll: first grouped by shrub cluster (section 1), then ranked by yield within each cluster (section 2), then sorted globally by yield (section 3). The scroll-driven transition reveals whether clusters are predictive of yield.
- **Data manipulation applied:** Site glyph encodes: yield as fill color intensity (high yield = deep green, low yield = pale), species richness as a small radial bar inside the glyph, management intensity as glyph border thickness. Cluster group assignment from existing cluster analysis data.
- **Marks:** Circular glyph icons (each = one site); inner radial bar = species richness profile; outer border = management intensity
- **Channels:**
  - Glyph fill color saturation = mean yield (quantitative → color intensity)
  - Inner radial segments = species richness per plant group (quantitative, categorical)
  - Border thickness = management intensity score (quantitative)
  - Grid grouping (section 1) = shrub cluster (categorical)
  - x-position within group or globally (section 2–3) = yield rank (ordinal)
- **User task supported:** Compare, rank, identify cluster structure, spot which cluster groups are high performers
- **What it shows for our data:** Whether sites within the same shrub cluster group share similar yield levels; which site-level factors visually distinguish top from bottom performers
- **Persona it serves:** Hana Abebe — she needs to compare her sites and identify which shrub structure cluster is associated with higher production; the rearranging layout makes the cluster-yield relationship visible through motion
- **Interaction if needed:** Hover on any site icon reveals a tooltip with exact yield values per year (showing whether yield is stable or variable across the 3 measured years).
- **Page reference:** p. 139–141

---

### Idea: Opacity-Gradient Trade-off Map — Who Gets "Faded Out" by Yield? (inspired by p. 125)

- **Basic visuals combined:** Scatterplot + opacity as a secondary encoding of biodiversity risk
- **What the combination adds:** A plain yield vs. management scatterplot shows sites by performance. Adding opacity to encode species richness creates a "fading" effect: high-yield, high-management sites become visually bright and dominant; low-yield, high-richness sites become dimmer — literally fading into the background. This mimics the metaphorical reality: in the push for yield, biodiversity is "faded out." The combination makes the trade-off emotionally legible.
- **Data manipulation applied:** Sites normalized for yield and species richness. Opacity derived directly from species richness (high richness = low opacity — inverted from Royal Constellations to communicate the "erasure" narrative). Color hue encodes management intensity cluster.
- **Marks:** Circles (each = one site)
- **Channels:**
  - x-position = management intensity (composite score, quantitative)
  - y-position = mean yield (quantitative)
  - Opacity = species richness (quantitative, inverted — more biodiverse sites are MORE transparent, visually "disappearing")
  - Color hue = shrub cluster group (categorical)
  - Size = total number of plant species present (quantitative)
- **User task supported:** Spot trade-off, identify what is lost, emotionally engage with the biodiversity cost
- **What it shows for our data:** As management intensity and yield increase, the richest biodiversity sites become invisible — the chart literally shows biodiversity being "faded out" by intensification
- **Persona it serves:** Sofia Almeida — the inverted opacity encoding is a persuasive rhetorical device; the visualization argues the case visually, not just analytically
- **Semantic novelty note:** Standard scatterplots use opacity for depth/density. Using inverted opacity as a rhetorical/narrative device (more valuable = less visible) is semantically novel and emotionally powerful.
- **Interaction if needed:** Hover restores full opacity to any site and shows its species richness breakdown; a toggle allows Sofia to "flip" the opacity to normal mode for analytical comparison.
- **Page reference:** p. 125
