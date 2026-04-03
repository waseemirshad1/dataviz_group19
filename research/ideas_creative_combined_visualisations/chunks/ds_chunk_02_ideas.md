# [agent_07] Data Sketches — pages 51-100

## Creative Combined Visualization Ideas

---

### Idea: Site Flower Cluster Map (inspired by p.53–58, Film Flowers)
- **Basic visuals combined:** Scatter plot (sites by yield vs. management intensity) + custom flower glyph per site (encoding species richness per plant group as petal size/number)
- **What the combination adds:** The scatter plot alone shows the yield–management gradient but not what biodiversity looks like at each site. The flower glyph alone shows species richness but not where the site sits in the yield space. Together, a viewer can see whether sites at the high-yield end of the scatter have smaller, simpler flowers (fewer species, less diversity) and sites at the low-yield end have larger, more complex flowers — making the trade-off visible in one unified image.
- **Data manipulation applied:** Species richness per plant group (woody/herbaceous/bryophyte) normalized to comparable scale. Mean yield used rather than 3 individual years, to reduce noise. Management intensity (coffee density or dominance) used as one axis.
- **Marks:** Custom multi-petal flower glyph per site; each petal group represents one plant group (e.g., 3 petal types: woody, herbaceous, bryophyte). Overall flower size = total species richness. Number of petals per group = species count in that group.
- **Channels:** x-position = coffee management intensity (quantitative); y-position = mean coffee yield (quantitative); flower size = total species richness (quantitative); petal group size/length = species richness per plant group (quantitative); petal group color = plant group identity (categorical, 3 colors); position along x–y axes = most important comparison (yield vs. management).
- **User task supported:** Spot trade-off (yield vs. biodiversity), compare sites, identify outliers (sites with both high yield and high richness).
- **What it shows for our data:** Yield × management gradient with species composition as the glyph, across 60 sites.
- **Persona it serves:** Sofia Almeida — directly shows whether high-yield sites (upper right of scatter) have smaller/simpler flowers than low-yield sites. Also serves Hana Abebe for identifying high-performing sites. Semantic novelty: a scatter plot where every data point is itself a structured biodiversity glyph — the data point IS the site profile.
- **Interaction if needed:** Hover over a flower to see site name, exact yield values per year, species richness breakdown per group. Filter by plant group to isolate which group drives the pattern.
- **Page reference:** p.53–58

---

### Idea: Feather Fan of Species per Site (inspired by p.62–76, Olympic Feathers)
- **Basic visuals combined:** Radial/feather chart (sites arranged in a fan) + stacked bar within each feather (species groups per site) + color gradient for yield
- **What the combination adds:** A standard bar chart of species richness per site cannot simultaneously show species group composition AND yield AND site identity in one view. A heatmap of species × sites loses the group breakdown. The feather fan combines all three: each site is one feather, the feather's length = total species richness, the internal stacking = species group composition, and the color = yield level.
- **Data manipulation applied:** Sites sorted by mean yield (low to high) going around the fan. Species richness per group aggregated per site. Yield mapped to a continuous color scale (e.g., green–yellow–brown for ecological intuition, or neutral sequential palette).
- **Marks:** Feather arc per site (one of 60 feathers arranged in a semicircle or full circle); internal stacked colored bands within each feather = species groups; feather length = total species richness.
- **Channels:** Feather length/radius = total species richness (quantitative); internal band width within feather = richness per plant group (quantitative); color hue of feather base or outline = mean yield (sequential quantitative color scale); angular position = site identity sorted by yield (ordinal rank); stacked band color = plant group (categorical, 3 colors).
- **User task supported:** Spot trade-off (do shorter feathers cluster at the high-yield end?), compare biodiversity composition across the yield gradient, identify outlier sites.
- **What it shows for our data:** Whether sites sorted by yield show systematically shorter feathers or different species group compositions.
- **Persona it serves:** Sofia Almeida — makes the trade-off legible and persuasive. Also useful for Elena Novak to see which plant group shrinks most across the yield gradient. Semantic novelty: the feather metaphor, normally used for sports and time (Olympics), here applied to ecological sites where feather "fullness" = ecological richness — a natural metaphor for ecological vitality.
- **Interaction if needed:** Hover a feather to see site name, exact species counts per group, and yield values per year. Click to highlight all sites from a management cluster.
- **Page reference:** p.62–76

---

### Idea: The Yield–Diversity Trade-off Fractal River (inspired by p.78–88, Dive Fractals)
- **Basic visuals combined:** Parallel coordinates chart (sites as lines across multiple variable axes) + fractal/organic line rendering (line texture encodes species composition variability)
- **What the combination adds:** A plain parallel coordinates plot shows correlations between variables but all lines look identical. Adding fractal noise to each line — driven by the within-site species variability data — makes lines from biodiverse sites look "richer" (more varied texture) and lines from managed sites look "smoother" (more uniform). This adds an aesthetic data dimension that reinforces the story without requiring another explicit channel.
- **Data manipulation applied:** Species composition variability per site computed as a dispersion measure (e.g., standard deviation of abundance across species, or Shannon diversity). This scalar is used to seed fractal line noise intensity. Sites sorted by yield for consistent ordering.
- **Marks:** One fractal line per site connecting axes: yield, management intensity, total species richness, shrub cluster group.
- **Channels:** x-position = variable axes (yield / management / species richness / shrub cluster) (categorical axis); y-position on each axis = value on that variable (quantitative); line color = yield level (sequential, low=green, high=brown); line texture/fractal noise intensity = within-site biodiversity variability (quantitative); line opacity = site count in cluster group (fainter for rare cluster patterns).
- **User task supported:** Explore variable correlations, spot trade-off pattern, compare site profiles across all key variables simultaneously.
- **What it shows for our data:** How yield, management, species richness, and shrub cluster co-vary, with biodiversity variability visible in line texture.
- **Persona it serves:** Elena Novak — reveals which variables co-vary and which are independent; shows whether shrub cluster groups separate cleanly in the space. Semantic novelty: parallel coordinates are standard for multivariate analysis, but using fractal texture to encode a fifth variable (within-site variability) within the line itself is unusual.
- **Interaction if needed:** Hover a line to highlight that site and show all its values. Filter axes by clicking to reorder — important for correlation exploration. Filter by cluster group to isolate patterns.
- **Page reference:** p.78–88

---

### Idea: Compressed Species Timeline per Site — Yield as the Axis (inspired by p.92–100, My Life in Vacations)
- **Basic visuals combined:** Sorted strip chart (sites as rows, sorted by yield) + compressed/variable-width columns for species groups (column width proportional to species count in that group per site) + within-column pattern encoding species composition
- **What the combination adds:** A standard heatmap of species × sites shows presence/absence but loses the group structure and yield ranking simultaneously. A grouped bar chart shows group richness per site but not individual species composition. This design compresses or expands the column for each species group based on its richness at that site, so biodiverse sites have wide, textured columns and impoverished sites have narrow, sparse ones — making the gradient visible across the layout itself.
- **Data manipulation applied:** Sites sorted by mean yield (rows). Species richness per group determines column width (not a fixed grid). Individual species presence encoded as texture within each column (dots, lines, or small marks).
- **Marks:** One row per site; within each row, three variable-width rectangular blocks (one per plant group: woody/herbaceous/bryophyte); within each block, small marks (dots or lines) representing individual species present.
- **Channels:** Row position = site rank by yield (ordinal/quantitative); block width = species richness in that group (quantitative); block color = plant group (categorical hue); mark density within block = number of individual species (quantitative, approximate); row color or side annotation = yield value (sequential quantitative); blur/fading on marks = species rarity (present at few sites = faint marks).
- **User task supported:** Spot trade-off (do rows compress toward the top/high-yield end?), identify which plant group is most sensitive, compare composition across yield gradient.
- **What it shows for our data:** Species composition profile across all 60 sites arranged by yield, showing which groups shrink or diversify as yield changes.
- **Persona it serves:** Sofia Almeida — persuasive visual argument that high-yield rows are narrower and sparser. Elena Novak — shows which species group is most systematically affected. Semantic novelty: the "squeezed month" idea from the vacation visualization applied to species groups — empty/impoverished groups shrink visually, making the ecological impoverishment of managed sites literally more compressed in the image.
- **Interaction if needed:** Hover a mark within a block to see species name and how many sites it occurs in. Filter by plant group to focus on one dimension. Click a site row to see detailed yield by year.
- **Page reference:** p.92–100

---

### Idea: Yield-Stability Flower Grid (inspired by p.53–58, Film Flowers + p.92–100 timeline)
- **Basic visuals combined:** Small multiple grid (one cell per site, 60 cells arranged in yield-ranked order) + radar/spider chart within each cell (encoding management variables, species richness, shrub cluster) + year dots inside each cell (3 years of yield as dots showing stability)
- **What the combination adds:** A radar chart per site shows multi-dimensional site profile. A grid arrangement by yield rank shows how profiles change across the yield spectrum. The year dots inside each cell show whether the site's yield is stable or volatile — something that neither the radar nor the grid layout alone can show.
- **Data manipulation applied:** Sites ranked by mean yield. Radar axes: management intensity, coffee density, coffee dominance, total species richness, shrub cluster group (normalized 0–1). Three yield-year values plotted as dots along a vertical mini-strip within each radar.
- **Marks:** Small radar/spider chart per site cell (filled polygon); three dots per cell = 3 years of yield; grid layout of 60 cells.
- **Channels:** Grid position (rank order) = mean yield rank (ordinal); radar axis value = management/biodiversity variable (quantitative, 5 axes); cell fill color = mean yield level (sequential color scale); dot vertical position within cell = yield value per year (quantitative); dot spread/dispersion = year-to-year stability (quantitative derived); radar polygon shape = management-biodiversity profile (multivariate pattern).
- **User task supported:** Compare site profiles across yield gradient; spot what distinguishes top performers from bottom performers; identify whether top-yield sites are reliably high or volatile.
- **What it shows for our data:** How the full site profile (management + biodiversity + shrub structure) changes across the yield spectrum, and whether yield is consistent across years.
- **Persona it serves:** Hana Abebe — directly answers which site conditions are associated with high production and whether high-yield sites are reliable. Elena Novak — shows variable co-variation and cluster structure in a visually rich grid.
- **Interaction if needed:** Hover a cell to expand it and see full variable values, site name, and year-by-year yield data. Filter cells by shrub cluster group to isolate one structural type.
- **Page reference:** p.53–58

---

### Idea: Species × Yield Association Bubble Feathers (inspired by p.62–76, Olympic Feathers)
- **Basic visuals combined:** Bubble chart (species as bubbles, size = number of sites where species occurs) + color encoding = average yield of those sites + arranged in radial feathers by plant group
- **What the combination adds:** A bubble chart of species by yield association shows which species "predict" high yield vs. low yield. Arranging bubbles into feather-shaped groups by plant group reveals whether the high-yield-associated species cluster in one group (e.g., woody species) vs. others, which neither a flat bubble chart nor a bar chart can show simultaneously.
- **Data manipulation applied:** Per species: count of sites where it occurs; mean yield across those sites. Species grouped by plant group (woody tree/shrub/liana, ground herb, epiphyte, moss, liverwort). Within each feather, species sorted from most high-yield-associated (outer) to most low-yield-associated (inner).
- **Marks:** Circle/bubble per species; feather-shaped grouping per plant group (7 feathers).
- **Channels:** Bubble size = number of sites where species occurs (quantitative, prevalence); bubble color = mean yield of sites where species occurs (sequential diverging scale: green=low yield, brown=high yield); radial position within feather = yield association rank (quantitative); feather identity = plant group (categorical, 7 groups); feather length = total number of species in that group (quantitative).
- **User task supported:** Identify which species are associated with high vs. low yield; compare plant groups for yield sensitivity; find rare species (small bubbles) that only occur at high-yield sites.
- **What it shows for our data:** The species × yield link dataset across all 407 species, organized by plant group to reveal ecological patterns.
- **Persona it serves:** Sofia Almeida — shows which species are threatened (found only at low-yield biodiverse sites = outer edge of feather, small bubble). Hana Abebe — shows which species are indicators of high-yield conditions. Semantic novelty: an Olympic-style feather normally encodes sports/athletes over time; here each feather is a plant functional group and each "medal" is a species — the metaphor transfers well from competitive achievement to ecological niches.
- **Interaction if needed:** Hover a bubble to see species name, sites count, and mean yield. Filter to show only rare species (bubble size < threshold). Highlight feathers from one plant group at a time.
- **Page reference:** p.62–76
