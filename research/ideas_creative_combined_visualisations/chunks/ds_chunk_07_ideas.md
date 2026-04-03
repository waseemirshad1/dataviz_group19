# [agent_12] Data Sketches — pages 301-350

## Creative Combined Visualization Ideas

---

### Idea: "Breathing Sites" — Pulsating Dot Map of Site Biodiversity (inspired by p.322–331)

- **Basic visuals combined:** Spatial dot map (one circle per site) + animated or interactively controlled circle size/color encoding biodiversity and yield.
- **What the combination adds:** The dot-map alone shows "where are the sites." Making circle size and color represent biodiversity/yield simultaneously turns the spatial layout into a variable-comparison tool. The "breathing" animation concept (from "Breathing Earth") could be replaced here with interactive hover/filter that "pulses" sites by different variables.
- **Data manipulation applied:** Normalize yield and biodiversity metrics to a 0–1 scale for size and color mapping. Can use multiple biodiversity dimensions (woody/herbaceous/bryophyte species richness) mapped to separate visual passes or toggled interactively.
- **Marks:** Circles (one per site, 60 total).
- **Channels:** Position (geographic location of sites, or ordinal x/y if no GPS data), size (coffee yield), color saturation/hue (species richness — e.g., green intensity = total biodiversity), opacity (a secondary variable like structure index).
- **User task supported:** Identify spatial clusters of high-yield vs. high-biodiversity sites; spot the yield–biodiversity trade-off spatially.
- **What it shows for our data:** Whether high-yield sites (large circles) cluster spatially, and whether those same circles are lighter/less green (lower biodiversity). The core tension — yield vs. biodiversity — becomes visible as a size-color opposition.
- **Persona it serves:** Sofia Almeida (conservationist — trade-off made spatially legible and emotionally vivid) and Hana Abebe (farmer — can spot high-yield site clusters).
- **Interaction if needed:** Hover to see site details; toggle the channel assignment (e.g., switch color from total richness to woody richness); filter to show only high-yield or high-biodiversity sites.
- **Page reference:** p.322–331

---

### Idea: "The Seasonal Block" — Site Performance Profile Chart (inspired by p.305–306)

- **Basic visuals combined:** Grouped block/bar chart where blocks represent sites, grouped by management cluster, with block height = yield and color = biodiversity category.
- **What the combination adds:** The seasonal block chart (p.305) showed that grouping first by a primary category (season/cluster) and mapping height to a second variable (interest/yield) reveals patterns invisible when all blocks are the same height. Applied to our data: grouping by management cluster shows whether higher-yield sites cluster within specific management types, and whether the trade-off with biodiversity is consistent within clusters.
- **Data manipulation applied:** Assign each site to a management cluster (cluster variable already exists). Within each cluster, sort sites by yield. Map total species richness to a color gradient (green = high biodiversity, yellow = low). Block height = yield.
- **Marks:** Rectangular blocks (one per site).
- **Channels:** Height (yield magnitude), color saturation (species richness — green gradient), x-position within cluster group (sorted by yield), cluster grouping (faceted or color-coded group label).
- **User task supported:** Compare → which management clusters produce high yield? Identify → which clusters have the yield/biodiversity trade-off vs. which manage both?
- **What it shows for our data:** If cluster A consistently has tall (high yield) but pale (low biodiversity) blocks, while cluster B has shorter but greener blocks, the trade-off pattern is visually immediate.
- **Persona it serves:** Hana Abebe (farmer — spot which cluster type maximizes yield), Elena Novak (scientist — see if cluster structure correlates with yield-biodiversity trade-off).
- **Interaction if needed:** Toggle the y-axis between yield and different biodiversity metrics; hover to see site ID and detailed stats.
- **Page reference:** p.305–306

---

### Idea: "Drip and Rise" Beeswarm — Sites by Biodiversity Trade-off (inspired by p.338–340)

- **Basic visuals combined:** Beeswarm plot (one dot per site) with a vertical metaphor: sites that "sacrifice" biodiversity for yield drip downward; sites that maintain both biodiversity and yield rise upward.
- **What the combination adds:** The beeswarm (p.338) is powerful for showing individual items + distribution simultaneously. The visual metaphor (p.339) — frustrations "drip down," satisfaction "rises up" — directly applies to the yield-biodiversity trade-off tension. High yield + low biodiversity = "drip" (environmental cost). High yield + high biodiversity = "rise" (sustainable). This is semantic encoding, not just positional.
- **Data manipulation applied:** Compute a composite "sustainability score" = (yield rank + biodiversity rank) / 2. Sites below a threshold drip; sites above rise. Use D3 force layout to spread dots horizontally by a third variable (e.g., total species richness or management intensity) without overlapping.
- **Marks:** Circles (one per site, 60 total).
- **Channels:** Y-position (above/below dividing line = rise/drip metaphor for yield-biodiversity trade-off direction), X-position (continuous: e.g., coffee yield or species richness), color hue (management cluster category), size (optional: structure index), fill vs. outline (e.g., top-10 yield sites filled).
- **User task supported:** Identify → which sites represent the best and worst trade-off outcomes? Explore → what characterizes the "rising" sites vs. the "dripping" ones?
- **What it shows for our data:** Sites that are high-yield AND high-biodiversity are rare and float above the center line. Most high-yield sites drip below. The visual makes the trade-off emotionally legible.
- **Persona it serves:** Sofia Almeida (conservationist — trade-off made emotionally vivid) and Elena Novak (scientist — can see individual sites + overall distribution simultaneously).
- **Interaction if needed:** Hover to see site name and full variable profile; brush to filter sites by cluster; overlay box-and-whisker for group medians.
- **Page reference:** p.338–340

---

### Idea: "Species × Yield Arc Timeline" — Per-Species Impact View (inspired by p.305–307)

- **Basic visuals combined:** Arc/timeline chart per species showing how many sites each species appears in, with arc direction indicating whether those sites tend toward high yield (arc above) or low yield (arc below).
- **What the combination adds:** The arc timeline (p.305) encoded year-over-year directional change. Applied to our species data: each species gets a position on an x-axis (number of sites it occurs in), and an arc above/below indicates whether its associated sites tend above or below the mean yield. This replaces "time" with "spread" (how many sites) and replaces "trend direction" with "yield association direction."
- **Data manipulation applied:** From the "species × average coffee yield" dataset, for each species compute: (1) n_sites (how widely distributed it is) and (2) mean yield of sites where it occurs minus overall mean yield (positive = yield-associated, negative = biodiversity-associated). Map these to position and arc direction respectively.
- **Marks:** Circles (species), arcs (connecting their n_sites position to their yield association direction).
- **Channels:** X-position (n_sites — how widely the species occurs), arc direction (above = positively yield-associated, below = negatively), arc height (magnitude of yield association), color hue (plant group: woody/herbaceous/bryophyte).
- **User task supported:** Identify → which species are strongly associated with high-yield sites? Which species signal biodiversity-rich but lower-yield sites?
- **What it shows for our data:** Species whose arcs rise above the axis are potential "companion species" for high-yield agroforests. Species whose arcs dip below are biodiversity indicators but not yield predictors.
- **Persona it serves:** Hana Abebe (farmer — which species to look for as signs of a productive site), Sofia Almeida (conservationist — which species are uniquely associated with biodiverse, lower-yield sites worth conserving).
- **Interaction if needed:** Click a species to see which sites it occurs in; filter by plant group; hover to show species name and yield delta.
- **Page reference:** p.305–307

---

### Idea: Linked Dual Beeswarm — Cross-Variable Correlation Explorer (inspired by p.339–340)

- **Basic visuals combined:** Two beeswarm plots side by side, one for yield distribution and one for biodiversity distribution of the same 60 sites, linked by brush interaction.
- **What the combination adds:** The single beeswarm (p.338) shows one variable's distribution across sites. Two linked beeswarms (p.339) let you brush a sub-group in one (e.g., high-yield sites) and immediately see where those same sites fall in the other (e.g., biodiversity). This makes the correlation — or trade-off — directly interactive and explorable, more honest than a single correlation coefficient.
- **Data manipulation applied:** Each site is a dot in both panels. Panel 1 x-axis = yield; panel 2 x-axis = total species richness. Vertical grouping = management cluster. Brush in panel 1 to select high-yield sites; see those same sites highlighted in panel 2.
- **Marks:** Circles (one per site per panel).
- **Channels:** X-position (yield in panel 1, richness in panel 2), Y-position (management cluster), color hue (cluster group), opacity (full = selected by brush, faded = not selected), size (optional: structure index).
- **User task supported:** Explore → is there always a yield-biodiversity trade-off, or are some clusters exceptions? Compare → how does the pattern differ between management clusters?
- **What it shows for our data:** Whether the high-yield cluster (top of panel 1) is consistently the low-biodiversity cluster (bottom of panel 2). Outlier sites that defy the trade-off become immediately visible.
- **Persona it serves:** Elena Novak (scientist — rigorous correlation exploration), Sofia Almeida (conservationist — see which sites are genuinely both productive and biodiverse).
- **Interaction if needed:** Brush filtering (core mechanism); dropdown to switch between biodiversity metrics in panel 2; hover for site detail.
- **Page reference:** p.339–340

---

### Idea: "Custom Glyph Per Site" — Multi-Variable Site Profile (inspired by p.307, p.338–339)

- **Basic visuals combined:** Small multiples of custom glyphs (one per site), where each glyph encodes multiple variables simultaneously (yield, species richness by group, management cluster), arranged in a layout sorted by yield.
- **What the combination adds:** The beeswarm shows distribution but not per-item profiles. The custom glyph (like a radar/spider chart per site, or a bar glyph) shows the full variable profile of every site at once. Small multiples arranged by yield let you scan from highest to lowest yield while seeing whether the biodiversity profile changes systematically.
- **Data manipulation applied:** Normalize all variables (yield, woody richness, herbaceous richness, bryophyte richness, structure index) to 0–1 scale. Each glyph = a radial bar or petal chart with 5 arms. Sort sites left-to-right by yield rank.
- **Marks:** Petal/radial bar glyphs (custom), one per site.
- **Channels:** Glyph arm length (per-variable value, normalized), color hue of arm (variable type), position in small-multiple grid (yield rank), overall glyph size (optional: total richness).
- **User task supported:** Identify → what do high-yield sites look like across all variables simultaneously? Spot patterns → do high-yield sites consistently have short biodiversity arms?
- **What it shows for our data:** Whether sites at the top of the yield ranking systematically show a "collapsed" biodiversity profile (short arms on richness dimensions) vs. a "full" profile. Outlier sites with all arms extended (high on everything) stand out immediately.
- **Persona it serves:** Hana Abebe (farmer — see the full profile of top-performing sites), Elena Novak (scientist — inspect variable co-variation at the site level).
- **Interaction if needed:** Hover for site name; click to expand a single glyph to full detail; filter to show only a specific cluster.
- **Page reference:** p.307, p.338–339

---

### Idea: "Animated Reveal" — Steppers to Introduce the Yield-Biodiversity Trade-off (inspired by p.310)

- **Basic visuals combined:** A stepper-based animated introduction using a scatter plot (yield vs. biodiversity), where each step adds a new layer of information: first yield, then biodiversity, then management cluster colors, then outlier annotations, then a regression line.
- **What the combination adds:** The steppers technique (p.310) — auto-play with click-to-replay — manages the complexity of a multi-variable scatter plot by introducing one channel at a time. The reader sees the trade-off emerge step by step, which is pedagogically more effective than presenting the full chart at once.
- **Data manipulation applied:** Simple scatter of 60 sites; add cluster color coding at step 3; add regression line at step 4; highlight outliers at step 5.
- **Marks:** Points (sites), regression line, annotation labels.
- **Channels:** X-position (yield), Y-position (total species richness), color hue (introduced at step 3 — management cluster), size (optional: structure index), annotation labels (step 5 — outlier sites named).
- **User task supported:** Explore → understand the trade-off; Identify → which clusters and sites are exceptions to the general trend.
- **What it shows for our data:** The yield-biodiversity negative correlation, modulated by management cluster. Some clusters may have a less severe trade-off.
- **Persona it serves:** All three personas — but especially Sofia Almeida (clear emotional narrative) and Hana Abebe (accessible step-by-step introduction).
- **Interaction if needed:** Click-to-replay each step; hover for site detail at any step.
- **Page reference:** p.310
