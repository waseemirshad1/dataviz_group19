# Data Visualization Knowledge — Synthesized Reference

> Synthesized from: Munzner *Visualization Analysis and Design* (VAD), Bremer & Wu *Data Sketches* (DS), Cairo *Cool Infographics* (CI), class examples on energy data (EC), and example student reports (ER).
> Sources cited inline as (VAD p.X), (DS p.X), (CI p.X), (EC p.X).

---

## 1. Goal and Function of Visuals

### Why Visualize at All?

- **Visualization augments human cognition** by offloading memory to the perceptual system. External representations speed search and recognition through spatial organization. (VAD p.6)
- **Vision is high-bandwidth**: massive parallel preattentive processing lets us absorb an overview in milliseconds. Sound is sequential and inferior for this. (VAD p.6–7)
- **Showing data in detail reveals structure hidden by summaries**: Anscombe's Quartet — four datasets with identical mean, variance, correlation, and regression line — look completely different when visualized. Never rely on statistics alone. (VAD p.7–8)
- The brain dedicates ~50% of resources to visual processing; we are hardwired for pattern recognition. Vision processes shapes, colors, movement, and spatial relationships in parallel. (CI p.27)
- **The Picture Superiority Effect**: text alone is recalled at ~10% after 3 days; text + relevant image at ~65% — a 650% improvement in retention. (CI p.32–33)

### Core Definition (Munzner)

> "Computer-based visualization systems provide visual representations of datasets designed to help people carry out tasks more effectively." (VAD p.1)

- Vis is appropriate when the goal is to **augment human capability**, not automate decisions. Use it when problems are **ill-specified** — when many possible questions exist and you don't know in advance which are correct. (VAD p.2)
- Vis serves multiple modes: exploratory analysis, presentation, algorithm debugging, monitoring. (VAD p.3–4)
- The design space is vast; most combinations are poor matches with human perception or the intended task. Good strategy: **satisfice** (find one of many good solutions), not optimize. Maintain a large consideration space and avoid fixating on the first idea. (VAD p.12–13)

### The Language of Context

- **"Data visualization is the language of context."** A single number without comparison is meaningless. A bar chart with one bar provides no insight; adding a second comparison value immediately makes the first meaningful. (CI p.29–30)
- **All data visualization is biased.** Every choice — which numbers to include, how far back to go, which comparison to make — introduces a designer's perspective. Acknowledge this. (CI p.30)
- The designer controls which comparison is included, which shapes perception. Example: 2.27 billion internet users compared to the US population (311M) feels enormous; compared to Earth's population (7B) it suddenly feels like a minority. Same data, different story. (CI p.30–31)

### When a Visualization Is Complete

- A good infographic communicates its key message in under **5 seconds** of skimming. (CI p.208)
- **Big fonts are not data visualizations.** Displaying a number in large type gives no context; each reader interprets it from their own perspective. The designer loses control of interpretation. (CI p.211)
- If data is important enough to include, it is important enough to visualize. (CI p.212)
- Reflect on purpose before designing or critiquing — exploratory vs. expressive goals call for different standards. (DS p.13–14)

---

## 2. Data Types — the "What"

Understanding data type is the first step of any vis design. Munzner's framework (VAD Ch. 2) is the standard reference.

### Five Basic Data Elements (VAD p.23)

1. **Items** — discrete entities (rows in a table, nodes in a network)
2. **Attributes** — specific measurable properties (salary, species richness, yield)
3. **Links** — relationships between items (network edges)
4. **Positions** — spatial locations in 2D or 3D space
5. **Grids** — sampling strategy for continuous data; defines cells in a field

### Four Dataset Types (VAD p.24–25)

| Dataset Type | Components | Example |
|---|---|---|
| **Tables** | Items + Attributes | Spreadsheet: rows = sites, columns = variables |
| **Networks** | Nodes + Links + Attributes | Social graph, species co-occurrence network |
| **Fields** | Grids + Positions + Attributes | Temperature map, satellite imagery |
| **Geometry** | Positions only | Geographic outlines, topographic surfaces |

### Attribute Types (VAD p.31–33, p.56–59)

```
Attributes
├── Categorical (nominal) — no implicit ordering (species names, plant groups)
└── Ordered
    ├── Ordinal — ordering without full arithmetic (rankings, survey scales)
    └── Quantitative — supports arithmetic (height, yield, temperature)
          ├── Sequential — min to max (mountain heights)
          ├── Diverging — two directions from a zero point (deviation from average)
          └── Cyclic — wraps around (hour of day, month of year)
```

- **Key vs. value semantics**: Key attributes are independent indices used to look up items (like row ID or time); value attributes are dependent measurements. This distinction determines idiom choice. (VAD p.34–37)
- Attributes can have **hierarchical structure**: day → week → month → year; postal code → city → country. (VAD p.33)

### The Derive Action — a Critical Design Step

- **Do not just draw what you are given.** Actively decide what to show; create it with transformations; draw that. (VAD p.51, 76)
- Derived attributes can: change type (quantitative → ordinal → categorical), compute new quantities (trade balance = exports − imports), or transform dataset type (table → network via similarity scores). (VAD p.50–53)
- Encoding the derived quantity directly (e.g., a difference score) is easier to perceive than requiring users to compute differences mentally from two raw curves. (VAD p.77–78)
- Examples of worthwhile derivations: hierarchical clustering as a key for reordering a heatmap; log-transforming a scatterplot axis to reveal hidden linear correlations; computing a composite score to rank items; converting time-series to cumulative form. (VAD p.147, 160; EC p.1)

---

## 3. Marks and Channels

### Core Definitions

- **Marks** are geometric primitives used to represent data items: points, lines, areas, volumes, connections. (VAD p.95–99; DS p.48)
  - Points/dots — individual items (one site, one species)
  - Lines — connection or trend over time
  - Areas/regions — magnitude or enclosure
  - Bars — quantity along an axis (a constrained line)
  - Glyphs — custom shapes encoding multiple variables at once (e.g., a battery where fill = quantity)
- **Channels** are appearance properties that carry meaning: position, length, angle, area, color hue, saturation, luminance, shape, motion, curvature. (VAD p.95–99; DS p.48)
- **Mapping rules** (DS p.48):
  - Quantitative attributes → positions (x, y, angle), sizes, continuous color scales
  - Categorical attributes → shapes and discrete color hues

### Full Channel Rankings (VAD p.101–102, Figure 5.6)

**Magnitude channels (for ordered / quantitative data) — most to least effective:**

1. Position on common (aligned) scale
2. Position on unaligned scale
3. Length (1D size)
4. Tilt / angle
5. Area (2D size)
6. Depth (3D position)
7. Color luminance
8. Color saturation
9. Curvature
10. Volume (3D size)

**Identity channels (for categorical data) — most to least effective:**

1. Spatial region
2. Color hue
3. Motion
4. Shape

**Key insight**: Spatial position appears at the top of BOTH lists. It is the only channel effective for both ordered and categorical data. The attribute encoded with position dominates the user's mental model more than any other channel. (VAD p.101–102)

### Channel Properties — Five Criteria

**Accuracy** (VAD p.103–105): Stevens' Power Law — perceived sensation scales as physical intensity raised to a power n. Length has n=1.0 (perfectly linear perception). Area has n≈0.7 (underestimated). Volume has n<0.7 (badly underestimated). Cleveland & McGill experiments confirmed: aligned position > unaligned position > length > angle > area; volume and curvature are worst.

**Discriminability** (VAD p.106): Each channel has a limited number of distinguishable bins. Line width works for 3–4 values; color hue ~6–12 bins for small separated marks; luminance ~3–5 bins; saturation ~3 bins. The number of attribute values must not exceed the available bins for the chosen channel — otherwise aggregate or switch channel.

**Separability** (VAD p.106–109): Some channel pairs can be attended to independently (separable); others fuse into a combined perception (integral). Position + color hue = fully separable. Width + height = perceived as area (integral). RGB red + green = perceived as a single fused hue. **Use separable channels when encoding two different attributes; use integral channels only when a single combined perception is desired.**

**Popout / Preattentive processing** (VAD p.109–111): A distinct item stands out immediately (parallel processing, time independent of set size) when it differs on a single channel: color hue, shape, size, tilt, proximity, motion. **Popout is NOT additive** — combining two differing channels usually eliminates popout and forces serial search. Only rely on popout for one channel at a time.

**Grouping** (VAD p.111–112): Strongest to weakest grouping cues: containment marks > connection marks > proximity (spatial region) > color hue / motion / shape. Proximity explains why spatial region ranks highest as an identity channel.

### Color in Depth

- Three separable color channels: **Luminance** (magnitude, for ordered data), **Saturation** (magnitude, for ordered data), **Hue** (identity, for categorical data). (VAD p.219)
- **RGB is computationally convenient but perceptually non-uniform** — do not use RGB for perceptual comparisons or interpolation. Use L\*a\*b\* (perceptually uniform) for any color computation. (VAD p.221–222)
- **HSL lightness L is not perceptually linear luminance** — a common mistake. (VAD p.221)
- Luminance contrast is the ONLY way to resolve fine detail and crisp edges. Hue contrast does not produce detectable edges. Text needs 10:1 luminance contrast ratio (3:1 minimum). (VAD p.223)
- **For small marks** (points, lines): use high saturation, bright colors. **For large background areas**: use low saturation (pastels). (VAD p.224, 252)
- Hue discriminability: ~6–12 bins for small separated regions; up to ~21 bins for large contiguous areas. Include background and default colors in the count. (VAD p.251–254)
- **Colorblind-safe design**: Red-green color blindness affects ~8% of males. Always vary luminance or saturation in addition to hue. Avoid red-green diverging colormaps. Use simulators to check. (VAD p.260)
- **Avoid rainbow colormaps**: (1) hue has no implicit ordering — it is an identity channel used for magnitude data; (2) perceptually non-linear — equal numeric ranges look unequal; (3) fine detail cannot be perceived via hue. Prefer monotonically increasing luminance colormaps. (VAD p.257–258)
- **Colormap type must match data type**: categorical → categorical colormap; sequential ordered → sequential colormap (one hue, varying luminance); diverging ordered → diverging colormap (two hues, neutral midpoint). (VAD p.225)

### Weber's Law and Relative Perception (VAD p.112–114)

- Perception is based on relative differences, not absolute ones. The detectable difference is a fixed percentage of the reference magnitude. This is why aligned bars (common baseline) are more accurate than unaligned bars — the unfilled frame creates a large relative difference to judge.
- Color and luminance perception are entirely contextual: the same gray looks different depending on its surroundings (checkerboard illusion). Color channels are unreliable for precise quantitative encoding.

---

## 4. Task Abstraction — the "Why"

### Why Abstract Tasks?

Domain-specific language obscures what idiom would work. "Contrast prognosis between patient groups" and "see if tissue sample results match" are both "compare values between two groups." Translating to abstract vocabulary enables reuse of solutions across domains. (VAD p.43–44, 68–69)

### Three-Level Action Hierarchy (VAD p.45–55)

**Level 1: Analyze (high-level)**

| Action | Description |
|---|---|
| Discover | Find new knowledge; generate or verify hypotheses; open-ended exploration |
| Present | Communicate already-known information to an audience; tell a story |
| Enjoy | Casual, curiosity-driven encounter |
| Annotate | Add graphical or textual annotation to existing vis elements |
| Record | Save persistent artifacts: screenshots, bookmarks, logs |
| Derive | Create new data attributes from existing ones |

**Level 2: Search (mid-level)**

| Type | Target known? | Location known? |
|---|---|---|
| Lookup | Yes | Yes |
| Locate | Yes | No |
| Browse | No | Yes |
| Explore | No | No |

**Level 3: Query (low-level)**

| Query | Scope |
|---|---|
| Identify | One target — retrieve characteristics of a single item |
| Compare | Multiple targets — requires more sophisticated idioms |
| Summarize | All targets — overview of the entire distribution |

### Targets (VAD p.55–57)

- **All data**: Trends, Outliers, Features
- **Single attribute**: Individual value, Extremes (min/max), Distribution
- **Multiple attributes**: Dependencies, Correlations, Similarities
- **Network data**: Topology, Paths
- **Spatial data**: Shape

---

## 5. Task-Encoding Fit

The core design question: given what the user needs to **do** with a variable, which channel best supports that action?

### Fundamental Pairings

| User task | Best encoding | Rationale |
|---|---|---|
| **Compare** values | Position (aligned scale) or Length | Most accurate magnitude channels |
| **Rank** items | Sorted position along a common axis | Sorting exploits the highest-ranked channel |
| **Identify** categories | Color hue or Shape | Identity channels — highest ranked after spatial region |
| **Spot overall trend** | Position along a common scale | Perceptually most accurate for ordered data |
| **See magnitude** | Length or Area | Area is less precise; use length for exact comparison |
| **Find outliers** | Position + Color (redundant encoding) | Dual channels maximize salience |
| **Show part-to-whole** | Stacked bars or Treemap | NOT pie charts when precision matters |
| **Show correlation** | Scatterplot (two quantitative axes) | Both axes express quantitative values |
| **Show distribution** | Histogram, Boxplot, Beeswarm | Each reveals a different distributional property |
| **Show change over time** | Line chart (ordered key) | Connection marks imply ordered trend |
| **Compare distributions** | Boxplot or Violin plot per category | Summarizes distribution per group |

### Key Expressiveness Rules

- Use **magnitude channels for ordered data** only (position, length, area, angle, luminance, saturation). Using them for categorical data implies a false ordering. (VAD p.101)
- Use **identity channels for categorical data** only (color hue, shape, spatial region). Using hue for ordered data is incorrect — hue has no implicit ordering. (VAD p.101)
- **Line charts only for ordered keys**, never for categorical keys. Zacks & Tversky study: line charts on categorical axes elicit false "trend" answers from viewers. (VAD p.156–157)
- **Pie charts**: only appropriate for a few slices (2–4) showing rough part-to-whole. Angle judgements are less accurate than length. A normalized stacked bar chart does the same job with higher accuracy. (VAD p.168–170; CI p.199–200)

### Common Task-Encoding Mismatches

| Mistake | Why it fails | Fix |
|---|---|---|
| Pie chart for multi-select survey data | Values do not sum to 100%; pie shows parts of a whole | Use a bar chart |
| Line chart for categorical key | Implies false ordering | Use bar chart or dot chart |
| 3D bars for abstract data | Perspective distortion; harder to read | Use 2D bar chart |
| Radial layout for non-cyclic data | Angle channel implies cyclicity | Use rectilinear layout |
| Rainbow colormap for ordered data | No perceptual ordering in hue | Use sequential luminance colormap |
| Size encoding for primary comparison | Area is less accurate than length | Put primary variable on position/length axis |
| Single pie chart with no comparison | No context; reader supplies their own | Add a second comparison value |

### Redundant Encoding

Encoding the same variable with two channels simultaneously (e.g., position + color) improves accuracy and accessibility, especially for finding outliers or for colorblind users. It costs no extra visual complexity when channels are separable. (VAD p.101; CI p.161–162)

### Radial vs. Rectilinear Layouts (VAD p.166–170)

- Radial layouts are mathematically equivalent to rectilinear but **perceptually not equivalent**: angle is less accurate than aligned position, and the cyclic nature misleads when data is not cyclic.
- When to use radial: when data is inherently cyclic (hours, months, seasons), or when one attribute is more important (goes in sectors) and the other less so (goes in rings). (VAD p.170; EC p.1)
- When time is encoded radially, **map time to angle** (equal arc lengths for equal time units). Mapping time to radius makes early periods smaller in circumference than late periods, misrepresenting equal intervals. (DS p.109)

---

## 6. Data Manipulation and Transformation

Worthwhile aggregations, transformations, and derivations — and which visual type suits each.

### Aggregation Operations

| Transformation | What it shows | Best visual form |
|---|---|---|
| Mean / median | Central tendency per group | Bar chart, dot chart |
| Distribution (all values) | Spread and shape | Histogram, Boxplot, Beeswarm |
| Cumulative sum | Total burden over time; rate encoded as slope | Cumulative line chart |
| Ratio / proportion | Part-to-whole | Stacked bar, Treemap |
| Difference / delta | Change between conditions | Derived attribute on its own axis |
| Correlation (pairwise) | Relationship strength between two variables | Scatterplot, Heatmap cell |
| Ranking | Relative order of items | Sorted bar chart, Bump chart |
| Dimensionality reduction | Structure in high-dimensional space | Scatterplot (2D MDS/tSNE output) |
| Hierarchical clustering | Grouping by similarity | Cluster heatmap with dendrogram |

### When to Simplify or Abstract

- **Over-aggregating hides signal**: Anscombe's Quartet shows four datasets with identical summary statistics but radically different visual structure. Show distributions, not just means. (VAD p.7–8, 330)
- **Standard boxplots assume unimodal data**. For multimodal distributions, use a vase/violin plot (width encodes density). (VAD p.334–335)
- **Individual data points alongside summaries** (beeswarm + boxplot overlay) provides the best of both worlds — the distribution shape and the individual variation. (DS p.339)
- When too many items create visual noise: aggregate into bins (histograms), cluster into groups, or use a density-encoded continuous scatterplot. (VAD p.331–333)
- When too many attributes overwhelm: filter to the most relevant, use dimensionality reduction (PCA, tSNE, MDS) to synthesize new axes, or use small multiples to show subsets. (VAD p.339–345)
- **Bin size for histograms is critical and tricky**: the same data looks very different with different bin widths. Offer interactive control or compute bins from dataset characteristics. (VAD p.331)

### Sorting and Ordering

- **Sorting is a powerful manipulation** that exploits position — the highest-ranked channel — to reveal patterns. Always sort by a meaningful attribute, not alphabetically, when trend comparison is the task. (VAD p.150, 271)
- Main-effects ordering (sort rows/columns by median of derived attribute) makes both trends and outliers visible simultaneously. (VAD p.308)
- Order of partitioning in multi-level views dramatically changes which patterns are visible — always explore multiple orderings. (VAD p.311)

### Log Transformation

- Log-transforming scatterplot axes reveals hidden linear relationships in skewed data. The derived axis encodes orders-of-magnitude differences more legibly. (VAD p.147–148)

### Text and Linguistic Data

- Text cleaning pipeline: remove digits, punctuation, stop words; compute word counts; word cloud as first exploratory step. (DS p.153–154)
- Filtering to only nouns and adjectives (using NLP POS tagging) removes obvious common words and exposes more revealing signal. (DS p.281)
- Synonym collapsing before ranking: multiple source words mapping to the same concept must be merged for fair cross-group comparisons. (DS p.281–282)

---

## 7. Specific Visualization Idioms — When to Use Each

### Scatterplot (VAD p.146–148)

- **Data**: two quantitative value attributes, one item per mark.
- **Tasks**: find trends, outliers, distribution, correlation, clusters.
- **Augment with**: color hue (categorical), size (quantitative) → bubble plot. Regression line when correlation is the primary task.
- **Scale**: dozens to hundreds of items. For thousands, use continuous scatterplot (density colormap).
- **Limitation**: overplotting when items stack up. Fix with jitter, transparency, or density encoding.

### Bar Chart (VAD p.150–151)

- **Data**: one quantitative value + one categorical key. Line marks with aligned position.
- **Tasks**: lookup and compare values.
- **Key rule**: order by value attribute for trend detection; alphabetical ordering hides patterns.
- **Scale**: dozens to hundreds of categories.

### Stacked Bar Chart (VAD p.151–153)

- **Data**: one quantitative value + two categorical keys.
- **Tasks**: part-to-whole relationship, find trends.
- **Limitation**: only the bottom sub-bar is aligned to baseline — the others are harder to compare across bars. Order of stacking matters.
- **Scale**: main axis dozens–hundreds; stacked axis ~3–12 categories.

### Line Chart (VAD p.155–157)

- **Only for ordered keys** (time, continuous quantitative). Connection marks imply trend — violates expressiveness for categorical keys.
- Banking to 45°: adjust aspect ratio so slopes cluster near 45° for most accurate angle perception.

### Heatmap / Cluster Heatmap (VAD p.158–161)

- **Data**: two categorical keys + one quantitative value. Area marks colored by value.
- **Tasks**: find clusters, outliers; high-level overview; correlation between rows.
- **Cluster heatmap**: reorder rows and columns by hierarchical clustering; dendrograms on periphery.
- **Scale**: up to ~1 million cells; only 3–11 distinguishable color bins per cell (use sparse, distinguishable colormap).

### Parallel Coordinates (VAD p.163–166)

- **Data**: many quantitative attributes simultaneously.
- **Tasks**: overview of all attributes, find ranges, outlier detection.
- **Limitation**: axis ordering is critical — only neighboring axes show pairwise relationships clearly. Interactive reordering needed. Not effective for thousands of items (severe overplotting).
- SPLOMs are typically easier for correlation detection; parallel coordinates are better for range selection and overview.

### SPLOM — Scatterplot Matrix (VAD p.161–162)

- **Data**: all pairwise combinations of quantitative attributes.
- **Tasks**: find correlations across all attribute pairs.
- **Scale**: ~12 attributes, dozens–hundreds of items.

### Treemap (VAD p.213–214)

- **Data**: hierarchical data with quantitative leaf attribute.
- **Tasks**: spotting outliers of large attribute values; part-to-whole at each level.
- **Limitation**: poor for topological path tracing.
- **Scale**: up to 1 million leaf nodes.

### Node-Link Diagram (VAD p.201–208)

- **Tasks**: path tracing, finding shortest paths, adjacent nodes, topological structure.
- **Limitation**: hairball at high density (L > 4N rule: links should not exceed ~4× nodes). Nondeterministic force-directed layout prevents reliable spatial memory.
- Use matrix view for large dense networks; node-link for small or topologically interesting networks.

### Adjacency Matrix View (VAD p.208–209)

- **Tasks**: approximate node/edge count, most connected node, finding direct links.
- **Scale**: nodes up to 1,000; links up to 1 million.
- **Limitation**: path tracing is harder than in node-link.

### Boxplot (VAD p.333–335)

- Summarizes distribution to 5 derived values: median, lower/upper quartile, lower/upper fence. Outliers shown as explicit dots.
- Assumes unimodal data — use vase/violin plot if distribution may be multimodal.

### Choropleth Map (VAD p.181; CI p.234–235)

- Quantitative attribute encoded as color over geographic regions.
- Region granularity is a major design choice. Beware the Modifiable Areal Unit Problem: different aggregation boundaries produce dramatically different results. (VAD p.338)

### Radial Bar Chart / Polar Area Chart (VAD p.167–170)

- Like a bar chart but with radial layout; generally inferior to rectilinear for comparison tasks.
- Polar area chart (rose plot): varies wedge length rather than angle — more accurate than pie. Popularized by Florence Nightingale.

### Streamgraph (VAD p.153–155)

- Generalized stacked area chart with organic baseline; emphasizes continuity over time.
- Layer order computed algorithmically (by volatility or onset time).
- Good for categorical time-series with many categories that appear/disappear.

### Dense Pixel-Level Displays (VAD p.172–174)

- Use 1-pixel marks for maximum information density. Available channels at that scale: planar position and color only. Combine with zoomable detail view.

---

## 8. Combining and Faceting Views

### Why Combine Views

- No single encoding is optimal for all tasks. Linked multiple views allow the user to see how a spatial neighborhood in one encoding is distributed in another. (VAD p.290–291)
- Trade-off: display area (scarce external resource) vs. working memory (scarce internal resource). Juxtaposed views increase external resource use; animation increases internal load. (VAD p.291)

### Design Matrix for Coordinating Views (VAD p.301)

| Encoding | Data | Result |
|---|---|---|
| Same | Same | Redundant — avoid |
| Same | Subset | Overview–detail |
| Same | Partition | Small multiples |
| Different | Same | Multiform |
| Different | Subset | Multiform overview–detail |
| Different | No linkage | No linkage — avoid |

### Small Multiples (VAD p.298–299)

- Same encoding, different data partitions → common reference frame for comparison.
- Strength: simultaneous visibility; no memory load.
- Often preferable to animation for complex, spatially distributed changes.
- Operational limit: ~few dozen views × several hundred elements each.

### Superimposing Layers (VAD p.313–314)

- Maximum ~2–3 layers if layers contain substantial area marks. Many layers only work if each layer has very few marks (e.g., single lines).
- Use non-overlapping ranges of visual channels per layer. Check luminance contrast explicitly.
- Overlay blend modes can corrupt color channels when color encodes meaningful data. (DS p.211)

### Linked Highlighting / Brushing

- Selection in one view immediately highlights matching items in all other views. Core benefit: seeing whether a spatial neighborhood in one encoding is contiguous in another. (VAD p.265–270)
- Linked navigation: moving viewpoint in one view synchronizes others (VAD p.301).

### Overview–Detail

- Large view for detail exploration + small "bird's-eye" view for context.
- Rectangle in overview shows currently visible region in detail view. Bidirectional: rectangle in overview can also move the detail view. (VAD p.294–296)

### Partitioning Design Choices (VAD p.304)

1. How many splits to carry out
2. Which attributes to split by (and in which order)
3. Data-driven vs. predetermined number of views

Order of partitioning dramatically changes visible patterns — always explore multiple orderings.

### Trellis / Small-Multiple Matrix (VAD p.307–309)

- Partitions multiattribute data into a 2D matrix of views.
- Main-effects ordering (by median) makes outliers visible against general trends.

### Grouped vs. Small-Multiple Bar Charts (VAD p.306–307)

- Grouped bar chart: facilitates comparison **between attributes**.
- Small-multiple bar charts: facilitates comparison **within a single attribute**.

---

## 9. Interaction Design

### Why Interact

- Interactivity is the computer display's fundamental advantage over print. It enables dynamic response: filtering, zoom, linking, drill-down. (VAD p.269)
- Five major options for handling complexity (VAD p.269): (1) derive new data, (2) change view over time, (3) facet into multiple views, (4) reduce data shown, (5) embed focus+context.

### Shneiderman's Mantra (VAD p.135)

> "Overview first, zoom and filter, details on demand."

- Overview: show all items simultaneously to find regions worth drilling into. Used throughout exploration, not just at start.
- Three idiom families for overview+detail: (1) separate views, (2) single view with zoom/filter, (3) focus+context in one view.

### Hover / Detail-on-Demand

- Hover reveals detail without cluttering the primary design. The default state is clean; detailed state is accessible. (CI p.47; DS p.38, 43–44; VAD p.276–278)
- Expand hover target to a logical group when individual marks are too small — hovering tiny marks causes flicker. (DS p.111)
- Design hover as a reward for engaged users — a tooltip that tells a small story (trend line + word cloud) is far more valuable than one that just repeats the data point's value. (DS p.288)

### Filter (VAD p.325–328)

- Dynamic queries principle: display updates immediately when user changes a filter. Users cannot be expected to know which numbers to type — show options visually.
- "Out of sight, out of mind": users tend to forget about filtered-out items. Aggregation (showing a stand-in) is cognitively safer than removal.
- Scented widgets: augment standard filter controls with concise statistical graphics (bar charts in slider headers) to show the distribution before filtering.

### Selection (VAD p.274–278)

- What can be selected: items, links, attributes, levels of an attribute, views themselves.
- Highlighting methods: color change (most common; hides existing encoding temporarily), outline addition (preserves encoding; less salient), size change, motion coding (oscillation — empirically best [Ware & Bobrow 04]).
- Highlight must create visual popout — sufficient hue, luminance, or saturation contrast.
- Selection is often the first step in a chained sequence: the output becomes input to the next action (filter, aggregate, encode, navigate).

### Navigation (VAD p.279–286)

- **Geometric zooming**: object appearance is fixed, only size changes.
- **Semantic zooming**: representation adapts to available pixels — appearance can change dramatically (e.g., color-only at tiny scale, full axis labels at large scale).
- **Constrained navigation**: limits camera motion to prevent getting lost; auto-calculate trajectory to frame selected item.
- Slice, cut, project: reduce dimensionality of view to manage complexity.

### Responsiveness Thresholds (VAD p.137–140)

| Time constant | Value | Relevant for |
|---|---|---|
| Perceptual processing | 0.1 s | Screen updates |
| Immediate response | 1 s | Selection feedback, animated transitions |
| Brief tasks | 10 s | Task granularity chunks |

- System must provide visual feedback within the relevant time class. Progress indicators when crossing latency classes.
- Fluid interaction enables focus on mental model building. Latency mismatch "jars" users out of flow.

### Animated Transitions (VAD p.273–274; DS p.139)

- Benefits: maintain user context; show how items move from old to new positions.
- Limitations: only effective when the amount of change is limited. When many objects change simultaneously, even pause/replay does not help — change blindness takes over.
- Small multiples often outperform animation for complex, spatially distributed changes.
- Animated transitions are powerful for transitions between two states; video-style multi-frame playback has high cognitive load.
- **Scrollytelling design principle**: leave a static window in each section so the user can read text before the visualization changes. Simultaneous text + visualization movement is overwhelming. (DS p.139)
- **Steppers vs. scrollytelling**: auto-animate through steps but allow clicking a step to replay from that point — user retains pacing control. (DS p.310)

### Focus + Context (VAD p.347–366)

- Embed detailed information about a focus within a single view that also shows overview context.
- Three approaches: (1) Elide — filter some; summarize others; (2) Superimpose layers — local focus layer over background context; (3) Distort geometry — magnify focus, compress context.
- **Degree of Interest (DOI) function**: DOI = Interest(x) − Distance(x, focus). Items above threshold shown in detail; below threshold aggregated or elided. (VAD p.350)
- Distortion best for topological exploration where precise metric judgements are not needed. Continuous magnification (fisheye) can be disorienting; discrete two-level magnification (magnifying lens) is simpler but occludes.
- Guaranteed visibility: items with high importance are always visible regardless of scale — a custom aggregation strategy where geometric distance is a poor proxy for importance. (VAD p.357–358)

### Interaction Patterns from Practice (DS)

- **Bidirectional filtering**: support interaction from both categorical dimensions — "who was in this chapter?" and "which chapters did this character appear in?" (DS p.402)
- **Dead-end prevention**: disable filter options that would produce zero results rather than showing an empty state. (DS p.175–176)
- **Sidebar / graph as navigation**: a relationship graph that doubles as a navigation control — clicking a node switches the main view. (DS p.241)
- **Expand/collapse carousel**: when multiple items compete for space, expand the selected item and minimize the rest. (DS p.273–274)
- **Mini-map for long scrollable visuals**: a persistent small-scale overview panel showing current position in the whole. (DS p.225)

---

## 10. Design Process Guidance

### The What–Why–How Framework (VAD p.16–17)

Every visualization instance can be described along three dimensions:
- **What** data the user sees (data types, attributes)
- **Why** the user needs the vis (task abstraction)
- **How** the vis idiom is constructed (encoding choices)

Complex vis = chained sequences of instances where the output of one becomes the input to the next.

### The Four-Level Nested Model (VAD p.92–100)

1. **Domain situation** — who are the users, what do they do, what data do they have
2. **Task and data abstraction** — translate domain specifics into generic, domain-independent form
3. **Visual encoding and interaction idiom** — specific encoding and interaction choices
4. **Algorithm** — efficient computational implementation

Each level has its own validation methods and failure modes. Errors at upstream levels cascade to all downstream levels. The hardest stage to get right is usually abstraction — designers frequently skip it.

### Diverge → Emerge → Converge

- **Diverge**: generate many ideas independently before sharing. Wide variety of types and levels of complexity.
- **Emerge**: cluster ideas by theme/content. Use tools like Miro for spatial grouping. Multiple independent clustering criteria (by information content, by format) often reveal different patterns.
- **Converge**: compare within and across clusters; select the most promising; describe the full evolution from sketch to final design, including rejected options with reasons.
- Techniques to aid ideation: SCAMPER (Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse); matrix-based approaches; sketching to a friend to reveal logical errors. (DS p.65; ER report_2 p.2)

### Sketch Before You Code (DS p.67, 284)

> "If you can't make your design work logically on paper, it's definitely not going to work on the computer with the actual data."

- Sketch multiple alternatives before committing — the first idea is rarely the best. (DS p.33)
- Sketch the math too: place arrows, paths, and angles on paper to work out trigonometric formulas before coding.
- Use a tool with limited options so you stay focused on communicating the concept, not fine-tuning settings. (DS p.23)
- Find the "hardest step" first. If that step is impossible, change the design before over-investing. (DS p.34)

### Explore Data Before Designing (DS p.73, 106)

Shirley Wu's personal data exploration workflow:
1. Identify the "lowest" unit of data (one item, one observation)
2. List all attributes and tag each as quantitative / categorical / ordinal / temporal / spatial
3. Highlight interesting attributes
4. Formulate hypotheses and test with quick charts

Use standard charting tools (R/ggplot2, Vega-Lite, Observable) for rapid hypothesis testing — not custom code. Common exploration charts: **bar charts** for comparisons, **box plots/histograms** for distributions, **scatterplots** for correlations, **line charts** for temporal trends. (DS p.337)

### Precalculate Visual Variables (DS p.69, 162)

- Compute placement, rotation, offsets, sizes, and color assignments as separate "visual variables" in whatever language is easiest (R, Python), then pass them to the rendering tool (D3.js).
- Visual variables have no meaning in the original dataset — only in the layout. Separating this from rendering simplifies both.

### Check Your Data (DS p.64)

- Check sums, counts, averages against common sense. Compare against a second source. Use a proxy dataset to find gaps.
- Wrong data shows up as outliers in summary statistics. Missing data requires knowing what *should* be there.
- "Checking the accuracy of your data is a standard practice...not the most fun activity, is a lesson we have to constantly relearn."

### Iterative Failure Is Normal (DS p.393, 400; DS p.307)

- Design frequently involves spending hours on a technique that does not make the final cut. This is not wasteful — it teaches what does and does not work.
- When stuck, switch gears: "If I've been banging my head for a while, it's often more helpful to give it some space and work on something else."
- Peer feedback is a high-value, low-cost design intervention. Showing others an intermediate version often surfaces the most important insight or interaction improvement.

### Storytelling Structure

Three-part infographic story format (CI p.35–37):
1. **Introduction/Foundation** — introduce topic; tell audience why they should care; basic context visualizations
2. **Ah-Ha! The Main Event** — new, surprising insight; dominant visualization; triggers Picture Superiority Effect
3. **Conclusion/Call-to-Action** — wrap up; explicit next step for the reader

Monroe's Motivated Sequence for persuasive designs (CI p.85–86): Key message → Problem → Danger → Solution → What can I do?

### Apply Existing Styles to New Domains (CI p.33–34)

Applying a known design style to a new subject creates memorability through surprise. Example: subway map style applied to human body systems ("Underskin") went viral. The style was familiar; the subject was new.

---

## 11. Common Mistakes and Anti-Patterns

### Encoding Mistakes

- **Pie charts that don't sum to 100%**: the most common infographic error. Pie charts show parts of a whole; multi-select survey questions can never be shown as a pie. (CI p.199–200)
- **Sizing circles by diameter, not area**: if you triple the diameter, area becomes ~9× larger. Always calculate circle sizes by area. Formula: Radius = √(Area/π). (CI p.203–205)
- **3D for abstract data**: perspective distortion destroys positional accuracy; occlusion hides data; tilted text is illegible; depth perception follows a power law of n=0.67 — worse than area. 3D is only justified when the task requires understanding inherently 3D spatial structure. (VAD p.117–130)
- **Using the same channel for two different variables**: color already used for categories, then also used for a second category — visual confusion. Never use one channel for two attributes. (DS p.179)
- **Encoding ordered data with hue** (e.g., rainbow colormap): hue has no implicit ordering. (VAD p.257)
- **Encoding categorical data with magnitude channels**: implies a false ordering that does not exist in the data. (VAD p.101)
- **Integral channel pairs for independent attributes**: width × height perceived as area, not two separate dimensions. (VAD p.108)
- **Relying on popout for two channels simultaneously**: combining two differing channels usually eliminates popout. (VAD p.110)

### Visual Clutter and Overload

- **Too many elements without abstraction**: rendering every data item as a mark when there are thousands creates unmanageable visual noise. Aggregate into bins, clusters, or density encodings. (DS p.171)
- **Composing too many variables on one mark**: the filled circle + outer ring + dots-on-ring encoding was self-described as "overwhelming and confusing." Every channel must earn its place by answering a question the user actually has. (DS p.141)
- **Too many simultaneous animations**: if text and visualization both move during a transition, users don't know where to look. (DS p.139)
- **Hairball networks**: force-directed layout with more than ~4× links-to-nodes collapses into an unreadable cluster. (VAD p.206)
- **Overlapping area charts**: non-stacked overlapping areas are hard to read. Use stacking or step-curves. (DS p.239)
- **Overloading a chart format**: 56 sports in one circle made each medal only a few pixels wide — calculate physical fit before committing. (DS p.66)

### Cognitive and Perceptual Mistakes

- **No context**: a single value with no comparison provides no insight. The audience will fill in their own context, which may be wrong. (CI p.29)
- **Replacing context with big fonts**: large text showing a number gives no frame of reference. Always provide a second value for comparison. (CI p.211)
- **All data using identical chart styles**: audiences cannot distinguish designs and remember nothing. Every chart must be visually distinctive for the Picture Superiority Effect to work. (CI p.33; CI p.179)
- **Legends instead of inline labels**: chart legends force repeated back-and-forth eye movement. Embed labels directly into charts. (CI p.214–215)
- **Aggregating when you should show individuals**: stacked bar charts hiding individual variation that is the real story. Show individual points and layer summary statistics on top. (DS p.337–338)
- **Reciting facts instead of telling a story**: "The Hamilton project received poor reception because it stated data facts rather than telling a story or conveying personal meaning." (DS p.144)
- **Sketching before exploring data**: designing a visualization without checking if the data will support it leads to designs that fail when real data is plugged in. (DS p.106)

### Process Mistakes

- **Fixating on the first idea** without considering alternatives: increases probability of landing in a poor region of the design space. (VAD p.13)
- **Drawing what you are given** without considering derived attributes: limits the design space unnecessarily. (VAD p.51)
- **Making assumptions about user needs** rather than observing users. What users say they do ≠ what they actually do. (VAD p.94–95)
- **Implicitly skipping abstraction**: assuming the first abstraction that comes to mind is correct, then jumping to idiom design. (VAD p.96)
- **Too many data visualizations in one infographic**: visual noise, reader confusion — best designs limit to 3 or fewer. (CI p.137)

---

## 12. Practical Rules of Thumb

These are concrete, actionable guidelines from all sources.

### Channel and Encoding Rules

1. Match channel type to attribute type: magnitude channels for ordered data, identity channels for categorical data. (VAD p.101)
2. Encode the most important attribute with position. (VAD p.102)
3. Use length for accurate 1D comparisons; area for approximate magnitude; avoid volume for precise comparisons. (VAD p.104; CI p.203–205)
4. Number of attribute values must not exceed discriminable bins for the chosen channel. (VAD p.106)
5. Use separable channel pairs when encoding two independent attributes. (VAD p.108)
6. Rely on popout for one channel at a time only. (VAD p.110)
7. Assign primary importance to the most salient channel — largest marks should correspond to most important data. (DS p.196–197)
8. Use grey for missing data — a culturally understood signal for absent/null values. (DS p.197)
9. Small marks: high saturation colors. Large background areas: low saturation (pastels). (VAD p.224)
10. Colorblind-safe: always vary luminance or saturation in addition to hue; avoid red-green diverging ramps. (VAD p.260)
11. Get it right in black and white: encode the most important attribute with luminance; use hue/saturation as secondary channels. (VAD p.140)
12. Contain all shapes within rows of 10 when using icon grids (never 12, 17, 20, or 24). (CI p.191)
13. Restrict categorical shape encoding to ~4 distinct shapes maximum. (DS p.50)
14. When using radial layouts, map time to angle (not radius) to keep equal time units at equal arc lengths. (DS p.109)

### Data and Transformation Rules

15. Always provide a second value for comparison when visualizing a large number. (CI p.29–30)
16. Choose comparisons deliberately — the reference value is a design decision that shapes the narrative. (CI p.30)
17. Derive and encode the variable of interest directly rather than making users compute differences perceptually. (VAD p.51–52)
18. Size circles by area, not diameter: Radius = √(Area / π). (CI p.203–205)
19. Never use quantitative chart types for qualitative sample data (n < 30); use literal person-icon counts instead. (CI p.193)
20. Order categorical regions by value attribute for trend detection, not alphabetically. (VAD p.150)
21. Use smoothed density curves over histograms for distribution shape comparison across small multiples. (DS p.200)
22. Filtering is "out of sight, out of mind" — aggregation is cognitively safer when items must remain in context. (VAD p.325)
23. For DR scatterplots: only relative distances matter; only large-scale cluster structure is reliable; avoid 3D. (VAD p.344–345)

### Interaction and Layout Rules

24. Overview first, zoom and filter, details on demand. (VAD p.135)
25. Eyes beat memory: simultaneous visible views impose far less cognitive load than comparing with remembered states. Small multiples over animation for complex changes. (VAD p.131–134)
26. Respond within 0.1s (screen update), 1s (feedback), 10s (task completion). (VAD p.137)
27. Animated transitions: only effective when the amount of change is limited. (VAD p.132–133)
28. Two layers superimposed: feasible. Three: possible with care. More: very difficult. (VAD p.291, 314)
29. No unjustified 3D: 3D is justified only for tasks requiring inherently 3D spatial understanding. (VAD p.117)
30. No unjustified 2D: a 1D list beats a 2D layout for lookup and text density when topology is not the point. (VAD p.131)
31. Justify radial layout for cyclic data only; rectilinear is more accurate otherwise. (VAD p.167)
32. Add a mini-map for any very long or tall scrollable visualization. (DS p.225)
33. Constrained navigation prevents getting lost; auto-frame-selected-item is good design. (VAD p.282)

### Design Process Rules

34. Always try multiple sketch ideas before committing; identify the one hardest step and prove it works first. (DS p.33–34)
35. Explore data before designing — list all attributes, tag types, formulate hypotheses, test with quick charts. (DS p.106)
36. Minimalism is the destination after iteration, not the starting point. Start with more, strip away what does not add focus. (DS p.290)
37. Function first, form next: effective but ugly can be refined; beautiful but ineffective must be discarded. (VAD p.140–141)
38. Test designs with peers before calling them done — they spot angles and interactions you missed. (DS p.225, 237)
39. When a visualization looks interesting but insight extraction is inefficient: start over. (DS p.304)
40. One clear key message per infographic — include only data and visuals that support it. (CI p.208)
41. Annotations are vital — they guide readers toward what the creator considers most important and teach readers how to read non-standard charts. (DS p.363, 399, 424)
42. "Remix, don't copy": use existing code/examples as a starting point, then meaningfully transform for your data and style. (DS p.354)
43. Constraints can make you more creative — try placing explicit time or tool limits. (DS p.426)

### Infographic-Specific Rules

44. Include in every infographic footer: company logo, landing page URL, source citations with dates, license, designer credit. (CI p.217–218)
45. Cite the original data source (specific URL and date), not just a news article that quoted it. (CI p.216)
46. Publish infographics at 800px wide in tall/vertical format for online sharing. (CI p.68)
47. Horizontal format infographics fail when shared online — reduced to unreadably small sizes. (CI p.69)
48. Test color-dependent designs in grayscale; test printed on the lowest-quality office printer. (CI p.161–162; VAD p.140)

---

## 13. What Good Reports Look Like in Practice

*This section is synthesized exclusively from example student reports (ER = er_chunk_01_summary.md). It describes actual KU Leuven Data Visualisation course reports.*

### Report Structure

Both strong reports follow the same template: Metadata → Project Description → Visual Design (diverge/emerge/converge) → Implementation → Findings → Individual Contributions → Appendix. Report 2 additionally includes a Reflections section ("most proud of" / "least proud of") not present in Report 1 — this is considered a strength.

Report 1 runs approximately: 0.5 page metadata, 1.5 pages project description, 6 pages visual design (diverge/emerge/converge), 4 pages implementation, 3 pages findings, 0.5 pages contributions, 1 page appendix.

Report 2 runs approximately: 1 page metadata, 1.5 pages project description, 3 pages visual design, 5 pages implementation, 2 pages findings, 1 page reflections, 1 page contributions, 1 page appendix.

### What a Strong Design-Choice Justification Looks Like

Strong justifications name marks and channels explicitly, connect them to the user task, and explain rejected alternatives:

- Report 1: "Each circle, serving as marks, represents the revenue and average order price... On the vertical axis, serving as position channel..." — uses theory vocabulary directly. (ER report_1 p.8)
- Report 1: Explicitly explains why saturation was rejected at the individual product level: "this visualization method became impractical, losing its informativeness when applied to 2,101 individual products instead of product types." (ER report_1 p.8)
- Report 2: Visual Encoding is a dedicated section header, with numbered bullet points: "1. Battery Shapes: Each distribution center is represented by a vertical cylinder (battery)... 2. Y-Axis: Indicates the quantity of materials as a percentage..." (ER report_2 p.6)
- Report 2: Justifies color operationally: "green indicates both inventory and forecasted quantities are above the threshold... Orange indicates that one of the forecasted quantities falls below the target... Red alerts that both inventory and forecasted quantities are below the threshold." (ER report_2 p.7)
- Report 2: References specific prior sketches by ID in the converge section: "Converge 2 integrates elements from sketches JA_4, JA_5, SH_6, SH_9, and SH_10." (ER report_2 p.5) This makes design lineage traceable.

The key pattern: **every channel choice is justified by the question it answers**, not by aesthetics.

### How the Diverge/Emerge/Converge Process Is Shown

**Report 1 — highly visible process:**
- Sections explicitly labelled "A. Diverge", "B. Emerge", "C. Converge".
- Diverge: each team member created individual sketches independently, then shared at a group meeting.
- Emerge: used Miro to cluster sketches in two ways — by information content AND by format. Three clusters emerged: (1) Revenue by type/subtype, (2) Circular visualizations, (3) Maps.
- Converge: compared within and across clusters; selected one per cluster; described full evolution from initial sketch to final design for each; explicitly states three converge candidates and explains which two were selected for implementation and why.
- Sketches are photographed and embedded inline with IDs (VVB11, SMM2, etc.). Shows genuine iteration, not post-hoc reconstruction.

**Report 2 — briefer but technique-named:**
- Diverge/emerge/converge language used in prose.
- Names techniques explicitly: SCAMPER, Miro, video calls, "matrix-based approaches."
- Converge section answers a specific template question: "Which 2-3 reworked sketches would you want implemented?"
- Sketches shown with both an image and a bullet-point encoding description side by side.

### How Theory Is Connected to Specific Design Decisions

Neither report cites Munzner or any named textbook — a weakness. Theory is applied implicitly through encoding vocabulary ("marks," "channels," "visual encoding," "saturation"), which is considered acceptable but less convincing than explicit citation.

Report 1 uses theory-adjacent language without attribution: "while adhering to good design principles" — this is too vague. Report 2 names SCAMPER as a design technique but does not cite a source.

The strongest connection between theory and design in both reports happens through **task-encoding alignment**: each design choice is justified by the analytical question it answers, not by abstract principle. This is the right approach even without explicit citation.

### What Persona / User Framing Looks Like

Neither report defines formal personas — a weakness highlighted as a gap. Instead:

- Report 1 uses the client (D.E.A.D company) as an implicit user. User tasks are framed as business questions: "which product categories are excelling and which could be omitted?" Phrases like "the company should consider reallocating resources" frame the user as a business analyst.
- Report 2 uses "SunCharge" as the implicit user organization. Tasks are framed operationally: "quickly identify bottlenecks," "enhance inventory management practices," "optimize logistics operations."

**The alert system (green/orange/red) in Report 2 implicitly defines a monitoring user** — someone who needs to act on anomalies at a glance without a formal persona statement. This is a practical alternative to formal persona writing.

### Pitfalls That Appeared in Both Reports

- **No theory citations**: neither report cites Munzner or any visualization textbook, even when using encoding vocabulary. Using "marks and channels" without attribution is less convincing than tying it to the theoretical framework.
- **Loose findings sections**: Report 1's findings read as a bullet-point data summary rather than visualization-derived insight. The link back to specific visual features is sometimes absent.
- **Thin findings in Report 2** (2 pages for 2 implementations): findings are descriptive of what the tool shows, not analytical insights discovered through the tool.
- **Too-positive "intended vs. actual" comparisons**: "This implementation serves as a comprehensive realization of the initial idea" (ER report_1 p.9) — no critical reflection.
- **Large gap between intended and actual** in Report 2: advanced features (moving splines, animated transitions) were listed as intended but not implemented. Acknowledging gaps is good; having such large gaps is not.
- **No formal persona definitions**: design choices have no explicit user grounding beyond client business questions.
- **No accessibility consideration** in either report (colour-blindness, contrast ratios, etc.).
- **Neither report includes a formal limitations or future work section** beyond the "intended vs. actual" comparison.

### What the Combined Visualizations Actually Looked Like

**Report 1 — Visualization A: "Revenue and average order value by types and areas" (Bubble Grid)**

A 2D grid with 5 areas (North, South, East, West, Underdark) on the vertical axis and 8 product types on the horizontal axis. Each cell contains a circle: size encodes total revenue for that area × product type combination; blue saturation encodes average order value (darker = more expensive). Hover shows exact values; checkboxes on the right filter by area and product type, grouping remaining circles for cleaner comparison. Implemented in Svelte. Two channels used per mark (size + saturation), both justified by distinct business questions.

**Report 1 — Visualization B: "D.E.A.D's Revenue Across The World" (Compass-Map Hybrid)**

A circular layout divided into 5 coloured sectors (the 5 areas, positioned like compass directions). Within each sector, irregular polygon tiles represent nations (57 total). Tile size encodes revenue; tile colour encodes area identity; brightness encodes proportion of late deliveries (lighter = fewer late deliveries). Green dot overlays on tiles encode number of high-value orders (larger dot = more). Hover shows all four metrics; previously examined tiles blur/dim to aid tracking. Implemented in 3D. A genuine combined visualization: proportional symbol map + tile map + brightness encoding + dot encoding in one view.

**Report 2 — Implementation 1: "Distribution Centers Performance Monitoring Tool"**

Two-component visualization per Distribution Center, shown side by side for all 5 DCs (Antwerp, Wroclaw, Lyon, Birmingham, Goteborg):

*Top component (Battery Visualization)*: Each DC is a vertical cylinder drawn as a battery. Cylinder divided into coloured sections — yellow for EV Car Battery forecast quantity, teal for Home Battery forecast quantity. Height of each section encodes percentage of forecast. An alarm dot at top: green (both above threshold), orange (one below), red (both below). Updates dynamically based on year and threshold dropdowns.

*Bottom component (Gauge Visualization)*: Below each battery, a semi-circular gauge dial per material type. Multiple coloured needles and arcs represent Gross Inventory, On-Shelf Inventory, In-Transit, and Order quantities. Outer gauge = EV Car Battery; inner gauge = Home Battery. Implemented in Svelte + D3.js.

**Report 2 — Implementation 2: "Plant Shipment Performance to Distribution Centers"**

Two-map visualization with a transition between them:

*World Map*: External vendors as red circles and production plants as green rectangles on a world map. Splines connect vendors to plants, encoding Total Inbound Lead Time. Hovering resizes circles/rectangles to show name/location. Material dropdown filters which splines are highlighted. Clicking a plant transitions to the EU map.

*EU Map*: Plants/internal vendors as green rectangles and 5 DCs as yellow rectangles. Five overlay boxes appear on the map (one per DC) containing bar charts with shipping time metrics. A Return button goes back. The blur/darkening transition between maps uses animation as a semantic signal that the scope is changing.

### Key Observations for Your Own Report

1. **Embed sketch photos inline** — not in an appendix. Show intermediate sketches with IDs. This demonstrates genuine iteration.
2. **Name marks and channels explicitly** for every implemented visualization, as a numbered or bulleted list under a "Visual Encoding" header.
3. **Connect every visualization to a specific research question** — create a coherent question → design → finding loop.
4. **Describe rejected options with reasons** — this is what distinguishes genuine iteration from post-hoc description.
5. **Metric reformulation counts as an iteration step** — switching from average delivery time to proportion >20 days is an analytical design decision worth documenting.
6. **Reflections section adds value** — acknowledging what you are least proud of (and why) demonstrates critical thinking.
7. **Name the ID of each sketch** that contributed to each converge design — this makes lineage traceable.
8. **Cite Munzner** when using encoding vocabulary. Even one or two citations ("following Munzner's channel effectiveness ranking (VAD p.101)...") elevates the theoretical grounding of the report considerably.
