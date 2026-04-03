# [agent_16] Visualization Analysis and Design — pages 1-50

## Creative Combined Visualization Ideas
### Dataset: 60 Ethiopian coffee agroforest sites
### Core tension: Higher yield = lower plant biodiversity

---

## Theoretical basis from pages 1-50

Before the ideas: key principles from these chapters that directly inspire each design.

- **Anscombe's Quartet principle (p.7–8)**: Summary statistics hide structure. Show the data in detail, not just averages. Our dataset has 3 years of yield — showing all three may reveal something that mean alone hides.
- **Derive principle (p.50–53)**: "Don't just draw what you're given; decide what the right thing to show is, create it with transformations, and draw that." We can derive yield stability (variance across 3 years), yield change (year 3 − year 1), species loss rate, biodiversity-weighted yield.
- **Chained instances (p.17)**: Design sequences where the output of one view (e.g., a site cluster) becomes the input to the next (species composition of that cluster).
- **Task framework (p.45–57)**: Different personas need different query scopes — Hana needs compare (rank sites), Sofia needs summarize+present (overview of trade-off), Elena needs explore+identify (outliers, correlations).
- **Direct encoding of derived attributes (p.52, Figure 3.5)**: Instead of showing yield AND richness and asking users to compare, show the derived trade-off score directly.
- **Discover vs. Present (p.46–47)**: Sofia needs a present idiom; Elena needs a discover idiom; Hana needs both.

---

## Idea 1: The Yield-Biodiversity Trade-Off Scatterplot with Cluster Coloring (inspired by p.7–8, p.52)

### Idea: Trade-off plot — Anscombe's lesson applied to coffee sites

- **Basic visuals combined:** Scatterplot + color encoding of cluster group + size encoding of site area or coffee density
- **What the combination adds:** The scatterplot shows the core tension (yield vs. total species richness) for all 60 sites at once; the cluster color reveals whether high-yield clusters are structurally different from low-yield clusters; this answers: "Is the yield-biodiversity trade-off uniform, or do some management types escape it?"
- **Data manipulation applied:** Derive mean yield across 3 years; derive total species richness from the four groups; use cluster assignment from Coffee_structure_index_variables.xlsx as a categorical color attribute
- **Marks:** Points (sites as items)
- **Channels:** Position x = mean coffee yield (quantitative — most accurate channel for comparison); position y = total species richness (quantitative); color hue = cluster group (categorical — 4-5 groups); size = coffee plant density (quantitative, optional)
- **User task supported:** Explore (find outlier sites that are high in both); Compare (does one cluster dominate the upper-left "high yield + low biodiversity" region?); Identify (which specific sites are exceptions?)
- **What it shows for our data:** If clusters separate cleanly along the trade-off line, management type determines both yield and biodiversity simultaneously. If outlier sites exist (high yield AND high richness), those are the most interesting cases to investigate further.
- **Persona it serves:** Elena (correlation structure, clusters, outliers); Sofia (the trade-off made undeniable); Hana (which sites are the top performers?)
- **Interaction if needed:** Hover to label site; click to filter to that cluster; toggle between total richness and individual groups (woody/herbaceous/bryophytes)
- **Page reference:** p.7–8 (Anscombe — show detail, not summaries), p.52 (direct encoding of derived variable)

---

## Idea 2: The Three-Year Yield Stability Plot — Anscombe's Quartet Applied to Sites (inspired by p.7–8)

### Idea: Yield stability strip — are 3 yield years "essentially the same"?

- **Basic visuals combined:** Dot plot (each site = 3 dots, one per year) + connecting lines between same-site dots + color encoding of cluster
- **What the combination adds:** Shows whether yield is stable (tight dots) or variable (spread dots) per site, and whether certain clusters are more stable than others. This directly answers Elena's question: "Are the 3 yield years essentially the same?" without averaging away variation.
- **Data manipulation applied:** Use the 3-year yield columns separately (not averaged); derive yield range per site (max − min across 3 years) as a derived quantitative attribute encoding stability; sort sites by mean yield
- **Marks:** Points (3 per site — one per year), Lines (connecting same-site dots across years)
- **Channels:** Position x = site (ordered by mean yield — categorical/ordinal key); position y = yield value (quantitative); color hue = cluster group (categorical); line length = yield range = instability
- **User task supported:** Identify (which sites are unstable?); Compare (are some clusters more variable?); Summarize (is stability correlated with yield level?)
- **What it shows for our data:** If high-yield sites also have high year-to-year variance, the 3-year mean may mislead. Semantically novel: a standard connected dot plot used to answer a methodological question about data quality and reliability.
- **Persona it serves:** Elena primarily (methodological rigor, variability); also Hana (trust in yield rankings)
- **Interaction if needed:** Sort by range instead of mean to find most unstable sites; filter to one cluster at a time
- **Page reference:** p.7–8 (Anscombe — summaries hide structure; show data in detail)

---

## Idea 3: The Biodiversity Breakdown Stacked Bar — What Kind of Richness? (inspired by p.52, p.57)

### Idea: Species richness decomposition — stacked bar ordered by yield

- **Basic visuals combined:** Stacked bar chart (sites ordered by yield) + color encoding of species group type (woody/herbaceous/bryophyte/total)
- **What the combination adds:** A stacked bar ordered by yield shows not only total richness but which type of species disappears first as management intensifies. This answers Sofia's question: "Which species disappear as management intensifies?" for entire groups, not individual species.
- **Data manipulation applied:** Merge Plant_species_richness.xlsx (richness by group) with Coffee_yield.xlsx (mean yield); sort sites by ascending yield; the stacking shows part-whole composition of biodiversity
- **Marks:** Bars (one per site); stacked areas (one per species group)
- **Channels:** Position x = site (ordered by ascending mean yield — ordinal key); bar height = total species richness (quantitative); color hue = species group (categorical: 4 groups); bar segment height = richness of that group
- **User task supported:** Summarize (overview of all sites); Compare (how does species composition change across the yield gradient?); Browse (examine a particular yield region)
- **What it shows for our data:** If herbaceous species disappear earlier in the yield gradient than woody species, this points to different management pressures. The ordering by yield turns a static bar chart into a gradient story — semantically novel role for a standard idiom.
- **Persona it serves:** Sofia (persuasive overview of trade-off, grouped for presentation); Hana (where do high-yield sites sit relative to others?)
- **Interaction if needed:** Toggle stacking to show each group separately; highlight a single species group; filter to high-yield sites only
- **Page reference:** p.52 (derive and encode directly); p.57 (the How framework — arrange by key)

---

## Idea 4: Site Profiles as Parallel Coordinates — All Variables at Once (inspired by p.57, p.44)

### Idea: Parallel coordinates of all management + biodiversity + yield variables

- **Basic visuals combined:** Parallel coordinates plot + cluster color coding + yield highlighted as a special axis
- **What the combination adds:** Shows all available variables (coffee structure index, density, dominance, 4 richness measures, mean yield, cluster) simultaneously for all 60 sites. Answers: "What combination of variables distinguishes top-yield sites?" — Hana's core question. Also reveals whether cluster assignment aligns with the full multivariate pattern.
- **Data manipulation applied:** Join all datasets by site; standardize each variable to [0, 1] for cross-axis comparison; place yield as the rightmost axis so the visual flows "toward yield"
- **Marks:** Lines (one per site, crossing all axes)
- **Channels:** Line path across axes (multivariate quantitative profile); color hue = cluster group (categorical); opacity = line density (to manage overplotting); selected lines highlighted in bold
- **User task supported:** Explore (find unusual site profiles); Compare (do cluster lines follow similar paths?); Identify (select a site and trace its full profile)
- **What it shows for our data:** Sites with high yield AND relatively high richness will show an unusual line pattern — crossing rather than following the general negative correlation. These are the sites of highest interest to both Hana and Sofia.
- **Persona it serves:** Elena (full correlation structure across variables; does cluster add information beyond density?); Hana (what makes a top site different across all variables?)
- **Interaction if needed:** Brush on yield axis to filter to top 20% yield sites; reorder axes to place correlated axes adjacent; click site line for full label and detail
- **Page reference:** p.44 (abstract task analysis — compare tasks require more sophisticated idioms); p.57 (the How framework — map + arrange)

---

## Idea 5: Species × Yield Dot Matrix — Which Species Signal High Yield? (inspired by p.50–53)

### Idea: Species occurrence matrix sorted by average yield association

- **Basic visuals combined:** Dot matrix (407 species × 60 sites presence/absence) + reordering by derived attributes + color stripe for site yield
- **What the combination adds:** Reordering species columns by "average yield of sites where species occurs" and reordering site rows by yield turns the presence/absence matrix into a pattern-revealing display. Species in the upper-left quadrant occur frequently in high-yield sites; lower-right species are rare and appear in low-yield sites.
- **Data manipulation applied:** From Plant_species_and_average_coffee_yield.xlsx: derive species-level average yield (already provided); from Total_species_composition.xlsx: presence/absence matrix; sort species by descending species-level average yield; sort sites by descending yield; add a color bar strip (top row = site mean yield)
- **Marks:** Filled dots or rectangles (presence); empty space (absence); color strip at top (quantitative site yield)
- **Channels:** Position x = species (ordered by yield association — derived ordinal); position y = site (ordered by site yield — ordered); color fill = presence (binary categorical: present/absent); top strip color saturation = site mean yield (quantitative)
- **User task supported:** Identify (which species are unique to high-yield sites?); Browse (which sites share a rare species?); Summarize (do high-yield sites have a distinct species composition?)
- **What it shows for our data:** If a block of species clusters in the upper-left corner with high co-occurrence in high-yield sites, those species are potential indicators or drivers of high yield — directly actionable for Hana and Sofia.
- **Persona it serves:** Sofia (undeniable visual proof of species loss along yield gradient); Hana (specific species to watch for on high-yield sites); Elena (is community composition structured or random along yield gradient?)
- **Interaction if needed:** Filter to only species occurring in more than N sites; hover on species to see its name, total presence count, average yield; click site to highlight its full species list
- **Page reference:** p.50–53 (derive principle — derived ordering transforms the encoding); p.57 (arrange by key)

---

## Idea 6: The "Yield vs. Richness Trade-Off Map" for Sofia — Designed for Presentation (inspired by p.46–47, p.51)

### Idea: Annotated trade-off plot for a specific persuasive presentation narrative

- **Basic visuals combined:** Scatterplot (yield vs. total richness) + bold annotation layer (trade-off line + quadrant labels) + specific sites labeled by name + cluster color
- **What the combination adds:** Unlike Idea 1 (designed for exploration), this version is **designed for presentation**. The trade-off relationship is annotated with a fitted line; the four quadrants are labeled ("Low yield, High biodiversity" etc.); a small number of named sites act as anchors for the story. The presenter guides the audience through the visual narrative.
- **Data manipulation applied:** Fit a linear regression of richness on yield; derive residuals to identify sites furthest above and below the trend line; annotate the 3–5 most extreme outliers by name
- **Marks:** Points (sites), Line (fitted trade-off trend), Shaded regions (quadrants), Text labels (key sites)
- **Channels:** Position x = yield (quantitative); position y = total species richness (quantitative); color hue = cluster (categorical); text labels = site identifiers for key outliers
- **User task supported:** Present (guided narrative); Identify (named sites as specific examples); Summarize (the overall trade-off pattern)
- **What it shows for our data:** Makes the negative correlation between yield and richness undeniable as a single, clean visual argument. The annotated outliers give Sofia talking points: "This site has high yield AND high biodiversity — what makes it different?"
- **Persona it serves:** Sofia exclusively — designed as a persuasive presentation visual
- **Interaction if needed:** None required (static is fine for presentation); optional: click quadrant to highlight all sites in that quadrant
- **Page reference:** p.46–47 (present goal — communicating known information; guided audience through cognitive operations)

---

## Idea 7: Chained Instance — Cluster Profiler (inspired by p.17, p.51–53)

### Idea: Two-step chained analysis: cluster overview → species composition detail

- **Basic visuals combined:** Step 1: Scatterplot (yield vs. total richness, cluster-colored) as overview → Step 2: On cluster selection, a grouped bar chart showing mean richness per species group and mean yield for that cluster
- **What the combination adds:** Implements the chained instance concept: output of Step 1 (cluster selection) becomes input to Step 2 (cluster profile). The combination answers: "What is the biodiversity and yield profile of each management cluster?"
- **Data manipulation applied:** Aggregate by cluster: mean yield, mean richness per group, SD of yield; derive a "cluster profile" summary table
- **Marks:** Step 1: Points; Step 2: Bars (grouped per species type)
- **Channels:** Step 1: Position (yield × richness), color hue (cluster); Step 2: Bar length (mean richness/yield), color hue (species group type), error bars (SD)
- **User task supported:** Explore → Identify (Step 1 explores clusters visually; Step 2 identifies what defines each cluster); Compare (compare two clusters by selecting both)
- **What it shows for our data:** Answers: "Does cluster add information beyond coffee_density?" (Elena) by showing whether clusters differ in more than just yield, or also in species composition structure.
- **Persona it serves:** Elena (methodological — does the cluster variable add new information?); Hana (what kind of sites are in the top-yield cluster?)
- **Interaction if needed:** Click cluster in Step 1 to populate Step 2; shift-click for multi-cluster comparison; toggle between showing individual sites vs. cluster means
- **Page reference:** p.17 (chained instances — output of one becomes input to next), p.51–53 (derive — cluster-level aggregations as derived attributes)

