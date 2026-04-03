# [agent_11] Data Sketches — pages 251-300

## Creative Combined Visualization Ideas

---

### Idea: Species Richness Fractal Tree — Biodiversity as Living Structure (inspired by p.271–274)

- **Basic visuals combined:** Fractal tree (branching structure) + dot/mark encoding per species + color coding by plant group
- **What the combination adds:** A bar chart shows how many species a site has; a fractal tree shows *what kind* of biodiversity looks like — sparse vs. lush. The combination answers: "Does this site feel rich or bare, and which groups dominate?" — a question neither a bar chart nor a species list alone can answer.
- **Data manipulation applied:** Aggregate species count per plant group per site (woody / herbaceous / bryophytes). Optionally pick a representative subset of species per site (e.g., top 20 most abundant) to avoid rendering 407 marks per tree. Normalize branch thickness to group abundance.
- **Marks:** Each branch represents a plant group (3 main branches off a trunk = woody / herbaceous / bryophytes). Each leaf/flower on a branch = one species present at that site. Trunk thickness = total species richness.
- **Channels:**
  - Color hue → plant group (e.g., green = woody, yellow-green = herbaceous, grey-blue = bryophytes)
  - Branch density / number of leaves → species count per group
  - Trunk thickness → total species richness
  - Color saturation of the whole tree → coffee yield (lush/saturated = high biodiversity, muted/faded = high yield / low diversity)
- **User task supported:** Identify, explore, spot trade-off
- **What it shows for our data:** Per-site species richness breakdown by plant group; visual metaphor makes the biodiversity–yield trade-off emotionally legible (a bare tree = high-yield site stripped of diversity)
- **Persona it serves:** Sofia — answers "Where is biodiversity highest, and are those sites sacrificed for yield?" The tree metaphor is persuasive and emotionally resonant for an activist audience.
- **Interaction if needed:** Hover a tree → show site name, exact species count by group, yield value. Filter slider on yield range → highlight trees in that range to show how tree "lushness" correlates with yield.
- **Page reference:** p.271–274

---

### Idea: Site Journey — Fractal Branch Timeline of Yield Across 3 Years (inspired by p.271–274)

- **Basic visuals combined:** Fractal branching layout + small multiples (one branch per year) + dot marks for sites
- **What the combination adds:** A standard line chart shows yield change over 3 years; a branching layout adds the idea of divergence — sites that started similar but diverged over time become visually separated. The combination answers: "Which sites are stable vs. unreliable producers, and do they cluster?"
- **Data manipulation applied:** Compute year-over-year yield change (delta_year2 = yield_year2 - yield_year1; delta_year3 = yield_year3 - yield_year2). Group sites by trajectory type: consistently high, consistently low, improving, declining, erratic.
- **Marks:** Each site = a dot/leaf positioned on a 3-branch structure (branch 1 = year 1, branch 2 = year 2, branch 3 = year 3). Sites with similar trajectories cluster on the same sub-branch.
- **Channels:**
  - Position along branch → yield value that year
  - Branch assignment → year
  - Color hue → trajectory type (stable high / stable low / improving / declining / erratic)
  - Dot size → mean yield across all 3 years
- **User task supported:** Compare, rank, find outlier, identify
- **What it shows for our data:** Yield stability across 3 years per site; which sites are reliable performers vs. volatile; whether volatility correlates with biodiversity or management variables
- **Persona it serves:** Hana — answers "Is yield stable across years, or are some sites unreliable producers?" and "Which sites are strong vs. weak performers?"
- **Interaction if needed:** Hover a dot → show site ID, all 3 yield values, management cluster, total species richness. Click a trajectory group → highlight that group in all other linked views.
- **Page reference:** p.271–274

---

### Idea: Language-Similarity Network Adapted for Species Co-occurrence (inspired by p.289–296)

- **Basic visuals combined:** Network graph (nodes = sites, links = shared species) + color encoding for yield level + node size for species richness
- **What the combination adds:** A scatter plot shows yield vs. richness as two separate axes; a network shows which sites share their species community. The combination answers: "Do high-biodiversity sites form distinct ecological communities, or do species overlap across yield levels?" — neither a scatter plot nor a species table alone can answer this.
- **Data manipulation applied:** Compute Jaccard similarity (proportion of shared species) between every pair of sites from the presence/absence matrix. Threshold similarity (e.g., only draw links where Jaccard > 0.3) to prevent hairball. Use curvature to differentiate multiple links as in the book.
- **Marks:** Circles = sites; curved lines = shared species composition above threshold; single label on each link = the most distinctive shared species.
- **Channels:**
  - Node color hue → yield level (e.g., low / medium / high, three hues)
  - Node size → total species richness
  - Line curvature / thickness → Jaccard similarity strength
  - Line color → whether the link crosses yield groups (same-yield link = grey, cross-yield link = accent color)
- **User task supported:** Explore, identify, spot trade-off
- **What it shows for our data:** Whether high-yield sites form a distinct ecological cluster, or whether species communities are mixed across yield levels; which species bridge high- and low-yield communities
- **Persona it serves:** Sofia — answers "Which specific species are only found at low-yield (biodiverse) sites vs. widespread everywhere?"; Elena — answers "What is the community composition structure across the dataset?"
- **Interaction if needed:** Click a node → highlight all its links and show species list. Filter by plant group (woody / herbaceous / bryophytes) to see which group drives the clustering pattern.
- **Page reference:** p.289–296

---

### Idea: "Beautiful in English"-Style Word Ring Adapted to Species–Yield Ranking (inspired by p.285–295)

- **Basic visuals combined:** Radial arc / tree-ring chart + text-as-mark encoding + hover tooltip with trend detail
- **What the combination adds:** A standard ranked list shows species by how many sites they occur in; a radial arc makes the ranking visually hierarchical and draws attention to the top. The combination answers: "Which species are the most diagnostic of high-yield vs. low-yield sites, and how widely are they distributed?" — the radial layout makes both rank and association visible simultaneously.
- **Data manipulation applied:** Rank species by average yield of their associated sites (high to low). Show top 10–15 per plant group (woody / herbaceous / bryophyte) as three concentric ring sets. Only include species that occur in at least 3 sites to avoid noise from rare singletons.
- **Marks:** Arcs = individual species, placed at rank position. Text label on arc = species name (abbreviated). Three concentric sets of rings = three plant groups.
- **Channels:**
  - Radial ring level → rank (highest average yield = innermost / most prominent)
  - Arc color hue → plant group (woody / herbaceous / bryophyte)
  - Arc color saturation → number of sites the species occurs in (rare = faded, widespread = saturated)
  - Text size → whether it is a top-3 vs. lower-ranked species
- **User task supported:** Rank, identify, compare
- **What it shows for our data:** Which species are most strongly associated with high coffee yield; which are widespread vs. niche; which plant group dominates the high-yield associations
- **Persona it serves:** Hana — answers "Which individual species are most strongly associated with high or low yield?"; Sofia — answers "Which species disappear as management intensifies?"
- **Interaction if needed:** Hover an arc → reveal tooltip showing: species name in full, average yield of sites where it occurs, number of sites, presence/absence profile across yield quartiles (small bar chart). Click plant group legend to filter to that group only.
- **Page reference:** p.285–295 (semantic novelty: the "tree ring" rank structure is re-purposed from language ranking to species–yield ranking; the meaning of the rings changes from "language-specific popularity" to "cross-site ecological association")

---

### Idea: Beads-on-a-String Site Profiles (inspired by p.282–295)

- **Basic visuals combined:** "Beads on a string" sequential layout + per-site glyph (radar / flower mark) + color for yield
- **What the combination adds:** A scatter plot positions sites by one variable at a time; beads on a string positions sites along a yield gradient and attaches a multi-variable glyph to each. The combination answers: "As you move along the yield gradient from low to high, how do management and biodiversity variables shift simultaneously?" — a gradient-encoded multi-variable profile view no single chart provides.
- **Data manipulation applied:** Sort sites by mean yield (the string order). Normalise all other variables (species richness, coffee density, coffee dominance, shrub structure cluster) to a 0–1 scale for comparability within the glyph. Reduce to 5–6 key variables to avoid glyph overload.
- **Marks:** Each site = a circle/bead on the string; inside each bead, a small radar or petal glyph encoding the variable profile.
- **Channels:**
  - Position along string (x-axis) → mean yield (low left → high right)
  - Bead color saturation → overall species richness (faded = low richness)
  - Glyph petal lengths → individual variable values (coffee density, dominance, woody richness, herbaceous richness, bryophyte richness)
  - String curvature / bead spacing → optionally encode variability (spread of 3-year yield)
- **User task supported:** Compare, spot trade-off, explore
- **What it shows for our data:** The biodiversity–yield trade-off as a visual gradient: as yield increases along the string, glyph petals for biodiversity shrink and management petals grow. The "cost" of high yield becomes visible as you scan left to right.
- **Persona it serves:** Sofia — the trade-off is literally visible as a gradient. Elena — can scan for outliers (sites where the expected pattern breaks down). Hana — can identify what top-performing sites look like in terms of management variables.
- **Interaction if needed:** Hover a bead → expand glyph to full size with exact values. Filter string to show only a specific shrub cluster group. Toggle which variables appear as glyph petals.
- **Page reference:** p.282–295

---

### Idea: Responsive Network with Management Gradient — Ripple Layout (inspired by p.291, p.289)

- **Basic visuals combined:** Radial/concentric ring layout + network links + color-coded nodes for yield
- **What the combination adds:** A choropleth map shows geographic distribution; a concentric ring layout positions sites by management intensity (center = most intensively managed). The combination answers: "Do the most intensively managed sites form a tight cluster in species composition, and do they converge on the same management profile?" — neither a map nor a scatter can show this community-structure-plus-management question.
- **Data manipulation applied:** Position sites in concentric rings by coffee structure index (or coffee dominance) as the radial axis. Link sites within the same shrub cluster group. Color by yield. Compute a "management intensity" composite score if needed.
- **Marks:** Circles = sites (nodes); curved lines = shared shrub cluster membership; concentric rings = management intensity zones (innermost = most intensive).
- **Channels:**
  - Radial distance from center → management intensity (center = high intensity)
  - Node color hue → yield level (e.g., low = blue, high = orange)
  - Node size → total species richness
  - Link presence → same shrub cluster assignment
- **User task supported:** Explore, identify, spot trade-off
- **What it shows for our data:** Whether high management intensity and high yield go together spatially in the layout; whether cluster groups concentrate in certain management zones or span across them
- **Persona it serves:** Elena — answers "Does the cluster variable add information beyond what coffee_density already tells you?" (if clusters are spread across the rings, the cluster variable is informative beyond density alone). Hana — can see which management zone her sites fall in and what yield their neighbors achieve.
- **Interaction if needed:** Click a concentric ring zone → highlight all sites in that management band and show a summary. Toggle link layer on/off to reveal or hide cluster structure. Hover node for full site profile.
- **Page reference:** p.291, p.289–296
