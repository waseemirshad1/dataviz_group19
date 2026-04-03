# [agent_09] Data Sketches — pages 151-200

## Pages covered
- pp. 151–168: "Magic is Everywhere" (Nadieh) — custom glyphs for books in tSNE scatter space
- pp. 169–188: "Every Line in Hamilton" (Shirley) — filter tool for lyric streams, musical arc notation
- pp. 189–200: "The Top 2000" (Nadieh) — beeswarm by time, channel-stacking, vinyl metaphor marks

---

### Idea: Site Glyph Scatter — each site as a circular profile mark (inspired by p. 156–160)

- **Basic visuals combined:** Scatter plot (position = two key variables) + custom circular glyph (each site's biodiversity profile encoded as arc segments around a central dot)
- **What the combination adds:** A plain scatter of 60 sites along a yield vs. management axis shows the trade-off exists, but gives no clue *why* some sites deviate. The glyph encodes the full species breakdown (3 plant groups) per site, so you can immediately see whether a high-yield outlier is also high in woody species or if bryophytes collapse at high management. The combination answers: "Given where a site sits on the yield–management gradient, what does its biodiversity profile look like?"
- **Data manipulation applied:** Normalize species richness per plant group (woody/herbaceous/bryophyte) to a 0–1 scale so arcs are comparable across sites. Optionally compute a composite biodiversity index. Use management index as x-axis, mean yield as y-axis.
- **Marks:** Central dot (one per site); arc segments radiating outward around it (one arc per plant group: woody / herbaceous / bryophyte); arc length proportional to species richness of that group.
- **Channels:** x-position = management intensity (coffee dominance or structure index); y-position = mean coffee yield; arc segment length = species richness per plant group; arc color/hue = plant group identity (categorical: 3 colors); central dot size = total species richness.
- **User task supported:** Spot trade-off, identify outliers, compare sites across yield and management gradient
- **What it shows for our data:** The core yield–biodiversity trade-off across 60 sites, with each site's full species breakdown immediately visible. Reveals whether the trade-off is driven by one specific plant group collapsing under high management.
- **Persona it serves:** Sofia Almeida — directly shows whether high-yield sites have systematically depleted profiles across all plant groups, or if some groups are more sensitive. Also useful for Elena Novak to see which plant group co-varies most with management.
- **Interaction if needed:** Hover on a site to show exact species richness values and site name. Filter by shrub cluster group to highlight which management type each cluster falls into. Click to highlight a single site across all views.
- **Page reference:** p. 156–160 (custom glyph for book circles), adapted to site-level biodiversity profiles

---

### Idea: Yield-sorted Presence/Absence Heatmap with Species Group Bands (inspired by p. 155, 200)

- **Basic visuals combined:** Heatmap (species × sites, presence/absence) + sorted small multiple panels per plant group
- **What the combination adds:** A plain heatmap of 407 species × 60 sites is overwhelming without ordering. Sorting sites by mean yield (x-axis) and grouping species by plant group (row bands) transforms a data dump into a gradient-revealing pattern map. A plain bar chart of species richness per site cannot show *which specific species* are tracking the yield gradient. The combination answers: "Which individual species are systematically associated with high- or low-yield sites?"
- **Data manipulation applied:** Sort sites (columns) by mean coffee yield. Sort species (rows) within each plant group band by their "yield affinity" (average yield of sites where they occur — this variable is already in the dataset). Color encodes presence (1) or absence (0). Add a summary strip at the top (bar: total species richness per site) and a strip at the left (bar: number of sites per species).
- **Marks:** Filled rectangles (cells); bar strip at top; bar strip at left.
- **Channels:** Cell fill color = presence/absence (binary, but can add opacity for frequency); x-position = site sorted by yield (quantitative ordering); y-position = species sorted by yield affinity within group bands; row-band color = plant group (categorical).
- **User task supported:** Spot trade-off, identify individual species patterns, compare across plant groups
- **What it shows for our data:** Which species drop out as yield increases (biodiversity-sensitive indicators), which persist across all sites, and which are only found in high-yield sites. Reveals whether the trade-off is taxonomically concentrated.
- **Persona it serves:** Sofia Almeida — shows exactly which species are sacrificed for yield, with species names visible for advocacy. Elena Novak — reveals which species are most informative indicators of management intensity, informing variable selection for future field studies.
- **Interaction if needed:** Hover on a row to highlight that species across all sites, and show its name + average yield. Click on a column to show that site's full management and yield profile. Filter to show only woody / only herbaceous / only bryophyte rows.
- **Page reference:** p. 155 (tSNE scatter), p. 200 (small multiples with shared axis)

---

### Idea: Beeswarm by Management Intensity with Site Profile Rings (inspired by p. 193–198)

- **Basic visuals combined:** Beeswarm plot (sites clustered along management axis) + concentric ring glyph per site (each ring = one yield year)
- **What the combination adds:** A beeswarm of 60 sites along a management intensity axis shows density and distribution, but a plain dot gives no yield information. A ring glyph where each concentric ring represents one of the 3 years of yield data (radius = yield) shows both the level and the consistency of yield across years. The combination answers: "Along the management gradient, which sites produce reliably high yields vs. which are volatile year-to-year?"
- **Data manipulation applied:** Normalize the 3 annual yield values per site to a common scale for ring radii. Compute year-to-year variance as a derived variable. Use beeswarm force simulation (jitter vertically) to prevent overlap along the management x-axis.
- **Marks:** Central point per site; 3 concentric rings (one per year) drawn at radii proportional to that year's yield; optional outer ring = mean yield.
- **Channels:** x-position = management intensity index; vertical jitter = beeswarm (density); ring radius per year = annual yield; color of rings = year identity (3 categorical colors or sequential years); gap between inner and outer ring = year-to-year variability (visual indicator of volatility).
- **User task supported:** Compare sites, spot yield stability vs. volatility, rank by management intensity
- **What it shows for our data:** Whether highly managed sites produce reliably vs. variably; whether low-management sites are consistently low or occasionally competitive. Also reveals clusters of similar management intensities.
- **Persona it serves:** Hana Abebe — sees at a glance which sites are reliable producers and which have volatile yield, and where those sites fall on the management spectrum. Helps her decide whether to increase management intensity and whether that is likely to stabilize or destabilize yield.
- **Interaction if needed:** Hover to show site name, exact 3-year yields, management values. Filter to highlight sites by shrub cluster group.
- **Page reference:** p. 193–198 (beeswarm along x-axis, channel stacking for context)

---

### Idea: Scrollytelling Biodiversity Story — "The Cost of Coffee" (inspired by p. 177–183)

- **Basic visuals combined:** Scrollytelling dot stream (one dot per site) + small glyph per dot (species breakdown) + narrative text panels
- **What the combination adds:** A static scatter cannot guide a non-expert through the logic of the trade-off. A scrollytelling format lets the visualization transition between layouts on scroll, first showing all 60 sites as undifferentiated dots, then sorting them by yield, then coloring them by management intensity, then showing the biodiversity profile glyphs — building the argument step by step. The combination answers: "Can you walk me through the story of why high-yield sites are ecologically costly?"
- **Data manipulation applied:** Stages: (1) unsorted dots, (2) force-sort along yield axis, (3) reveal management color, (4) expand each dot into a glyph with species rings, (5) zoom in on specific sites for annotation.
- **Marks:** Dots (sites); transitions to glyphs; animated path between positions.
- **Channels:** Position changes with each scroll step; color = management intensity (sequential); glyph segment length = species richness by group; size = total species richness.
- **User task supported:** Explore (guided), spot trade-off, identify key cases
- **What it shows for our data:** The full yield–management–biodiversity story, told progressively so the argument builds for a reader who starts without context.
- **Persona it serves:** Sofia Almeida — a persuasive, emotionally legible narrative for advocacy. The scroll pacing controls the argument and ensures the trade-off is not missed.
- **Interaction if needed:** Scroll triggers layout transitions. Hover on any site (once dots are stable) to see species breakdown. Optional: a "free explore" mode at the end where filters can be applied.
- **Page reference:** p. 177–183 (scrollytelling dot animation for Hamilton lyrics)

---

### Idea: Filter Tool for Species–Site Associations (inspired by p. 173–176)

- **Basic visuals combined:** Interactive filter panel + site map / scatter + species list
- **What the combination adds:** A plain list of 407 species is unworkable. A scatter of sites without species information misses the compositional story. A filter tool where you select one or more plant species and the view highlights only sites where all/any of those species occur — and simultaneously shows those sites' yield and management values — answers: "If I care about species X, which sites protect it, and what are those sites' yield profiles?"
- **Data manipulation applied:** Precompute species × site presence/absence matrix. Filter logic: AND for sites (to find sites that have all selected species), OR for species groups (to broaden selection). Show resulting site subset highlighted on scatter; fade unaffected sites.
- **Marks:** Dots (sites on yield vs. management scatter); species tags in filter panel; highlighted vs. faded visual states.
- **Channels:** Position = yield vs. management; color = selected/unselected state; opacity = filtered in vs. filtered out (partial opacity for non-matching sites).
- **User task supported:** Identify (which sites have this species), explore (what do those sites have in common)
- **What it shows for our data:** Which specific sites harbour rare or sensitive species, and whether those sites are high- or low-yield. Reveals if protecting certain species requires sacrificing yield.
- **Persona it serves:** Sofia Almeida — to identify biodiversity hotspots and argue which specific sites should be protected. Elena Novak — to investigate whether certain indicator species reliably track management or yield gradients.
- **Interaction if needed:** Multi-select species (OR within group, AND between groups mirrors Hamilton filter logic). Dead-end prevention: disable species selections that would result in zero sites. Four visual states per species: selected / occurs-in-current-sites / occurs-in-dataset / absent-from-dataset.
- **Page reference:** p. 173–176 (Hamilton filter tool with AND/OR logic and dead-end prevention)

---

### Idea: Shrub Cluster Profile Comparison — "What makes each cluster" (inspired by p. 155, 197–198)

- **Basic visuals combined:** Radar/spider chart per cluster (showing all 7 morphological shrub variables) + strip of dots showing member sites' yields
- **What the combination adds:** A plain bar chart of cluster means hides within-cluster variability. A yield ranking of sites doesn't show what the shrub clusters look like morphologically. The combination — one radar per cluster, with a strip of yield dots below it for all member sites — shows simultaneously: what the shrub profile of each cluster is, and whether that profile predicts yield. Answers: "Do clusters that look different morphologically also differ in yield, and how large is the within-cluster spread?"
- **Data manipulation applied:** Normalize all 7 shrub variables to 0–1 per variable so radar axes are comparable. Compute cluster centroids. For each cluster panel, place all member sites as dots sorted by yield below the radar.
- **Marks:** Radar polygon (cluster centroid); shaded area (within-cluster range); dots (individual sites) in a strip below.
- **Channels:** Radar axis direction = shrub variable (categorical, 7 axes); radius on each axis = variable value (quantitative); polygon fill opacity = cluster identity; dot x-position in strip = yield rank; dot color = cluster (consistent across panels).
- **User task supported:** Compare clusters, identify cluster structure, spot outliers within cluster
- **What it shows for our data:** Whether the cluster analysis identified meaningfully different shrub morphologies, and whether those morphologies predict yield. Also reveals whether certain clusters are high-variance in yield (unreliable) vs. low-variance.
- **Persona it serves:** Elena Novak — validating cluster structure and assessing whether the 7 shrub variables are capturing meaningful groupings. Hana Abebe — which shrub cluster type is most associated with high yield, and which morphological properties matter.
- **Interaction if needed:** Hover on a site dot to see site name, exact yield, and which shrub variables drive its cluster membership. Toggle between cluster centroid view and individual site profiles.
- **Page reference:** p. 155 (comparing cluster algorithm outputs visually), p. 197–198 (channel stacking for context using remaining free visual channels)

---

### Idea: Annotated Top-N Species Bar Chart — "Yield boosters vs. yield suppressors" (inspired by p. 195–197)

- **Basic visuals combined:** Ranked bar chart (species sorted by yield association) + colored segment breakdown per bar (how many sites that species occurs in, split by high/low yield sites)
- **What the combination adds:** A ranked list of species by average associated yield tells you which species correlate with high yield — but a plain bar doesn't reveal whether that association is driven by many sites or a few. A stacked bar segment showing "occurs in N high-yield sites / M low-yield sites" adds reliability context. Semantically novel: the bar chart is not showing the quantity of a thing, but the ecological profile of a species as a yield predictor. Answers: "Which species are reliably found at high-yield sites (not just one lucky site) and which are indicators of low-yield conditions?"
- **Data manipulation applied:** For each of the 407 species: compute average yield of sites where it occurs (already in dataset) and split site occurrences into "above median yield" vs. "below median yield" counts. Rank species by average associated yield. Trim to top/bottom N (e.g., top 20 and bottom 20) to avoid overwhelming the viewer with all 407.
- **Marks:** Horizontal bars (one per species); stacked segments within the bar.
- **Channels:** Bar total length = average yield of sites where species occurs; stacked segment proportions = fraction of those sites that are high-yield vs. low-yield (green/orange or similar); color hue of bar label = plant group identity; bar position (rank) = yield association strength.
- **User task supported:** Rank (species by yield association), identify (which species are reliable indicators vs. noise)
- **What it shows for our data:** Top 20 species most associated with high-yield sites and bottom 20 most associated with low-yield sites, with reliability shown by the high/low site split in each bar.
- **Persona it serves:** Hana Abebe — which species in her agroforests signal a productive site condition. Sofia Almeida — which species are only found at the low-yield (biodiverse) sites and thus most at risk from yield-focused management.
- **Interaction if needed:** Filter by plant group to show only woody / herbaceous / bryophyte species. Hover to show species name, number of sites, exact average yield.
- **Page reference:** p. 195–197 (add context using remaining visual channels; primary variable should drive the most salient channel)
