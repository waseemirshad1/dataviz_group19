# [agent_21] Visualization Analysis and Design — pages 251-300

---

### Idea: Yield-Biodiversity Diverging Heatmap with Linked Site List (inspired by p.255–256, p.296–298)

- **Basic visuals combined:** Diverging colormap heatmap (sites × species groups) + linked text list of sites
- **What the combination adds:** The diverging colormap centers on the mean yield, making high-yield (low-biodiversity) and low-yield (high-biodiversity) sites equally visible in opposite hues. The linked site list allows browsing and direct lookup — inspired by the microarray system where "a text list seems trivial as a standalone view but plays useful roles in multi-view systems" (p.298).
- **Data manipulation applied:** Derive a yield-deviation attribute = site yield minus dataset mean yield; use this as the diverging axis. Also derive total species richness per site (sum across woody/herbaceous/bryophyte groups).
- **Marks:** Heatmap cell marks; text marks in site list
- **Channels:** Color diverging hue+luminance (yield deviation from mean); position y (sites sorted by yield); position x (species groups or individual dominant species); text list provides label channel
- **User task supported:** Identify high-yield vs low-yield sites; compare biodiversity profiles across the yield gradient; locate specific sites by name; discover which species groups track the yield gradient
- **What it shows for our data:** The core tension — high yield = low diversity — is literally visible as a color gradient from one hue (high yield, sparse species) to the opposite hue (low yield, rich species). The diverging center makes the middle-yield, middle-biodiversity sites appear neutral.
- **Persona it serves:** Sofia (conservationist) — "Show richest sites = lowest yield" is directly answered by the diverging visual; Elena (scientist) — can see which species groups track the gradient
- **Interaction if needed:** Clicking a site in the list navigates to it in the heatmap (constrained navigation); brushing in the heatmap highlights corresponding sites in the list
- **Page reference:** p.255–256 (diverging colormaps), p.296–298 (text list as supporting view)

---

### Idea: Management Gradient as Slope Graph — Species Disappearance Tracker (inspired by p.272)

- **Basic visuals combined:** Slope graph (bump chart) + small multiple bar charts per species group
- **What the combination adds:** The slope graph shows how individual species (or species group richness) changes in rank across the management intensity gradient (low → medium → high coffee density). Crossing lines = species that dramatically change in relative importance as management intensifies. Small multiples beneath show absolute richness per group per management tier.
- **Data manipulation applied:** Bin sites into three management intensity tiers based on coffee density or structure index. Rank species richness of each plant group within each tier. Compute relative change in rank between tiers.
- **Marks:** Line marks connecting the same species group across management tiers (slope graph); bar marks for absolute counts (small multiples)
- **Channels:** Slope/angle (magnitude of rank change); color hue (plant group identity — woody/herbaceous/bryophyte/total); position y (rank within tier); bar length (absolute species richness)
- **User task supported:** Identify which species groups disappear as management intensifies; compare trajectories; locate the tier where the steepest drop occurs
- **What it shows for our data:** Directly answers Sofia's question "Which species disappear as management intensifies?" — steep downward slopes toward high-density management tiers identify vulnerable groups; flat lines identify resilient groups
- **Persona it serves:** Sofia (conservationist) primarily; Elena (scientist) for comparing group-level vs species-level trajectories
- **Interaction if needed:** Highlight individual species group on hover; filter to show only species present in at least N sites
- **Page reference:** p.272 (slope graphs / bump charts in LineUp), p.298–299 (small multiples)

---

### Idea: Site Comparison Matrix — Small Multiples of Yield vs Richness Scatterplots by Species Group (inspired by p.298–300)

- **Basic visuals combined:** Small multiple scatterplots (one per plant group) + shared diverging color encoding across all panels
- **What the combination adds:** Each small multiple shows yield (x) vs richness (y) for one plant group (woody, herbaceous, bryophytes, total). Shared axis scales and a shared color channel (cluster assignment) allow visual comparison across panels. The combination reveals whether the yield-diversity tradeoff is consistent across plant groups or differs by group — a question that neither a single scatterplot (confounded groups) nor a heatmap (no continuous relationship visible) could answer alone.
- **Data manipulation applied:** Standardize axes across all panels so position is directly comparable (Cerebral-style, p.299); color-code by cluster assignment from the structural cluster variable
- **Marks:** Point marks (one per site per panel)
- **Channels:** Position x (coffee yield); position y (species richness, group-specific); color hue (cluster assignment — categorical identity); shape (optionally encode management tier — 3 levels)
- **User task supported:** Compare the yield–diversity relationship across plant groups; identify which groups drive the overall pattern; find sites that are outliers in one group but not others (linked highlighting across panels would reveal this)
- **What it shows for our data:** Elena's question "Does cluster add info beyond coffee density?" — if clusters occupy distinct positions in ALL panels, cluster adds information; if only in some, it's group-specific
- **Persona it serves:** Elena (scientist) for methodological rigor; Sofia (conservationist) for identifying which biodiversity dimension is most impacted
- **Interaction if needed:** Linked highlighting across panels (select a site in one panel → highlighted in all others, showing its multi-group profile); reorder panels by strength of correlation
- **Page reference:** p.298–300 (small multiples, Cerebral), p.293–294 (linked highlighting / EDV)

---

### Idea: LineUp-Style Multi-Attribute Ranking of Sites — Yield vs Biodiversity Dimensions (inspired by p.271–273)

- **Basic visuals combined:** Multi-attribute stacked bar chart (LineUp-style) + slope graph columns between key attributes
- **What the combination adds:** Each row is a site; columns encode yield, woody richness, herbaceous richness, bryophyte richness, total richness, coffee density, structure index. The user can sort by any column or a weighted combination. Slope graphs between neighboring columns reveal which sites maintain their rank vs which sites swap dramatically between yield rank and biodiversity rank — making the tradeoff visible as crossing slopes.
- **Data manipulation applied:** Normalize all attributes to [0,1] for bar comparability; compute weighted combination rank on the fly; derive a "yield–diversity gap" = rank(yield) − rank(total richness) per site
- **Marks:** Horizontal bar marks (attribute values); connecting slope graph lines (same site across ranking columns)
- **Channels:** Bar length (normalized attribute value); slope angle (rank change between columns); position y (current sort rank); color hue (cluster assignment as background color of each row)
- **User task supported:** Compare sites by multiple attributes simultaneously; identify sites that are top performers on yield but bottom on biodiversity (or vice versa); explore how ranking changes when weight shifts from yield to richness
- **What it shows for our data:** Hana's question "Compare sites by yield; spot top performers; multiple variables" is directly served. The yield-to-richness slope graph makes the tradeoff literally visible as crossing lines — sites that fall dramatically in rank moving from the yield column to richness columns.
- **Persona it serves:** Hana (farmer) for yield-focused ranking; Sofia (conservationist) for tradeoff identification; Elena (scientist) for correlation between dimensions
- **Interaction if needed:** Sort by weighted combination; toggle column visibility; filter to show only top-N sites; adjustable weight slider
- **Page reference:** p.271–273 (LineUp), p.272 (slope graphs / bump charts)

---

### Idea: Semantic Zoom Site Explorer — From Cluster Overview to Shrub-Level Structure (inspired by p.280–281)

- **Basic visuals combined:** Scatter plot overview (sites in yield × total richness space) + semantic zoom to reveal shrub structure radar/glyph charts for individual sites
- **What the combination adds:** At the overview scale, sites are positioned by yield (x) and total species richness (y), colored by cluster. Zooming in semantically (not geometrically) changes site marks from colored dots → small bar glyphs → full spider/radar charts showing all 7 shrub structure variables. This collapses the high-dimensional shrub data into the same spatial frame as the yield-biodiversity plot without separate views.
- **Data manipulation applied:** Compute mean values of 7 shrub structure variables per site; normalize within each variable; encode as radar chart spokes; trigger rendering at pixel-size thresholds (inspired by LiveRAC, p.280–281)
- **Marks:** Point marks (overview); small glyph marks (intermediate zoom); radar/star chart marks (zoomed in)
- **Channels:** Position x (coffee yield); position y (total species richness); color hue (cluster identity); glyph shape and spoke length (7 shrub structure variables at detail level); size (reflects zoom level)
- **User task supported:** Explore the distribution of sites in yield-richness space; zoom to sites of interest to compare shrub structural profiles; identify whether cluster assignment correlates with shrub structure at the detail level
- **What it shows for our data:** Elena's question "Does cluster add info beyond coffee density?" — if sites within the same cluster show similar radar shapes, the cluster does add information. Hana can zoom to top-yield sites to see what structural profile they share.
- **Persona it serves:** Elena (scientist) for structural detail; Hana (farmer) for understanding what high-yield sites look like structurally
- **Interaction if needed:** Semantic zoom triggered by scroll or explicit zoom gesture; hovering site shows cluster membership; clicking site shows full species list for that site
- **Page reference:** p.280–281 (LiveRAC / semantic zooming)

---

### Idea: Diverging + Monotonic-Luminance Choropleth of Site Yield Deviation with Species Overlay (inspired by p.255–258)

- **Basic visuals combined:** Diverging colormap choropleth of yield deviation (site-level spatial map if coordinates available, otherwise ordered by site ID) + overlaid glyphs encoding total species richness
- **What the combination adds:** The diverging colormap uses monotonically increasing luminance toward both extremes from a neutral midpoint (mean yield), eliminating the rainbow colormap problems (p.257–258). A secondary glyph (bar or dot size) overlaid on each site position encodes total species richness. The combination makes the yield–biodiversity tradeoff visible in the spatial arrangement of sites: high-yield bright-colored sites will have small glyphs; low-yield (opposite hue) sites will have large glyphs.
- **Data manipulation applied:** Derive yield deviation = site yield − mean yield (creates the diverging variable); normalize species richness for glyph sizing; apply monotonically increasing luminance colormap design rather than standard diverging hue-only
- **Marks:** Area or point marks (sites); bar or circle marks (richness glyphs overlaid)
- **Channels:** Color hue (yield direction: above/below mean); color luminance (monotonically increasing toward extremes — high accuracy for fine structure); size/length (species richness); position (spatial if coordinates available, otherwise ordinal)
- **User task supported:** Identify spatial clustering of high-yield vs high-diversity sites; discover whether sites are geographically segregated by yield; find outliers (high yield AND high diversity = conservation priority)
- **What it shows for our data:** Sofia's case — "show richest sites = lowest yield" — becomes a spatial argument: if rich sites cluster geographically, a protected zone argument is visible. The monotonic luminance prevents the rainbow problem of unequal perceptual steps.
- **Persona it serves:** Sofia (conservationist) for spatial biodiversity argument; Elena (scientist) for checking spatial autocorrelation
- **Interaction if needed:** Toggle between yield and species group overlays; filter to show only extreme-yield or extreme-richness sites; color blindness safe alternative colormap (avoid red-green, p.260)
- **Page reference:** p.255–258 (monotonically increasing luminance colormaps, rainbow anti-pattern)

---

### Idea: Three-Year Yield Consistency Small Multiples + Linked Variance Indicator (inspired by p.298–299, p.291)

- **Basic visuals combined:** Small multiples of site-level bar charts (one panel per year: year 1, year 2, year 3) + linked variance indicator strip
- **What the combination adds:** Three small multiple bar charts (one per year) show yield per site in the same spatial order. Since small multiples use the same encoding and shared position axis, visual comparison is immediate — differences in bar height between panels reveal inter-annual variation. A linked indicator strip below shows the coefficient of variation per site. The combination answers Elena's question "Are the 3 yield years essentially the same?" without animation and with the "Eyes Beat Memory" benefit of simultaneous visibility (p.291).
- **Data manipulation applied:** Sort sites by mean yield (shared sort order across all panels); derive coefficient of variation (CV) per site = std/mean; derive Spearman rank correlation between pairs of years as a summary statistic displayed as a header annotation
- **Marks:** Bar marks (yield per site per year); point or bar marks (CV indicator); reference line mark (mean yield across years)
- **Channels:** Bar length (yield value); position y (site rank by mean yield, shared across panels); luminance variation in CV strip (magnitude of inter-annual instability)
- **User task supported:** Compare year-to-year stability of site rankings; identify sites with high inter-annual variance (unreliable yield); confirm whether mean yield is a valid summary
- **What it shows for our data:** Elena's methodological question directly — if bars are nearly identical across all three panels, the mean is a reliable summary. If specific sites show large cross-panel differences, those sites have unstable yields that the mean obscures.
- **Persona it serves:** Elena (scientist) for methodological rigor; Hana (farmer) for identifying reliable high-yield sites vs lucky single-year performers
- **Interaction if needed:** Sort panels by year 1, year 2, year 3, or mean; click site to see all three year values in a detail panel; color by cluster assignment
- **Page reference:** p.298–299 (small multiples), p.291 (Eyes Beat Memory — juxtapose vs animate)

---

### Idea: Multiform Overview–Detail — Cluster Profile Overview + Per-Species Yield Impact Detail (inspired by p.296–298)

- **Basic visuals combined:** Overview: cluster-level bar chart (mean yield and mean richness per cluster, 4 clusters) + Detail on demand: species × average yield heatmap for the selected cluster
- **What the combination adds:** The overview gives the within-cluster summary (which clusters are high yield vs high diversity). Selecting a cluster triggers a detail view showing which individual species are most associated with that cluster's sites. The combination bridges the aggregate cluster level (overview) and the species level (detail) — neither view alone answers "which species are associated with high-yield clusters?"
- **Data manipulation applied:** Compute mean yield and mean richness per cluster (aggregation); in the detail view, filter the species × average yield dataset to species primarily found in selected cluster's sites; sort species by their average coffee yield across the sites where they occur
- **Marks:** Bar marks (overview: cluster summaries); heatmap cell marks (detail: species × metric); reference line marks
- **Channels:** Bar length (mean yield or richness); color hue (cluster identity, shared across overview and detail); position y (species sorted by yield association); luminance (species occurrence count or site count as secondary encoding)
- **User task supported:** Identify which clusters are high-yield vs high-biodiversity; drill into species-level composition for a specific cluster; discover "indicator species" associated with high-yield or low-yield management
- **What it shows for our data:** Hana can identify which cluster (management profile) is associated with top yield; Sofia can see which species characterize the highest-diversity clusters; Elena can verify whether cluster composition is ecologically meaningful
- **Persona it serves:** All three personas — each focuses on a different dimension of the overview→detail drill
- **Interaction if needed:** Click cluster bar to trigger detail view; sort species list by occurrence count vs yield association; toggle detail axis between average yield and site count
- **Page reference:** p.296–298 (multiform overview-detail, microarray example)
