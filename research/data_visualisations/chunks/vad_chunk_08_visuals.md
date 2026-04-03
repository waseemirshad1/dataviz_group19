# [agent_23] Visualization Analysis and Design — pages 351-400

## Visualization Catalogue: Chapter 14 (cont.) & Chapter 15

---

### Toolglass / Magic Lens (p. 351)

- **What it shows:** A local, see-through foreground layer superimposed on a larger background scene. Within the lens, a different visual encoding is shown (e.g., color-coded Gaussian curvature); outside the lens, the original rendering provides context.
- **When to use:** When you want to reveal hidden or computed attributes in a local area without replacing the rest of the view. Especially useful for 3D scenes or dense backgrounds where context matters.
- **When to avoid:** When the focus area is large enough to justify a separate view; when occlusion of the lens region is unacceptable.
- **Interesting properties:** The lens occludes what is beneath it (foreground replaces background locally). Multiple lens types can be swapped for different encodings of the same underlying scene.
- **Marks:** The lens boundary (a circle or rectangle); the encoded marks within (colors, values, etc.)
- **Channels:** Color (for the encoded attribute inside the lens); the lens position encodes spatial selection
- **Annotation options:** Numeric readout at lens center (e.g., curvature value at cursor point)
- **Data types suited for:** Any spatial or abstract data where two simultaneous encodings of the same space are useful
- **Interesting feature extraction/manipulation of data:** Computes a derived attribute (e.g., Gaussian curvature) that is only shown within the lens region; the original rendering remains untouched everywhere else

---

### Fisheye Lens (p. 353–354, 360–361)

- **What it shows:** A moveable magnification lens applied to any layout. The region under the lens is magnified with continuous radial distortion (high magnification at center, decreasing toward edges), keeping it embedded within the surrounding context.
- **When to use:** Navigating large, dense displays where labels are illegible but spatial context matters. Good for browsing node-link graphs where topological structure (not metric) is the primary task.
- **When to avoid:** Tasks requiring distance or length comparisons (distortion impairs metric judgements). Unfamiliar structures where continuous magnification adds disorienting cognitive load. When occlusion from a discrete magnifying lens would be acceptable.
- **Interesting properties:** No occlusion — distorted and undistorted regions co-exist continuously. However, continuous magnification gradient is harder to mentally "undo" than a discrete jump.
- **Marks:** All marks of the underlying layout (nodes, lines, areas, etc.)
- **Channels:** Spatial position is distorted; all other channels (color, size, shape) remain undistorted within the lens
- **Annotation options:** Labels become readable inside the lens where they were too small outside
- **Data types suited for:** Any (spatial, abstract, network, table)
- **Interesting feature extraction/manipulation of data:** Dynamically computes vertex positions under the lens using vertex shaders; modern GPU hardware makes this interactive at high performance

---

### Cone Trees (p. 352–353)

- **What it shows:** A 3D node-link tree layout using standard perspective projection as a distortion mechanism — items near the viewer are shown larger and in more detail.
- **When to use:** Historical reference; once popular for exploring large trees. Perspective creates an intuitive depth-based focus+context effect.
- **When to avoid:** Abstract (non-spatial) data, where 3D costs (occlusion, perspective distortion making metric judgements hard) outweigh benefits. Mostly superseded by 2D alternatives.
- **Interesting properties:** Familiar from everyday 3D experience; strong first impression but loses appeal over time. Interaction is standard geometric navigation (rotation).
- **Marks:** Nodes (dots/spheres), links (lines/cylinders)
- **Channels:** 3D spatial position, size via perspective foreshortening, depth cues
- **Annotation options:** Node labels (readable near focus, illegible at periphery)
- **Data types suited for:** Trees
- **Interesting feature extraction/manipulation of data:** Relies entirely on the implicit magnification of standard 3D perspective transforms

---

### Hyperbolic Tree / H3 (p. 354–356)

- **What it shows:** A layout that maps a tree or network onto a non-Euclidean hyperbolic space then projects it to a Euclidean circle (2D) or sphere (3D). Items near the center of projection are magnified; items at the periphery are minimized. Interaction is hyperbolic translation (moving the focus point).
- **When to use:** Trees and networks that grow exponentially — where standard Euclidean space cannot accommodate all nodes at a readable size. When topological exploration (not metric) is the task.
- **When to avoid:** When precise angle/distance comparisons are needed. The 3D version adds occlusion overhead.
- **Interesting properties:** Mathematically elegant: infinite non-Euclidean plane maps to a finite Euclidean circle. Provides global fisheye-like effect but with a coherent mathematical model. The enclosing circle serves as a distortion indicator.
- **Marks:** Nodes, connection lines
- **Channels:** Radial position encodes distance-from-focus; size encodes depth/proximity to focus
- **Annotation options:** Node labels readable near center
- **Data types suited for:** Trees, networks
- **Interesting feature extraction/manipulation of data:** Hyperbolic translation is mathematically equivalent to changing the projection origin; animated transitions show structural changes smoothly

---

### Stretch and Squish Navigation / TreeJuxtaposer (p. 356–358)

- **What it shows:** Two or more large trees (or any layout) where the user can interactively stretch specific rectangular regions of the display (making them larger) while the rest is automatically squished. All items remain visible. Supports direct comparison of large structures.
- **When to use:** Side-by-side comparison of large trees or sequences; situations where guaranteed visibility of high-importance items is required.
- **When to avoid:** Tasks requiring global metric comparisons (squished regions distort distance judgements). Dense data where even squished representations are too small to be meaningful.
- **Interesting properties:** **Guaranteed visibility** — items with high importance values are always rendered visible even when hundreds of items fall within a single pixel (custom sub-pixel aggregation). Borders of the sheet stay fixed so nothing leaves the viewport.
- **Marks:** Nodes (may reduce to single pixels), rectangles for focus regions
- **Channels:** Spatial position (distorted); color (for importance/attributes); size (varies by distortion)
- **Annotation options:** High-importance items maintain visible marks regardless of region size
- **Data types suited for:** Trees, sequences, any layout
- **Interesting feature extraction/manipulation of data:** Derived "importance" attribute controls sub-pixel aggregation behavior; colored marks (e.g., sequence differences in red) always stay visible

---

### Nonlinear Magnification Fields (p. 358–359)

- **What it shows:** A general framework for applying multiple overlapping magnification/minimization zones of arbitrary shapes and levels to any layout. The implicit magnification field required to achieve a desired transformation is computed automatically.
- **When to use:** Complex interactive exploration where multiple focal points of different priorities exist simultaneously. Data-driven magnification of specific trajectories or events.
- **When to avoid:** Simple tasks where a single fisheye or magnifying lens suffices.
- **Interesting properties:** Can expose the magnification field itself as a visual object (shown as a height field / surface). Supports data-driven magnification trails (e.g., following moving objects).
- **Marks:** All marks of the underlying layout; optionally the magnification surface itself
- **Channels:** Spatial position (distorted); magnification field height as an additional visual variable
- **Annotation options:** Superimposed grid or shading showing the distortion field explicitly
- **Data types suited for:** Any
- **Interesting feature extraction/manipulation of data:** Derives the implicit magnification field from desired transformation specifications; field can be driven by data attributes (e.g., event importance)

---

### Scagnostics / Scatterplot of Scatterplots (p. 342–345)

- **What it shows:** A SPLOM where each point represents an entire scatterplot from a larger SPLOM. Nine quantitative shape measures (outlying, skewed, clumpy, sparse, striated, convex, skinny, stringy, monotonic) are computed for each pairwise attribute combination and displayed as points in a new SPLOM.
- **When to use:** Exploring large scatterplot matrices where the number of attribute pairs is too large to inspect manually. Guiding attention to unusual/interesting attribute relationships.
- **When to avoid:** When the number of original attributes is small (< ~6 pairs) — a regular SPLOM suffices. When the nine measures don't capture the specific pattern of interest.
- **Interesting properties:** A "meta-display" — a display of displays. Outliers in the scagnostics SPLOM correspond to the most unusually shaped (interesting) scatterplots in the original SPLOM.
- **Marks:** Points (each representing one scatterplot); popup detail view showing the full scatterplot on hover/select
- **Channels:** Position (scagnostics measure values on X and Y axes of each cell); linked highlighting in red for selected point
- **Annotation options:** Popup detail view; linked highlighting between meta-SPLOM and original SPLOM
- **Data types suited for:** Tables with many quantitative attributes
- **Interesting feature extraction/manipulation of data:** Derives 9 shape measures per pairwise attribute combination. Shapes include convex hull properties, MST properties, and rank correlation. This is a major data transformation: from raw table to per-pair shape descriptors.

---

### VisDB Dense Pixel Display (p. 347–350)

- **What it shows:** A large database table visualized as dense colored square area marks, where mark color encodes query relevance. Two layout variants: (1) small multiples, one view per attribute; (2) single view with per-item multi-attribute glyphs.
- **When to use:** Database exploration with a specific query; when discovering which items are most relevant and how relevance correlates across attributes. Very large tables (millions of rows).
- **When to avoid:** When precise value reading is important (dense pixels are perceptual, not precise). When the query-centric framing doesn't suit the task.
- **Interesting properties:** Spiral spatial ordering (not standard aligned layout). Multi-hue sequential colormap with monotonically increasing luminance (supports both categorical and ordered perception). Uses filtering to cap display at ~1M items.
- **Marks:** Square area marks (one per item)
- **Channels:** Color (multiple hues + ordered luminance) encodes relevance; spatial position in spiral encodes ranked order; size is uniform
- **Annotation options:** Color legend; query interface; relevance filtering slider
- **Data types suited for:** Large tables with quantitative attributes and a query/relevance function
- **Interesting feature extraction/manipulation of data:** Derives k+1 relevance attributes per item (one per original attribute + overall relevance). Overall relevance serves as the ordering and primary coloring criterion.

---

### Hierarchical Clustering Explorer (HCE) — Cluster Heatmap (p. 351–354)

- **What it shows:** A heatmap where rows are items (e.g., genes) and columns are attributes (e.g., experimental conditions), reordered by hierarchical clustering. A dendrogram on top (and optionally side) shows the clustering hierarchy. Two coordinated views: aggregated overview + detail for selected cluster.
- **When to use:** Exploring large multidimensional tables where discovering clusters, gaps, outliers, and correlations across both dimensions simultaneously is the goal. Genomics, demographics, any multivariate tabular data.
- **When to avoid:** When the number of conditions is very large (>80); when cluster structure is not a meaningful concept for the data.
- **Interesting properties:** Minimum Similarity slider interactively filters the dendrogram and adjusts cluster count in real time. Rank-by-feature idiom adds derived reorderings based on chosen criteria. Overview-detail coordination with linked yellow highlighting.
- **Marks:** Area marks (heatmap cells); line marks (dendrogram edges)
- **Channels:** Color (diverging colormap for gene activity values); spatial position (ordered by clustering); containment (in dendrogram structure)
- **Annotation options:** Dendrogram labels; interactive filter slider; linked highlighting; boxplot/histogram/scatterplot detail views
- **Data types suited for:** Multidimensional tables; especially useful when hierarchical clustering is a natural abstraction
- **Interesting feature extraction/manipulation of data:** Computes hierarchical clustering as derived data; derives per-attribute and per-pair orderings for rank-by-feature; supports multiple ranking criteria

---

### HCE Rank-by-Feature (p. 353–354)

- **What it shows:** A systematic ordering interface for exploring which attribute orderings and pairwise attribute combinations are most interesting. A compact matrix overview (SPLOM-style) with a single area mark per cell + 1D list + detail (histogram or scatterplot).
- **When to use:** When exploring a large multidimensional table and wanting to systematically identify the most interesting single attributes or attribute pairs.
- **When to avoid:** When the dataset is small enough to inspect all pairs directly.
- **Interesting properties:** Three levels of detail in coordinated views: compact matrix overview → 1D ordered list → full histogram or scatterplot detail. Single or double sliders for navigation.
- **Marks:** Area marks (compact; one per attribute or pair); bar marks (histogram); point marks (scatterplot)
- **Channels:** Color (diverging blue-white-brown for chosen criterion); spatial position (ordered by criterion); containment (within matrix cell)
- **Annotation options:** Criterion value labels; slider for selecting attribute to display in detail
- **Data types suited for:** Multidimensional tables
- **Interesting feature extraction/manipulation of data:** Derives orderings for all n attributes and all n(n-1)/2 pairs; computes multiple ranking criteria per pair

---

### PivotGraph (p. 355–358)

- **What it shows:** A derived aggregate network where groups of nodes sharing the same values of 1–2 chosen categorical attributes are collapsed into single aggregate nodes, and all links between groups are collapsed into aggregate links. Node size = number of items in group; link width = number of edges between groups.
- **When to use:** Summarizing large networks to understand cross-group relationships based on categorical attributes (e.g., gender × office location). Extremely large networks where node-link diagrams are intractable.
- **When to avoid:** When understanding individual topological features (paths, cycles, neighborhoods) is important — use node-link views instead.
- **Interesting properties:** Visual complexity is determined only by the number of attribute levels chosen for roll-up, independent of network size. Animated transitions when roll-up choices change. Can encode an additional quantitative attribute via diverging colormap on aggregate nodes.
- **Marks:** Nodes (area, scaled by group size); curved connection links (width = edge count); optional color on nodes
- **Channels:** Size (group count); line width (edge count); color (additional quantitative attribute via diverging colormap); position (2D grid for 2 attributes, line for 1)
- **Annotation options:** Node labels (group identity); color legend; roll-up attribute selectors
- **Data types suited for:** Networks with categorical node attributes
- **Interesting feature extraction/manipulation of data:** Roll-up transformation creates a derived network; additional quantitative node attributes (e.g., in/out link ratio) are derived and color-coded

---

### InterRing — Radial Space-Filling Tree (p. 358–360)

- **What it shows:** A hierarchy visualized as concentric rings (space-filling radial layout), where each ring level represents a tree depth level and each arc segment represents a node. Interactive distortion enlarges selected subtrees while shrinking siblings.
- **When to use:** Exploring hierarchies; situations requiring navigation, selection, rollup/drilldown, and even direct editing of the hierarchy structure. Multiple foci useful when comparing subtrees.
- **When to avoid:** When tree depth > a few dozen levels (overwhelming). When the number of nodes exceeds ~thousands.
- **Interesting properties:** ~3× more legible labels than classical node-link at the same label size. Structure-based coloring redundantly encodes hierarchy — can be replaced by attribute coloring in single-view use, but is useful when shared across multiple linked views.
- **Marks:** Arc segments (nodes); optional containment structure
- **Channels:** Arc length (relative node weight/size); radial position (depth in tree); color (structure or attribute); spatial angle (order among siblings)
- **Annotation options:** Label text on arcs; interactive distortion focus indicators
- **Data types suited for:** Trees, hierarchies
- **Interesting feature extraction/manipulation of data:** Interactive distortion dynamically reallocates space across the tree; supports rollup/drilldown as an in-place operation

---

### Constellation — Multilevel Network Browser (p. 360–366)

- **What it shows:** A complex multilevel linguistic network (paths × subgraphs × nodes) with spatial position encoding query relevance (horizontal = plausibility rank) and path order (vertical = source-to-sink). Dynamic layering minimizes the perceptual impact of edge crossings. Semantic zooming changes space allocation by word type as zoom level changes.
- **When to use:** Highly specialized: browsing query results over complex multilevel networks where spatial relevance encoding is crucial and label reading is a primary task. Domain specialists needing to verify algorithmic output.
- **When to avoid:** General audiences; tasks where network topology (not query relevance) is the focus; large public datasets.
- **Interesting properties:** Node duplication (proxies in gray, master in black) maximizes local subgraph readability at the cost of global space. Horizontal position is sacrificed for algorithmic crossing minimization and used instead for the plausibility attribute — an unusual and deliberate encoding choice. Semantic zooming across 3 zoom levels.
- **Marks:** Containment boxes (hierarchical segments); rectilinear link lines (definitions); slanted proxy-master connections; curvilinear grid cells
- **Channels:** Horizontal position = plausibility; vertical position = path order; color (link type via 8-category colormap); size (relative importance at current zoom level); luminance/saturation (foreground vs. background layer distinction)
- **Annotation options:** Extensive text labels; link type color legend; layer toggling
- **Data types suited for:** Multilevel networks with quantitative relevance attribute; ordered categorical link types
- **Interesting feature extraction/manipulation of data:** Bins dozens of link type categories into 8; derives plausibility ranking from traversal algorithm; resizes grid cells to eliminate empty rows and columns; computes dynamic space allocation for semantic zooming
