# [agent_14] Data Sketches — pages 401-428

## Creative Combined Visualization Ideas — Inspired by Pages 401–428

Dataset: 60 Ethiopian coffee agroforest sites
Core tension: Higher yield = lower plant biodiversity

---

### Idea: Species × Site Radial Co-occurrence Ring (inspired by pp. 401–404)

- **Basic visuals combined:** Radial chord/network layout (Cardcaptor Sakura style) + color-encoded outer ring
- **What the combination adds:** Answers the question "which species consistently co-occur in high-yield sites, and which are exclusive to low-yield sites?" — a question neither a simple scatter plot nor a species table can answer at a glance
- **Data manipulation applied:** From the 407-species presence/absence matrix, pre-filter to the top ~30–50 most frequent or most yield-discriminating species (using, e.g., a Mann-Whitney or simple mean-yield difference between sites where the species is present vs. absent). Arrange the 60 sites as pills on the outer ring; place selected species on the inner circle. Connect species to sites where they are present.
- **Marks:** Arc segments (sites on outer ring), dots/nodes (species on inner circle), lines (presence connections)
- **Channels:** Color hue of outer ring segments — encodes yield level (e.g., green-to-brown gradient from high to low yield); line density around a species node (implicit frequency); angular position of inner nodes (species group: woody / herbaceous / bryophyte)
- **User task supported:** Pattern identification — "which species cluster on the high-yield side of the ring?"; exploration — hover a species to see which sites it appears in; compare — hover a high-yield site to see its full species complement
- **What it shows for our data:** Makes the yield–biodiversity trade-off visible as a spatial pattern — species with lines biased toward the green (high-yield) arc vs. the brown arc. Also reveals co-occurrence clusters (species that appear together in the same sites).
- **Persona it serves:** Elena (scientist) — identifies correlation structure and species-yield links; Sofia (conservationist) — makes the trade-off spatially undeniable
- **Interaction if needed:** Hover on site pill → highlight all species present; hover on species node → highlight all sites; filter by plant group (woody/herbaceous/bryophyte) to reduce visual complexity
- **Page reference:** pp. 401–404

---

### Idea: Site Illumination Map — Yield as Accumulated Brightness (inspired by pp. 408–410)

- **Basic visuals combined:** Small-multiples site glyph grid + brightness/opacity channel encoding yield + staggered reveal animation on scroll
- **What the combination adds:** Borrows the "dimmed by default, illuminated by attention" metaphor from the physical installation. Each of the 60 sites starts as a dim circle. As the viewer scrolls or interacts, sites "light up" in order of yield — the brightest sites are the highest yielders. The question answered: "which sites are the beacons, and what do they have in common?" — adding emotional weight to a factual ranking
- **Data manipulation applied:** Rank 60 sites by mean coffee yield. Assign brightness levels (opacity or luminance) proportional to yield rank. Group sites into 4 clusters using the existing cluster assignment variable from the coffee shrub structure data. Stagger the reveal animation by cluster group (analogous to the orb group-trigger in the installation).
- **Marks:** Circles (one per site), glyph overlays (small bar or petal showing species richness)
- **Channels:** Brightness/opacity (yield rank — primary channel); Size of inner biodiversity glyph (total species richness); Color hue (cluster group — 4 categories); Position in grid (sorted by yield, left-to-right, top-to-bottom)
- **User task supported:** Compare — which sites are brightest; Identify outliers — a dim site in a bright cluster region; Observe trade-off — bright sites tend to have smaller inner glyphs (lower biodiversity)
- **What it shows for our data:** The yield-vs-biodiversity tension becomes a visual contrast between large bright circles with small inner glyphs (high yield, low biodiversity) vs. small dim circles with large inner glyphs (low yield, high biodiversity)
- **Persona it serves:** Hana (farmer) — immediately spots which sites are top performers; Sofia (conservationist) — the "dimming" metaphor echoes the idea that biodiversity is being overshadowed
- **Interaction if needed:** Click on a site circle to expand detail panel (management variables, species list); toggle between "yield view" and "biodiversity view" to flip which dimension drives brightness
- **Page reference:** pp. 408–410

---

### Idea: Temporal Walk — Species Richness Journey Along a Yield Gradient (inspired by pp. 408, z-axis as time)

- **Basic visuals combined:** Scrollytelling path layout + species richness area chart + yield line overlay
- **What the combination adds:** Translates the physical-walk-through-time metaphor of the orb installation to a scroll-through-a-gradient experience. The viewer "walks" from the lowest-yield site to the highest-yield site as they scroll. At each step, species richness is shown as a growing/shrinking area. The new question answered: "as yield rises, how does the biodiversity landscape change, step by step?"
- **Data manipulation applied:** Sort the 60 sites by mean yield. Compute cumulative species richness (how many unique species have been seen so far as we accumulate sites from low to high yield). Also show per-site richness as a separate channel. This creates a "biodiversity depletion" curve as yield rises.
- **Marks:** Area fill (cumulative species richness), line (per-site richness), point (current site in the gradient)
- **Channels:** Position-x (yield rank / scroll position); Height of area (cumulative biodiversity); Color saturation of area (rate of new species addition — more saturated where many new species appear); Annotations at key inflection points
- **User task supported:** Pattern recognition — does biodiversity decline monotonically or are there inflection points?; Identify threshold — is there a yield level above which biodiversity drops sharply?
- **What it shows for our data:** Reveals whether the yield-biodiversity trade-off is gradual or threshold-based — critical information for policy and management decisions
- **Persona it serves:** Elena (scientist) — methodological rigor, variability, threshold identification; Sofia (conservationist) — a persuasive narrative arc showing biodiversity "walking off a cliff" as yield rises
- **Interaction if needed:** Scroll triggers animation; hover on any site point shows its management variables and cluster group; toggle between plant groups (woody/herbaceous/bryophyte) to see which group drives the pattern
- **Page reference:** p. 408

---

### Idea: Participation-Style Farmer Ranking Board (inspired by pp. 409, 421)

- **Basic visuals combined:** Dot-plot / strip chart + interactive user annotation layer
- **What the combination adds:** Inspired by the summary board where visitors place stickers, this visualization lets the viewer (e.g., a farmer or extension officer) mark which site-management strategy they currently use or aspire to. The base chart shows all 60 sites ranked by yield with management variable dots. The interaction layer lets the user annotate "this is me" or "I want to be here." The new question answered: "where do I stand relative to top performers, and what would I need to change?"
- **Data manipulation applied:** Rank sites by yield; compute management variable profiles (structure index, density, dominance) as normalized scores; cluster sites by management profile. Overlay yield quartile bands as background color regions.
- **Marks:** Dots (sites), vertical position (yield), horizontal jitter within cluster (visual separation), user-placed marker (a distinct glyph or colored dot the user can drag to their position)
- **Channels:** Position-y (yield rank); Color hue (cluster group / management profile type); Size (species richness); User-placed marker as an additional point in the same space
- **User task supported:** Compare — where am I vs. top performers; Identify — what cluster am I in; Explore — what management variables distinguish my cluster from higher-yield clusters
- **What it shows for our data:** Bridges the abstract dataset to personal relevance for a farmer audience — situates them within the distribution
- **Persona it serves:** Hana (farmer) — directly serves the task of comparing own situation to benchmarks and spotting what distinguishes top/bottom performers
- **Interaction if needed:** User selects their current management cluster from a dropdown; their "current position" marker appears; a panel shows the management profile of top performers in the next cluster up; optional: species list associated with that cluster
- **Page reference:** pp. 409, 421

---

### Idea: Grouped Stagger Reveal — Cluster-by-Cluster Biodiversity Cascade (inspired by p. 415)

- **Basic visuals combined:** Animated bar/lollipop chart + categorical grouping + staggered entrance animation
- **What the combination adds:** Directly borrows the "group-triggered staggered lighting" mechanic from the orb installation — when one site in a cluster is clicked/hovered, the other sites in the same cluster reveal their full species richness breakdown with a staggered delay. This communicates cluster membership through timing rather than just color. The new question answered: "do sites in the same management cluster share a similar biodiversity profile?"
- **Data manipulation applied:** Assign each of the 60 sites to its cluster (4 clusters from coffee shrub structure variables). For each site, compute species richness by plant group (woody, herbaceous, bryophyte). Normalize within-cluster for comparison.
- **Marks:** Bars or lollipop sticks (species richness by group), dots at tips (totals)
- **Channels:** Bar length (species richness); Color hue (plant group type); Stagger delay timing (cluster membership — sites in the same cluster reveal together); Position-x (site ID within cluster)
- **User task supported:** Compare within-cluster similarity; Identify which clusters are biodiversity-rich vs. depauperate; Pattern recognition — do all high-yield clusters look alike?
- **What it shows for our data:** Shows whether the 4 management clusters are coherent in terms of biodiversity, or whether yield-based clustering cuts across biodiversity patterns
- **Persona it serves:** Elena (scientist) — cluster coherence, variability; Sofia (conservationist) — which clusters are most valuable for conservation
- **Interaction if needed:** Click any site bar to trigger its cluster group to cascade in; click again to collapse; optional filter by plant group
- **Page reference:** p. 415
