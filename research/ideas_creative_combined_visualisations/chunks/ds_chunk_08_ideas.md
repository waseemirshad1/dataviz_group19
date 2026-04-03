# [agent_13] Data Sketches — pages 351-400

## Source Context
Pages 351–400 of Data Sketches cover three visualization projects: Nadieh's star-constellation map "Figures in the Sky", Shirley's 3D crystal glyph field "Legends", and Nadieh's radial manga visualization for Cardcaptor Sakura. The key techniques are: multi-ring radial layouts with inner/outer circles connected by arcs; 3D glyph fields encoding 4+ variables; K-means color extraction from images; small donut overlays on spatial maps; mini thumbnails in a ring for overview + detail-on-demand; and the CMYK halftone aesthetic.

---

### Idea: Radial Site-Chapter Ring — Coffee Sites as Radial "Pills" (inspired by p.389–400)

- **Basic visuals combined:** Donut ring of 60 site arcs (outer ring) + inner circle of management cluster groups + curved arc connections between sites and their cluster + center panel for site-level detail on hover.
- **What the combination adds:** A radial layout answers "which sites belong to which management cluster?" at a glance (connection pattern), while the outer ring color encodes a quantitative variable (yield), letting the user see whether cluster membership predicts yield. The center panel shows the full variable profile for any selected site.
- **Data manipulation applied:** Group sites (1–60) by cluster assignment (4 clusters from `Coffee_structure_index_variables.xlsx`). Color each outer arc by yield (continuous color scale, e.g., yellow to dark green). Normalize arc widths equally (one arc = one site, sequential order). Connection lines from site arc to its cluster segment in the inner donut.
- **Marks:** Arc segments (outer ring, one per site); donut segments (inner ring, one per cluster); curved connection arcs (site → cluster, shown on hover only); central circular panel (site detail card).
- **Channels:** Outer arc color → yield (ordered, sequential color); arc angular position → site ID (1–60); inner segment size → number of sites per cluster; connection arc → membership; center panel text/sparklines → full variable profile.
- **User task supported:** Identify cluster membership; compare yield across clusters; drill into a single site.
- **What it shows for our data:** Are high-yield sites concentrated in one cluster? Are low-yield sites all in a different cluster? Does cluster assignment add information beyond yield alone?
- **Persona it serves:** Elena (scientist) — cluster validity; Hana (farmer) — which cluster type has the best yields.
- **Interaction if needed:** Hover on outer arc → show connection to cluster + highlight all sites in same cluster + show site detail card in center. Click to lock selection.
- **Page reference:** p.389–400

---

### Idea: Multi-Variable Glyph Field — 60 Sites as Crystals (inspired by p.371–377)

- **Basic visuals combined:** Glyph field (60 items) where each site is a custom multi-channel glyph, arranged in a 2D scatter plot by species richness (x) vs. yield (y).
- **What the combination adds:** The scatter plot position immediately shows the core trade-off (richness vs. yield). The glyph encodes additional variables — cluster, coffee density, and dominance — without requiring separate charts. This directly embeds the "why" behind the trade-off in the visual.
- **Data manipulation applied:** X = total species richness (from `Plant_species_richness.xlsx`); Y = mean 3-year yield (from `Coffee_yield.xlsx`). Glyph shape/size attributes from `Environmental_and_management_variables.xlsx`: coffee structure index (size), density (number of "faces" or spikes), dominance (color saturation). Cluster = color hue.
- **Marks:** Custom glyphs (one per site) — circular with variable-count radiating spokes or facets; positioned in scatter space.
- **Channels:** X-position → species richness; Y-position → yield; glyph size → coffee structure index; spoke/facet count → density category; color hue → cluster (4 categories); color saturation → dominance.
- **User task supported:** See trade-off pattern; identify outlier sites that have both high richness and above-average yield; compare clusters.
- **What it shows for our data:** Whether the yield–richness trade-off is consistent across all 4 management clusters, or whether some clusters buck the trend (high yield AND high richness). Outlier sites — "win-win" candidates — stand out immediately.
- **Persona it serves:** Sofia (conservationist) — trade-off visibility; Elena (scientist) — cluster and outlier analysis.
- **Interaction if needed:** Hover on glyph → show site ID, all variable values, and which species are present. Color-filter by cluster.
- **Page reference:** p.371–377 (semantic novelty: standard scatter plot in novel role as glyph field +2)

---

### Idea: Species Disappearance Timeline — Sites as a Gradient Strip with Species Presence/Absence (inspired by p.362–368)

- **Basic visuals combined:** Small multiple heatmaps (one strip per plant group) aligned on a shared x-axis ordered by management intensity (coffee density, low → high). Each row = one species; filled = present, empty = absent.
- **What the combination adds:** The small multiple structure answers Sofia's question "Which species disappear as management intensifies?" by showing disappearance patterns per species group side by side. Shared x-axis makes cross-group comparison direct.
- **Data manipulation applied:** Order 60 sites by coffee density (ascending). Extract presence/absence from `Total_species_composition.xlsx`. Separate into panels by plant group (woody/herbaceous/bryophyte). Sort species rows by "disappearance threshold" — the density value at which a species is last seen.
- **Marks:** Filled rectangles (presence = colored, absence = empty/gray).
- **Channels:** X-position → site (ordered by management intensity); Y-position → species (sorted by disappearance threshold); fill color → plant group identity (one hue per panel); fill opacity → present/absent.
- **User task supported:** Identify which species are most sensitive to management intensification; compare across plant groups.
- **What it shows for our data:** Are bryophytes or woody species more sensitive to management intensification? Which species are the last to disappear (most robust)?
- **Persona it serves:** Sofia (conservationist) — which species disappear; Elena (scientist) — is the pattern consistent across groups.
- **Interaction if needed:** Hover on a species row → highlight that species across all panels; click to filter to only sites where that species is present and show their yield distribution.
- **Page reference:** p.362–368 (small multiple sky map concept adapted to presence/absence matrix)

---

### Idea: Overview + Detail Sky-Map Style — Each Site as a "Star" with Donut Overlay (inspired by p.353–361)

- **Basic visuals combined:** A spatial scatter plot of 60 sites (x = species richness, y = yield) where each site is rendered as a small star-like mark, surrounded by a mini donut chart encoding the composition of its species richness by plant group.
- **What the combination adds:** The scatter gives the overview trade-off; the donut overlays add a third dimension (richness composition) without needing a separate chart. Clicking a site expands it into a full detail view — exactly the "click thumbnail to expand" pattern used in the constellation ring.
- **Data manipulation applied:** X = total species richness; Y = yield. Donut slice proportions = percent woody / herbaceous / bryophyte of total richness (from `Plant_species_richness.xlsx`). Site positioned in scatter space, donut drawn around it.
- **Marks:** Point (site center); arc segments (donut around each point); larger detail panel (on click).
- **Channels:** X-position → species richness; Y-position → yield; donut arc angle → proportion of richness by plant group; arc color → plant group (3 hues); site marker size → coffee density (optional).
- **User task supported:** Compare 60 sites on trade-off; distinguish which type of richness (woody vs. bryophyte vs. herbaceous) varies most across the yield gradient.
- **What it shows for our data:** Is the trade-off driven more by woody species richness or by bryophyte richness? Are high-yield sites that still have moderate total richness rich in one particular group?
- **Persona it serves:** Hana (farmer) — compare sites; Sofia (conservationist) — richness composition; Elena (scientist) — which plant group best predicts yield.
- **Interaction if needed:** Click on a site → expand into full profile (yield 3 years, all species richness values, management variables, cluster); hover → show site name and key stats.
- **Page reference:** p.353–361 (semantic novelty: sky map overlay technique adapted to scatter plot +2)

---

### Idea: K-Means Color Extraction Analogy — "Color Profile" of Each Site's Biodiversity (inspired by p.387–388)

- **Basic visuals combined:** A horizontal bar chart per site (similar to the CCS color distribution bars) where each segment represents one species group, and segment width = proportion of total richness. Bars stacked in a heatmap grid (60 rows × 3+ columns), sorted by yield.
- **What the combination adds:** Translating the K-means color composition idea to biodiversity composition gives a visual "fingerprint" for each site — its biodiversity profile. Sorting by yield reveals whether high-yield sites have a characteristic profile.
- **Data manipulation applied:** Compute proportional richness: woody/total, herbaceous/total, bryophyte/total per site. Sort sites by mean yield (descending). Plot as stacked bars, one per site, sorted.
- **Marks:** Horizontal stacked bar segments (one per plant group); one row per site.
- **Channels:** Row position → yield rank; segment width → proportion of richness; segment color → plant group (3 fixed hues).
- **User task supported:** Do high-yield sites have a different richness composition profile from low-yield sites?
- **What it shows for our data:** A consistent shift in the proportion of one plant group (e.g., bryophytes declining) along the yield gradient would be immediately visible as a color wedge narrowing or widening down the sorted list.
- **Persona it serves:** Sofia (conservationist) — compositional trade-off; Elena (scientist) — which group best tracks the yield gradient.
- **Interaction if needed:** Click on a bar to highlight that site's position in a companion scatter plot.
- **Page reference:** p.387–388

---

### Idea: Circular Arc Connection Map — Species × High-Yield Sites (inspired by p.393–400)

- **Basic visuals combined:** Two semicircles facing each other: top = top 20 highest-yield sites; bottom = top 50 most widespread species. Arcs connect a species to the sites where it occurs. Arc thickness = how many of the 20 top sites include that species. A second version mirrors the pattern for the 20 lowest-yield sites.
- **What the combination adds:** This directly answers "Which species are associated with high-yield sites vs. low-yield sites?" (from `Plant_species_and_average_coffee_yield_in_sites_where_the_species_occurs.xlsx`). The arc pattern immediately reveals specialist species (thin arcs to few sites) vs. generalists (thick arcs spanning many sites), and whether high-yield or low-yield sites share species.
- **Data manipulation applied:** Filter to top 20 / bottom 20 sites by yield. Aggregate species presence/absence for those 20 sites. Compute: for each species, count how many of the 20 target sites include it. Filter to species present in ≥3 target sites. Arc thickness = count.
- **Marks:** Semicircular nodes (sites, top arc); semicircular nodes (species, bottom arc); curved connection arcs.
- **Channels:** Node position → site/species identity; arc thickness → co-occurrence frequency; arc color → species group (woody/herb/bryophyte); opacity → frequency (thicker + more opaque = more shared).
- **User task supported:** Which species co-occur with high-yield sites? Which are shared between high and low yield? Which are exclusive to one end of the yield spectrum?
- **What it shows for our data:** Species that are exclusive to the low-yield (high-diversity) end and absent from high-yield sites are the most critical for conservation arguments. Species present in both ends are not indicators.
- **Persona it serves:** Sofia (conservationist) — which species to protect; Hana (farmer) — which species to watch as indicators of land condition.
- **Interaction if needed:** Hover on a species node → highlight all sites where it occurs + show average yield; filter by plant group.
- **Page reference:** p.393–400 (radial arc connection concept adapted to bipartite site × species network)

---

### Idea: Progressive Disclosure 3D — Walk Through Sites, Fly Above for Pattern (inspired by p.377)

- **Basic visuals combined:** A 3D WebGL scatter (Three.js) where each site is a glyph placed in 3D space: x = species richness, y = yield, z = coffee density. At ground level: individual site glyphs dominate (identity + details). Flying above: the trade-off pattern (richness vs. yield gradient) becomes apparent as a slope in the point cloud.
- **What the combination adds:** The progressive disclosure by camera angle is a genuine insight tool — the z-axis (density) is only fully interpretable from a rotated perspective, just as in Shirley's Nobel Laureate piece (temporal dimension revealed only from above).
- **Data manipulation applied:** Normalize all three axes. Use cluster assignment for glyph color. Size glyph by dominance.
- **Marks:** 3D glyphs (one per site).
- **Channels:** x → richness; y → yield; z → coffee density; color hue → cluster; size → dominance.
- **User task supported:** Explore whether the trade-off is consistent across all three management dimensions simultaneously; find 3D outlier sites.
- **What it shows for our data:** Sites at the intersection of high density + high richness + above-average yield — the "win-win-win" outliers — would stand out as isolated points in the upper-density region of the 3D cloud.
- **Persona it serves:** Elena (scientist) — 3D correlation structure; advanced exploration.
- **Interaction if needed:** Orbit/rotate; hover for site label; click to lock and show full profile.
- **Page reference:** p.377

---

### Idea: Annotation-First Trade-Off Scatter — "Four Quadrants" with Annotation Callouts (inspired by p.363, p.399)

- **Basic visuals combined:** A simple scatter plot (species richness × yield) divided into four quadrants (high/low yield × high/low richness) with color-coded quadrants and heavy editorial annotations calling out notable sites by name, cluster, and interesting properties.
- **What the combination adds:** Annotations transform a passive scatter into an editorial argument — Sofia can use this to show "the trade-off is real and undeniable" by annotating the emptiness of the upper-right quadrant (high yield AND high richness). Named outliers make it personal and actionable.
- **Data manipulation applied:** Compute median yield and median richness as quadrant boundaries. Label top 5 outlier sites per quadrant. Color points by cluster. Annotate the empty upper-right quadrant explicitly ("no sites here — the trade-off").
- **Marks:** Points (sites); quadrant boundary lines; annotation callouts with leader lines.
- **Channels:** X → species richness; Y → yield; color hue → cluster; annotation → site name + key variable.
- **User task supported:** Communicate the trade-off as a persuasive argument; identify exceptions.
- **What it shows for our data:** The emptiness of the high-richness + high-yield quadrant is the main argument for conservation. Annotating it explicitly makes it undeniable.
- **Persona it serves:** Sofia (conservationist) — persuasive communication; Hana (farmer) — where do I want to be?
- **Interaction if needed:** Static (printable); optionally click quadrant to filter to those sites.
- **Page reference:** p.363, p.399 (annotation-first design; d3-annotation edit-mode workflow)
