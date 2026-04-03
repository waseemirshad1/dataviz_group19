# [agent_16] Visualization Analysis and Design — pages 1-50

## Visualization Catalogue: Chapters 1–3

Pages 1–50 are primarily theoretical (definitions, framework, data types, task types). Concrete idioms are introduced only as illustrative examples or in the "How: A Preview" section. The chapters lay groundwork for the detailed idiom coverage in Chapters 5–14. Below are all visualization types named or illustrated in these pages.

---

### Scatterplot (p.8, p.18, referenced throughout)
- **What it shows:** Joint distribution of two quantitative attributes; each item is a point positioned by its two attribute values
- **When to use:** Exploring correlations, dependencies, clusters, outliers between two quantitative variables; showing detailed distribution (not just summary statistics)
- **When to avoid:** When items are so dense they overlap into an unreadable mass; when one or both attributes are categorical
- **Interesting properties:** Anscombe's Quartet (p.7–8) shows that four structurally different datasets can have identical summary statistics but completely different visual patterns — scatterplots reveal what summaries hide; classic demonstration of why showing detail matters
- **Marks:** Points (items as 0-dimensional marks)
- **Channels:** Position x (quantitative), position y (quantitative); additional channels can include color hue (categorical), size (quantitative), shape (categorical)
- **Annotation options:** Regression lines, reference lines, quadrant labels, text labels on individual points
- **Data types suited for:** Flat tables with two or more quantitative attributes; items as rows
- **Interesting feature extraction/manipulation of data:** Derive new attributes (e.g., difference, ratio, residual) and encode them as x or y instead of raw values to make the quantity of interest directly readable (p.52, Figure 3.5)

---

### Bar Chart (referenced p.10, listed in table of contents p.150)
- **What it shows:** Quantity of a quantitative attribute across categories; one bar per item or category
- **When to use:** Comparing magnitudes across categorical groups; ranking items
- **When to avoid:** When order within categories is irrelevant and a dot plot would reduce ink; when the zero baseline is not meaningful
- **Interesting properties:** Mentioned as a classic idiom (p.10) that can be linked interactively with other views (e.g., selecting a bar highlights associated items in a scatterplot)
- **Marks:** Bars (area marks); rectangular regions
- **Channels:** Length (quantitative attribute value) — highly accurate channel; position on shared baseline; color hue (categorical grouping)
- **Annotation options:** Value labels on bars, reference lines, error bars
- **Data types suited for:** Tables with one categorical key and one quantitative value attribute
- **Interesting feature extraction/manipulation of data:** Derive aggregates (sum, mean, count) per category before encoding; sort bars by value to enable ranking tasks

---

### Line Chart / Dot and Line Chart (p.10, table of contents p.155)
- **What it shows:** Trends in a quantitative attribute over an ordered dimension (typically time); each data point is a dot, connected by lines to imply continuity
- **When to use:** Time-series data; showing trends, periodicity, seasonal patterns; comparing trajectories of multiple series
- **When to avoid:** When the x-axis is categorical with no inherent order; when many overlapping lines create visual clutter
- **Interesting properties:** Example in p.54 (browse task): user examines share price on a specific date by looking at the height of each line on that day
- **Marks:** Points (items), Lines (connections between ordered items)
- **Channels:** Position x (ordered/temporal key), position y (quantitative value); color hue to distinguish multiple series
- **Annotation options:** Highlighted time points, anomaly markers, trend lines, shaded confidence intervals
- **Data types suited for:** Time-series tables (time as key, quantitative value); ordered sequences
- **Interesting feature extraction/manipulation of data:** Derive difference series, moving averages, seasonal decomposition; multiple temporal scales (daily/weekly/monthly) can be shown by aggregating at different levels

---

### Choropleth Map (p.54, table of contents p.181)
- **What it shows:** Geographic regions colored or shaded by a quantitative or categorical attribute; one region = one item
- **When to use:** Showing spatial distribution of an attribute across regions; identifying geographic clusters or patterns
- **When to avoid:** When region size is highly variable (large regions dominate visually regardless of their values); for precise quantitative comparison
- **Interesting properties:** Used in election results example (p.54–55): states colored red/blue with saturation showing margin of victory; supports identify (one state), compare (state vs. state), summarize (all states) tasks
- **Marks:** Areas (region boundaries as area marks)
- **Channels:** Color saturation (ordered/quantitative magnitude), color hue (categorical attribute such as party affiliation)
- **Annotation options:** Text labels on regions, legend, reference lines
- **Data types suited for:** Tables with geographic key (state, country, region) and one quantitative or categorical value attribute
- **Interesting feature extraction/manipulation of data:** Derive aggregated values per region (totals, percentages, ratios); normalize by area or population to avoid size bias

---

### Node-Link Network Diagram (p.5, p.10, table of contents p.201–207)
- **What it shows:** Network topology — nodes as items, links as relationships; spatial layout encodes proximity/grouping
- **When to use:** Understanding connectivity, topology, paths, clusters in relational data; genealogies, social networks, gene interaction networks
- **When to avoid:** Very dense networks where edges overlap into a visual hairball; when adjacency matrix would be clearer
- **Interesting properties:** Figure 1.2 (Cerebral, p.5): layered layout captures biological textbook style — layers = cellular locations; interactivity highlights neighbors on mouseover; illustrates how computation enables layouts impossible by hand
- **Marks:** Points/glyphs (nodes), Lines (links/edges)
- **Channels:** Position (encodes topology via layout algorithm); color hue (node category, e.g., gene type); size (node importance/degree); shape (node type)
- **Annotation options:** Node labels, edge labels, highlighted paths, cluster hulls
- **Data types suited for:** Network datasets (nodes + links); tree datasets
- **Interesting feature extraction/manipulation of data:** Derive centrality metrics (Strahler number, p.60–61) to filter peripheral nodes and show only the important skeleton; derive similarity scores to create a network from a table (p.52–53, VxInsight example)

---

### Treemap (table of contents p.213)
- **What it shows:** Hierarchical data using nested rectangles; area of each rectangle encodes a quantitative value
- **When to use:** Showing proportions in large hierarchies (file systems, organizational structures, taxonomies); when space-filling is important
- **When to avoid:** When exact comparisons are needed (area is a less accurate channel than length/position); when hierarchy is not meaningful
- **Interesting properties:** Mentioned in table of contents; space-filling layout maximizes information density
- **Marks:** Areas (nested rectangles)
- **Channels:** Area (quantitative); color hue (categorical level); color saturation (quantitative within category)
- **Annotation options:** Text labels within rectangles (when large enough), color legend
- **Data types suited for:** Tree datasets with quantitative value attributes on leaf nodes
- **Interesting feature extraction/manipulation of data:** Aggregate leaf values up the hierarchy; derive relative proportions; sort children by value within each parent

---

### Streamgraph / Stacked Area Chart (table of contents p.153)
- **What it shows:** Evolution of multiple categorical components over an ordered axis (usually time); total and part-whole proportions simultaneously
- **When to use:** Showing how composition of a total changes over time; multiple time series that sum to a meaningful total
- **When to avoid:** When individual series values need to be read precisely (stacking makes baselines non-zero for all but the bottom series); when there are too many categories
- **Interesting properties:** Streamgraph is a variant where the baseline is centered to give a flowing, organic visual appearance rather than a flat bottom baseline
- **Marks:** Areas (one area per category, stacked)
- **Channels:** Area (quantitative — part of total at each time point); color hue (categorical — which component); position x (ordered time key)
- **Annotation options:** Category labels at end of bands, interactive tooltips
- **Data types suited for:** Tables with a categorical key (component/category) + temporal key (time) + quantitative value (amount)
- **Interesting feature extraction/manipulation of data:** Aggregate by time period; normalize to percentage of total for relative view; reorder layers by total magnitude

---

### Parallel Coordinates (table of contents p.162)
- **What it shows:** Multiple quantitative attributes simultaneously for many items; each item = one polyline crossing all axes
- **When to use:** Exploring multidimensional data; finding correlations and clusters; comparing items across many attributes
- **When to avoid:** When items are so many that the display is an unreadable mass of overlapping lines; when attributes are categorical
- **Interesting properties:** Each axis = one attribute; crossing or parallel lines indicate negative/positive correlations; brushing on one axis filters items shown
- **Marks:** Lines (one per item, crossing all axes)
- **Channels:** Position on each axis (quantitative value per attribute); color hue (categorical group); opacity (density in crowded displays)
- **Annotation options:** Axis labels, highlighted selections, range filters
- **Data types suited for:** Tables with multiple quantitative attributes; items as rows
- **Interesting feature extraction/manipulation of data:** Reorder axes to place correlated or compared attributes adjacent; normalize axes to [0,1] for cross-attribute comparison; derive cluster assignments and color accordingly

---

### Scatterplot Matrix / SPLOM (table of contents p.160)
- **What it shows:** All pairwise scatterplots of a multivariate dataset in a matrix layout; diagonal shows distribution of each individual attribute
- **When to use:** Initial exploration of correlation structure in a multivariate dataset; identifying which attribute pairs are most interesting
- **When to avoid:** When there are many attributes (matrix grows as n²); when individual plots become too small to read
- **Interesting properties:** Provides a comprehensive overview of all pairwise relationships in one view; efficient for datasets with 3–8 attributes
- **Marks:** Points within each cell (items)
- **Channels:** Position x and y within each cell (two attributes per cell); color/size for additional attributes
- **Annotation options:** Regression lines, correlation coefficients in cells, histograms on diagonal
- **Data types suited for:** Tables with multiple quantitative attributes
- **Interesting feature extraction/manipulation of data:** Reorder rows/columns by attribute cluster; filter to subset of attributes; color by a categorical variable to reveal group structure

---

### Cluster Heatmap (table of contents p.158)
- **What it shows:** Matrix of values with rows and columns reordered by hierarchical clustering; color encodes the value in each cell
- **When to use:** Revealing clusters and patterns in a data matrix (e.g., gene expression across conditions); when both row and column ordering matters
- **When to avoid:** When precise quantitative reading is needed (color is a less accurate channel); when the matrix is not square or not meaningful to cluster
- **Interesting properties:** Hierarchical clustering of rows and columns (shown as dendrograms) reveals natural groupings; commonly used in biology (gene expression)
- **Marks:** Areas (one rectangle per cell)
- **Channels:** Color saturation/luminance (ordered quantitative value); position (row = one item, column = one attribute); dendrograms encode clustering structure
- **Annotation options:** Row/column labels, color scale legend, dendrogram branch annotations
- **Data types suited for:** Tables with quantitative values; multidimensional tables (gene × condition = expression level)
- **Interesting feature extraction/manipulation of data:** Derive normalized z-scores per row for comparable color encoding; apply hierarchical clustering to derive row/column ordering; derive cluster membership as a new categorical attribute

---

### Glyph / Multilevel Network (Figure 1.4, p.10–11 — Grouse vis)
- **What it shows:** Network at multiple levels of hierarchy simultaneously; metanodes represent collapsed subnetworks
- **When to use:** Very large networks where full detail cannot be shown at once; hierarchically structured networks where zooming into clusters is needed
- **When to avoid:** When the network has no meaningful hierarchical structure
- **Interesting properties:** Figure 1.4 (Grouse): metanode color encodes topological structure; hexagons = closed metanodes; discs = open ones; illustrates complex idiom combining encoding and interaction
- **Marks:** Points (leaf nodes — square), Glyphs (metanodes — disc/hexagon), Lines (links)
- **Channels:** Color hue (topological structure within metanode); shape (open vs. closed metanode vs. leaf node); size (metanode = more items)
- **Annotation options:** Name labels on opened nodes, detail insets for selected clusters
- **Data types suited for:** Compound networks (network + hierarchy); large social or citation networks
- **Interesting feature extraction/manipulation of data:** Derive hierarchical grouping of nodes; derive topological features (cliques, clusters) to assign metanode color

---

### Name Voyager / Stacked Stripe Chart (Figure 3.3, p.48)
- **What it shows:** Popularity of names over time (1900–present); each name = one horizontal stripe, height = popularity at each year; brighter = currently popular
- **When to use:** Showing trends over time for many categorical items simultaneously; combining temporal trend with magnitude
- **Interesting properties:** Originally for present task (parents choosing names), widely adopted for enjoy/discover tasks — demonstrates that task goals can diverge from designer's intent (p.48)
- **Marks:** Areas (one stripe per name)
- **Channels:** Height of stripe (quantitative — popularity); color luminance/brightness (recency/current popularity); color hue (categorical — gender: pink/blue); position x (temporal key — year)
- **Annotation options:** Interactive label appearing on hover; text search input to filter names
- **Data types suited for:** Tables with categorical key (name) + temporal key (year) + quantitative value (popularity rank/frequency)
- **Interesting feature extraction/manipulation of data:** Filter to names starting with a typed prefix; aggregate annual counts into smoothed trends; normalize by total births per year

---

### Graphical History View (Figure 3.4, p.49–50 — Tableau)
- **What it shows:** Branching history of analysis states during a vis session; each node = snapshot of the vis at a particular state
- **When to use:** Supporting analytical provenance; allowing users to revisit and compare earlier states; recording and presenting the analysis process
- **Interesting properties:** Branching meta-visualization; supports record goal; allows undo/redo and exploration of alternative analysis paths
- **Marks:** Points/thumbnails (history states), Lines (transitions between states)
- **Channels:** Spatial position (temporal/logical ordering of states); thumbnail image (visual summary of each state)
- **Annotation options:** User-added notes per state, timestamps, parameter values
- **Data types suited for:** Interaction log data; sequences of parameter settings
- **Interesting feature extraction/manipulation of data:** Derive diffs between consecutive states to highlight what changed; group branching points by type of interaction

---

### Tree Visualization with Strahler Filtering (Figure 3.10, p.60–61)
- **What it shows:** Large hierarchical tree with nodes filtered to show only the most topologically important skeleton; nodes colored by centrality
- **When to use:** Summarizing large trees where full detail would overwhelm; communicating overall topology rather than individual node details
- **Interesting properties:** Strahler number = derived centrality attribute; filtering to top 5000 of 500,000+ nodes still produces a recognizable skeleton — demonstrates power of derived attributes (p.60–61)
- **Marks:** Points (nodes), Lines (links)
- **Channels:** Color (Strahler number — quantitative centrality); size (optional — node importance); position (layout algorithm)
- **Annotation options:** Node labels for important nodes only
- **Data types suited for:** Tree datasets (hierarchical networks)
- **Interesting feature extraction/manipulation of data:** Derive Strahler number (global computation, not local); filter peripheral nodes; use derived attribute both for filtering and as an additional color channel simultaneously

