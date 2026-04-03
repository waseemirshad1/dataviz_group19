# [agent_22] Visualization Analysis and Design — pages 301-350

## Visualization Catalogue: Pages 301-350

---

### Coordinated Multiple Views — Census System (p.302-303)
- **What it shows:** Multivariate geographic + demographic data; highlighting shared across views reveals cluster structure and spatial distribution simultaneously
- **When to use:** Large multidimensional tables where no single encoding captures all relevant relationships; when users need to compare across many attributes simultaneously
- **Avoid when:** Low-information tasks, small datasets, or when one view suffices
- **Interesting properties:** Bivariate sequential–sequential colormap shared across all views; linked highlighting creates cross-view brushing; overview map + detail map linked by navigation
- **Marks:** Points (scatterplot, city points), lines (parallel coordinates), areas (choropleth), cells (matrix)
- **Channels:** Position (scatterplot axes, map), color (bivariate sequential–sequential), size (city points)
- **Annotation options:** Legend for shared colormap; labels in reorderable list views; axis tick marks
- **Data types suited for:** Geographic + multidimensional table; one key attribute (county), many quantitative attributes
- **Interesting feature extraction/manipulation:** Partition data by attribute into list views; linked highlighting enables cross-view selection

---

### Grouped Bar Chart (p.306-307)
- **What it shows:** Multibar glyphs within each region; shows multiple attributes per item side by side
- **When to use:** When the primary task is **comparing attributes against each other** within each item group
- **Avoid when:** Primary task is comparing one attribute across all groups — small multiples are better
- **Interesting properties:** Interleaved second-level regions (bars) within first-level regions (groups); multibar glyph per item
- **Marks:** Line marks (bars); multiple bars per glyph
- **Channels:** Length (bar height), position (x-axis for groups, spacing for categories), color (categorical hue to distinguish attribute categories)
- **Annotation options:** Axis labels, tick marks, legend for color categories
- **Data types suited for:** Multidimensional table; two categorical key attributes, one quantitative value
- **Interesting feature extraction/manipulation:** Compute median per group for ordering; derive group aggregates

---

### Small-Multiple Bar Charts (p.306-307)
- **What it shows:** One standard bar chart per attribute value; same attribute consistently on the shared axis
- **When to use:** When the primary task is **comparing items within a single attribute** (e.g., ranking sites within one variable)
- **Avoid when:** Cross-attribute comparison is primary goal — grouped bars are better
- **Interesting properties:** Contiguous second-level regions per attribute; easily compare the same item across positions; supports per-attribute pattern detection
- **Marks:** Line marks (bars); one chart per attribute group
- **Channels:** Length (bar height), position (x-axis for items within each small multiple), spatial position of panels for grouping variable
- **Annotation options:** Shared axes, per-panel titles
- **Data types suited for:** Same as grouped bar chart; two categorical keys + one quantitative value
- **Interesting feature extraction/manipulation:** Main-effects ordering by median; derive per-attribute statistics

---

### Trellis / Dot Chart Matrix (p.307-309)
- **What it shows:** A multiattribute dataset faceted into a 2D matrix of dot chart views; each row = one level of a key, each column = another key; within each view, a third key spreads along the vertical axis with quantitative values on horizontal
- **When to use:** Multidimensional table with 3+ categorical key attributes and one quantitative value; when outlier detection against general trends is important
- **Avoid when:** Only one or two categorical keys; when the number of combinations makes the matrix too large to read
- **Interesting properties:** **Main-effects ordering** (by median) makes both trends and outliers visible; without it (alphabetical order) no patterns emerge; Morris anomaly in barley dataset only visible with main-effects ordering
- **Marks:** Dots (point marks)
- **Channels:** Horizontal position (quantitative value), vertical position (key attribute levels within panel), panel position in matrix (two categorical keys)
- **Annotation options:** Shared axis labels, row/column headers for matrix keys, median lines
- **Data types suited for:** Multidimensional table: multiple categorical key attributes + one quantitative value attribute
- **Interesting feature extraction/manipulation:** Derive medians per partition for main-effects ordering; color-encode a second attribute to combine within one view (Figure 12.10)

---

### HiVE Recursive Subdivision / Treemap Hybrid (p.310-313)
- **What it shows:** Recursive spatial partitioning of a multiattribute dataset into nested rectangular regions; at lowest level, color encodes a derived quantitative attribute (e.g., price variation or average price)
- **When to use:** Multiattribute data where hierarchy of key attributes matters; exploring different orderings of partitioning to discover patterns; when spatial/geographic awareness is useful
- **Avoid when:** Only one or two attributes; when color alone cannot carry the key quantitative message
- **Interesting properties:** Same data, same encoding, different partitioning order → radically different visual patterns; can become treemap (size proportional to count), matrix, or choropleth depending on arrangement
- **Marks:** Area marks (rectangles, or geographic regions)
- **Channels:** Spatial containment (hierarchy), color (quantitative derived attribute: price variation or average), size of region (optional: count-proportional for treemap variant)
- **Annotation options:** Color legend, labels for high-level partitions
- **Data types suited for:** Multidimensional table with several categorical key attributes + quantitative value; geographic data at second level
- **Interesting feature extraction/manipulation:** Derive price variation or average within each partition group; spatially-aware treemap layout [Wood and Dykes 08]

---

### Cartographic Layering (p.314-315)
- **What it shows:** A geographic map with multiple visual layers distinguishable by luminance, saturation, and mark type
- **When to use:** Geographic data with multiple classes of features (e.g., roads, water, land, parks) that must all be readable simultaneously
- **Avoid when:** More than ~3 layers with area marks — too many layers becomes illegible
- **Interesting properties:** Each layer occupies a non-overlapping luminance range; "Get It Right in Black and White" check validates layer separability; background layers use unsaturated colors, foreground uses saturated
- **Marks:** Area marks (background: regions), line marks (foreground: roads)
- **Channels:** Color hue (categorical: water/park/land), color saturation (layer distinction), luminance (layer separation), line width (road importance)
- **Annotation options:** Text labels for place names, road identifiers
- **Data types suited for:** Geographic geometry with categorical region type and categorical road type
- **Interesting feature extraction/manipulation:** Luminance contrast check as validation step

---

### Superimposed Line Charts (p.315-316)
- **What it shows:** Multiple time series within a single shared frame, one line per categorical item
- **When to use:** Comparing trends within a local visual span; up to ~dozen time series; local maximum task (finding highest value at a specific time)
- **Avoid when:** More than a few dozen series (occlusion becomes unmanageable); global slope or global discrimination tasks across many series (use juxtaposed small multiples instead)
- **Interesting properties:** Empirical evidence: superimpose best for local tasks, juxtapose best for global tasks (p.317); thin lines create minimal occlusion; works with nearly one dozen items
- **Marks:** Line marks (one per time series)
- **Channels:** Vertical position (quantitative value), horizontal position (time/ordered attribute), color hue (categorical: one per machine/item)
- **Annotation options:** Axis labels, legend for color-to-series mapping
- **Data types suited for:** Multidimensional table: one ordered key (time), one categorical key (item), one quantitative value
- **Interesting feature extraction/manipulation:** Derive min/max per series for comparison annotation

---

### Hierarchical Edge Bundles (p.317-319)
- **What it shows:** A compound network (call graph) with an underlying source code hierarchy; network edges bundled to reduce occlusion; three superimposed layers
- **When to use:** Compound networks where both a base network and a cluster hierarchy over nodes exist; when distinguishing tree structure from network connections is important
- **Avoid when:** No underlying hierarchy; few nodes (overkill); when edges do not benefit from bundling (sparse network)
- **Interesting properties:** Bundling reduces occlusion just as cable ties bundle physical wires; three layers (gray tree, red-green edges, gray nodes) distinguished by both color and mark type; idiom does not require specific spatial layout for the tree
- **Marks:** Containment circle marks (hierarchy/tree, back layer), connection link marks (network edges, middle layer), point marks (nodes, front layer)
- **Channels:** Color hue (gray = tree/nodes vs. red-green = network edges), color saturation (background vs. foreground), line curvature (edge bundling)
- **Annotation options:** Node labels at leaf positions
- **Data types suited for:** Compound graph: network + hierarchy whose leaves are network nodes
- **Interesting feature extraction/manipulation:** Edge bundling uses tree hierarchy to route edges; back-to-front rendering order via graphics hardware z-planes

---

### FilmFinder Dynamic Query Scatterplot (p.326-328)
- **What it shows:** Interactive scatterplot of movies with dynamic filtering via sliders and buttons; visual encoding adapts to remaining items
- **When to use:** Browsing an unknown dataset by attribute value ranges; exploration where user doesn't know what to query; overview-first, detail-on-demand tasks
- **Avoid when:** User has precise known query; very small datasets; when exact attribute values are needed rather than ranges
- **Interesting properties:** Marks auto-enlarge and add labels when filtered-down set is small enough; multiform overview + popup detail on click; dual sliders for min+max range selection; alpha sliders for text-string filtering
- **Marks:** Point marks (one per movie)
- **Channels:** Horizontal position (year made), vertical position (popularity), color hue (genre), size (adaptive: grows when few items remain)
- **Annotation options:** Auto-labels on marks when sparse; popup detail view with text and images
- **Data types suited for:** Table with multiple value attributes (nine: genre, year, title, actors, rating, popularity, length, etc.)
- **Interesting feature extraction/manipulation:** Dynamic queries; real-time filtering with immediate visual update; auto-adapt mark size to item density

---

### Scented Widgets (p.328)
- **What it shows:** Standard GUI filter widgets augmented with concise visual encodings of the dataset to guide filtering choices
- **When to use:** High-information-density displays where filter controls must coexist with little additional screen real estate; datasets where filter choices are non-obvious
- **Avoid when:** Simple low-dimensional datasets where the range is immediately obvious
- **Interesting properties:** Uses no/minimal additional screen space; provides "information scent" — cues about whether drilling down in a given direction will be valuable
- **Marks:** Small bar/line chart within widget, or widget parts treated as marks
- **Channels:** Hue, saturation, opacity embedded within widget areas; bar length (count), line trend (temporal)
- **Annotation options:** Icons, text labels within widget
- **Data types suited for:** Any dataset with quantitative or text attributes suitable for range filtering
- **Interesting feature extraction/manipulation:** Insert statistical summary graphic (bar chart, line chart) directly into slider track or widget background

---

### Star Plots / DOSFA (p.329)
- **What it shows:** Radial/star glyph per item showing multiple attributes simultaneously; attribute filtering+ordering applied to make patterns visible
- **When to use:** High-dimensional table data (many attributes per item) where dimensionality filtering is needed; when similarity structure across attributes matters
- **Avoid when:** Few attributes (normal bar/line chart is better); when individual attribute precision is needed
- **Interesting properties:** With 215 unordered attributes, patterns are invisible; after ordering by similarity + filtering → clear visual structure emerges; order and spacing of axes critically affects readability
- **Marks:** Line marks (polygon outline per item), one arm per attribute
- **Channels:** Length of arm (quantitative attribute value), angle (attribute identity)
- **Annotation options:** Axis labels, attribute ordering legend
- **Data types suited for:** Table with many quantitative value attributes
- **Interesting feature extraction/manipulation:** Compute similarity measure between attributes; compute variance per attribute; order axes by similarity; filter by importance threshold

---

### Histograms (p.331-332)
- **What it shows:** Distribution of a quantitative attribute, aggregated into bins; shows count per bin
- **When to use:** Summarizing the distribution of a single quantitative attribute; especially useful for large datasets where individual item plots would overplot
- **Avoid when:** Only a few items; when distribution shape detail matters more than bin counts (use KDE); when bin count choice is contentious and not interactively adjustable
- **Interesting properties:** No gaps between bars (imply continuity, unlike bar charts); bin size choice radically changes appearance; can compute bin count from dataset characteristics or offer interactive control
- **Marks:** Line marks (bars, touching without gaps)
- **Channels:** Length/height (count per bin), horizontal position (bin range = ordered key)
- **Annotation options:** Bin edge annotations, frequency labels, overlaid KDE curve
- **Data types suited for:** Table: one quantitative value attribute → derived: one ordered key (bin) + one quantitative value (count)
- **Interesting feature extraction/manipulation:** Derive bin boundaries; count items per bin; interactive bin-size control; can generalize to continuous scatterplot in 2D

---

### Continuous Scatterplots (p.332-333)
- **What it shows:** Density of overplotted points at each pixel, encoded with a sequential colormap; solves scatterplot occlusion problem for large datasets
- **When to use:** Large datasets where many points overlap in a standard scatterplot; when the density/distribution across two quantitative attributes matters more than individual points
- **Avoid when:** Small datasets; when individual point identity matters; when precise value reading is needed
- **Interesting properties:** Generalizes discrete scatterplot to continuous density function; log-scale colormap handles skewed densities; dark blues → reds → yellows/whites as density increases
- **Marks:** Dense pixel-level area marks (one color per pixel)
- **Channels:** Color hue + luminance (density, sequential colormap); horizontal/vertical position (two quantitative attributes)
- **Annotation options:** Colormap legend, axis labels
- **Data types suited for:** Table: two quantitative value attributes → derived: x/y pixel locations + overplot density
- **Interesting feature extraction/manipulation:** Compute overplot density per pixel; apply log-scale transformation for dynamic range compression

---

### Boxplot Charts (p.333-335)
- **What it shows:** Statistical distribution summary of a quantitative attribute using 5 derived values (median, lower/upper quartile, lower/upper fence); outliers explicitly shown as dots
- **When to use:** Comparing distributions across many categories (dozens); when spread, skew, and outliers are the key tasks; when individual values are less important than distributional shape
- **Avoid when:** Multimodal data (vase plot or violin plot better); when showing all individual values is important (dot plot, jitter)
- **Interesting properties:** Highly scalable — compresses millions of values to 5 numbers; only moderate screen space needed per boxplot; assumes unimodal distribution
- **Marks:** Line marks (whiskers), rectangle mark (interquartile box), horizontal line (median), point marks (outlier dots)
- **Channels:** Vertical spatial position (all 5 derived values), horizontal position (categorical key, 1D list alignment)
- **Annotation options:** Axis labels, outlier value annotations, mean markers
- **Data types suited for:** Table: many quantitative value attributes → derived: 5-number summary per attribute
- **Interesting feature extraction/manipulation:** Derive median, quartiles, fences; identify outliers; compare spread and skew across groups

---

### Vase Plot (p.334-335)
- **What it shows:** Boxplot variant where the width of the central box varies with density — allows detection of multimodal distributions
- **When to use:** When checking whether distribution is unimodal vs. bimodal/multimodal
- **Avoid when:** Screen space is very limited (requires more horizontal space than standard boxplot)
- **Interesting properties:** Adds one additional spatial dimension (width) to standard boxplot encoding
- **Marks:** Variable-width line/area marks for box body, line marks for whiskers
- **Channels:** Vertical position (quantitative value), horizontal width (density at each value), horizontal position (categorical key)
- **Annotation options:** Same as boxplot
- **Data types suited for:** Same as boxplot; especially valuable for continuous quantitative distributions
- **Interesting feature extraction/manipulation:** Derive density function; compute KDE or histogram-derived widths

---

### SolarPlot / Radial Histogram (p.335-336)
- **What it shows:** Circular histogram of a temporal quantitative attribute; user controls aggregation level by changing circle radius
- **When to use:** Temporal/cyclic data (e.g., ticket sales over 30 years) where both trend (long-term) and periodicity (seasonal) need to be visible; when interactive aggregation control is useful
- **Avoid when:** Non-temporal or non-cyclic data; when precise value reading is needed
- **Interesting properties:** Circle radius indirectly controls bin count; small circle → high aggregation → trend visible; large circle → lower aggregation → seasonal patterns visible; aggregation operator = count
- **Marks:** Line marks (radial bars)
- **Channels:** Line length (count per bin), angle (time: ordered key attribute)
- **Annotation options:** Time labels at angle positions, count scale labels
- **Data types suited for:** Table: one quantitative attribute → derived: bins by time, count per bin
- **Interesting feature extraction/manipulation:** Derive bin count dynamically based on circle radius; compute count per time bin at multiple granularities

---

### Hierarchical Parallel Coordinates (p.336-337)
- **What it shows:** Parallel coordinates with hierarchical clustering overlay; clusters shown as bands of varying width (min-max range) and opacity; single slider controls level of detail
- **When to use:** Very large multidimensional tables (10,000–100,000 items) where standard parallel coordinates would show too many individual lines; when cluster structure is the goal
- **Avoid when:** Small datasets (standard parallel coordinates work fine); when individual item tracing is important
- **Interesting properties:** In the limit, a cluster of one item = single line (reduces to standard idiom); proximity-based coloring distinguishes clusters; interactive aggregation dial from highly aggregated (one broad band) to detailed (dozens of narrow bands)
- **Marks:** Band marks (variable width and opacity per cluster), line marks (individual items at finest level)
- **Channels:** Vertical position (value range at each axis), width (min-max span of cluster at each axis), opacity (cluster size/level), color (proximity in cluster hierarchy), horizontal position (attribute identity)
- **Annotation options:** Axis labels, cluster identity legend, level-of-detail slider
- **Data types suited for:** Table with many quantitative attributes → derived: hierarchical clustering with 5 per-cluster stats (count, mean, min, max, depth)
- **Interesting feature extraction/manipulation:** Compute hierarchical clustering; derive per-cluster mean, min, max, count, depth; interactive LOD slider

---

### Geographically Weighted Boxplots / Geowigs (p.338-340)
- **What it shows:** Boxplots for multiple attributes at two spatial scales, with global distribution in gray background and local scale distribution in green foreground; matched with choropleth map showing selected region
- **When to use:** Multivariate geographic data where local vs. global distributional comparison is the task; exploratory spatial data analysis at multiple scales
- **Avoid when:** Non-spatial data; when only one scale of analysis is relevant
- **Interesting properties:** Directly demonstrates MAUP; superimposed layers (gray global + green local) within same boxplot frame; interactive scale selection changes which areas contribute to local statistics
- **Marks:** Line marks (whiskers), rectangle marks (IQR box), horizontal lines (median) — two overlaid per attribute
- **Channels:** Vertical position (value distribution), color hue (global=gray vs. local=green), horizontal position (attribute identity)
- **Annotation options:** Scale weighting maps, choropleth map highlighting selected region
- **Data types suited for:** Geographic geometry + table with key (area) and several quantitative attributes → derived: 5-number summaries at multiple scales
- **Interesting feature extraction/manipulation:** Geographically weighted regression; geographically weighted summary statistics; MAUP exploration

---

### Dimensionality Reduction Scatterplot (MDS/DR) (p.340-345)
- **What it shows:** Items from a high-dimensional space projected into 2D (or few-D) coordinates that preserve relative distance structure; color codes conjectured cluster membership
- **When to use:** Very high-dimensional data (thousands of attributes) where cluster structure is the goal; document collections, image collections; when direct multi-attribute comparison is infeasible
- **Avoid when:** Only a few attributes (scatterplot or SPLOM suffices); when absolute positions must be interpretable; when fine-grained structure matters (DR loses detail)
- **Interesting properties:** Only **relative distances** matter — rotation, reflection, rescaling do not change meaning; only large-scale cluster structure is reliable; fine-grained distances may not be meaningful; 2D and SPLOM are safest; 3D scatterplots are worst case for depth perception
- **Marks:** Point marks (one per item)
- **Channels:** Horizontal + vertical position (two synthetic DR dimensions), color hue (conjectured cluster membership)
- **Annotation options:** Text labels for verified clusters; popup detail view on click (showing keywords or document text); SPLOM if more than 2 DR dimensions
- **Data types suited for:** High-dimensional table → derived: 2 or few synthetic attributes via MDS
- **Interesting feature extraction/manipulation:** Bag-of-words transformation for text; MDS/UMAP/t-SNE; two-stage chained derivation (raw → high-D table → low-D table); color by conjectured clustering to verify

---

### DOITrees Revisited — Elision Focus+Context (p.350)
- **What it shows:** A very large tree (600,000 nodes) with multiple selected focus nodes shown in detail; context shown as shaded triangles representing elided subtrees
- **When to use:** Very large trees/hierarchies where only a few nodes are of immediate interest; when maintaining context around focus nodes matters
- **Avoid when:** Small trees (full display works); when all nodes need equal attention
- **Interesting properties:** Combines filtering (elision) and aggregation (shaded triangle summaries); multiple foci supported; context computed via tree traversal from focus up to common ancestors; distance = topological hops (not Euclidean)
- **Marks:** Node–link marks, triangle marks (elided subtrees)
- **Channels:** Vertical/horizontal position (tree layout), size of triangle (subtree size), visual distinction of focus nodes vs. context
- **Annotation options:** Node labels at focus nodes; triangle size annotations
- **Data types suited for:** Tree (hierarchy) with up to hundreds of thousands of nodes
- **Interesting feature extraction/manipulation:** DOI function: DOI = I(x) − D(x, y); tree traversal for context computation; topological distance calculation
