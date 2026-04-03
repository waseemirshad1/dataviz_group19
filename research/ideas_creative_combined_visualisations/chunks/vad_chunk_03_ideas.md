# [agent_18] Visualization Analysis and Design — pages 101-150

## Creative Combined Visualization Ideas

Dataset: 60 Ethiopian coffee agroforest sites
Core tension: Higher yield = lower plant biodiversity

---

### Idea: Yield-Biodiversity Separation Matrix (inspired by p. 101–102, 149–150)

- **Basic visuals combined:** Bar chart (yield per site) + color-coded region separation (biodiversity cluster) + color saturation overlay (species richness magnitude)
- **What the combination adds:** The bar chart answers "how much yield?" while the color region separation answers "which biodiversity regime does this site belong to?" — a question neither alone can answer. The combination makes the trade-off structure immediately visible: are high-yield bars consistently in low-richness color regions?
- **Data manipulation applied:** Sort sites by mean coffee yield (derived ordering). Assign sites to biodiversity clusters (k-means or quartile split on total species richness). Use that cluster as the region-separation key.
- **Marks:** Line marks (bars), with background region bands
- **Channels:** Aligned vertical position (yield — magnitude, highest accuracy), spatial region/background color hue (biodiversity cluster — categorical identity), bar color saturation (total species richness — ordered magnitude secondary)
- **User task supported:** Compare yields across sites; identify whether yield correlates with biodiversity cluster (region grouping makes this a preattentive task)
- **What it shows for our data:** Sites sorted by yield; the background color bands show immediately whether high-yield sites cluster in the low-biodiversity region or are mixed — making the yield-biodiversity trade-off visible without any calculation
- **Persona it serves:** Elena (scientist — correlation structure) and Sofia (conservationist — trade-off visible and persuasive)
- **Interaction if needed:** Hover tooltip showing all species counts per site; toggle to sort by different biodiversity group (woody/herbaceous/bryophyte) to reveal which type drives the pattern
- **Page reference:** p. 101–102 (channel rankings, expressiveness principle), p. 149–150 (separate by categorical, order by value)

---

### Idea: Shrub Structure Popout Map (inspired by p. 109–111)

- **Basic visuals combined:** Scatterplot (sites positioned by two dominant structural variables) + single-channel color hue popout (cluster membership) + shape encoding (management intensity)
- **What the combination adds:** The scatterplot shows continuous structural variation; the preattentive color hue popout instantly identifies which structural cluster each site belongs to without serial search. Shape adds management context. The combination answers: "do structurally similar sites share a management type AND a cluster?" — impossible from either a list or a single chart.
- **Data manipulation applied:** PCA or direct use of two highest-variance structural index variables as x/y axes. Cluster assignment from the existing cluster variable in the data. Derive a management intensity ordinal from structure index + density + dominance.
- **Marks:** Points (one per site)
- **Channels:** Horizontal position (structural variable 1 — quantitative), vertical position (structural variable 2 — quantitative), color hue (shrub cluster — categorical, max 4 levels for clean popout per p. 110), shape (management intensity — 3–4 levels max per discriminability rule p. 106)
- **User task supported:** Identify cluster membership (popout, p. 109); find outliers (position + color); pattern detection in structural space
- **What it shows for our data:** The 7 shrub structure variables (16 shrubs × 60 sites) reduced to a 2D structural space; cluster membership pops out; outlier sites (unusual structure) are immediately visible
- **Persona it serves:** Elena (scientist — dataset structure, methodological rigor) and Hana (farmer — spot top performers visually)
- **Interaction if needed:** Hover to show site name + yield value; brushing to select a cluster and see corresponding sites highlighted in a linked yield chart
- **Page reference:** p. 109–111 (popout, one channel at a time), p. 106 (discriminability — max bins per channel), p. 146–148 (scatterplot design)

---

### Idea: Biodiversity Trade-off Scatterplot with Regression Overlay (inspired by p. 147–148)

- **Basic visuals combined:** Bubble plot (scatterplot with size encoding) + regression line overlay + color hue for plant group type
- **What the combination adds:** The scatterplot position answers "is there a correlation between yield and total richness?" The regression line makes the direction and strength of trade-off explicit. The color hue separation of plant groups (woody/herbaceous/bryophyte) answers the follow-up: "which biodiversity type drives the negative correlation?" — a nested question requiring simultaneous comparison
- **Data manipulation applied:** Compute total species richness as derived aggregate. Fit linear regression lines per plant group (derived). Log-transform yield if distribution is skewed (per p. 147–148 — log reveals linear relationships hidden in raw scale).
- **Marks:** Points (sites), lines (regression)
- **Channels:** Horizontal position (mean coffee yield — quantitative), vertical position (species richness — quantitative), color hue (plant group type — categorical: woody/herbaceous/bryophyte/total), size/area (site-level structural dominance — quantitative, optional bubble encoding)
- **User task supported:** Find correlation/trend (regression line makes this explicit); compare trade-off strength across plant groups (color separation); find outliers (position + color)
- **What it shows for our data:** The core yield-biodiversity tension made quantitatively explicit; whether woody species or herbaceous species show a stronger negative yield correlation; sites that deviate from the trend (high yield AND high richness) are visible outliers
- **Persona it serves:** Sofia (conservationist — trade-off persuasive and visible), Elena (scientist — correlation structure, variability)
- **Interaction if needed:** Toggle to show/hide individual plant group regression lines; hover for site identity and species counts; brush to select outlier sites
- **Page reference:** p. 147–148 (scatterplot, regression overlay, log-transform), p. 101 (color hue as categorical identity channel)

---

### Idea: Calendar-Style Site Pattern Comparison — Yield × Season (inspired by p. 127, 133)

- **Basic visuals combined:** Calendar-layout grid (sites as "days", years as "weeks") + aggregate line curves showing within-year yield variation + color hue for cluster type
- **What the combination adds:** Directly inspired by the van Wijk & van Selow linked calendar + aggregate curves (p. 127). The calendar grid shows which sites belong to which yield pattern cluster; the aggregate curves show the shape of each pattern across three years. Neither alone answers "which sites follow the same multi-year trajectory AND what does that trajectory look like?"
- **Data manipulation applied:** Hierarchical or k-means clustering of 3-year yield trajectories per site. Average curve per cluster = representative trajectory. Sites sorted by cluster within calendar rows. Color shared between views.
- **Marks:** Cells (calendar grid), lines (aggregate curves)
- **Channels:** Calendar cell position (site identity — categorical), color hue (yield trajectory cluster — categorical, shared across both views), y-axis in curve view (yield value — quantitative), x-axis in curve view (year — ordinal)
- **User task supported:** Identify which sites share temporal yield patterns; compare pattern shapes across clusters; find sites that switch clusters (anomalies)
- **What it shows for our data:** Whether sites fall into "consistently high yield," "declining," "recovering," or "variable" trajectory types across 3 years; which clusters correlate with biodiversity levels
- **Persona it serves:** Hana (farmer — compare sites, spot top performers), Elena (scientist — dataset structure, variability)
- **Interaction if needed:** Click on a calendar cell to highlight the site in a linked scatterplot; toggle to reorder sites by biodiversity level instead of cluster
- **Page reference:** p. 127 (linked calendar + aggregate curve view design), p. 133 (eyes beat memory, simultaneous views)

---

### Idea: Species × Yield Link Heatmap with Ordered Clusters (inspired by p. 146, p. 150)

- **Basic visuals combined:** Heatmap (species × sites matrix) + bar chart column headers (mean yield per site) + dendrogram row clustering (species groups)
- **What the combination adds:** The heatmap shows presence/absence across 407 species × 60 sites; the bar chart column headers immediately show whether high-yield sites cluster together in the matrix; the row dendrogram groups species that co-occur. The combination answers: "do high-yield sites share a distinct species composition profile?" — impossible from any single view.
- **Data manipulation applied:** Hierarchical clustering of sites by species composition → derived site ordering. Hierarchical clustering of species by co-occurrence across sites → derived species grouping. Sort site columns by mean yield (derived) as alternative ordering. Average yield per species-group as derived aggregate.
- **Marks:** Rectangle/cell (heatmap), line (bar chart headers), dendrogram lines
- **Channels:** Horizontal position (site — categorical, ordered by yield), vertical position (species group — categorical), color luminance/saturation (presence/abundance — quantitative), bar height (yield — aligned position, highest accuracy)
- **User task supported:** Pattern detection across full composition matrix; compare yield between species-composition clusters; identify species strongly associated with high or low yield sites
- **What it shows for our data:** Whether the 407-species composition cleanly separates high-yield from low-yield sites; which species groups dominate high-yield vs. low-yield agroforests — the biodiversity-yield core tension made structurally visible
- **Persona it serves:** Sofia (conservationist — biodiversity hotspots, composition changes), Elena (scientist — dataset structure, correlation)
- **Interaction if needed:** Toggle site ordering between "by yield" and "by composition cluster"; click species row to see bar chart of per-site yield only for sites where that species occurs
- **Page reference:** p. 146 (keys and values — 2 keys → heatmap), p. 150 (order by value, not alphabetically), p. 101–102 (color saturation as ordered channel for heatmap cells)

---

### Idea: Discriminability-Bounded Glyph View of Management Variables (inspired by p. 106, 108)

- **Basic visuals combined:** Scatterplot (sites by yield and total richness) + custom glyphs encoding 3–4 management variables per point
- **What the combination adds:** Position answers the yield-biodiversity correlation. The glyph encodes whether management choices explain the outliers — sites with high yield AND high richness. Neither alone answers "what management profile characterizes the biodiversity-preserving high-yield sites?"
- **Data manipulation applied:** Choose 3 management variables with most variance: structure index, density, dominance. Normalize each to [0,1]. Glyph design: bar length within glyph for each variable (length channel — most accurate non-position channel, p. 103). Keep to 3 variables max per discriminability rules (p. 106): each bar channel has limited bins.
- **Marks:** Points (sites in scatterplot), small bar-glyphs overlaid on each point
- **Channels:** Horizontal position (yield), vertical position (total richness), glyph bar lengths (up to 3 management variables — length channel, n=1.0 accuracy per p. 103–104), color hue of glyph outline (structural cluster — categorical)
- **User task supported:** Find outliers (position); identify management profile of outlier sites (glyph comparison); compare management across yield-richness regimes
- **What it shows for our data:** The outlier sites (high yield + high richness) and whether their management glyphs look distinctly different from typical sites — a critical question for conservation recommendations
- **Persona it serves:** Hana (farmer — multiple variables, top performer identification), Sofia (conservationist — management context for biodiversity hotspots)
- **Interaction if needed:** Hover to show full variable values; filter by cluster to see only sites of one type; adjust glyph size slider
- **Page reference:** p. 106 (discriminability — max 3–4 channels per glyph), p. 108 (separability — use separable channels for independent attributes), p. 103–104 (length = most accurate non-position channel)

---

### Idea: Popout-Driven Site Anomaly Detector (inspired by p. 109–111, 140)

- **Basic visuals combined:** Dot plot of sites ordered by yield + single-channel size popout for outlier flagging + color hue separation by biodiversity quartile
- **What the combination adds:** Ordering reveals the yield ranking; size popout (large dot) immediately draws attention to sites that violate the yield-biodiversity trade-off (high yield + top biodiversity quartile). Color confirms which biodiversity quartile each site is in. The popout mechanism (single channel, p. 110) makes anomalous sites instantly visible without serial search.
- **Data manipulation applied:** Rank sites by mean yield → derived ordinal position. Assign biodiversity quartile (total richness) → 4-level categorical. Derive a "trade-off anomaly score" (high yield + high richness) → boolean flag mapped to large dot size.
- **Marks:** Points (variable size)
- **Channels:** Horizontal position (yield rank — ordinal), vertical position (jitter or stacking to avoid overlap), color hue (biodiversity quartile — 4 categorical levels, within discriminability limit), size (anomaly flag — 2 levels: normal vs. anomaly → clean popout per p. 109–110)
- **User task supported:** Identify anomalous sites (popout), compare yield (position), locate biodiversity class (hue)
- **What it shows for our data:** Sites that break the expected yield-biodiversity trade-off are immediately salient; conservationists and farmers can find "best of both worlds" sites instantly
- **Persona it serves:** Hana (farmer — top performers), Sofia (conservationist — biodiversity hotspots that are also productive)
- **Interaction if needed:** Click anomaly site to show full species list and management variables; filter by plant group (woody vs. herbaceous richness)
- **Page reference:** p. 109–110 (single-channel popout — do not combine channels), p. 140 (get it right in black and white — size popout survives grayscale)

---

### Idea: Separability-Aware Multi-Channel Site Profile (inspired by p. 106–109)

- **Basic visuals combined:** Parallel coordinates plot (multiple quantitative variables per site) + color hue for yield cluster + line thickness for dominance variable
- **What the combination adds:** Parallel coordinates show the full multi-dimensional profile of each site (yield, richness by group, management variables). Color hue (separable from position, p. 107) highlights which yield cluster each site belongs to. Line thickness (separable from both position and hue for 3–4 levels per p. 106) shows a third categorical attribute (dominance level). The combination answers: "what is the full profile of each yield cluster, and does it systematically differ across all variables simultaneously?"
- **Data manipulation applied:** Normalize all axes to [0,1] for parallel coordinates display. Compute yield cluster (derived). Bin dominance into 3–4 levels (derived, within discriminability limit p. 106). Order axes by correlation with yield (derived ranking) to put the most yield-correlated variables nearest to the yield axis.
- **Marks:** Lines (one per site across all axes)
- **Channels:** Position along each parallel axis (quantitative variable values — the most accurate channel per p. 101), color hue (yield cluster — categorical, separable from position per p. 107), line thickness (dominance level — 3–4 bins, within limit per p. 106)
- **User task supported:** Compare profiles across sites; identify which variables systematically differ between yield clusters; find outliers (crossing lines); pattern detection
- **What it shows for our data:** Whether high-yield clusters show a consistent pattern across all biodiversity and management variables simultaneously — the full multi-dimensional correlation structure visible in one view
- **Persona it serves:** Elena (scientist — correlation structure, methodological rigor, dataset structure)
- **Interaction if needed:** Brush on any axis to filter to a value range; reorder axes interactively; highlight a single site's line on hover
- **Page reference:** p. 107 (separable channels: position + hue + thickness), p. 106 (discriminability: max bins per channel), p. 101 (channel ranking justification)
