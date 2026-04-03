# [agent_04] Cool Infographics — pages 151-200

---

### Idea: Yield–Biodiversity Trade-Off Opposing Bar Chart (inspired by p.183–184)

- **Basic visuals combined:** Back-to-back opposing horizontal bar chart (from sales vs. profit example) + color-saturation gradient encoding
- **What the combination adds:** The opposing bar layout makes it impossible to ignore that the ranking on one metric (yield) is the inverse of the other (species richness). A plain scatterplot shows correlation but not rank inversion; opposing bars make the inversion viscerally readable.
- **Data manipulation applied:** Sort sites by mean coffee yield (descending). For each site: mean yield (left bar, left-extending) and total species richness (right bar, right-extending). Sites are ranked rows.
- **Marks:** Horizontal bars (two per site row, extending in opposite directions from a central site-label axis)
- **Channels:** Left bar length = mean coffee yield; right bar length = total species richness; bar color saturation = management intensity (coffee structure index) — darker = more intensively managed; site label in center = site identity
- **User task supported:** Spot trade-off; rank; compare
- **What it shows for our data:** The yield–biodiversity tension across all 60 sites in a single view. Sites at the top (high yield) have short right bars; sites at the bottom (high biodiversity) have short left bars.
- **Persona it serves:** Sofia Almeida — directly answers "Is the trade-off real and visible?" making it hard to deny. Also serves Hana Abebe — shows which sites are top yield performers and what they sacrifice.
- **Interaction if needed:** Hover over a site row to reveal species group breakdown (woody/herbaceous/bryophytes) as a stacked mini-bar inside the species richness bar; this adds the "which plant group suffers most" detail without cluttering the main view.
- **Page reference:** p.183–184

---

### Idea: Site Profile Glyph — Radial Satellite Circle Map (inspired by p.181–182)

- **Basic visuals combined:** Radial proportional circle diagram (budget poster style) + small multiples per site
- **What the combination adds:** Each site becomes a radial glyph: a central circle (sized by yield) surrounded by satellite circles (sized by species count per plant group). Neither a bar chart nor a scatterplot can show this multi-variable site profile simultaneously.
- **Data manipulation applied:** Normalize yield and species counts to a common scale for circle sizing. Place 60 site-glyphs on a 2D layout sorted by yield (x-axis) or management intensity (y-axis) — this turns the small multiples into a gradient display.
- **Marks:** Circles (central = yield, satellites = species group counts)
- **Channels:** Central circle area = mean coffee yield; satellite circle area = species richness per group (woody/herbaceous/bryophyte = three fixed positions around the center, like a clock); satellite circle color hue = plant group identity; spatial position of glyph = rank by yield or management intensity
- **User task supported:** Compare site profiles; spot trade-off; identify outliers (sites with large center AND large satellites = both high yield and high biodiversity — are there any?)
- **What it shows for our data:** Whether any sites achieve high yield AND high biodiversity simultaneously; which species group shrinks first as yield increases
- **Persona it serves:** Sofia Almeida — "Are there any sites that manage both high yield and high biodiversity?" Elena Novak — reveals dataset structure, outliers, cluster patterns
- **Interaction if needed:** Click a glyph to expand it and show the full species composition for that site; filter by management cluster group to compare groups
- **Page reference:** p.181–182

---

### Idea: Species × Site Heatmap with Yield Gradient (inspired by p.190–192)

- **Basic visuals combined:** 10×10 grid / waffle chart concept (small multiples of binary data) + heatmap sorted by a continuous variable
- **What the combination adds:** Standard heatmap shows presence/absence but does not reveal which species track yield. Sorting columns (sites) by yield and rows (species) by their average yield of sites where they occur reveals yield-tracking species — a pattern invisible in an unsorted matrix.
- **Data manipulation applied:** Sort 60 sites (columns) by mean coffee yield descending. For each of the 407 species: compute average yield of sites where it occurs. Sort species (rows) by that value. Show presence/absence as fill. This creates a structured gradient heatmap where the top-right = species found only in high-yield sites; bottom-left = species found only in low-yield sites.
- **Marks:** Rectangles (one per species × site cell)
- **Channels:** Fill color = presence (colored) vs. absence (grey); column position = site rank by yield; row position = species rank by average yield of occurrence; color hue of filled cell = plant group (woody/herbaceous/bryophyte/epiphyte)
- **User task supported:** Identify; explore; spot trade-off; find outliers
- **What it shows for our data:** Which species are exclusive to high-yield sites, which are exclusive to low-yield sites, and which are ubiquitous (present across all sites regardless of yield)
- **Persona it serves:** Sofia Almeida — "Which specific species are only found at low-yield (biodiverse) sites?"; Elena Novak — reveals co-occurrence structure and which species could serve as yield indicators
- **Interaction if needed:** Hover on a species row to highlight all sites where it occurs and show its average yield; filter by plant group to isolate one taxonomic group at a time
- **Page reference:** p.190–192

---

### Idea: Three-Year Yield Stability Person-Icon Array (inspired by p.193–194)

- **Basic visuals combined:** Isotype/icon array (person icons for literal count) + small multiples per site
- **What the combination adds:** Neither a line chart nor a bar chart makes year-to-year stability intuitively legible. An icon array where each icon represents one year, colored by whether that year's yield was above/below the site mean, makes reliability immediately visible — 3 green icons = stable high; 2 green 1 red = somewhat unstable; etc.
- **Data manipulation applied:** For each site: classify each of the 3 yearly yields as above-mean (site mean), at-mean, or below-mean. Represent as 3 icons per site. Sort sites by mean yield to create a stability-across-yield-gradient view.
- **Marks:** Year-icons (square or leaf-shaped for coffee theme — 3 per site), arranged in small multiples rows
- **Channels:** Icon color = yield category (above/at/below site mean); icon count = number of years (always 3, making sample size visible); row position = site rank by mean yield
- **User task supported:** Compare; identify reliable vs. unreliable sites
- **What it shows for our data:** Whether top-yield sites are consistently high or erratic; whether low-yield sites are stable or variable — answers Hana's "is yield stable across years?"
- **Persona it serves:** Hana Abebe — "Are some sites unreliable producers?"; Elena Novak — "How strongly do the 3 yearly measurements agree? Is the mean a reliable proxy?"
- **Interaction if needed:** None required — the 3-icon array is simple enough to read statically; could add a tooltip showing exact values
- **Page reference:** p.193–194

---

### Idea: Management Gradient Dual Word Cloud (inspired by p.194–195)

- **Basic visuals combined:** Dual word cloud (sentiment split) + species name list filtered by yield group
- **What the combination adds:** A standard species list is unreadable at 407 entries. A word cloud of species names where font size = how many sites the species occurs in, and two clouds are split by yield group (high-yield sites vs. low-yield sites), reveals which species names dominate each regime — a qualitative ecology portrait.
- **Data manipulation applied:** Split species into two groups: species whose average yield of sites of occurrence is above median vs. below median. For each group, build a word cloud where font size = number of sites the species occurs in (frequency, not just presence). Color: warm tones for high-yield species, cool tones for low-yield species.
- **Marks:** Species name text at varying sizes
- **Channels:** Font size = frequency of occurrence (number of sites); color hue = yield association group (warm=high-yield, cool=low-yield); two separate cloud panels = yield regime
- **User task supported:** Identify; explore; spot trade-off
- **What it shows for our data:** Which species are most frequently found in high-yield vs. low-yield agroforests — a qualitative biodiversity portrait of each regime
- **Persona it serves:** Sofia Almeida — visual rhetoric for which species are associated with each farming intensity; provides emotionally legible contrast between "productive" and "biodiverse" species communities
- **Interaction if needed:** Hover on a species name to reveal: how many sites it occurs in, its average yield, and its plant group; this manages the 407-species depth without cluttering the cloud
- **Page reference:** p.194–195

---

### Idea: Shrub Cluster Group Profile Radial Diagram (inspired by p.181–182)

- **Basic visuals combined:** Radial proportional circle diagram + small multiples per cluster group
- **What the combination adds:** A standard radar/spider chart shows a single cluster profile. Using the radial circle approach — where each morphological variable is a satellite circle sized by its mean value within the cluster — makes it possible to compare 4+ cluster groups side by side, and the size differences are more readable than radar polygon areas.
- **Data manipulation applied:** Compute mean of each of the 7 morphological variables per shrub cluster group. Normalise across all groups. Display as one radial glyph per cluster group with 7 satellite circles at fixed positions (like clock hours).
- **Marks:** Central circle (cluster identity), 7 satellite circles (one per morphological variable)
- **Channels:** Central circle color = cluster group identity; satellite circle area = mean variable value within cluster; satellite position (clock position) = variable identity (fixed assignment)
- **User task supported:** Compare; identify cluster distinctiveness; explore variable importance
- **What it shows for our data:** What makes each shrub cluster group structurally distinct — which morphological variables are large vs. small within each group
- **Persona it serves:** Elena Novak — "What is the internal structure of the shrub cluster groups?" Hana Abebe — "Which site conditions are associated with higher production?" (if cluster groups link to yield)
- **Interaction if needed:** Hover over a satellite circle to show the exact mean value and the distribution (min/max) within the cluster; click cluster glyph to highlight all sites belonging to that cluster on a yield-ranked list
- **Page reference:** p.181–182

---

### Idea: Variable Co-Variation Opposing Bar Matrix (inspired by p.183–184, p.190–192)

- **Basic visuals combined:** Back-to-back opposing bar chart + small multiples grid
- **What the combination adds:** A correlation matrix shows pairwise relationships but not direction and magnitude simultaneously in a readable format for a non-statistician. An opposing bar approach per variable pair — where left bars show correlation with yield, right bars show correlation with species richness — reveals which variables are antagonistic (positively correlated with yield, negatively with biodiversity) at a glance.
- **Data manipulation applied:** Compute Pearson or Spearman correlation of each management variable and structural variable with: (1) mean coffee yield, and (2) total species richness. Display as opposing bars — left = correlation with yield, right = correlation with species richness. Color = positive (filled) vs. negative (hatched or opposite color).
- **Marks:** Horizontal bars (two per variable, opposing)
- **Channels:** Left bar length = correlation magnitude with yield; right bar length = correlation magnitude with species richness; bar color = positive (blue/orange) vs. negative correlation (paler/hatched); row = variable identity; center axis = zero correlation
- **User task supported:** Compare; rank variable importance; identify trade-off variables
- **What it shows for our data:** Which variables are the strongest drivers of yield AND which variables simultaneously predict biodiversity loss — the ones with long bars on both sides are the core trade-off variables
- **Persona it serves:** Elena Novak — "Which management variables most strongly co-vary with yield and with biodiversity? Which variables would she prioritise measuring?"
- **Interaction if needed:** Hover to show exact correlation coefficient and sample size; click to show a scatterplot of that variable vs. yield/species richness
- **Page reference:** p.183–184, p.190–192

---

### Idea: Site Yield Profile with Enriched Process-Timeline Style (inspired by p.186, Fig. 5-7)

- **Basic visuals combined:** Enriched timeline with sized circles + small multiples per site
- **What the combination adds:** A simple bar chart shows mean yield per site. Adding circle size = year-to-year variance, color = management cluster, and satellite dots = species richness per plant group on the same horizontal axis turns a single-variable ranking into a six-variable site portrait readable in a ranked sequence.
- **Data manipulation applied:** Rank 60 sites by mean yield. For each site: compute yield variance across 3 years; assign management cluster color; compute species richness per plant group.
- **Marks:** Circles on a horizontal ranked axis (one per site); small satellite dots at fixed positions around each circle
- **Channels:** Circle diameter = yield variance (larger = more variable); circle color hue = management cluster group; horizontal position = yield rank; satellite dot size = species richness per plant group (3 dots, fixed positions); background bar = mean yield (optional, to anchor position)
- **User task supported:** Compare sites; spot outliers (high yield + high variance = risky); identify cluster patterns
- **What it shows for our data:** Which sites are both high-yield AND stable; which sites are high-yield but erratic; where biodiversity is distributed along the yield gradient
- **Persona it serves:** Hana Abebe — combines yield ranking with stability and biodiversity context in one view; Elena Novak — reveals dataset structure and cluster separation
- **Interaction if needed:** Hover over a circle to show exact values for all encoded variables; filter by management cluster to focus on one group
- **Page reference:** p.186

---

### Idea: Species Occurrence × Yield Bar Chart with Biodiversity Context (inspired by p.190–192 waffle grids + p.183–184 opposing bars)

- **Basic visuals combined:** Ranked bar chart (species by average yield of sites where they occur) + 10×10 grid inset showing prevalence
- **What the combination adds:** A plain ranked bar chart of the 407 species by average associated yield answers "which species track high yield?" but gives no sense of how common or rare each species is. Adding a 10×10 mini-grid beside each bar (number of sites filled = occurrence count out of 60) makes both questions answerable simultaneously.
- **Data manipulation applied:** Filter to species occurring in at least 5 sites (reduces to manageable subset). Rank by average associated yield. For each species: show bar = average yield, grid = occurrence rate (n/60 sites, shown as filled squares in a 10×60... simplified to icon count out of 10 where each icon = 6 sites).
- **Marks:** Horizontal bars (one per species); 10-icon mini-grids beside each bar
- **Channels:** Bar length = average yield of sites where species occurs; icon fill in grid = occurrence frequency (out of 60 sites); bar color = plant group identity; grid icon color = same plant group color
- **User task supported:** Rank; identify species most associated with high/low yield; spot rare vs. common species
- **What it shows for our data:** Top species associated with high-yield sites AND how widespread they are — distinguishes "rare yield indicators" from "common yield indicators"
- **Persona it serves:** Hana Abebe — "Which individual species are most strongly associated with high or low yield?"; Sofia Almeida — which species are ubiquitous vs. restricted to biodiverse low-yield sites
- **Interaction if needed:** Hover to show species name in full, plant group, exact occurrence count, exact average yield; filter to show only one plant group at a time
- **Page reference:** p.190–192, p.183–184
