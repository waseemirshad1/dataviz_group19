# [agent_24] Visualization Analysis and Design — pages 401-430

## Note on Content

Pages 401–430 are back matter only (Bibliography, Idiom & System Examples Index, Concept Index, ebook access page). No new visualization idioms are introduced here. The Idiom and System Examples Index (pp. 422–423) provides a complete catalogue of all idioms discussed in the book with their page references.

The entries below are drawn from the **Idiom and System Examples Index** (pp. 422–423) and represent the complete set of named visualization types in the book. Where the Concept Index or Bibliography adds detail (e.g., channel/data type information), that is noted with cross-references to where the idiom is actually taught.

---

### Bar Charts (p. 150–151)
- **What it shows:** One quantitative value attribute per categorical or ordered key; height/length encodes quantity.
- **When to use / avoid:** Use for discrete comparison of categorical items. Avoid for continuous ordered keys (use line chart). Avoid for more than ~30 bars without interaction.
- **Interesting properties:** Most effective ordered channel (length) after position. Clustered/grouped variants add a second categorical attribute.
- **Marks:** Line/bar (area marks implicitly)
- **Channels:** Position (aligned), length
- **Annotation options:** Value labels, error bars, reference lines
- **Data types suited for:** Table: one quantitative value, one categorical/ordinal key
- **Interesting feature extraction/manipulation:** Sort by value to reveal ranking; normalize to show proportion (stacked normalized bar chart)

---

### Stacked Bar Charts (p. 151–153)
- **What it shows:** Part-to-whole relationships across categories; a second categorical attribute stacked within bars.
- **When to use / avoid:** Use to show composition within groups. Avoid when comparing non-baseline segments (only baseline segment is perceptually accurate).
- **Interesting properties:** The normalized version (100% stacked) shows proportions but loses absolute magnitudes.
- **Marks:** Area (stacked rectangles)
- **Channels:** Position (aligned for baseline only), length, color hue
- **Annotation options:** Value labels per segment; color legend
- **Data types suited for:** Table: one quantitative value, two categorical keys (one nested)
- **Interesting feature extraction/manipulation:** Reorder segments to move segment of interest to the baseline

---

### Streamgraphs (p. 153–154)
- **What it shows:** Temporal evolution of multiple value streams, stacked and smoothed around a central axis.
- **When to use / avoid:** Use for aesthetic overview of temporal composition changes. Avoid when precise values are needed (baseline shifts make reading difficult).
- **Interesting properties:** ThemeRiver variant. Visually striking but perceptually weak for quantitative reading.
- **Marks:** Area (curved/organic)
- **Channels:** Position (y = magnitude, x = time), color hue (stream identity), area
- **Annotation options:** Labels at end/peak of stream; hover tooltips
- **Data types suited for:** Table: quantitative value, temporal key, categorical attribute (stream identity)
- **Interesting feature extraction/manipulation:** Sorting streams by temporal pattern (early peak vs. late peak) reveals structure

---

### Dot and Line Charts (p. 155–156)
- **What it shows:** One quantitative value against one ordered key; dots emphasize individual points, lines emphasize trend/connection.
- **When to use / avoid:** Line charts for ordered (temporal/sequential) keys only. Dot charts (Cleveland dotplots) for categorical keys, as alternatives to bar charts.
- **Interesting properties:** Banking to 45° — optimal visual perception of slope when lines near 45° angle (p. 156–157).
- **Marks:** Point marks; line (connection marks)
- **Channels:** Position (both axes), color hue for third attribute
- **Annotation options:** Labels, trend lines, confidence bands
- **Data types suited for:** Table: one quantitative value, one ordered key
- **Interesting feature extraction/manipulation:** Multiscale banking — adjust aspect ratio to maximize perceptual accuracy of trend reading

---

### Multiscale Banking to 45° (p. 156–157)
- **What it shows:** A single time series, but the aspect ratio is automatically computed so that the average absolute slope is 45°.
- **When to use / avoid:** Use to optimize trend perception in line charts. Avoid when exact values are primary task.
- **Interesting properties:** Perceptual science-based design; implemented in Heer & Agrawala's Tableau-like tool.
- **Marks:** Line
- **Channels:** Position (both axes)
- **Annotation options:** Standard axis labels
- **Data types suited for:** Time-series, quantitative value
- **Interesting feature extraction/manipulation:** Derive optimal aspect ratio from slope distribution of the data

---

### Cluster Heatmaps (p. 158–160)
- **What it shows:** Matrix of values between two categorical axes, color-encoded, with rows and columns reordered by hierarchical clustering to reveal patterns.
- **When to use / avoid:** Use for large tables where pattern detection matters more than individual lookup. Avoid for small tables where a simple table suffices.
- **Interesting properties:** Matrix reordering (seriation) is critical — the same data looks very different depending on ordering. Dendrograms alongside show the clustering structure.
- **Marks:** Area (cells/rectangles)
- **Channels:** Color (luminance/saturation for ordered values; hue for categorical)
- **Annotation options:** Dendrogram, row/column labels, color scale legend
- **Data types suited for:** Table: quantitative value, two categorical keys (row × column)
- **Interesting feature extraction/manipulation:** Biclustering; optimal leaf ordering algorithms; row/column normalization

---

### Scatterplot Matrix / SPLOM (p. 160–161)
- **What it shows:** All pairwise relationships among multiple quantitative attributes simultaneously.
- **When to use / avoid:** Use for initial exploration of multivariate data to find correlations and outliers. Avoid when more than ~10 attributes (matrix becomes too dense).
- **Interesting properties:** Diagnonal cells can show univariate distributions (histograms or KDE). Scagnostics can characterize each cell automatically.
- **Marks:** Point
- **Channels:** Position (x and y vary per cell), color hue for grouping
- **Annotation options:** Regression lines, correlation coefficients, marginal histograms
- **Data types suited for:** Multivariate table
- **Interesting feature extraction/manipulation:** Scagnostics (graph-theoretic measures of shape: clumpy, outlying, monotone, etc.) to automatically rank interesting pairs

---

### Parallel Coordinates (p. 162–166)
- **What it shows:** Each data item as a polyline crossing multiple vertical axes (one per attribute); patterns visible as convergence/divergence.
- **When to use / avoid:** Use for detecting correlations and clusters in high-dimensional data. Avoid for very large N (overplotting) without filtering or aggregation.
- **Interesting properties:** Only adjacent axes can be visually compared easily — axis ordering is critical. Hierarchical parallel coordinates aggregate items to reduce clutter.
- **Marks:** Line (polyline)
- **Channels:** Position (y per axis = attribute value), tilt/slope between axes
- **Annotation options:** Brushing on individual axes; color by cluster; axis reordering
- **Data types suited for:** Multivariate table: many quantitative attributes
- **Interesting feature extraction/manipulation:** Inverse correlation: lines that cross between axes reveal negative correlation; parallel lines = positive correlation

---

### Hierarchical Parallel Coordinates (p. 311–312)
- **What it shows:** Aggregated parallel coordinates where clusters of items are shown as bands/ribbons rather than individual polylines.
- **When to use / avoid:** Use for large datasets where individual polylines create hairballs. Avoids overplotting.
- **Interesting properties:** Opacity and width of band can encode variance/density.
- **Marks:** Area (band/ribbon)
- **Channels:** Position, area/width (density), opacity
- **Annotation options:** Color by cluster; expandable detail
- **Data types suited for:** Large multivariate tables with categorical grouping
- **Interesting feature extraction/manipulation:** Hierarchical aggregation — drill down into sub-clusters interactively

---

### Radial Bar Charts (p. 167–168)
- **What it shows:** Bar charts arranged in a circular (polar) layout; length = value radiating from center.
- **When to use / avoid:** Use for cyclical data (months, hours) where the circular metaphor is meaningful. Otherwise, linear bar charts are more perceptually accurate.
- **Interesting properties:** Length perception degrades near center (inner bars compressed). Aesthetic appeal but weak perceptual accuracy.
- **Marks:** Bar (wedge shape)
- **Channels:** Length (radial), angle (category position), color hue
- **Annotation options:** Labels on outer ring; color legend
- **Data types suited for:** Table: quantitative value, cyclic/ordinal key
- **Interesting feature extraction/manipulation:** Normalize to highlight relative patterns

---

### Pie Charts (p. 168–170)
- **What it shows:** Part-to-whole proportions for a set of categories summing to 100%.
- **When to use / avoid:** Use only for 2–5 categories and when part-to-whole relationship is the primary task. Avoid for comparison of segments — angle/area perception is weak.
- **Interesting properties:** The coxcomb / polar area chart (Nightingale) uses area-encoded sectors. Pie charts are nearly always inferior to bar charts for comparison tasks.
- **Marks:** Area (sector/wedge)
- **Channels:** Angle, area, color hue
- **Annotation options:** Percentage labels, callout lines
- **Data types suited for:** Table: categorical key, quantitative value summing to whole
- **Interesting feature extraction/manipulation:** Donut chart variant frees center for summary label

---

### Scatterplots (p. 146–148)
- **What it shows:** Two quantitative attributes as x/y position per item; reveals correlation, clusters, outliers.
- **When to use / avoid:** Use for correlation analysis between two quantitative attributes. Avoid for very large N without density encoding (overplotting).
- **Interesting properties:** Bubble plots add a third quantitative attribute as size. Color adds a fourth (categorical or quantitative).
- **Marks:** Point
- **Channels:** Position x and y (both quantitative), size, color hue/luminance, shape
- **Annotation options:** Regression line, confidence ellipse, annotations on outliers
- **Data types suited for:** Table: two quantitative value attributes
- **Interesting feature extraction/manipulation:** Continuous scatterplots (p. 307–308) for very large datasets — density-encode overlapping points with color

---

### Continuous Scatterplots (p. 307–308)
- **What it shows:** Like a scatterplot but density at each location encoded as color, to handle overplotting in large datasets.
- **When to use / avoid:** Use when N is too large for individual point marks.
- **Interesting properties:** Loses individual identity; shows density topology.
- **Marks:** Area (rasterized)
- **Channels:** Position (x, y), color luminance/saturation (density)
- **Annotation options:** Color scale; contour lines
- **Data types suited for:** Large tables with two quantitative attributes
- **Interesting feature extraction/manipulation:** Log-scaling density to reveal sparse and dense regions simultaneously

---

### Histograms (p. 306)
- **What it shows:** Distribution of a single quantitative attribute, binned.
- **When to use / avoid:** Use for univariate distributions. Avoid too-coarse or too-fine binning.
- **Interesting properties:** Bin width choice critically affects perceived shape. KDE is a smooth alternative.
- **Marks:** Area (bar per bin)
- **Channels:** Position (x = value range), length (y = frequency)
- **Annotation options:** Mean/median lines, normal distribution overlay
- **Data types suited for:** Table: one quantitative attribute
- **Interesting feature extraction/manipulation:** Bin size optimization (Freedman-Diaconis rule)

---

### Boxplot Charts (p. 308–310)
- **What it shows:** Five-number summary (min, Q1, median, Q3, max) plus outliers per group.
- **When to use / avoid:** Use for comparing distributions across groups. Avoid for unimodal vs. multimodal distinction (violin plot is better).
- **Interesting properties:** SolarPlot and vase plot are variants showing more distributional detail. Geographically weighted boxplots (p. 313–315) adapt boxplots for spatial data.
- **Marks:** Line (box, whiskers), point (outliers)
- **Channels:** Position (y = value), length (box height = IQR)
- **Annotation options:** Notches for median CI; jittered data overlay
- **Data types suited for:** Table: one quantitative value, one categorical key
- **Interesting feature extraction/manipulation:** Sort groups by median; overlay raw data points (beeswarm)

---

### Treemaps (p. 213–214)
- **What it shows:** Hierarchical data as nested rectangles; area encodes quantitative attribute; color encodes a second attribute.
- **When to use / avoid:** Use for part-to-whole hierarchy with quantitative leaf values. Avoid for deep hierarchies (rectangles too small) and when path-based navigation matters.
- **Interesting properties:** Space-filling — uses all available pixels. Squarified treemap algorithm optimizes aspect ratios for readability.
- **Marks:** Area (nested rectangles)
- **Channels:** Area (quantitative), color hue/luminance (second attribute), containment (hierarchy)
- **Annotation options:** Labels in cells; zoom on click; color legend
- **Data types suited for:** Tree with quantitative leaf values
- **Interesting feature extraction/manipulation:** Interactive drill-down; spatially ordered treemaps (p. 288) embed geographic ordering

---

### Adjacency Matrix View (p. 208–209)
- **What it shows:** Network/graph as a matrix where rows and columns are nodes and cell fill/color indicates edge presence/weight.
- **When to use / avoid:** Use for dense graphs where node-link becomes a hairball. Avoid when path-following is the primary task (node-link is better for that).
- **Interesting properties:** Matrix reordering (seriation) reveals cluster structure. Hybrid: NodeTrix combines node-link and matrix within the same view.
- **Marks:** Area (cell)
- **Channels:** Color (edge weight/presence), position (node pair)
- **Annotation options:** Row/column labels; dendrogram alongside; color scale
- **Data types suited for:** Network: nodes + edges with optional edge weights
- **Interesting feature extraction/manipulation:** Optimal matrix permutation algorithms reveal block structure

---

### Choropleth Maps (p. 181)
- **What it shows:** Geographic regions colored by a quantitative or categorical attribute value.
- **When to use / avoid:** Use when geographic distribution of an attribute matters. Avoid when areas differ greatly in size (large areas dominate visually even with small populations).
- **Interesting properties:** Cartogram variant distorts area to normalize by population. MAUP (modifiable areal unit problem) — results depend on how regions are defined.
- **Marks:** Area (geographic regions)
- **Channels:** Color (hue for categorical, luminance/saturation for ordered), containment
- **Annotation options:** Legend, labels, interactive hover tooltips
- **Data types suited for:** Spatial geometry with attribute table
- **Interesting feature extraction/manipulation:** Normalize by area or population to reduce confound

---

### Node-Link Diagrams / Force-Directed Placement (p. 201–208)
- **What it shows:** Network structure with nodes as points and edges as lines; force-directed layout minimizes edge crossings and equalizes edge lengths.
- **When to use / avoid:** Use for sparse networks where path-following and cluster detection matter. Avoid for dense networks (hairball problem) — use adjacency matrix instead.
- **Interesting properties:** Non-deterministic layout means same graph looks different each run (unless seed fixed). sfdp (scalable force directed placement) for large graphs.
- **Marks:** Point (nodes), line (edges)
- **Channels:** Position (force-directed), size (node attribute), color hue (node category/cluster)
- **Annotation options:** Node labels; edge labels; degree-sized nodes
- **Data types suited for:** Networks/graphs
- **Interesting feature extraction/manipulation:** LinLog layout for revealing community structure; Strahler numbers for trees (p. 60–61)

---

### Hierarchical Edge Bundles (p. 292–294)
- **What it shows:** Network edges routed along a hierarchical spine to reduce visual clutter; adjacency within hierarchy visible via bundles.
- **When to use / avoid:** Use when a known hierarchy imposes structure on the network. Avoid without a meaningful hierarchy.
- **Interesting properties:** Edge tension parameter controls how tightly edges follow the hierarchy.
- **Marks:** Line (curved, bundled)
- **Channels:** Color hue (edge direction or type), opacity (edge density)
- **Annotation options:** Hover to highlight incident edges; color coding by direction
- **Data types suited for:** Compound network (network + hierarchy)
- **Interesting feature extraction/manipulation:** Reveal intra- vs. inter-cluster connectivity patterns

---

### Small Multiples / Trellis (p. 282–284)
- **What it shows:** The same visualization repeated across a grid, one panel per value of a conditioning variable.
- **When to use / avoid:** Use to compare patterns across groups while keeping scales consistent. Avoid when panels become too small to read detail.
- **Interesting properties:** Trellis / faceting (Becker, Cleveland & Shyu). The most powerful faceting approach uses consistent scales across panels.
- **Marks:** Same as the repeated idiom (any)
- **Channels:** Position in the grid encodes the conditioning variable; internal channels same as base idiom
- **Annotation options:** Panel labels; shared axis labels; consistent scale
- **Data types suited for:** Any multidimensional dataset with a grouping variable
- **Interesting feature extraction/manipulation:** Main-effects ordering — sort panels by a summary statistic to reveal trends

---

### Linked Views / Coordinated Multiple Views (p. 267–296)
- **What it shows:** Multiple different visualizations of the same dataset, linked so selections/highlights propagate across views.
- **When to use / avoid:** Use when no single view captures all relevant aspects. Avoid excessive linking that confuses users — limit to 2–4 coordinated views.
- **Interesting properties:** Linked highlighting (brushing) is the core interaction primitive. Overview–detail is a common linked-view pattern.
- **Marks:** Varies per view
- **Channels:** Varies per view; color highlight indicates selection across views
- **Annotation options:** Selection bands, tooltips
- **Data types suited for:** Any multidimensional dataset
- **Interesting feature extraction/manipulation:** Cross-filtering — selections in one view filter data shown in others

---

### Focus+Context Displays (p. 323–338)
- **What it shows:** The region of interest at full detail while maintaining context of surrounding data at reduced scale/detail.
- **When to use / avoid:** Use when navigating large datasets where overview context helps interpretation. Avoid when context and detail compete for the same space confusingly.
- **Interesting properties:** Fisheye lens distorts space continuously. DOI (degree-of-interest) assigns importance scores. Hyperbolic geometry maps infinite space onto finite display. Stretch-and-squish navigation (DOITrees).
- **Marks:** Varies
- **Channels:** Size/spatial position modulated by importance/distance from focus
- **Annotation options:** Focus indicator; smooth animated transition during navigation
- **Data types suited for:** Trees, networks, large maps, any large dataset
- **Interesting feature extraction/manipulation:** Object constancy — items must maintain identity through transitions to avoid disorientation

---

### Superimposed Line Charts (p. 290–291)
- **What it shows:** Multiple time series on the same axis, layered on top of each other.
- **When to use / avoid:** Use for 2–5 series comparison. Avoid for more series (color discrimination limit, occlusion).
- **Interesting properties:** Horizon graphs (Sizing the Horizon, p. 90–91) fold multiple lines into a space-efficient layered representation.
- **Marks:** Line
- **Channels:** Position (y = value, x = time), color hue (series identity)
- **Annotation options:** Legend, labels at endpoints, interactive hover
- **Data types suited for:** Table: quantitative value, temporal key, categorical attribute (series)
- **Interesting feature extraction/manipulation:** Normalize each series (z-score) to compare shapes rather than magnitudes

---

### Dimensionality Reduction for Document Collections (p. 316–319)
- **What it shows:** High-dimensional feature vectors (e.g., TF-IDF) projected to 2D using MDS, t-SNE, or similar, then shown as a scatterplot.
- **When to use / avoid:** Use for exploring similarity structure in high-dimensional data. Avoid trusting distances as exact — projections distort.
- **Interesting properties:** Multidimensional scaling (MDS) preserves pairwise distances. Glimmer uses multilevel MDS on GPU for large corpora. Dimensionality reduction loses information — must validate.
- **Marks:** Point
- **Channels:** Position (derived from similarity), color hue/size (metadata attribute)
- **Annotation options:** Cluster labels; zoom for text snippets
- **Data types suited for:** High-dimensional tables, document-term matrices
- **Interesting feature extraction/manipulation:** Scagnostics on the projection to detect clusters, outliers, patterns

---

### Graph-Theoretic Scagnostics (p. 342–346)
- **What it shows:** Summary statistics of scatterplot shape (computed via minimum spanning tree, convex hull, etc.) used to rank which pairs of variables in a SPLOM are most interesting.
- **When to use / avoid:** Use to prioritize exploration of large SPLOM matrices. Not a visualization itself but a tool to guide attention.
- **Interesting properties:** Nine scagnostic measures: outlying, skewed, clumpy, sparse, striated, convex, skinny, stringy, monotone.
- **Marks:** Not a display idiom — a derived metric
- **Channels:** N/A (output is a ranked list or color-coded SPLOM)
- **Annotation options:** Color-coded SPLOM cells by highest scagnostic score
- **Data types suited for:** Multivariate table: many quantitative attributes
- **Interesting feature extraction/manipulation:** Automatically surface non-linear correlations, clusters, bimodal distributions that linear correlation misses

---

### LineUp (p. 246–248)
- **What it shows:** Multi-attribute rankings: items sorted by a weighted combination of multiple attributes, with bar charts per attribute to show values.
- **When to use / avoid:** Use when users need to explore and compare multi-criteria rankings.
- **Interesting properties:** Users can adjust weights interactively; attribute columns can be stacked, grouped, or reordered.
- **Marks:** Bar (per attribute per item)
- **Channels:** Length (attribute value), position (rank)
- **Annotation options:** Sort handles, weight sliders, color coding
- **Data types suited for:** Multidimensional table: multiple quantitative attributes per item
- **Interesting feature extraction/manipulation:** Stacking bars for composite score; separating groups for comparison
