# [agent_17] Visualization Analysis and Design — pages 51-100

## Note on Pages 51–100

These chapters (Ch. 2 continued, Ch. 3, Ch. 4) focus on *data abstraction*, *task abstraction*, and *design validation framework*. They are primarily theoretical and methodological. The visualization examples cited are illustrative of the framework, not full descriptions of chart types. The full catalogue of visualization idioms is introduced in Chapters 7–14 (referenced but not yet covered). However, the examples shown here are documented below.

---

### Node-Link Diagram (network / tree layout) (p.51–52, p.85–87)
- **What it shows:** Nodes (items) and links (relationships between them). For trees, shows hierarchical parent-child structure.
- **When to use:** Whenever the dataset type is a network or tree, and the task involves understanding topology, paths, or hierarchical structure.
- **When to avoid:** Dense networks where many cross-links create visual clutter ("hairball" effect). Not suitable for showing attribute distributions.
- **Interesting properties:** Spatial layout is a *design choice*, not given by the data — the abstract network concept is separate from its drawn arrangement. Can be filtered by derived centrality attributes (e.g. Strahler number) to show a simplified skeleton.
- **Marks:** Points/circles (nodes), line segments (links/edges).
- **Channels:** Position (node placement), color (hue for category, saturation/luminance for quantitative attributes like Strahler number), size (node importance), line style (link attributes).
- **Annotation options:** Text labels on nodes; color coding of nodes and links by derived attributes; highlight/selection states.
- **Data types suited for:** Network (graph), Tree, Compound network.
- **Interesting feature extraction/manipulation of data:** Derive Strahler number (centrality metric) as a new quantitative attribute → filter to top-N nodes → reveals structural skeleton of even very large trees (>500,000 nodes) (p.86–87).

---

### Choropleth Map (p.79–80)
- **What it shows:** Geographic areas (e.g. states) color-coded by an attribute value (e.g. election results, margin of victory).
- **When to use:** When data has geographic attributes and the task involves spatial comparison, distribution, or identifying geographic patterns.
- **When to avoid:** When precise value comparison is needed (color is a weak channel for quantitative judgment). Can mislead when large-area regions dominate visually regardless of population or importance.
- **Interesting properties:** Supports all three query levels: identify (one state's result), compare (two states), summarize (overall distribution across all states). Spatial structure carries meaning.
- **Marks:** Filled areas (2D regions).
- **Channels:** Color hue (categorical winner), color saturation (margin of victory / ordered magnitude).
- **Annotation options:** Labels, tooltips showing exact values, outlines for emphasis.
- **Data types suited for:** Spatial/geographic data with one key attribute (location) and one or more value attributes (categorical or quantitative).
- **Interesting feature extraction/manipulation of data:** Diverging color scale suits diverging data (e.g. margin in favor of party A vs. party B, meeting at 0). Saturation encodes magnitude within each hue.

---

### Line Graph / Time-Series Graph (p.79, p.163 ref)
- **What it shows:** Values of one or more quantitative attributes over a sequential or temporal key.
- **When to use:** When time (or another ordered sequential attribute) is the key and the task is to find trends, correlations, anomalous spikes, or periodic patterns.
- **When to avoid:** When data is not ordered/temporal, or when too many overlapping lines create confusion.
- **Interesting properties:** Supports browse search (scanning all lines at a specific date) and explore search (finding outliers/spikes). Encoding the *derived difference* between two lines as a new attribute is often preferable to asking users to judge gap between two curves visually (p.77–78).
- **Marks:** Lines (paths connecting points).
- **Channels:** Position (x = time, y = value), color hue (distinguish different series/companies), line weight.
- **Annotation options:** Reference lines, annotated peaks/troughs, labeled events.
- **Data types suited for:** Tables with temporal key; time-series datasets.
- **Interesting feature extraction/manipulation of data:** Derive difference attribute (e.g. trade balance = exports − imports) and encode it directly instead of both raw series — reduces perceptual demand for comparison tasks (p.77).

---

### Name Voyager (Stacked Area Chart variant) (p.73–74)
- **What it shows:** Popularity of baby names in the US since 1900; each name is a stripe whose height encodes popularity at a given year. Brighter = currently more popular; gender encoded by hue.
- **When to use:** When the task is to explore trends for one or more items filtered by an interactive query (e.g. type letters to filter names). Suited to the "enjoy" goal.
- **When to avoid:** When precise quantitative comparison between names is needed (stacked/overlapping stripes make precise reading difficult).
- **Interesting properties:** Originally designed for one user goal (expectant parents), but was adopted enthusiastically by people with entirely different goals (historical trend analysis for enjoyment) — illustrates how real user goals can diverge from designer intent.
- **Marks:** Filled strips/bands.
- **Channels:** Height (length) = popularity (quantitative); Color hue = gender (categorical); Color brightness/saturation = recency of popularity.
- **Annotation options:** Name labels; interactive query input.
- **Data types suited for:** Multidimensional table: key = (name, year); value = popularity count. Plus categorical attribute of gender.
- **Interesting feature extraction/manipulation of data:** Interactive filtering by text prefix immediately narrows the dataset to a subset of names in real time — demonstrates dynamic interaction linked to filtering.

---

### Scatterplot (implied in multiple examples) (p.87–89)
- **What it shows:** Relationship between two quantitative attributes by encoding each item as a point with position along two spatial axes.
- **When to use:** When the task is to find correlation, dependency, clustering, or outliers between two quantitative attributes. Very commonly paired with derived attributes to reveal structures not visible in original data.
- **When to avoid:** When data is categorical or ordinal without quantitative encoding; when overplotting obscures the data (too many identical or very close points without opacity or jitter).
- **Interesting properties:** In the computational fluid dynamics example, scatterplots of derived attributes (vorticity vs. enthalpy; pressure vs. temperature) reveal spatial structures (recirculation zones, wake regions) that are not distinguishable in the original physical space view (p.87–89).
- **Marks:** Points.
- **Channels:** Position x (quantitative), position y (quantitative), color hue (categorical group), color saturation (quantitative attribute).
- **Annotation options:** Color highlighting of brushed/selected regions, linked highlighting across multiple views.
- **Data types suited for:** Tables with at least two quantitative value attributes; especially suited when applied to derived attributes.
- **Interesting feature extraction/manipulation of data:** Creating many derived attributes and plotting each pair in separate linked scatterplots is a powerful technique for feature detection in spatial field data. Regions brushed in one derived-space view are highlighted in all other linked views.

---

### Multiple Juxtaposed Linked Views (p.87–89, Figure 3.12)
- **What it shows:** Multiple simultaneously visible views of the same dataset, each showing a different projection or pair of derived variables; views are coordinated so selections in one are highlighted in all.
- **When to use:** When the dataset has multiple attributes or can yield many derived attributes, and the task involves discovering, browsing, and comparing features across multiple projections. Particularly powerful for spatial field data with derived attributes.
- **When to avoid:** When screen space is limited; when views are too numerous and cognitive load becomes overwhelming; when the user task is narrow and only one view is needed.
- **Interesting properties:** The combination of juxtaposition + shared color highlighting enables the user to understand where spatially contiguous regions in one view fall in other views. Features that are indistinguishable in physical space can be clearly selected and followed through all derived spaces.
- **Marks:** Points (scatterplots), or other mark types depending on the individual view.
- **Channels:** Position (within each view), color hue (shared highlight across views — links data between views).
- **Annotation options:** Selection brushing with shared color code; derived-attribute palette showing all available variables.
- **Data types suited for:** Spatial fields; also any multivariate tabular data with many attributes.
- **Interesting feature extraction/manipulation of data:** Must first derive many new quantitative attributes from the original data, then facet them into multiple views. The faceting + coordination is the key interaction idiom.

---

### SpaceTree (p.84–86)
- **What it shows:** Large tree structure where navigation/selection automatically aggregates and filters unselected branches.
- **When to use:** When the task is to present a path traced between two nodes of a large tree, and space is limited.
- **When to avoid:** When users need to see the full tree context alongside the selected path; when the automatic filtering would obscure information the user needs.
- **Interesting properties:** Selection is tied to aggregation/filtering — unselected parts of the tree automatically collapse. Reduces clutter but limits context.
- **Marks:** Nodes (points/rectangles), links (lines).
- **Channels:** Position (layout), highlighting (selection state).
- **Annotation options:** Node labels; path highlight.
- **Data types suited for:** Trees (hierarchical networks).
- **Interesting feature extraction/manipulation of data:** Uses the idiom of focus+context: selecting a node/path hides peripheral nodes. Equivalent to a filter derived from the selection state.

---

### TreeJuxtaposer (p.84–86)
- **What it shows:** Large tree with explicit arrangement to ensure two subtrees are visible simultaneously for comparison.
- **When to use:** When the task requires showing a path between two distant nodes without hiding surrounding context.
- **When to avoid:** When screen space is extremely limited; for tasks that don't require explicit side-by-side comparison of tree regions.
- **Interesting properties:** Does not use automatic aggregation/filtering (unlike SpaceTree). Uses spatial arrangement to create visibility. Allows users to navigate and select paths with surrounding tree context preserved.
- **Marks:** Nodes, links.
- **Channels:** Position (explicit arrangement), color/highlight (selected path).
- **Annotation options:** Path highlight; labels.
- **Data types suited for:** Trees, large hierarchical networks.
- **Interesting feature extraction/manipulation of data:** Uses derived spatial arrangement (layout algorithm) to solve visibility; the spatial transformation of the tree is the key design choice.

---

### Word Tree (p.97, Figure 4.3)
- **What it shows:** A hierarchical tree of keywords laid out horizontally, preserving context of keyword usage within original text.
- **When to use:** When the task involves understanding the context and patterns of keyword usage in a text corpus.
- **When to avoid:** Very large corpora with many divergent contexts (visual clutter).
- **Interesting properties:** Combines visual encoding idiom (horizontal hierarchical tree) with interaction idiom (navigation by keyword selection). A good example where encoding and interaction idioms are tightly coupled.
- **Marks:** Text labels arranged as tree nodes; lines connecting branches.
- **Channels:** Position (horizontal = depth/proximity in text context), indentation (hierarchy level).
- **Annotation options:** Selected keyword highlighted; navigable branching paths.
- **Data types suited for:** Text corpus (derived as a tree structure via parsing).
- **Interesting feature extraction/manipulation of data:** Text is transformed into a tree structure — an example of dataset-type transformation (unstructured text → hierarchical tree with quantitative frequency attributes).

---

### Graphical History / Analytical Provenance View (p.74–75, Figure 3.4)
- **What it shows:** A branching meta-visualization of all the static snapshots from an analysis session (e.g. Tableau's graphical history feature). Each snapshot shows the state of the vis at a specific moment.
- **When to use:** When the task involves a complex, exploratory analysis session where the user needs to revisit earlier states, parameter settings, or compare current results to previous ones. Supports "record" produce goals.
- **When to avoid:** Casual / short analysis sessions; when provenance tracking would overwhelm the interface.
- **Interesting properties:** Turns the process of analysis itself into a visualizable artifact. Supports analytical provenance.
- **Marks:** Small thumbnail images (miniaturized vis snapshots), linking lines (branching history).
- **Channels:** Position (temporal sequence), connectivity (branching).
- **Annotation options:** Labels on each snapshot; bookmarked states.
- **Data types suited for:** Any vis output — this is a meta-visualization of the interaction log.
- **Interesting feature extraction/manipulation of data:** Records parameters and interaction logs — represents the "derive" and "record" produce actions explicitly.
