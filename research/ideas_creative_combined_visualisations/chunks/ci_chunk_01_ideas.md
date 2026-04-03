# [agent_01] Cool Infographics — pages 1-50

---

## Notes on Inspiration Sources

Pages 1–50 of *Cool Infographics* are primarily theoretical and introductory — they define what infographics are, why they work cognitively, and introduce media formats (static, zooming, clickable, animated). The visual examples shown are illustrative of general principles rather than complex multi-variable charts. Key transferable techniques observed:

- **Contextual comparison**: always pair a key number with a reference value to create meaning (p.29–31)
- **Three-part story structure**: introduction/foundation → Ah-Ha! main event → conclusion/call-to-action (p.35–37)
- **Semantic repurposing**: apply a known visual grammar (subway map, circular timeline) to a novel domain to create surprise and memorability (p.33–34, p.50)
- **Pop-up/hover to manage complexity**: keep the primary design clean; reveal detail only on demand (p.47)
- **Unit translation**: convert abstract numbers into human-scale units to make magnitude visceral (p.25, p.37)
- **Radial category wheel**: encode category membership spatially and with color for many items simultaneously (p.47)
- **Cluster bubble network**: show hierarchical ownership/membership through spatial proximity of sized circles (p.45)

---

### Idea: The Yield–Biodiversity Trade-Off as a Contextual Circle Comparison (inspired by p.30–31)

- **Basic visuals combined:** Proportional circle comparison (like the internet users vs. US population circles) + scatter plot positioning
- **What the combination adds:** A plain scatter plot shows the yield vs. biodiversity correlation but gives no visceral sense of *how much* biodiversity is lost. By replacing each scatter point with a proportional circle whose area encodes total species richness, the viewer simultaneously reads the yield-biodiversity correlation (position) and the absolute biodiversity magnitude (circle size). A scatter plot alone cannot show that some high-yield sites have dramatically fewer species in absolute terms.
- **Data manipulation applied:** Normalize species richness to max observed value; compute mean yield across 3 years; color-code circle by management intensity cluster (low/medium/high dominance)
- **Marks:** Circles (one per site)
- **Channels:** X-position = mean coffee yield; Y-position = total species richness; Circle area = total species richness (redundant encoding reinforces the magnitude); Color hue = coffee dominance level (management intensity, 3 categories)
- **User task supported:** Spot trade-off, compare, find outliers
- **What it shows for our data:** The inverse relationship between yield and total biodiversity across 60 sites; outlier sites that achieve both moderate yield and high richness; how management intensity (dominance) tracks with both
- **Persona it serves:** Sofia Almeida — directly answers "Is the trade-off real and visible?" and "Are there any sites that manage both high yield and high biodiversity?"; also useful for Elena Novak to assess correlation structure
- **Interaction if needed:** Hover over any circle to reveal the site's species breakdown by plant group (woody/herbaceous/bryophytes) as a small stacked bar — this reveals which group drives the richness difference
- **Page reference:** p.30–31

---

### Idea: Site Performance Dashboard — "Tower of Sites" Ranked Strip (inspired by p.37–38)

- **Basic visuals combined:** Ranked bar chart (sites ordered by yield) + small glyph profile attached to each bar
- **What the combination adds:** A ranked bar chart tells Hana which sites are strong vs. weak in yield, but not *why*. Attaching a small multivariable glyph (a mini radar or stacked icon) to the end of each bar adds the "why" — which management variables characterize that site's rank. Neither the bar alone nor the glyph alone answers both questions simultaneously.
- **Data manipulation applied:** Rank 60 sites by mean 3-year yield; compute z-scores for management variables (coffee structure index, density, dominance) to normalize them for the glyph; assign each site to its shrub cluster group (A/B/C/D from cluster analysis)
- **Marks:** Horizontal bars (sites), small stacked bar or radar glyphs at bar end (management profile)
- **Channels:** Bar length = mean yield (most important variable for Hana, so gets the most accurate channel); color hue of bar = shrub cluster group (categorical identity); glyph segment lengths = normalized management variable values; position on Y axis = rank order
- **User task supported:** Rank, compare, identify what distinguishes top performers
- **What it shows for our data:** Which of the 60 sites are top/bottom performers; what management profile and shrub cluster tends to appear in top-performing sites vs. bottom-performing sites
- **Persona it serves:** Hana Abebe — directly answers "Which sites are strong vs. weak?" and "Which conditions are associated with higher production?"; the glyph answers "What can I act on?"
- **Interaction if needed:** Click any bar to expand to a full site profile page showing all 7 shrub morphology variables and 3-year yield stability; hover to show exact yield value and species richness count
- **Page reference:** p.37–38

---

### Idea: Biodiversity Gradient Heatmap — Species × Sites Sorted by Yield (inspired by the contextual comparison principle, p.29–31)

- **Basic visuals combined:** Heatmap (presence/absence matrix of 407 species × 60 sites) + yield gradient bar along the top column axis
- **What the combination adds:** A presence/absence matrix alone is a pattern-finding tool but gives no context about what drives the pattern. Sorting columns (sites) by ascending yield and adding a color-gradient bar at the top that shows yield level turns a static matrix into a gradient-revealing tool. Rows (species) can then be clustered by whether they appear more in the left (low-yield) or right (high-yield) columns. Neither the matrix alone nor the bar alone makes the species-tracking-yield pattern visible.
- **Data manipulation applied:** Sort 60 sites (columns) by mean yield; for each of the 407 species (rows), compute a "yield association score" = mean yield of sites where species is present; sort rows by this score to bring high-yield-associated species to the top and low-yield-associated species to the bottom; group rows by plant group (woody/herbaceous/bryophyte)
- **Marks:** Small rectangles (matrix cells); a color-gradient strip at the top (yield bar); row group separator lines
- **Channels:** Cell color (present = dark, absent = light — presence/absence); column position = yield rank of site; row position = species yield-association rank; row color band (left margin) = plant group category
- **User task supported:** Explore, identify which species track yield vs. avoid yield, spot community composition changes
- **What it shows for our data:** Which species are found predominantly in high-yield vs. low-yield sites; which plant group (woody/herbaceous/bryophyte) has the most species sensitive to yield gradient; which sites cluster together in species composition
- **Persona it serves:** Sofia Almeida — answers "Which specific species are only found at low-yield (biodiverse) sites?" and "Which plant group is most sensitive to management intensity?"; Elena Novak — answers "Which variables would I prioritize measuring?"
- **Interaction if needed:** Hover over any cell to show species name, plant group, site yield, and site management intensity; click a species row to highlight all sites where it occurs; filter by plant group to reduce row count
- **Page reference:** p.29–31 (context comparison principle), inspired by sorting technique

---

### Idea: Radial Wheel of Species by Yield Association (inspired by VinTank radial category wheel, p.47)

- **Basic visuals combined:** Radial category wheel + magnitude encoding via distance from center
- **What the combination adds:** The standard radial wheel groups items by category but does not encode a second quantitative variable. By placing each species at a distance from the center proportional to the average yield of sites where it occurs, the wheel simultaneously shows species membership in plant group (angular sector = color) AND its yield association (radial distance = yield). Neither a plain categorical wheel nor a simple scatter achieves this together.
- **Data manipulation applied:** Use the "species × yield" dataset directly: for each of the 407 species, compute mean site yield and site count; filter to species occurring in at least 3 sites to avoid noise; group by plant group (4–5 categories = angular sectors)
- **Marks:** Dots (each dot = one species), sector wedges (plant group areas)
- **Channels:** Angular sector (plant group — categorical); radial distance from center (mean yield of sites where species occurs — quantitative); dot size (number of sites species occurs in — quantitative); color hue (plant group, redundant with sector for clarity)
- **User task supported:** Identify which species are associated with high yield vs. low yield; compare plant groups by their yield association distribution; find species that are both widespread and yield-associated
- **What it shows for our data:** Which plant groups contain species most strongly associated with high or low yield; whether there are species that are both common (large dots) and yield-associated (outer ring); which species are rare but occur only in high-yield sites (small dots, far out)
- **Persona it serves:** Hana Abebe — "Which individual species are most strongly associated with high yield?"; Sofia Almeida — "Which species are only found at low-yield (biodiverse) sites?" (innermost dots of each sector)
- **Interaction if needed:** Hover over any dot to reveal species name, plant group, site count, and mean yield; toggle plant groups on/off; click a species dot to highlight the 60-site strip and show which sites contain it
- **Page reference:** p.47

---

### Idea: "Underskin"-Style Body of a Coffee Site — Multilayer System Map (inspired by Underskin subway map, p.33–34)

- **Basic visuals combined:** Thematic layer diagram (like the Underskin subway map) + site-level comparison via small multiples
- **What the combination adds:** The Underskin approach maps multiple parallel systems through a shared spatial structure. For a coffee site, the "body" is the site itself: one canonical site diagram shows the layers of the agroforest (canopy / coffee shrub layer / ground layer / bryophyte layer), with colored lines for each plant group running through the layers, and management intensity shown as a separate overlay. By creating this diagram once and then showing it as a small multiple for 5–10 selected sites, the viewer can visually compare how the layer composition differs between high-yield and low-yield sites.
- **Data manipulation applied:** For each selected site: compute species richness per plant group per canopy layer (requires some simplification/grouping); compute management intensity score; assign site to yield quintile; show 5 sites across the yield spectrum as small multiples
- **Marks:** Lines (plant group "routes" through the site layers), nodes (major species abundance peaks), rectangles (management intensity overlay)
- **Channels:** Color hue (plant group category); line thickness (relative abundance/frequency); position (vertical = canopy layer, horizontal = arbitrary left-right); background shade (management intensity — light = low intensity, dark = high intensity)
- **User task supported:** Explore, compare, spot pattern across yield gradient
- **What it shows for our data:** How the structure of the biological community changes from low-yield (diverse, multi-layered) to high-yield (simpler, management-dominated) sites
- **Persona it serves:** Sofia Almeida — makes the community composition change "visible and hard to deny" across a yield gradient; Elena Novak — reveals which layers show the most structural change
- **Interaction if needed:** Static version works for 5 sites; interactive version allows selecting any of the 60 sites and sliding along the yield axis to animate the layer composition change
- **Page reference:** p.33–34

---

### Idea: Yield Stability Strip Chart — Three-Year Lines per Site (inspired by multi-line chart and contextual comparison, p.19–20, p.29)

- **Basic visuals combined:** Strip/dot plot (sites ranked by mean yield) + small sparkline per site (3-year yield trajectory)
- **What the combination adds:** Ranking sites by mean yield answers Hana's question about which sites are strong performers, but hides whether their yield is stable or volatile across the three years. Embedding a 3-point sparkline inside the site strip shows variability without adding a separate chart. Neither the ranking strip alone nor a standard line chart of all 60 sites simultaneously achieves this.
- **Data manipulation applied:** Compute mean yield and standard deviation across 3 years per site; rank sites by mean yield; for each site, normalize the 3 years to show the trajectory (up/down/flat); optionally flag sites where year-to-year variance exceeds 1 SD as "unreliable"
- **Marks:** Dots (mean yield position), small 3-point line (sparkline of 3 years), optional colored flag (stable vs. volatile)
- **Channels:** X-position = mean yield (primary variable); Y-position = rank order; sparkline shape = year-to-year stability; color of sparkline = stable (cool) vs. volatile (warm); dot size = optional (shrub cluster group)
- **User task supported:** Compare, rank, identify reliable vs. unreliable producers
- **What it shows for our data:** Which sites are both high-yield AND stable (double winners for Hana); which sites have high mean but extreme variance (risky); whether high-yield sites tend to be more or less stable than low-yield sites
- **Persona it serves:** Hana Abebe — directly answers "Is yield stable across years, or are some sites unreliable producers?"; Elena Novak — "How strongly do the 3 yearly yield measurements agree? Is the mean a reliable proxy?"
- **Interaction if needed:** Hover to reveal the three exact yield values; click to see full site profile; filter to show only sites in a selected shrub cluster group
- **Page reference:** p.19–20, p.29

---

### Idea: Management–Biodiversity Tension Bar — The Trade-Off as a Diverging Structure (inspired by contextual comparison principle and waffle chart approach, p.29–32)

- **Basic visuals combined:** Diverging bar chart (biodiversity left, yield right) + color gradient encoding management intensity
- **What the combination adds:** A diverging bar chart where each row is one site, left bars show total species richness (biodiversity) and right bars show mean yield, makes the trade-off structure literally visible as a visual divergence. Sites with long left bars tend to have short right bars. Adding a color gradient to each bar (from low to high management intensity) adds the third dimension — showing that management is the mechanism of the trade-off. No single standard chart type achieves all three simultaneously.
- **Data manipulation applied:** Normalize yield and species richness to the same 0–100 scale so bar lengths are comparable; sort rows by yield (ascending left to right); assign each site to a management intensity tier (low/medium/high dominance) for color
- **Marks:** Horizontal bars (left = species richness, right = yield)
- **Channels:** Bar length left = species richness (biodiversity); bar length right = mean yield; color hue = management intensity (three tiers — cool = low intensity, warm = high intensity); position (Y) = site rank by yield
- **User task supported:** Spot trade-off, compare, identify sites that break the pattern
- **What it shows for our data:** The yield–biodiversity trade-off as a structural pattern across all 60 sites; whether management intensity consistently tracks the trade-off; outlier sites that have above-average on both sides
- **Persona it serves:** Sofia Almeida — makes the trade-off "visible and hard to deny"; the diverging structure is emotionally legible and argumentatively strong; Hana Abebe — shows which management tier tends to produce high yield
- **Interaction if needed:** Hover to reveal site name, exact yield, exact species richness, and management variables; click to drill into the full species composition of a site; toggle to show only one plant group's richness on the left bar
- **Page reference:** p.29–32
