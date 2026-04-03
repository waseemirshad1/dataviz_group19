# Combined Visualization Ideas — Ethiopian Coffee Agroforest Dataset
### Synthesized from 25 chunk files across 5 source books/document sets

**Dataset:** 60 Ethiopian coffee agroforest sites. Each site has: 3-year coffee yield, species richness by plant group (woody/herbaceous/bryophytes/total), presence/absence of 407 plant species, management variables (structure index, density, dominance), 7 shrub morphological variables + cluster assignment, per-species yield association.

**Core tension:** Higher coffee yield is associated with lower plant biodiversity. This trade-off is the central story the visualizations must communicate.

**Three personae:**
- **Hana Abebe** — coffee farmer: compare sites, spot top performers, identify what distinguishes them, check yield stability
- **Sofia Almeida** — biodiversity activist: make the trade-off undeniable, show which species/groups are sacrificed, persuade
- **Elena Novak** — agroecology scientist: correlation structure, cluster validity, variable prioritization, methodological rigor

---

## Table of Contents

1. [Ideas primarily for Hana Abebe](#persona-hana)
2. [Ideas primarily for Sofia Almeida](#persona-sofia)
3. [Ideas primarily for Elena Novak](#persona-elena)
4. [Ideas from real student submissions](#student-reports)

---

<a name="persona-hana"></a>
## Part 1 — Ideas for Hana Abebe (Coffee Farmer)

---

### Idea H-01: Site Performance Dashboard — Ranked Bar with Glyph Profile [SEMANTICALLY NOVEL]
*(sources: ci_chunk_01, ci_chunk_04, ds_chunk_02, ds_chunk_03)*

- **Basic visuals combined:** Ranked horizontal bar chart (sites by yield) + small multivariable glyph (radar or stacked bar) attached to each bar end
- **What the combination adds:** A ranked bar chart shows which sites are strong vs. weak in yield, but not *why*. The glyph at each bar end shows the management profile and shrub cluster simultaneously. Neither alone answers "which sites are top performers AND what do they have in common?" A ranked bar chart alone cannot reveal the structural fingerprint of top performers.
- **Data manipulation applied:** Rank 60 sites by mean 3-year yield. Normalize management variables (structure index, density, dominance) to z-scores for glyph display. Assign shrub cluster color as bar fill (4 categorical colors). Optionally compute biodiversity composition as a stacked mini-bar within the glyph.
- **Marks:** Horizontal bars (one per site), small radar or stacked-bar glyphs at bar end, color-coded by shrub cluster
- **Channels:** Bar length = mean coffee yield (primary; most accurate channel for the primary comparison task); Y-position = yield rank; color hue of bar = shrub cluster group (categorical identity); glyph segment lengths = normalized management variable values; optional: glyph background shade = species richness level
- **User task supported:** Rank, compare, identify what distinguishes top performers
- **What it shows for our data:** Which of the 60 sites are top/bottom performers; whether high-yield sites share a consistent shrub cluster or management profile; which management variables are elevated at top sites
- **Persona it serves:** Hana Abebe (primary) — answers "Which sites are strong vs. weak?" and "Which conditions are associated with higher production?"; secondary: Elena Novak for validating cluster-yield relationship
- **Interaction if needed:** Click any bar to expand to a full site profile (all 7 shrub morphology variables + year-by-year yield stability); hover to show exact yield value and species richness count; filter by cluster group to compare within-cluster rank
- **Page reference:** ci_chunk_01 p.37–38; ci_chunk_04 p.186; ds_chunk_02 p.48–50; ds_chunk_03 p.139–141

---

### Idea H-02: Yield Stability Strip Chart — Three-Year Trajectories per Site [SEMANTICALLY NOVEL]
*(sources: ci_chunk_01, ci_chunk_03, ci_chunk_04, ci_chunk_05, ds_chunk_03, ds_chunk_04, vad_chunk_02)*

- **Basic visuals combined:** Strip/dot plot (sites ranked by mean yield) + sparkline or three-dot connected line per site (showing year-to-year yield trajectory) + optional background color encoding management intensity
- **What the combination adds:** Ranking sites by mean yield answers which sites are strong performers, but hides whether their yield is stable or volatile across the three years. Embedding a 3-point sparkline inside the site strip shows variability without adding a separate chart. A background color gradient adds management intensity without requiring an additional axis. The combination answers: "Which sites are both high-yield AND reliably high year-to-year?" — impossible with either chart type alone.
- **Data manipulation applied:** Compute mean yield and standard deviation across 3 years per site; rank sites by mean yield; flag sites where year-to-year variance exceeds 1 SD as "unreliable"; normalize 3-year yield values per site for sparkline display; optionally encode coffee structure index as row background color saturation.
- **Marks:** Dots (mean yield position on x-axis), small 3-point connected line (sparkline per site), optional colored row background (management intensity)
- **Channels:** X-position = mean yield (primary); Y-position = rank order; sparkline shape = year-to-year trajectory (stable flat vs. volatile); sparkline color = stable (cool) vs. volatile (warm); row background saturation = management intensity (coffee structure index)
- **User task supported:** Compare, rank, identify reliable vs. unreliable producers, spot stability-yield co-variation
- **What it shows for our data:** Which sites are both high-yield AND stable (double winners); which sites have high mean but extreme variance (risky investment for a farmer); whether high-yield sites tend to be more or less stable than low-yield sites
- **Persona it serves:** Hana Abebe (primary) — directly answers "Is yield stable across years, or are some sites unreliable producers?"; secondary: Elena Novak — "How strongly do the 3 yearly measurements agree? Is the mean a reliable proxy?"
- **Interaction if needed:** Hover to reveal the three exact yield values per year; click to see full site profile; filter to show only sites in a selected shrub cluster group; sort toggle between mean yield and yield variance
- **Page reference:** ci_chunk_01 p.19–20; ci_chunk_03 p.132,138; ci_chunk_04 p.186; ci_chunk_05 p.210; ds_chunk_04 p.193–198; vad_chunk_02 p.7–8

---

### Idea H-03: Growth Trajectory Bundles — 3-Year Yield Lines Grouped by Shrub Cluster
*(sources: ci_chunk_02, ds_chunk_05, vad_chunk_04)*

- **Basic visuals combined:** Multi-series line chart (one line per site, 3 points = 3 years of yield) + color-coded grouping by shrub cluster archetype + optional small-multiple faceting by cluster
- **What the combination adds:** A line chart of all 60 sites simultaneously is unreadable without structure. Color-coding by the 4 shrub cluster groups creates readable bundles — the question answered is: "Do certain shrub clusters produce reliably high yield, and are they more stable year-to-year?" Neither the line chart alone nor the cluster color alone provides this.
- **Data manipulation applied:** Normalize year-1 yield to a common starting point within each cluster to compare trajectory *shape* (not absolute level). Alternatively show raw values with a visible per-site range. Cluster assignments come from existing Coffee_structure_index_variables.xlsx cluster analysis.
- **Marks:** Lines (one per site, 3 data points per line = year 1, year 2, year 3); semi-transparent to show bundle shape
- **Channels:** X-position = year (year 1 / year 2 / year 3); Y-position = yield value; color hue = shrub cluster group (4 groups, categorical); line opacity = semi-transparent for individual lines to show bundle; one bold line per cluster = cluster mean trajectory
- **User task supported:** Compare stability across clusters; identify unreliable sites; find which clusters are consistent high producers
- **What it shows for our data:** Whether the 4 shrub cluster groups differ in yield level, trajectory shape, and stability; whether some clusters are more volatile than others
- **Persona it serves:** Hana Abebe (primary) — wants to know which shrub cluster type is the most reliable producer; secondary: Elena Novak — does cluster assignment predict yield stability?
- **Interaction if needed:** Hover a line to highlight that site and show its ID; filter by cluster group checkbox to isolate one group; toggle between raw values and normalized trajectory; show/hide the cluster mean overlay
- **Page reference:** ci_chunk_02 p.59; ds_chunk_05 p.53–58; vad_chunk_04 p.126–128

---

### Idea H-04: Site Glyph Scatter — Scatterplot with Embedded Biodiversity Profile per Point [SEMANTICALLY NOVEL]
*(sources: ds_chunk_01, ds_chunk_04, ds_chunk_05, vad_chunk_03)*

- **Basic visuals combined:** Scatter plot (yield × management intensity as axes) + custom circular glyph per site (arc segments around each point encoding species richness per plant group)
- **What the combination adds:** A plain scatterplot shows where each site sits on the yield-management gradient but gives no clue *why* some sites deviate. The glyph encodes the full biodiversity breakdown per site, so the viewer can immediately see whether a high-yield outlier is also high in woody species or whether bryophytes collapse at high management. The combination answers: "Given where a site sits on the yield-management gradient, what does its biodiversity profile look like?" — something neither chart type alone can do.
- **Data manipulation applied:** Normalize species richness per plant group (woody/herbaceous/bryophyte) to a 0–1 scale for arc comparability across sites; use management intensity as x-axis and mean yield as y-axis; optionally compute a composite management intensity score from structure index + density + dominance.
- **Marks:** Central dot per site; arc segments radiating outward (one per plant group); arc length proportional to species richness of that group
- **Channels:** X-position = management intensity (quantitative); Y-position = mean coffee yield (quantitative); arc segment length = species richness per plant group (quantitative); arc color hue = plant group identity (categorical: 3 colors for woody/herbaceous/bryophyte); central dot size = total species richness
- **User task supported:** Spot trade-off (yield vs. biodiversity), compare sites, identify outliers (sites with both high yield and high richness — are there any?)
- **What it shows for our data:** The core yield-biodiversity trade-off across 60 sites, with each site's full species breakdown visible at a glance; reveals whether any sites achieve both high yield and high richness, and which plant group drives biodiversity variation at high-yield sites
- **Persona it serves:** Hana Abebe (primary) — spots outlier sites with both good yield and biodiversity, informs management decisions; secondary: Sofia Almeida — the trade-off is visible within each point
- **Semantic novelty:** A scatterplot is standard when points are uniform dots. It becomes semantically novel when each point is itself a species composition profile — the position shows where the site sits on the yield-management gradient; the glyph reveals the biodiversity cost at that position.
- **Interaction if needed:** Hover on a site to show exact species richness values and site name; filter by shrub cluster group to see whether one cluster type escapes the trade-off; click to highlight a site across all linked views
- **Page reference:** ds_chunk_01 p.48–50; ds_chunk_04 p.156–160; ds_chunk_05 p.53–58; vad_chunk_03 p.82–83

---

### Idea H-05: Shrub Cluster Radar Portraits — Four Clusters with Yield-Linked Strip
*(sources: ci_chunk_03, ds_chunk_04, vad_chunk_03)*

- **Basic visuals combined:** Radar / spider chart (one per shrub cluster, showing all 7 morphological shrub variables) + shaded band showing within-cluster variability + linked strip of yield dots per cluster below each radar
- **What the combination adds:** A plain bar chart of cluster means hides within-cluster variability. A yield ranking of sites doesn't show what the shrub clusters look like morphologically. This combination shows simultaneously: what the shrub structure of each cluster looks like AND whether that structure predicts yield AND how variable yield is within each cluster. Answers "Do clusters with different shrub architecture also differ in yield, and how cleanly?"
- **Data manipulation applied:** Cluster assignments from Coffee_structure_index_variables.xlsx. Compute mean and range of all 7 morphological variables per cluster. Normalize all variables to 0–1 scale for radar comparability. Compute mean yield and yield distribution per cluster for the strip plot below each radar.
- **Marks:** Radar polygon (cluster centroid profile); shaded area (within-cluster variable range); individual yield dots (all sites in that cluster) in a horizontal strip below
- **Channels:** Radar axis direction = shrub variable identity (categorical, 7 axes); polygon vertex distance = mean variable value (quantitative); shaded band width = within-cluster variability range; dot x-position in yield strip = individual site yield (quantitative); dot color = cluster identity (consistent across all 4 panels)
- **User task supported:** Compare clusters, identify cluster structure, discover which morphological traits associate with higher yield, spot within-cluster variability
- **What it shows for our data:** Whether the cluster analysis identified meaningfully distinct shrub morphologies, and whether the highest-yield cluster has distinctive morphological traits that Hana could target in shrub management
- **Persona it serves:** Hana Abebe (primary) — "Which shrub cluster type is associated with higher production? What morphological properties should I aim for?"; Elena Novak (secondary) — "What is the internal structure of the shrub cluster groups?"
- **Interaction if needed:** Hover on a site dot to see site name, exact yield, and management variables; hover on radar axis to see variable description and within-cluster histogram; toggle between cluster centroid and individual site profiles
- **Page reference:** ci_chunk_03 p.132; ds_chunk_04 p.155, 197–198; vad_chunk_03 p.68–76

---

### Idea H-06: Site Portrait Grid — Small Multiple Radars Sorted by Yield
*(sources: ci_chunk_05, ds_chunk_02, ds_chunk_04, vad_chunk_04)*

- **Basic visuals combined:** Small multiple grid layout (60 cells, one per site) + radar/spider chart per cell (encoding 5–6 key variables: yield, total species richness, coffee density, coffee dominance, coffee structure index) + shrub cluster encoded as background cell color
- **What the combination adds:** A single radar chart per site shows a multi-dimensional profile. Arranging all 60 sites as small multiples sorted by mean yield creates a grid where pattern recognition works across the full dataset. The question answered: "How does the full site profile change as you move from highest to lowest yield?" — neither a ranked list nor a single radar can answer this.
- **Data manipulation applied:** Normalize all variables to 0–1 within the dataset. Sort grid left-to-right, top-to-bottom by descending mean yield. Cell background color = shrub cluster (4 categorical hues). Yield may be excluded from the radar axes and used only as the sort key, or included as one axis.
- **Marks:** Small radar polygons (one per site, 60 total in a 10×6 or 12×5 grid); colored cell backgrounds (cluster group)
- **Channels:** Grid position (yield rank — upper-left = highest yield); polygon shape (the "fingerprint" of the 5–6 variables); polygon fill color (optional hue intensity = yield for visual reinforcement); cell background color = shrub cluster group (categorical)
- **User task supported:** Identify site profiles, spot which variables distinguish top-yield sites from low-yield sites, explore whether cluster group membership correlates with yield rank in the grid
- **What it shows for our data:** Whether the highest-yield sites share a consistent profile shape (e.g., consistently high coffee density + low species richness), suggesting actionable site conditions; whether any yield-quartile band shares a visual "fingerprint"
- **Persona it serves:** Hana Abebe (primary) — can see whether her highest-yield sites share a consistent visual profile; Elena Novak (secondary) — can identify which variables show the strongest visual differentiation between yield groups
- **Interaction if needed:** Hover to reveal site label and all raw variable values; click to isolate and enlarge a single site's radar; filter by shrub cluster group to see whether cluster members share visual profile shapes
- **Page reference:** ci_chunk_05 p.215; ds_chunk_02 p.53–58; ds_chunk_04 p.139–141; vad_chunk_04 p.68–76

---

### Idea H-07: Three-Year Yield Consistency — Small Multiples or Icon Array per Site
*(sources: ci_chunk_04, ds_chunk_05)*

- **Basic visuals combined:** Icon array (3 icons per site = 3 years) + small multiples grid sorted by mean yield
- **What the combination adds:** Neither a line chart nor a bar chart of mean yield makes year-to-year stability intuitively legible. An icon array where each icon represents one year, colored by whether that year's yield was above/below the site's own mean, makes reliability immediately visible — 3 consistent icons = stable producer; mixed icons = unreliable. Sorted by mean yield across the grid, this shows whether top-yield sites are also reliably top.
- **Data manipulation applied:** For each site: classify each of the 3 yearly yields as above-site-mean (green), at-mean (yellow), or below-site-mean (red). Represent as 3 icons per site (leaf-shaped for coffee thematic fit). Sort sites by mean yield.
- **Marks:** Year icons (3 per site, leaf-shaped or square), arranged in small multiples rows or a grid
- **Channels:** Icon color = yield category relative to site mean (above/at/below); icon count = always 3 (makes sample size visible); row/grid position = site rank by mean yield
- **User task supported:** Compare reliability across sites; identify unreliable producers; understand whether top performers are consistently top or just lucky in one year
- **What it shows for our data:** Whether top-yield sites are consistently high or erratic; whether low-yield sites are stable or variable
- **Persona it serves:** Hana Abebe (primary) — "Are some sites unreliable producers?"; Elena Novak (secondary) — "Is the 3-year mean a reliable proxy?"
- **Interaction if needed:** Hover to show exact values for all three years; click to expand full site profile; minimal interaction needed — the 3-icon format is legible statically
- **Page reference:** ci_chunk_04 p.193–194

---

### Idea H-08: LineUp-Style Multi-Attribute Site Ranking with Trade-off Slopes
*(sources: ds_chunk_06, vad_chunk_06, vad_chunk_07)*

- **Basic visuals combined:** LineUp-style multi-attribute horizontal bar chart (one row per site, columns for yield, woody richness, herbaceous richness, bryophyte frequency, structure index) + slope graph between neighboring columns (showing rank changes between attributes)
- **What the combination adds:** Each row is a site; each column encodes a different normalized attribute as a bar. Sorting by yield shows the yield ranking while the other columns reveal how biodiversity and management attributes co-vary. Slope graph connections between the yield column and the total richness column make the trade-off literally visible as crossing slopes — sites that drop dramatically in rank between yield and richness are the most ecologically costly high-yield sites.
- **Data manipulation applied:** Normalize all attributes to 0–1; compute yield rank and richness rank per site; derive "yield-to-richness rank gap" per site as a derived attribute; sort by yield descending.
- **Marks:** Horizontal bar marks (attribute value per column), connecting slope lines between column pairs for same site
- **Channels:** Bar length (normalized attribute value); slope angle (rank change between yield and richness columns); Y-position (current sort rank); color hue (cluster assignment as row background)
- **User task supported:** Compare sites by multiple attributes simultaneously; identify sites with high yield but low biodiversity (large rank drop); explore how ranking changes when weight shifts from yield to richness
- **What it shows for our data:** Top-yield sites visually show short biodiversity bars; crossing slopes between yield and richness columns make the trade-off viscerally visible; outlier sites that maintain biodiversity at high yield stand out immediately
- **Persona it serves:** Hana Abebe (primary) — yield-focused ranking with multi-variable context; Elena Novak (secondary) — correlation between dimensions
- **Interaction if needed:** Sort by any column or weighted combination; weight sliders for composite ranking; filter by cluster; highlight Pareto-optimal sites (high yield AND high biodiversity)
- **Page reference:** ds_chunk_06 p.271–273; vad_chunk_06 p.271–273; vad_chunk_07 p.326–328

---

### Idea H-09: Dynamic Query Site Finder — FilmFinder Pattern for Coffee Sites [SEMANTICALLY NOVEL]
*(sources: vad_chunk_07)*

- **Basic visuals combined:** Dynamic query scatterplot (yield vs. total species richness) + multi-attribute slider panel (yield range, species richness range, cluster checkbox, management variable sliders) + auto-label popout when few sites remain
- **What the combination adds:** Browsing sites by attribute ranges with immediate visual feedback is far better than typed queries when exploring an unknown dataset. Sliders let Hana ask "Show me sites with yield above X, species richness above Y, in cluster Z" and immediately see which sites qualify. Scented widget histograms embedded in the slider tracks show where data concentrates before the slider is moved, guiding the user to meaningful thresholds. When few sites remain, those sites auto-label themselves.
- **Data manipulation applied:** Precompute histograms of each attribute for slider backgrounds (scented widgets); compute auto-label trigger threshold (fewer than ~8 sites visible = names appear); precompute yield × richness scatter positions.
- **Marks:** Points (one per site in scatterplot), tiny bar marks within slider tracks (attribute histogram), text labels on auto-triggered sites
- **Channels:** Scatterplot H-position = yield; scatterplot V-position = richness; color hue = cluster; auto-size (sites grow when fewer than ~10 remain); bar height in slider = data density cue
- **User task supported:** Find sites meeting multiple criteria simultaneously; identify top performers within filtered subgroup; browse unknown dataset without prior knowledge of value ranges
- **What it shows for our data:** Which specific sites simultaneously achieve Hana's criteria; how few or many sites exist in a desirable region of the yield-biodiversity space
- **Persona it serves:** Hana Abebe (primary) — guided multi-variable filtering without requiring data expertise
- **Semantic novelty:** Using the FilmFinder/scented-widget movie-browser pattern in an agricultural ecology context is semantically novel — sites play the role of movies, yield plays the role of rating, cluster plays the role of genre.
- **Interaction if needed:** Dual-range sliders with embedded histograms for yield, species richness, structure index; checkboxes for cluster groups; alpha sliders for management variables; popup detail view on site click
- **Page reference:** vad_chunk_07 p.326–328

---

### Idea H-10: Participation-Style Farmer Ranking Board — "Where Do I Stand?"
*(sources: ds_chunk_09)*

- **Basic visuals combined:** Dot-plot / strip chart (all 60 sites ranked by yield with management variable context) + interactive user-placed marker layer (the user places "my site" marker)
- **What the combination adds:** The base chart shows all 60 sites ranked by yield with management variable profiles. The user can mark which site management strategy they currently use or aspire to. The visualization then shows: "Where do I stand relative to top performers, and what would I need to change?" — answering Hana's practical question by making her situation personally situated within the comparative view.
- **Data manipulation applied:** Rank sites by mean yield; compute normalized management variable profiles for context dots around each site mark; assign sites to yield quartile bands (background color regions); pre-compute "next cluster up" profile for the recommendation panel.
- **Marks:** Dots (sites on vertical yield axis), user-placed glyph (distinct shape that the user drags to their site), yield quartile background bands
- **Channels:** Y-position = yield rank; color hue = management cluster; size = species richness; user marker = distinct symbol and color; background bands = yield quartile identity
- **User task supported:** Compare (where am I vs. top performers); identify (which cluster am I in); explore (what management variables distinguish my cluster from higher-yield clusters)
- **What it shows for our data:** Bridges the abstract dataset to personal relevance for a farmer — situates their site within the distribution and shows the management gap to top performers
- **Persona it serves:** Hana Abebe (exclusively) — designed for the practical farming decision context
- **Interaction if needed:** User selects their current management cluster; a panel shows the management profile of top performers in the next cluster up; optional: species list associated with that cluster
- **Page reference:** ds_chunk_09 p.409, 421

---

### Idea H-11: Scrollytelling Yield Journey — Site Portraits Revealed in Steps
*(sources: ds_chunk_03, ds_chunk_04)*

- **Basic visuals combined:** Scrollytelling narrative + site circles that progressively reveal additional variable layers as the viewer scrolls
- **What the combination adds:** A static visualization of all 60 sites with all variables visible at once overwhelms a non-data-expert viewer like Hana. Scrollytelling introduces one variable layer at a time: (1) plain circles sorted by yield, (2) management intensity revealed as size, (3) species richness revealed as opacity, (4) shrub cluster revealed as color, (5) outlier sites annotated by name. Each section is legible on its own; the full picture emerges progressively without requiring the viewer to decode a complex chart cold.
- **Data manipulation applied:** Normalize each variable to 0–1 for consistent encoding across scroll steps; pre-compute which sites are "outliers" that escape the trade-off (above-average on both yield and richness) for the annotation layer.
- **Marks:** Circles (one per site, consistent mark across all sections — only channels are added/changed per section)
- **Channels (accumulated across scroll):** X-position = mean yield (constant throughout); Y-position = species richness (introduced at step 3); size = management intensity (step 2); color hue = shrub cluster (step 4); opacity = outlier flag (step 5)
- **User task supported:** Explore and be guided; compare; identify trade-off; spot outliers — with narrative pacing that controls complexity
- **What it shows for our data:** The full multi-dimensional picture of 60 sites, built up one variable at a time so the viewer understands each layer before the next is added
- **Persona it serves:** Hana Abebe (primary) — she needs to see which site conditions associate with higher production, but she is not a data analyst; secondary: general audience introduction
- **Interaction if needed:** After the narrative, a final free-exploration mode allows hover for site details and filter by cluster group
- **Page reference:** ds_chunk_03 p.137–143; ds_chunk_04 p.177–183

---

<a name="persona-sofia"></a>
## Part 2 — Ideas for Sofia Almeida (Biodiversity Activist)

---

### Idea S-01: Diverging Bar Chart — Yield vs. Biodiversity per Site (The Butterfly Spine) [SEMANTICALLY NOVEL]
*(sources: ci_chunk_01, ci_chunk_03, ci_chunk_04, ec_chunk_01)*

- **Basic visuals combined:** Diverging horizontal bar chart (left bars = biodiversity, right bars = yield) + color gradient on bars encoding management intensity
- **What the combination adds:** A diverging bar chart where each row is one site, left bars extend to show total species richness, right bars extend to show mean yield, makes the trade-off structure literally visible as a visual divergence. Sites with long left bars (high biodiversity) tend to have short right bars (lower yield). A color gradient on each bar (management intensity) adds the third dimension — showing that management is the mechanism driving the divergence. No single standard chart achieves all three simultaneously. The opposing bar directions make the relationship spatially undeniable.
- **Data manipulation applied:** Normalize yield and species richness to the same 0–100 scale so bar lengths are visually comparable. Sort rows by yield (ascending left to right), so the pattern of inversion reads naturally. Assign each site to a management intensity tier (low/medium/high) for the bar color encoding.
- **Marks:** Horizontal bars (two per site row, extending in opposite directions from a central axis labeled with site ID)
- **Channels:** Left bar length = total species richness (biodiversity); right bar length = mean yield; central axis = site identity; color hue of bar = management intensity tier (cool = low intensity, warm = high intensity); Y-position = site rank by yield
- **User task supported:** Spot trade-off, compare, identify sites that break the pattern (both bars moderately long = "sweet spot" sites)
- **What it shows for our data:** The yield–biodiversity trade-off as a structural visual inversion across all 60 sites; whether management intensity consistently tracks the trade-off; outlier sites that have above-average on both sides
- **Persona it serves:** Sofia Almeida (primary) — makes the trade-off "visible and hard to deny"; the diverging structure is emotionally legible and argumentatively strong; Hana Abebe (secondary) — shows which management tier tends to produce high yield
- **Semantic novelty:** Opposing bar directions encode the trade-off as a spatial structure rather than a correlation coefficient — making it undeniable without requiring statistical literacy.
- **Interaction if needed:** Hover to reveal site name, exact yield, exact species richness, and management variables; click to drill into full species composition; toggle to show only one plant group's richness on the left bar (to reveal which group drives the pattern)
- **Page reference:** ci_chunk_01 p.29–32; ci_chunk_03 p.141; ci_chunk_04 p.183–184; ec_chunk_01 p.2

---

### Idea S-02: Biodiversity Gradient Heatmap — Species × Sites Sorted by Yield [SEMANTICALLY NOVEL]
*(sources: ci_chunk_01, ci_chunk_02, ci_chunk_04, ds_chunk_01, ds_chunk_04, vad_chunk_02, vad_chunk_04)*

- **Basic visuals combined:** Presence/absence heatmap (407 species rows × 60 site columns) + yield gradient color bar along the top column axis + plant group color strip on the left row margin
- **What the combination adds:** A plain presence/absence matrix is a pattern-finding tool but gives no context about what drives the pattern. Sorting columns (sites) by ascending yield and adding a color-gradient bar at the top turns a static matrix into a gradient-revealing story. Sorting species rows by their own yield affinity (the mean yield of sites where each species occurs — already in the dataset) creates a diagonal structure: high-yield-associated species cluster top-right, low-yield-associated species cluster bottom-left. Neither the matrix alone nor the gradient bar alone makes this species-tracking-yield pattern visible.
- **Data manipulation applied:** Sort 60 sites (columns) by mean coffee yield. For each of 407 species (rows), use the pre-existing "average yield of sites where species occurs" from the species×yield link dataset to derive a yield-association rank. Sort rows by this rank. Add a color-gradient strip at the top (site yield level). Add a plant group color band on the left margin (woody/herbaceous/bryophyte). Presence = colored (by plant group), absence = grey.
- **Marks:** Filled rectangles (presence cells); color-gradient header strip; left-margin plant group color band
- **Channels:** Cell fill = presence vs. absence (binary); column position = site ranked by yield (ordinal left = low, right = high); row position = species yield-association rank; header strip color saturation = site yield level; left-margin color hue = plant group (categorical)
- **User task supported:** Identify which species track the yield gradient vs. which are ubiquitous; spot community composition changes; find species exclusive to low-yield (biodiverse) sites
- **What it shows for our data:** Which species are exclusively found at low-yield sites (they form a visible cluster in the bottom-left of the matrix, disappearing as columns move right); which plant group has the most species sensitive to the yield gradient
- **Persona it serves:** Sofia Almeida (primary) — answers "Which specific species are only found at low-yield (biodiverse) sites?" and "Which plant group is most sensitive to management intensity?"; Elena Novak (secondary) — answers "Which species would be the best indicators to measure in a new field study?"
- **Semantic novelty:** A heatmap is standard when rows and columns are arranged arbitrarily. It becomes semantically novel when columns are sorted by the yield gradient and rows by species-yield association — the sort order transforms a data dump into a biodiversity gradient story. The diagonal structure is the scientific argument.
- **Interaction if needed:** Hover over a cell to show species name, plant group, site yield, and species occurrence count; click a species row to highlight all sites where it occurs; filter by plant group to reduce rows to one group; persistent mini-map overview panel for navigation when zoomed in
- **Page reference:** ci_chunk_01 p.29–31; ci_chunk_02 p.79; ci_chunk_04 p.190–192; ds_chunk_01 p.28–43; ds_chunk_04 p.155; vad_chunk_02 p.50–53; vad_chunk_04 p.146

---

### Idea S-03: Stacked Area Chart of Biodiversity Over the Yield Gradient — Species Group Sensitivity [SEMANTICALLY NOVEL]
*(sources: ci_chunk_03, ds_chunk_05, ds_chunk_09, vad_chunk_04)*

- **Basic visuals combined:** Stacked bar or stacked area chart (species richness by group) + yield gradient as the horizontal axis + optional smoothed streamgraph rendering
- **What the combination adds:** Sites sorted along the x-axis by yield (low to high), with stacked bars or flowing area shapes showing species richness by plant group at each site position. The combination answers: "As yield increases across sites, do all plant groups decline together or at different rates, and which group collapses first?" A plain bar chart of total richness loses the group breakdown; a line chart of group richness loses the site-by-site detail.
- **Data manipulation applied:** Sort 60 sites by mean coffee yield. For each site, compute species richness per plant group (woody / herbaceous / bryophyte). Express as stacked bars (absolute richness) or as a streamgraph normalized to proportions. Optionally: apply LOESS smoothing to each group's richness curve to reveal the trend rather than individual site noise.
- **Marks:** Stacked vertical bars (one per site, 60 total) OR flowing ribbon areas (streamgraph); color bands within each for plant groups
- **Channels:** Horizontal position = yield rank (low → high); bar height / area width = species richness of each plant group; color hue = plant group (woody = brown/green, herbaceous = light green, bryophyte = grey-blue); stacked segment height = richness per group
- **User task supported:** Spot trade-off; identify which plant group is most sensitive; find threshold points where richness drops sharply
- **What it shows for our data:** Whether total and group-specific biodiversity systematically declines as yield increases; whether any plant group shrinks faster (e.g., bryophytes collapse while woody plants remain stable); whether the trade-off is gradual or threshold-based
- **Persona it serves:** Sofia Almeida (primary) — directly answers "Do high-yield sites have lower species richness?" and "Which plant group is most sensitive to management intensity?"; Elena Novak (secondary) — which management gradient shows the strongest biodiversity response?
- **Semantic novelty:** A stacked bar chart is standard when bars show quantities within categories. It becomes semantically novel when the x-axis is a yield gradient (not a categorical group label), transforming a static bar chart into a gradient story about ecological sensitivity.
- **Interaction if needed:** Hover over a bar/position to see site ID, exact species counts per group, and management variable values; filter by plant group to isolate one color band; toggle between stacked absolute and normalized proportion view
- **Page reference:** ci_chunk_03 p.138–140; ds_chunk_05 p.239–241; ds_chunk_09 p.305–307; vad_chunk_04 p.153–155

---

### Idea S-04: Monroe's Motivated Sequence — Persuasive Infographic for Advocacy
*(sources: ci_chunk_02)*

- **Basic visuals combined:** Structured narrative layout (persuasive 5-section sequence) + large number callout + scatter plot (yield × total richness) + grouped bar breakdown per plant group + species list
- **What the combination adds:** The Monroe's Motivated Sequence structure (Key Message → Problem → Danger → Solution → Call to Action) is a design skeleton that organizes multiple chart types into a persuasive argument. No single chart type creates a call to action alone. The structure turns data visualizations into an advocacy narrative designed for presentation to funders, policymakers, or the public.
- **Data manipulation applied:** (1) KEY MESSAGE — one large number: "42% fewer species at high-yield sites"; compute from dataset means. (2) PROBLEM — scatterplot of all 60 sites (yield × total richness). (3) DANGER — horizontal bars comparing mean richness per yield tercile for each plant group (shows which group loses most). (4) SPECIES AT RISK — top 10 species found only at low-yield sites (species name + site count). (5) CALL TO ACTION — annotated map of which sites need protection.
- **Marks:** Large number callout; scatter dots; horizontal bars; species text list
- **Channels:** Dot position (yield × richness); dot color (management intensity tercile); bar length (species count per group); bar color (plant group); bold text emphasis (key numbers)
- **User task supported:** Follow argument; identify at-risk species; be persuaded to act
- **What it shows for our data:** The full trade-off narrative from headline fact to species-level evidence to policy implication in a single page or slide sequence
- **Persona it serves:** Sofia Almeida (exclusively) — she uses visuals to argue a case; this is built for presentation to an advocacy audience and does not require data literacy
- **Interaction if needed:** Static format preferred — designed for print/presentation; if interactive, hover on scatter dots to see site name
- **Page reference:** ci_chunk_02 p.85–86

---

### Idea S-05: Radial Wheel of Species by Yield Association [SEMANTICALLY NOVEL]
*(sources: ci_chunk_01)*

- **Basic visuals combined:** Radial category wheel (angular sectors = plant groups) + magnitude encoding via radial distance from center (= mean yield of sites where species occurs) + dot size encoding (= number of sites species occurs in)
- **What the combination adds:** The standard radial wheel groups items by category but does not encode a second quantitative variable. By placing each species at a radial distance proportional to the average yield of sites where it occurs, the wheel simultaneously shows: (1) which plant group each species belongs to (angular sector = color), (2) how strongly that species is associated with high or low yield (radial distance), and (3) how common or rare the species is (dot size). Neither a plain categorical wheel nor a simple scatter achieves all three together.
- **Data manipulation applied:** Use the species×yield link dataset directly. For each of 407 species: compute mean site yield and site count. Filter to species occurring in at least 3 sites to avoid noise from singletons. Group by plant group (4–5 categories = angular sectors). Sort species within each sector by radial position.
- **Marks:** Dots (each dot = one species); sector wedge areas (plant group background)
- **Channels:** Angular sector = plant group (categorical); radial distance from center = mean yield of sites where species occurs (quantitative); dot size = number of sites species occurs in (quantitative, rarity vs. ubiquity); color hue = plant group (redundant with sector position for clarity at the boundary)
- **User task supported:** Identify which species are associated with high vs. low yield; compare plant groups by their yield association distribution; find species that are both widespread and yield-associated (large dots in outer ring)
- **What it shows for our data:** Which plant groups contain species most strongly associated with high or low yield; whether there are common species (large dots) that are also yield-associated (outer ring); which rare species occur only in high-yield sites (small dots, far out)
- **Persona it serves:** Sofia Almeida (primary) — "Which species are only found at low-yield biodiverse sites?" (innermost dots of each sector); Hana Abebe (secondary) — "Which species are most strongly associated with high yield?"
- **Semantic novelty:** A radial wheel is standard when it groups items categorically by sector. It becomes semantically novel when radial distance encodes an ecological association gradient — turning a static category display into a yield-association map.
- **Interaction if needed:** Hover over any dot to reveal species name, plant group, site count, and mean yield; toggle plant groups on/off; click a species dot to highlight the 60-site strip and show which sites contain it
- **Page reference:** ci_chunk_01 p.47

---

### Idea S-06: Site Flowers — Biodiversity Profile Glyphs Arranged by Yield Gradient
*(sources: ds_chunk_01, ds_chunk_02, ec_chunk_01)*

- **Basic visuals combined:** Flower glyph per site (petal length = species richness per plant group) + ranked or scatter layout (sorted by yield)
- **What the combination adds:** A flower glyph where petal length encodes species richness per plant group, and overall flower size encodes mean yield, allows 60 sites to be compared simultaneously as a gallery. Arranged in order of increasing yield, the gallery answers: "Do flowers become thinner and smaller as yield increases?" This makes the biodiversity-yield trade-off emotionally legible — wilting flowers at the high-yield end of the gallery.
- **Data manipulation applied:** Compute species richness per plant group (woody / herbaceous / bryophyte) per site. Normalize richness within each group for petal size comparability. Scale overall flower radius to mean coffee yield. Sort 60 flowers left-to-right (or in a grid) by ascending yield.
- **Marks:** Petal shapes (one per plant group per site); central circle (yield); grid cells (one per site)
- **Channels:** Petal length/radius = species richness per plant group; petal color hue = plant group (3 categorical colors); central circle size = mean coffee yield; position in gallery = yield rank
- **User task supported:** Compare biodiversity profiles across all sites; spot the trade-off visually; identify which plant group drives biodiversity variation; find outlier sites (large flower WITH large center)
- **What it shows for our data:** High-yield sites at the right of the gallery should appear as small central circles with short petals — visually "impoverished." Low-yield sites at the left should appear as full, richly-petalled flowers. The trade-off becomes a visual gallery of ecological vitality.
- **Persona it serves:** Sofia Almeida (primary) — the metaphor is persuasive and emotionally resonant for an activist audience; also useful for a general public presentation; Hana Abebe (secondary) — can spot which sites have both productive and diverse profiles
- **Interaction if needed:** Hover to reveal site name, exact yield, and species counts per group; filter by management intensity cluster
- **Page reference:** ds_chunk_01 p.44–50; ds_chunk_02 p.53–58; ec_chunk_01 p.2

---

### Idea S-07: Yield–Biodiversity Climate Stripes [SEMANTICALLY NOVEL]
*(sources: ec_chunk_01)*

- **Basic visuals combined:** Climate stripes encoding + yield-ranked site ordering
- **What the combination adds:** Each vertical stripe = one of the 60 sites, ordered left-to-right by ascending coffee yield. Stripe color encodes deviation of total species richness from the dataset mean: dark green = far above average richness, dark brown = far below. The combination asks: "As yield increases from left to right, do the stripes turn from green to brown?" If the trade-off is real, they do. No axes are needed — the image is self-explanatory and emotionally legible as a "before/after" ecological narrative.
- **Data manipulation applied:** Rank 60 sites by mean coffee yield. Compute deviation of total species richness from the dataset mean. Map deviation to a diverging color scale (green–white–brown).
- **Marks:** Vertical rectangles (one per site, equal width, filling the frame)
- **Channels:** Position x = yield rank (ordinal, left = low, right = high); color hue = direction of richness deviation (green = above mean, brown = below); color saturation = magnitude of deviation
- **User task supported:** Identify trade-off trend; spot outliers; communicate to non-technical audiences
- **What it shows for our data:** A single striking image confirming or complicating the yield-biodiversity trade-off narrative; exceptional sites appear as isolated "wrong color" stripes at either end
- **Persona it serves:** Sofia Almeida (primary) — the most accessible persuasive visual for non-technical advocacy; the format requires no chart literacy
- **Semantic novelty:** Climate stripes encode time on the x-axis — applying this to yield rank instead of year creates a new semantic role: the gradient communicates management intensification rather than temporal warming. The same visual language carries a different ecological argument.
- **Interaction if needed:** Click a stripe to reveal site details (name, cluster, management variables); minimal interaction needed for the persuasive static version
- **Page reference:** ec_chunk_01 p.2

---

### Idea S-08: Feather Fan of Species per Site — Radial Fullness Encodes Biodiversity
*(sources: ds_chunk_02)*

- **Basic visuals combined:** Radial feather chart (one feather arc per site, 60 feathers arranged in a fan) + internally stacked colored bands (species groups) + feather color encoding yield level
- **What the combination adds:** Each site is one feather arranged in a semicircle or full circle, sorted by yield. Feather length = total species richness; internal bands = species group composition; feather color = yield level. The combination answers: "Do shorter, duller feathers cluster at the high-yield end of the fan?" A standard bar chart of species richness per site cannot simultaneously show species group composition AND yield AND site identity in a single unified form.
- **Data manipulation applied:** Sort sites by mean yield (angular position in the fan, low to high). Species richness per group aggregated per site. Yield mapped to a continuous color scale (green-yellow-brown).
- **Marks:** Feather arc per site (60 feathers); internal stacked colored bands (species groups); feather tip = total richness endpoint
- **Channels:** Feather length/radius = total species richness; internal band width = richness per plant group (stacked); feather base or outline color = mean yield (sequential); angular position = site rank by yield; stacked band color hue = plant group (categorical)
- **User task supported:** Spot trade-off (shorter feathers at high-yield end); compare biodiversity composition; find outlier sites
- **What it shows for our data:** Whether sites sorted by yield show systematically shorter feathers or different plant group compositions; which group shrinks most at the high-yield end of the fan
- **Persona it serves:** Sofia Almeida (primary) — persuasive and visually distinctive for advocacy; Elena Novak (secondary) — which plant group shrinks most across the yield gradient
- **Semantic novelty:** An Olympic-style feather chart normally encodes sports performance over time; here each feather is a site and "fullness" = ecological richness — a natural metaphor for ecological vitality applied to agroforest data.
- **Interaction if needed:** Hover a feather to see site name, exact species counts per group, and yield values; click to highlight all sites from a management cluster
- **Page reference:** ds_chunk_02 p.62–76

---

### Idea S-09: Cumulative Species Accumulation Curves by Yield Quartile
*(sources: ec_chunk_01)*

- **Basic visuals combined:** Cumulative line chart (species accumulation curve) + multi-group overlay (one line per yield quartile)
- **What the combination adds:** X-axis = sites added one by one (ordered within each quartile by species richness). Y-axis = cumulative total species count. Four lines (one per yield quartile). The slope of each line reveals how quickly new species appear as more sites are added — how species-rich AND how compositionally unique each yield group's sites are. This reveals: "Do low-yield sites hold disproportionate species diversity that cannot be found elsewhere?" — a key conservation argument.
- **Data manipulation applied:** Divide 60 sites into four yield quartiles using mean coffee yield. Within each quartile, order sites by total species richness (ascending). Compute cumulative unique species count as sites are added one by one.
- **Marks:** Lines (four, one per quartile, on shared axes)
- **Channels:** X-position = number of sites added; Y-position = cumulative unique species count; color hue = yield quartile (light to dark, low to high yield); line slope = rate of new species per site added
- **User task supported:** Compare species accumulation rates across yield groups; identify whether low-yield sites hold disproportionate biodiversity; support conservation prioritization of specific site types
- **What it shows for our data:** If the low-yield quartile line rises steeply and plateaus late, those sites are compositely diverse — each adds unique species. If the high-yield quartile line rises quickly then flattens, those sites share the same impoverished community.
- **Persona it serves:** Sofia Almeida (primary) — biodiversity argument for low-yield site conservation; Elena Novak (secondary) — species accumulation curves are a standard ecological analysis tool for field study design
- **Interaction if needed:** Toggle individual quartile lines on/off; hover to see which site is being added at each step; shift view to show only a single plant group's accumulation
- **Page reference:** ec_chunk_01 p.1

---

### Idea S-10: "Underskin"-Style Site Structure — Multilayer System Map as Small Multiples
*(sources: ci_chunk_01)*

- **Basic visuals combined:** Thematic layer diagram (inspired by Underskin subway map) + small multiples of 5 selected sites across the yield spectrum
- **What the combination adds:** One canonical site diagram shows the layers of the agroforest (canopy / coffee shrub layer / ground layer / bryophyte layer), with colored lines for each plant group running through the layers. Management intensity appears as a background shade overlay. Showing this as small multiples for 5 sites selected across the yield spectrum answers: "How does the layer composition of the agroforest visually change from a low-yield (diverse, multi-layered) to a high-yield (simpler, management-dominated) site?" — neither a bar chart nor a scatter can show this structural narrative.
- **Data manipulation applied:** Select 5 representative sites: one from each yield quintile. For each site: compute species richness per plant group per canopy layer (requires grouping species by known canopy layer affinity). Compute management intensity score. Assign to yield quintile.
- **Marks:** Lines (plant group "routes" through the site layers); nodes (species abundance peaks); rectangles (management intensity overlay)
- **Channels:** Color hue = plant group (categorical); line thickness = relative abundance/frequency; vertical position = canopy layer (top = canopy, bottom = ground/bryophyte); background shade = management intensity
- **User task supported:** Explore community structure; compare across yield gradient; see how biological layers change with management
- **What it shows for our data:** Whether low-yield sites have a richer multi-layered agroforest structure while high-yield sites are simplified to the coffee shrub layer with a depleted canopy and ground layer
- **Persona it serves:** Sofia Almeida (primary) — makes community composition change "visible and hard to deny" across a yield gradient; the structural metaphor is compelling for advocacy
- **Interaction if needed:** Interactive version allows selecting any of the 60 sites and sliding along the yield axis to animate the layer composition change; static version works with 5 fixed sites
- **Page reference:** ci_chunk_01 p.33–34

---

### Idea S-11: Scrollytelling "The Cost of Coffee" — Dot Stream Narrative
*(sources: ds_chunk_04, ds_chunk_05)*

- **Basic visuals combined:** Scrollytelling dot stream (one dot per site, 60 total) + progressive layout transitions (unsorted → yield-sorted → colored by management → expanded into glyphs with species rings) + narrative text panels at each stage
- **What the combination adds:** A static scatter cannot guide a non-expert through the logic of the trade-off. The scrollytelling format lets the visualization transition between layouts on scroll, building the argument step by step. Each step is legible before the next is added. The combination answers: "Can you walk me through the story of why high-yield sites are ecologically costly?" — guiding the viewer through the cognitive operations needed to understand the trade-off.
- **Data manipulation applied:** Same 60 sites throughout; each scroll step uses the same marks but changes their positions, colors, and sizes; transitions are animated to maintain object constancy.
- **Marks:** Dots (consistent throughout); transitions to glyphs with species rings in later sections; animated paths between positions
- **Channels (changing per step):** Step 1 = uniform gray dots; step 2 = sorted along yield axis; step 3 = colored by management intensity (sequential); step 4 = expanded into glyphs with species richness rings; step 5 = annotation of outlier sites
- **User task supported:** Explore (guided); spot trade-off; identify key cases; follow a persuasive argument
- **What it shows for our data:** The full yield-management-biodiversity story, told progressively so the argument builds for a reader starting without context
- **Persona it serves:** Sofia Almeida (primary) — a persuasive, emotionally legible narrative for advocacy; the scroll pacing controls the argument and ensures the trade-off is not missed
- **Interaction if needed:** Scroll triggers layout transitions; hover on any site (once positions are stable) to see species breakdown; optional "free explore" mode at the end
- **Page reference:** ds_chunk_04 p.177–183; ds_chunk_05 p.92–100

---

### Idea S-12: Opacity-Gradient "Fading Out" Scatterplot [SEMANTICALLY NOVEL]
*(sources: ds_chunk_03)*

- **Basic visuals combined:** Scatterplot (management intensity × yield) + inverted opacity encoding for species richness
- **What the combination adds:** In a standard scatterplot, opacity is used for depth or density control. Here, opacity is inverted as a rhetorical device: sites with high species richness (the most biodiversity-valuable sites) are rendered most transparent — they literally fade into the background. Sites with low biodiversity and high yield are fully visible and dominant. The chart literally shows biodiversity being "faded out" by intensification — making the trade-off emotionally and rhetorically powerful beyond what an analytical chart achieves.
- **Data manipulation applied:** Sites normalized for yield and species richness. Opacity derived from species richness (high richness = low opacity — fully inverted). Color hue encodes management intensity cluster.
- **Marks:** Circles (one per site)
- **Channels:** X-position = management intensity (composite score); Y-position = mean yield; opacity = species richness (inverted — more biodiverse sites are MORE transparent); color hue = shrub cluster group; size = total number of plant species present
- **User task supported:** Spot trade-off; identify what is lost; emotionally engage with the biodiversity cost
- **What it shows for our data:** As management intensity and yield increase, the richest biodiversity sites visually vanish from the chart — the visualization argues the case rhetorically rather than analytically
- **Persona it serves:** Sofia Almeida (primary) — the inverted opacity is a persuasive rhetorical device intended for advocacy presentations
- **Semantic novelty:** Standard scatterplots use opacity for depth or density control. Using *inverted* opacity as a narrative device — where higher ecological value makes a site *less* visible — is semantically novel and emotionally powerful. (+2)
- **Interaction if needed:** Hover restores full opacity to any site and shows its species richness breakdown; a toggle allows switching to normal (analytical) opacity mode for comparison
- **Page reference:** ds_chunk_03 p.125

---

### Idea S-13: Annotation-First Trade-Off Scatter — "Four Quadrants" with Editorial Callouts [SEMANTICALLY NOVEL]
*(sources: ds_chunk_08)*

- **Basic visuals combined:** Scatter plot (species richness × yield) + four labeled quadrants + heavy editorial annotations on key sites by name + cluster color coding
- **What the combination adds:** Annotations transform a passive analytical scatter into an editorial argument. The four quadrant labels ("Low yield, High biodiversity" / "High yield, Low biodiversity" / etc.) pre-interpret the space for the viewer. The *emptiness* of the upper-right quadrant (high yield AND high richness) becomes the main argument when it is explicitly annotated: "No sites here — the trade-off." Named outliers at the quadrant boundaries give Sofia talking points.
- **Data manipulation applied:** Compute median yield and median richness as quadrant boundaries. Label top 5 outlier sites per quadrant with site names. Color points by cluster. Fit a regression line and annotate it as "the trade-off."
- **Marks:** Points (sites); quadrant boundary lines; annotation text boxes with leader lines; regression line
- **Channels:** X = species richness; Y = yield; color hue = cluster; annotation text = site identity + key variable; empty space in upper-right quadrant = the visual argument
- **User task supported:** Communicate the trade-off as a persuasive editorial argument; identify exceptions by name; locate one's site within the space
- **What it shows for our data:** The emptiness of the high-richness + high-yield quadrant is the main argument for conservation — annotating it makes it undeniable
- **Persona it serves:** Sofia Almeida (primary) — persuasive communication to non-technical audiences; designed for a poster or slide presentation
- **Semantic novelty:** Scatter plots are standard for correlation. Using the *empty space* in one quadrant as the primary visual argument — and explicitly labeling it as the trade-off — is a semantically novel editorial role for this chart type.
- **Interaction if needed:** Static (printable); optionally click quadrant to filter to those sites
- **Page reference:** ds_chunk_08 p.363, p.399

---

<a name="persona-elena"></a>
## Part 3 — Ideas for Elena Novak (Agroecology Scientist)

---

### Idea E-01: Parallel Coordinates — Full Multivariate Site Profile
*(sources: vad_chunk_01, vad_chunk_04, vad_chunk_05, ds_chunk_02)*

- **Basic visuals combined:** Parallel coordinates plot (all management + biodiversity + yield variables as axes) + cluster color coding + yield as the terminal (rightmost) axis
- **What the combination adds:** Shows all available variables (coffee structure index, density, dominance, woody richness, herbaceous richness, bryophyte richness, mean yield, cluster group) simultaneously for all 60 sites. The question answered: "What combination of variables distinguishes top-yield sites, and does cluster add information beyond yield alone?" — impossible to answer by comparing individual bar charts or scatterplots of pairs. Sites with high yield AND high richness will show unusual crossing lines — the visual exception to the general pattern.
- **Data manipulation applied:** Join all datasets by site. Standardize each variable to 0–1 scale for cross-axis comparison. Order axes by correlation with yield (most correlated variables adjacent to the yield axis). Place yield as the rightmost axis so the visual flows "toward yield" as the outcome.
- **Marks:** Lines (one per site, crossing all axes)
- **Channels:** Line path across axes = multivariate quantitative profile (most accurate channel available for each variable — position on aligned axis); color hue = cluster group (categorical, separable from line position); opacity = semi-transparent to manage overplotting; selected lines highlighted in bold
- **User task supported:** Explore (find unusual site profiles); compare (do cluster lines follow similar paths?); identify (select a site and trace its full profile); discover (which variables co-vary most with yield?)
- **What it shows for our data:** Whether high-yield clusters show a consistent cross-variable pattern; whether cluster membership adds information beyond what coffee density alone shows; sites with high yield AND relatively high richness show crossing lines that stand out visually
- **Persona it serves:** Elena Novak (primary) — full correlation structure across variables; Hana Abebe (secondary) — what makes a top site different across all variables?
- **Interaction if needed:** Brush on the yield axis to filter to top 20% yield sites; reorder axes by dragging; click a site line to label and drill into it; color by different attributes (yield, diversity, cluster); hierarchical version shows clusters as bands (mean ± range) to reduce hairball
- **Page reference:** vad_chunk_01 p.44, p.57; vad_chunk_04 p.163–166; vad_chunk_05 p.251–300; ds_chunk_02 p.78–88

---

### Idea E-02: Species × Site Cluster Heatmap with Dendrogram and Yield Sidebar
*(sources: vad_chunk_02, vad_chunk_03, vad_chunk_04, vad_chunk_08, ds_chunk_04)*

- **Basic visuals combined:** Presence/absence heatmap (407 species × 60 sites) + hierarchical dendrogram on both axes (sites clustered by composition similarity, species clustered by co-occurrence) + yield bar chart sidebar aligned to site columns + plant group color strips on species rows
- **What the combination adds:** The raw presence/absence matrix is too large to read without ordering. Hierarchical clustering of both axes groups sites with similar species composition together AND groups species that co-occur together. The dendrogram reveals the ecological cluster structure. The yield sidebar immediately shows whether high-yield sites form a distinct floristic block or are scattered. This is a classic double-dendrogram heatmap (bicluster matrix) applied to an ecologically meaningful question: "Do sites that cluster together by species composition also share similar yields?"
- **Data manipulation applied:** Hierarchical clustering of 60 sites (columns) by Bray-Curtis or Jaccard dissimilarity of species composition — derives the column dendrogram ordering. Hierarchical clustering of species (rows) by co-occurrence across sites — derives the row dendrogram ordering. Encode presence/absence as binary color (present = dark, absent = light). Add normalized yield bar alongside site dendrogram. Add plant group color strip on left row margin.
- **Marks:** Filled cells (heatmap); dendrogram line marks; bar marks (yield sidebar); color strip (plant group)
- **Channels:** Cell color = presence/absence (binary); dendrogram position = cluster membership hierarchy; bar length = yield (aligned position, highest accuracy channel for the yield variable); left margin color hue = plant group (categorical)
- **User task supported:** Explore (find species composition clusters); compare (do composition clusters correspond to yield groups?); identify (which species define each cluster?); discover (are there indicator species for high-yield sites?)
- **What it shows for our data:** Whether the 60 sites form natural groups by plant community that map onto the yield gradient; which species are found predominantly in high-yield vs. low-yield site clusters; whether there are species guilds that consistently appear together
- **Persona it serves:** Elena Novak (primary) — cluster structure, methodological rigor, dataset overview; Sofia Almeida (secondary) — identifies biodiversity hotspot clusters in the site dendrogram
- **Interaction if needed:** Hover on a cell for site name + species name + yield; click dendrogram branch to isolate a cluster of sites and highlight them in a linked scatterplot; filter to show only woody / herbaceous / bryophyte rows; minimum similarity slider to adjust cluster granularity
- **Page reference:** vad_chunk_02 p.61, p.78–80; vad_chunk_03 p.146; vad_chunk_04 p.158–162; vad_chunk_08 p.351–354; ds_chunk_04 p.155, 200

---

### Idea E-03: Three-Year Yield Consistency — Small Multiples by Year with Variance Strip
*(sources: vad_chunk_05, ci_chunk_02, vad_chunk_06)*

- **Basic visuals combined:** Three small multiple bar charts (one per year: year 1, year 2, year 3, with sites in the same spatial order) + linked coefficient-of-variation indicator strip below + Spearman correlation between year pairs as header annotations
- **What the combination adds:** Three small multiple bar charts, each showing all 60 sites' yield for one year, with the same sort order (by mean yield), allow immediate visual comparison. Differences in bar height between panels reveal which sites are unstable. The CV indicator strip quantifies instability per site. The combination answers Elena's methodological question: "Are the 3 yield years essentially the same measurement, or do they tell different stories?" — without averaging away the information and with the "eyes beat memory" benefit of simultaneous visibility.
- **Data manipulation applied:** Sort sites by mean yield across all 3 years (shared sort order across all panels). Derive coefficient of variation (CV = std/mean) per site. Derive Spearman rank correlation between year-pair rankings (e.g., year 1 vs. year 2) as a single-number header annotation. Derive year-over-year yield change (delta) per site.
- **Marks:** Bar marks (yield per site per year in each panel); indicator point or bar marks (CV strip); reference line (mean yield across years)
- **Channels:** Bar length = yield value; Y-position = site rank by mean yield (shared across all panels); color hue = cluster (optional, if clusters need to be visible); CV strip luminance = magnitude of inter-annual instability
- **User task supported:** Compare year-to-year stability of site rankings; identify sites with high inter-annual variance; confirm whether mean yield is a valid summary measure
- **What it shows for our data:** Whether bars are nearly identical across the three panels (mean is reliable) or whether specific sites show large cross-panel differences (mean is misleading); which sites are consistently top performers vs. which are lucky in one year
- **Persona it serves:** Elena Novak (primary) — methodological question about data reliability; Hana Abebe (secondary) — finding reliably high-yielding sites
- **Interaction if needed:** Sort panels by year 1, year 2, year 3, or mean to see whether site rankings are stable; click site to see all three year values in a detail panel; color by cluster assignment
- **Page reference:** vad_chunk_05 p.298–299; ci_chunk_02 p.59; vad_chunk_06 p.298–299

---

### Idea E-04: Yield-Biodiversity Trade-Off Scatterplot with Cluster Coloring — For Exploration and Presentation
*(sources: vad_chunk_01, vad_chunk_02, vad_chunk_03, vad_chunk_04)*

- **Basic visuals combined:** Scatterplot (yield × total species richness, all 60 sites) + cluster color coding + optional regression line overlay + optional bubble sizing for management intensity
- **What the combination adds:** The scatterplot shows the core yield-biodiversity trade-off for all 60 sites at once. Cluster color reveals whether high-yield clusters are structurally different from low-yield clusters. The regression line makes direction and strength of trade-off explicit. The bubble sizing (management intensity / coffee structure index) adds the third dimension — if highly managed sites cluster in the high-yield/low-richness corner, management drives the trade-off. This combination answers: "Is the yield-biodiversity trade-off uniform, or do some management types escape it?"
- **Data manipulation applied:** Derive mean yield across 3 years. Derive total species richness from the four groups. Use cluster assignment from Coffee_structure_index_variables.xlsx as categorical color. Derive a management intensity composite score for bubble sizing. Optionally log-transform yield if distribution is skewed. Fit linear regression of richness on yield; derive residuals to identify outlier sites.
- **Marks:** Points/bubbles (one per site); regression line; optional quadrant dividers
- **Channels:** X-position = mean coffee yield (quantitative — most accurate channel for the primary comparison); Y-position = total species richness (quantitative); color hue = cluster group (categorical identity, 4–5 groups); bubble area = management intensity (quantitative, correctly area-proportional); optional: text labels on top-5 outlier sites
- **User task supported:** Explore (find outlier sites that are high in both yield and richness); compare (does one cluster dominate the high-yield / low-richness region?); identify (which specific sites are exceptions?)
- **What it shows for our data:** If clusters separate cleanly along the trade-off line, management type determines both yield and biodiversity simultaneously. Outlier sites (high yield AND high richness) are the most interesting cases. Whether management intensity (bubble size) mediates the trade-off.
- **Persona it serves:** Elena Novak (primary) — correlation structure, cluster validity, outlier detection; Sofia Almeida (secondary) — the trade-off made undeniable; Hana Abebe (secondary) — which sites are top performers?
- **Interaction if needed:** Hover to label site; click to filter to that cluster and see management bar profile in a linked panel; toggle between total richness and individual plant groups (woody/herbaceous/bryophytes); brush to select outlier region; linked views with shared color highlighting
- **Page reference:** vad_chunk_01 p.7–8, p.52; vad_chunk_02 p.76–78; vad_chunk_03 p.147–148; vad_chunk_04 p.146–161

---

### Idea E-05: Site Trajectory Dashboard — "What-Why-How" for Cluster Analysis Validation
*(sources: vad_chunk_03, vad_chunk_04)*

- **Basic visuals combined:** Small multiples line graph (3-year yield trend per site) + dot strip plot (showing yield distribution across all sites for context) + site-level radar chart (showing 5 shrub structure variables for the selected site)
- **What the combination adds:** The line graph shows whether a site is improving or declining. The strip plot shows where that site sits relative to all others (rank context). The radar chart shows the structural profile underlying performance. Together they answer: "Is my site improving over time? Am I above average? What structural variables drive my performance?" — three questions that require three different chart types, linked by shared site selection.
- **Data manipulation applied:** Derive year-over-year yield change (delta) per site. Derive yield percentile rank per site for each year. Normalize the 5 shrub structure variables to 0–1 for radar display. Compute cluster mean radar as an overlay on the selected site's radar.
- **Marks:** Lines (yield trends per site in the line chart); points (strip plot positions); polygon fill (radar chart per site)
- **Channels:** X-position in line chart = year (sequential); Y-position in line chart = yield value; color hue = cluster (shared across all views); point position on strip = current yield rank; radar spoke length = structural variable value; radar shaded band = cluster average (for comparison)
- **User task supported:** Identify (look up a site's trend); compare (compare to cluster average and to overall distribution); discover (whether structural profile matches high-yield profiles)
- **What it shows for our data:** Whether yield is changing over the 3 years and whether that change is structurally explained; which cluster a site belongs to and whether it is performing above or below cluster average; whether Elena's cluster variable predicts yield beyond what individual structure variables explain
- **Persona it serves:** Elena Novak (primary) — cluster validity and variable contribution; Hana Abebe (secondary) — direct comparison to top performers
- **Interaction if needed:** Clicking a site on the strip plot populates the line trend and radar chart; toggle to show cluster average overlay on radar; filter strip plot by cluster group
- **Page reference:** vad_chunk_03 p.68–76; vad_chunk_04 p.158–162

---

### Idea E-06: Derived Difference Map — Yield Rank vs. Richness Rank Divergence [SEMANTICALLY NOVEL]
*(sources: vad_chunk_03)*

- **Basic visuals combined:** Two side-by-side ranked bar charts (one sorted by yield rank, one sorted by species richness rank) + connecting lines for each site across both rankings + derived "rank divergence" bar chart below
- **What the combination adds:** Directly encoding the derived divergence attribute (yield_rank − richness_rank) makes sites that achieve both above-average yield AND above-average richness immediately visible as sites with near-zero divergence. Connecting lines between the two rankings show visually which sites "cross" dramatically between the two orderings — these are the sites most strongly governed by the trade-off. Neither view alone provides this.
- **Data manipulation applied:** Derive rank of each site on yield. Derive rank of each site on total species richness. Compute divergence = yield_rank − richness_rank. Positive divergence = better at yield than richness; negative = better at richness than yield. Sites near zero are the "sweet spot" candidates.
- **Marks:** Bars (rank positions in each side-by-side chart); connecting lines (same site across two orderings); signed divergence bars (third chart)
- **Channels:** Bar length = rank position; connecting line presence and angle = magnitude and direction of rank shift; divergence bar length = magnitude of divergence; divergence bar color hue = direction (yield-favoring warm, richness-favoring cool)
- **User task supported:** Compare (which sites perform consistently on both?); identify (which sites are outliers that escape the trade-off?); summarize (is the divergence universal across all 60 sites?)
- **What it shows for our data:** Whether the yield-biodiversity trade-off is universal or whether some sites genuinely occupy a favorable rank on both dimensions simultaneously
- **Persona it serves:** Elena Novak (primary) — methodological interest in the divergence distribution; Hana Abebe (secondary) — identifies sites near her cluster that achieve the best combination
- **Semantic novelty:** Encoding the *derived difference* between two rankings as a bar chart rather than showing the two raw rankings in separate charts implements Munzner's principle that derived attributes should be encoded directly — a semantically sophisticated role for a standard signed bar chart.
- **Interaction if needed:** Click a connecting line to highlight that site and show its management profile in a popup; sort by divergence magnitude to find the most "trade-off extreme" sites
- **Page reference:** vad_chunk_03 p.77–78

---

### Idea E-07: Chained Instance — Cluster Profiler (Overview → Species Detail)
*(sources: vad_chunk_01)*

- **Basic visuals combined:** Step 1: scatterplot (yield × total richness, cluster-colored) as overview → Step 2: on cluster selection, grouped bar chart showing mean richness per species group and mean yield ± SD for that cluster
- **What the combination adds:** Implements the chained instance concept: the output of Step 1 (cluster selection) becomes the input to Step 2 (cluster profile). The combination answers Elena's methodological question: "Does cluster assignment add information beyond what coffee density already tells you?" — if clusters differ in species composition profile (Step 2), not just in yield, the cluster variable carries ecological meaning beyond a simple intensity ranking.
- **Data manipulation applied:** Aggregate by cluster: mean yield, mean richness per species group, SD of yield. Derive a "cluster profile" summary. Compute within-cluster Spearman correlations between yield and richness to see whether the trade-off is consistent within clusters.
- **Marks:** Step 1: points; Step 2: grouped bars with error bars (SD)
- **Channels:** Step 1: position (yield × richness), color hue (cluster); Step 2: bar length (mean richness / yield), color hue (species group type), error bar length (SD)
- **User task supported:** Explore → Identify: Step 1 explores clusters visually; Step 2 identifies what defines each cluster; Compare: compare two clusters by selecting both
- **What it shows for our data:** Whether clusters differ in species composition structure, not just yield level — directly tests the informational value of the cluster variable
- **Persona it serves:** Elena Novak (primary) — cluster validity; Hana Abebe (secondary) — what kind of sites are in the top-yield cluster?
- **Interaction if needed:** Click cluster in Step 1 to populate Step 2; shift-click for multi-cluster comparison; toggle between individual sites vs. cluster means
- **Page reference:** vad_chunk_01 p.17, p.51–53

---

### Idea E-08: Scagnostics-Inspired "Relationship Fingerprint" — Which Variable Pairs Tell the Same Story?
*(sources: vad_chunk_08, vad_chunk_09)*

- **Basic visuals combined:** SPLOM (scatterplot matrix) of all ~15 quantitative site variables + scagnostics ranking to surface the most structurally interesting cells + color by cluster assignment within each cell
- **What the combination adds:** The 60-site dataset has ~15 continuous variables (yield, total richness, woody richness, herbaceous richness, bryophyte richness, structure index, density, dominance, 7 shrub structure variables). That is 105 pairwise scatterplots. Scagnostics computes monotonic/outlying/clumpy/stringy scores for each pair and directs attention automatically to the most structurally interesting relationships. This reveals: "Which variable pairs have the strongest/weakest/most unusual structure?" without Elena having to read all 105 scatterplots.
- **Data manipulation applied:** Compute 9 scagnostics measures for each of the 105 pairwise variable combinations. Display SPLOM with cell background intensity encoding the most interesting scagnostic score. Overlay cluster color on points within each expanded cell.
- **Marks:** Points (scatterplot cells); colored rectangles for cell-level scagnostic scores
- **Channels:** Cell position x/y = which variable pair; cell background intensity = scagnostic score (outlying, monotone, or clumpy — whichever is most interesting); point color hue = cluster; point position within expanded cell = variable values
- **User task supported:** Discover correlations; identify structure; compare attribute pairs; identify collinear variables vs. independent predictors
- **What it shows for our data:** Whether yield-richness is truly the dominant monotonic pattern or whether shrub structure variables show stronger relationships; which management variables are collinear; potential confounders for Elena's field study design
- **Persona it serves:** Elena Novak (exclusively) — methodological rigor, correlation structure, dataset structure
- **Interaction if needed:** Click any SPLOM cell to open the full scatterplot with all 60 sites labeled; filter to subset of variables of interest; linked highlighting across cells
- **Page reference:** vad_chunk_08 p.342–345; vad_chunk_09 p.342–346

---

### Idea E-09: Management Gradient Slope Graph — Species Group Disappearance Tracker
*(sources: vad_chunk_06)*

- **Basic visuals combined:** Slope graph / bump chart (one line per plant group, tracking richness rank across management intensity tiers) + small multiple bar charts beneath (showing absolute richness per group per management tier)
- **What the combination adds:** The slope graph shows how species group richness changes in rank across the management intensity gradient (low → medium → high coffee density). Crossing lines reveal which groups change most in relative importance as management intensifies. The bar charts beneath show absolute richness loss. The combination answers: "As management intensifies, which plant group disappears first, and at which intensity level does the steepest drop occur?"
- **Data manipulation applied:** Bin sites into 3 management intensity tiers based on coffee density or structure index. Rank species richness of each plant group within each tier. Compute relative rank change between tiers. Compute group means per tier for the bar charts.
- **Marks:** Lines connecting ranks across 3 tiers (slope graph); bars (absolute richness per group per tier beneath)
- **Channels:** Slope/angle = magnitude of rank change between management tiers; color hue = plant group (woody/herbaceous/bryophyte/total); Y-position in slope chart = rank within management tier; bar length = absolute species richness in the small multiple bars
- **User task supported:** Identify which species groups disappear as management intensifies; find the management intensity tier where the steepest drop occurs; compare group-level vs. overall trajectories
- **What it shows for our data:** Directly answers Sofia's question "Which species disappear as management intensifies?" at the group level; steep downward slopes toward high-management tiers identify vulnerable groups; flat lines identify resilient groups
- **Persona it serves:** Elena Novak (primary) — comparing group-level vs. species-level trajectories, methodological rigor; Sofia Almeida (secondary) — which plant group is most at risk?
- **Interaction if needed:** Highlight individual plant group on hover; filter to show only species present in at least N sites; toggle between rank (slope) and absolute (bar) view
- **Page reference:** vad_chunk_06 p.272

---

### Idea E-10: Semantic Zoom Site Explorer — Overview to Shrub-Level Structure
*(sources: vad_chunk_06)*

- **Basic visuals combined:** Scatter plot overview (sites in yield × total richness space, colored by cluster) + semantic zoom revealing progressively more detailed mark encoding as the user zooms into individual sites
- **What the combination adds:** At the overview scale, sites are colored dots positioned by yield and richness. Zooming in semantically changes their marks: dots → small bar glyphs → full radar/spider charts showing all 7 shrub structure variables. This collapses the high-dimensional shrub data into the same spatial frame as the yield-biodiversity plot without separate views. The combination answers: "Which specific sites escape the trade-off, and what is their shrub structural profile?"
- **Data manipulation applied:** Compute mean values of 7 shrub structure variables per site; normalize per variable; encode as radar chart at maximum zoom; trigger rendering changes at pixel-size thresholds.
- **Marks:** Point marks (overview); small bar glyph marks (intermediate zoom); radar/star chart marks (zoomed in)
- **Channels:** X-position = coffee yield; Y-position = total species richness; color hue = cluster identity; glyph spoke lengths = 7 shrub structure variables (at detail zoom level); size = zoom-level trigger
- **User task supported:** Explore the distribution of sites in yield-richness space; zoom to outlier sites of interest; compare shrub structural profiles of outlier sites vs. typical sites
- **What it shows for our data:** Whether sites that escape the trade-off (upper-right quadrant outliers) have a distinctive shrub structural profile — directly answers whether cluster assignment predicts unusual performance
- **Persona it serves:** Elena Novak (primary) — structural detail with analytical context; Hana Abebe (secondary) — understanding what high-yield sites look like structurally
- **Interaction if needed:** Semantic zoom triggered by scroll; hover shows cluster membership; click to lock site for detail; compare mode lets two sites be simultaneously zoomed
- **Page reference:** vad_chunk_06 p.280–281

---

### Idea E-11: Site Adjacency Matrix Ordered by Yield × Biodiversity
*(sources: vad_chunk_05)*

- **Basic visuals combined:** Adjacency matrix view (site × site similarity) + color encoding of species composition similarity + row/column reordering by yield rank + yield quintile color strip on axes
- **What the combination adds:** Transforms species co-occurrence data into a spatial relational view. Each cell = similarity in species composition between two sites (Jaccard index). Reordering rows and columns by yield rank reveals whether high-yield sites form a visual cluster (block of high similarity on the diagonal) — answering "Do sites with similar yields have similar species compositions?" A force-directed network cannot make this structural question as directly answerable.
- **Data manipulation applied:** Derive site×site similarity matrix from species composition (Jaccard or Bray-Curtis). Reorder rows/columns by coffee yield rank. Fill cells = similarity value encoded with sequential luminance. Add separate color stripe along axes for yield quintile (categorical hue).
- **Marks:** Area marks (cells in 2D matrix); color stripes on both axes (yield quintile)
- **Channels:** Spatial position (site × site matrix, rows/columns ordered by yield); luminance/saturation = species composition similarity (sequential); axis strip color hue = yield quintile (categorical)
- **User task supported:** Find clusters (do high-yield sites form a distinct composition cluster?); detect anomalies (high-yield sites with high biodiversity similarity to low-yield sites)
- **What it shows for our data:** Whether high-yield sites form a compositionally coherent group or whether the trade-off is associated with compositional fragmentation; whether the 4 management clusters correspond to floristic clusters
- **Persona it serves:** Elena Novak (primary) — correlation structure, methodological rigor; Sofia Almeida (secondary) — whether the biodiversity trade-off is universal or has exceptions
- **Interaction if needed:** Reorder rows/columns interactively by different variables; hover cells to see which two sites are compared; filter to show only top-N or bottom-N yield sites
- **Page reference:** vad_chunk_05 p.208–212

---

### Idea E-12: Focus+Context Biodiversity Hotspot Navigator — DOI Lens
*(sources: vad_chunk_07)*

- **Basic visuals combined:** Overview scatterplot (yield × total richness, all 60 sites) as permanent context layer + expandable focus detail panel (species composition breakdown + management variables + 3-year yield trend) for selected sites, with DOI function controlling focus priority
- **What the combination adds:** The scatterplot keeps the full yield-biodiversity trade-off pattern visible as permanent context while Elena drills into individual site profiles. Nearby sites in yield-biodiversity space get aggregated into a summary, while the clicked focus site shows full detail. The DOI (degree of interest) function adapts which sites are shown in detail vs. summary based on proximity to the currently selected site.
- **Data manipulation applied:** Compute Euclidean distance in yield × total-species-richness space to define neighborhood. Derive DOI scores for all sites relative to the selected focus site. Aggregate context sites within radius into a summary profile. Show focus site in full detail (all 407 species + 7 shrub variables + 3-year yield).
- **Marks:** Point marks (context sites, low saturation); enlarged point marks (focus site, high saturation); bar marks (species richness breakdown in detail panel); line marks (3-year yield trend in detail panel)
- **Channels:** Position (yield × richness in overview); saturation (focus vs. context); size (DOI score as adaptive size); color hue (cluster membership — shared across views)
- **User task supported:** Identify individual sites of interest; maintain overall trade-off pattern as context during drill-down; compare focus site to its nearest neighbors in trade-off space
- **What it shows for our data:** Elena can identify any site in the trade-off space and immediately see its full ecological and management profile, while keeping the pattern context visible
- **Persona it serves:** Elena Novak (primary) — site-specific detail with pattern context maintained; Sofia Almeida (secondary) — biodiversity hotspot identification with yield context
- **Interaction if needed:** Click site to focus; hold Shift to add to multi-focus set; DOI slider to control neighborhood radius; animated transition when focus changes
- **Page reference:** vad_chunk_07 p.348–350

---

### Idea E-13: Multiform Overview–Detail — Cluster Profile → Species Yield Impact
*(sources: vad_chunk_06)*

- **Basic visuals combined:** Overview: cluster-level bar chart (mean yield and mean richness per cluster, 4 bars) → Detail on demand: species × average yield heatmap for the selected cluster's sites
- **What the combination adds:** The overview gives the cluster-level summary (which clusters are high yield vs. high diversity). Selecting a cluster triggers a detail view showing which individual species are most strongly associated with that cluster's sites. The combination bridges the aggregate cluster level (overview) and the species level (detail), answering: "Which species are indicator species for each management cluster?" — impossible from the overview alone.
- **Data manipulation applied:** Compute mean yield and mean richness per cluster. In the detail view, filter the species × average yield dataset to species primarily found in the selected cluster's sites; sort by average coffee yield of associated sites.
- **Marks:** Bar marks (overview cluster summaries with error bars); heatmap cell marks (detail species × metric); reference line marks
- **Channels:** Bar length = mean yield or richness; color hue = cluster identity (shared across overview and detail); row position in detail heatmap = species sorted by yield association; luminance in detail = species occurrence frequency
- **User task supported:** Identify which clusters are high-yield vs. high-biodiversity; drill into species-level composition for a specific cluster; discover indicator species per cluster type
- **What it shows for our data:** Elena can verify whether cluster composition is ecologically meaningful (different species sets per cluster) or redundant with a simple yield gradient
- **Persona it serves:** Elena Novak (primary) — cluster validity and species-level detail; all three personas can use different aspects of this view
- **Interaction if needed:** Click cluster bar to trigger detail view; sort species by occurrence count vs. yield association; toggle between cluster × yield view and cluster × richness view
- **Page reference:** vad_chunk_06 p.296–298

---

### Idea E-14: Linked Dual Beeswarm — Cross-Variable Correlation Explorer
*(sources: ds_chunk_06)*

- **Basic visuals combined:** Two beeswarm plots side by side (Panel 1: sites distributed along yield axis; Panel 2: same sites along total species richness axis) + linked brush interaction + management cluster as vertical grouping
- **What the combination adds:** A single beeswarm shows one variable's distribution. Two linked beeswarms allow brushing a sub-group in one (e.g., high-yield sites) and immediately seeing where those same sites fall in the other (low biodiversity?). This makes the correlation — or trade-off — directly interactive and explorable, more honest than a single correlation coefficient. The interaction reveals whether the trade-off is absolute or whether some clusters partially escape it.
- **Data manipulation applied:** Each site is a dot in both panels. Panel 1 x-axis = mean yield; Panel 2 x-axis = total species richness. Vertical position = management cluster (beeswarm force simulation within each cluster strip). Brush in Panel 1 selects sites; those sites are highlighted in Panel 2.
- **Marks:** Circles (one per site per panel)
- **Channels:** X-position (yield in Panel 1, richness in Panel 2); Y-position (management cluster strip); color hue (cluster group); opacity (full = selected by brush, faded = not selected)
- **User task supported:** Explore (is there always a yield-biodiversity trade-off across all clusters?); compare (how does the pattern differ between management clusters?); identify (outlier sites that defy the trade-off)
- **What it shows for our data:** Whether the high-yield sites in Panel 1 are consistently the low-biodiversity sites in Panel 2, across all 4 management clusters; whether any cluster breaks this pattern
- **Persona it serves:** Elena Novak (primary) — rigorous correlation exploration; Sofia Almeida (secondary) — identifies which sites genuinely achieve both
- **Interaction if needed:** Brush filtering (core mechanism); dropdown to switch between biodiversity metrics in Panel 2 (total / woody / herbaceous / bryophyte richness); hover for site detail
- **Page reference:** ds_chunk_06 p.339–340

---

<a name="student-reports"></a>
## Ideas from Real Student Submissions

*These ideas are extracted from `er_chunk_01_ideas.md` [from student report], which analyzed two student report designs from a data visualization course. The original designs used retail/supply chain datasets. Each idea is adapted to note how the technique could apply to the coffee agroforest dataset. All cards are marked `[from student report]`.*

---

### Idea SR-01: Bubble Grid — Two Quantitative Variables on a Categorical Matrix [from student report]
*(source: er_chunk_01, report_1 p.4, p.8–9, p.13)*

- **Basic visuals combined:** Scatter plot / position grid + proportional circle (bubble) + color saturation encoding
- **What the combination adds:** A standard bubble chart encodes one quantitative variable (size) per mark. This design encodes TWO quantitative variables per mark (size = one metric, saturation = another), placed at grid positions defined by two categorical axes. This surfaces "anomalous" cells — e.g., a high-saturation but small-bubble cell — that would require multiple separate charts to find otherwise.
- **Data manipulation applied:** In the original: revenue aggregated by (area × product type); average order price as mean per group. **Adaptation to coffee data:** Sites as cells in a grid defined by two categorical axes (e.g., shrub cluster group × management intensity tier). Circle area = mean coffee yield per cell. Color saturation = mean total species richness per cell. This directly shows whether cluster × management combinations achieve both high yield and high biodiversity, or whether the trade-off holds within each cell.
- **Marks:** Circles (one per grid cell)
- **Channels:** Size (circle area) = total mean yield; Saturation of color = average species richness; Vertical position = management intensity tier (3 levels); Horizontal position = shrub cluster group (4 groups)
- **User task supported:** Compare performance across two categorical dimensions simultaneously; identify outlier combinations; find which cluster-management combinations are underperforming on yield, richness, or both
- **What it shows for our data:** Which cluster-management type combinations achieve both high yield and high biodiversity; whether the trade-off holds uniformly across all cluster × management combinations or has exceptions
- **Persona it could serve:** Elena Novak (cluster × management interaction structure); Sofia Almeida (trade-off across cluster types); Hana Abebe (which cluster-management combination to target)
- **Interaction if present:** Hover tooltip showing exact yield and richness values; filter by cluster or management tier; filtered cells group together for cleaner comparison
- **Page reference:** report_1 p.4, p.8–9, p.13

---

### Idea SR-02: Circular Tile Map — Proportional Tiles in Sector Layout with Multiple Overlaid Channels [from student report]
*(source: er_chunk_01, report_1 p.6–7, p.10–11)*

- **Basic visuals combined:** Treemap (proportional area tiles) + sector arrangement (categorical identity) + dot overlay (high-value concentration) + luminance encoding (performance metric)
- **What the combination adds:** A standard treemap shows hierarchy and proportion but loses thematic structure. This design adds geographic or categorical sector orientation, plus brightness (delivery efficiency in the original; could encode management efficiency in our data) as a third channel, and dot overlays as a fourth channel. This allows three analytical questions to be answered from a single static view.
- **Data manipulation applied:** In the original: revenue by nation in geographic sectors; delivery metric as proportion of orders exceeding a threshold; high-value order concentration as dot size. **Adaptation:** Sites as tiles within shrub cluster sectors. Tile area = mean coffee yield (proportional). Luminance = species richness (brighter = richer). Dot overlay = presence of rare species (indicator of conservation value).
- **Marks:** Irregular polygon/tile (one per site); colored dots overlaid on high-richness tiles
- **Channels:** Tile area = mean coffee yield; Color hue = cluster sector identity (4 clusters, 4 hues); Luminance/brightness = total species richness (lighter = richer); Dot presence = whether site contains rare species (binary); Spatial sector = cluster identity
- **User task supported:** Identify which management clusters produce high yield while retaining richness; find rare-species hotspots; compare yield and biodiversity simultaneously across cluster groups
- **What it shows for our data:** Which cluster-site combinations are high on yield (large tile) AND high on richness (bright) — the "win-win" candidates; where rare species concentrate
- **Persona it could serve:** Sofia Almeida (conservation priority identification); Elena Novak (cluster structure and multivariate overview)
- **Interaction if present:** Hover reveals exact yield, richness, and rare species count; toggle between luminance = total richness and luminance = woody/herbaceous/bryophyte richness
- **Page reference:** report_1 p.6–7, p.10–11

---

### Idea SR-03: Battery-as-Vessel Metaphor — Domain-Semantic Stacked Bar Mark [from student report]
*(source: er_chunk_01, report_2 p.3–4, p.6–7, p.11)*

- **Basic visuals combined:** Stacked bar chart (proportional fill) + metaphorical domain object (battery/vessel shape) + pre-attentive alarm indicator (colored dot at top)
- **What the combination adds:** A standard stacked bar shows proportional composition but has no intrinsic domain meaning. Using a vessel shape as the mark creates immediate semantic resonance — the fill level is analogous to "how full" the site is of value. Adding a pre-attentive alarm dot at the top allows instant scanning across all 60 sites to identify which ones are "at risk" without reading values. The alarm dot adds an overview layer that a pure stacked bar lacks.
- **Data manipulation applied:** In the original: battery fill = percentage of forecasted inventory quantity; alarm dot color (green/orange/red) = whether both product types meet threshold. **Adaptation:** Each site = one "vessel." Fill height = coffee yield as percentage of maximum observed yield. Color segments within vessel = species groups (woody / herbaceous / bryophyte proportions of total richness). Alarm dot = traffic light based on a "sustainability threshold" (e.g., red if yield is high AND richness is below a conservation threshold — flagging sites where the trade-off is most acute).
- **Marks:** Vertical vessel/cylinder shapes (one per site); colored fill sections (species groups); small circle (alarm dot) at top of each vessel
- **Channels:** Fill height = coffee yield (percentage of maximum); Color segments within fill = species group proportional composition; Alarm dot color (green/orange/red) = sustainability status (both yield and richness adequate / one below threshold / both below); Horizontal position = site identity
- **User task supported:** Monitor multiple sites at a glance; identify which sites are at risk of the trade-off becoming most damaging; compare yield AND composition simultaneously
- **What it shows for our data:** Sites where the vessel is tall (high yield) but the alarm dot is red (richness below threshold) are the most ecologically costly high-yield sites — a direct visual argument for conservation intervention
- **Persona it could serve:** Sofia Almeida (sustainability monitoring, persuasive rhetoric); Hana Abebe (site performance monitoring at a glance)
- **Interaction if present:** Hover tooltip shows species groups and yield; threshold selector allows adjusting the alarm trigger; year filter to show individual year yield vs. 3-year mean
- **Page reference:** report_2 p.3–4, p.6–7, p.11

---

### Idea SR-04: Gauge (Speedometer) — Multi-Metric KPI Dashboard per Site [from student report]
*(source: er_chunk_01, report_2 p.3, p.7, p.11)*

- **Basic visuals combined:** Semi-circular gauge dial + multiple needle encoding (4 metrics per gauge) + nested dual gauges (outer = one metric type, inner = another)
- **What the combination adds:** A single gauge conveys one value; nesting two gauges and placing multiple color-coded needles on each allows 6–8 metrics to be read per site without requiring a table or multiple charts. The angular needle position is rapidly scannable for anomalies — needles clustered at the low end signal a problematic site; needles spread across the dial signal a diverse site.
- **Data manipulation applied:** **Adaptation:** Each gauge = one site. Outer gauge arc = biodiversity metrics (needles: total richness, woody richness, herbaceous richness, bryophyte frequency). Inner gauge arc = management metrics (needles: structure index, coffee density, dominance, mean yield). Needle color = metric identity (4 distinct colors per gauge).
- **Marks:** Arcs (gauge backgrounds); needles (metric values); color fills; nested circles
- **Channels:** Needle angle = metric value; Color of needle = metric identity; Gauge radius (outer vs. inner arc) = metric category (biodiversity vs. management); Position across layout = site identity
- **User task supported:** Compare multiple metrics across sites simultaneously; identify sites where biodiversity and management needles are maximally opposed (trade-off is acute); monitor multi-metric KPI performance
- **What it shows for our data:** Whether biodiversity needles (outer gauge) and yield/management needles (inner gauge) consistently point in opposite directions — visualizing the trade-off as a physical angular opposition within each site's gauge
- **Persona it could serve:** Hana Abebe (monitoring multiple site metrics simultaneously); Elena Novak (multi-variable site comparison)
- **Interaction if present:** Hover tooltip decodes needle values; paired with another view for cross-validation; cluster filter to compare sites within a management group
- **Page reference:** report_2 p.3, p.7, p.11

---

### Idea SR-05: Drilldown Map Transition — Overview to Site-Level Detail with Overlay Charts [from student report]
*(source: er_chunk_01, report_2 p.8–9, p.12)*

- **Basic visuals combined:** Geographic overview map (site locations with yield color encoding) + blur transition to regional detail map + overlay bar chart boxes at each site position + linked charts
- **What the combination adds:** A single map cannot simultaneously show overview context and per-site analytical detail without overplotting. The drilldown transition (click a region → detail map appears with overview blurred behind) allows navigation between scales without losing spatial context. Per-site overlay boxes with bar charts combine geographic encoding with quantitative comparison — a question neither view alone can answer.
- **Data manipulation applied:** **Adaptation:** Overview: 60 sites plotted at geographic coordinates (or within a spatial layout if GPS unavailable), colored by yield quintile. Click a management cluster region → detail view shows only sites in that cluster with overlay bar charts showing species richness breakdown and management variables at each site.
- **Marks:** Circles (sites on overview map); overlapping/blurred background (context during detail view); small bar chart boxes overlaid at each site position in detail view
- **Channels:** Geographic position (real coordinates); color hue (yield quintile on overview); bar length (species richness per group in overlay boxes); overlay box position = site location on detail map
- **User task supported:** Navigate from cluster-level overview to site-level detail; compare species richness within a management cluster; identify outlier sites within a geographic or cluster region
- **What it shows for our data:** Whether sites within the same management cluster are also spatially clustered; which sites within a cluster are outliers in richness or yield
- **Persona it could serve:** Sofia Almeida (identifying spatial concentration of biodiversity hotspots); Elena Novak (comparing site profiles within a geographic or cluster context)
- **Interaction if present:** Click cluster region to trigger blur transition to detail; hover on site overlay box to show full variable profile; return button to return to overview; management variable dropdown to change overlay chart content
- **Page reference:** report_2 p.8–9, p.12

---

### Idea SR-06: Multi-Level Supply Chain Overview — Battery Marks + Histograms + Time-Series Lines Combined [from student report]
*(source: er_chunk_01, report_2 p.5)*

- **Basic visuals combined:** Metaphorical domain marks (vessel/battery shapes per site cluster) + linked arrows (cluster-to-site relationships) + histograms (yield distribution over time) + translucent circle plots (individual site yield as dots) + line charts (yield and richness trends)
- **What the combination adds:** No single chart type can simultaneously show the organizational hierarchy (clusters → sites), the time-series behaviour of yield (3 years), and the distribution of individual yield values across sites. This converge sketch stacks all three within a spatial layout that preserves the cluster → site hierarchy as the primary organizing structure, with detail plots appearing below each cluster.
- **Data manipulation applied:** **Adaptation:** Cluster vessels at the top level (4 clusters, battery-fill = mean cluster yield). Downward arrows from each cluster to its member sites. Below each cluster: histogram of yield distribution across its member sites for each year (3 years × 3 bars per cluster). Translucent circles = individual site yield values. Line charts below = mean yield trend across 3 years + mean species richness trend.
- **Marks:** Vessel/battery cylinders (clusters); downward arrows (cluster-to-site links); histogram bars (yield distributions); translucent circles (individual sites); lines (yield and richness trends)
- **Channels:** Battery fill = mean cluster yield; Arrow direction = cluster membership hierarchy; Histogram bar color = year identity (3 colors); Circle size = individual site yield; Line color = yield vs. richness metric type; Time on x-axis = year 1 / year 2 / year 3
- **User task supported:** Identify seasonal patterns in yield; compare cluster performance; understand yield vs. richness trends within each cluster; see how the trade-off evolves across years
- **What it shows for our data:** An end-to-end cluster × site × temporal view; whether yield-richness trade-off is stable across 3 years within each cluster or shifts over time
- **Persona it could serve:** Elena Novak (temporal structure and cluster × year interaction); Hana Abebe (overall performance view combining cluster structure and production output)
- **Interaction if present:** Year filter; hover for per-site detail; linked highlights between cluster level and individual site circles
- **Page reference:** report_2 p.5

---

*End of combined-viz-ideas.md*
*Synthesized from: ci_chunk_01–05 (Cool Infographics), ds_chunk_01–09 (Data Sketches), ec_chunk_01 (Dutch course examples), er_chunk_01 (student reports), vad_chunk_01–09 (Visualization Analysis and Design).*
*Total source ideas consolidated: ~180+ idea cards across 25 chunk files.*
*Total deduplicated ideas in this document: 43 idea cards (37 main + 6 student report cards).*
