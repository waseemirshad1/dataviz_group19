# [agent_23] Visualization Analysis and Design — pages 351-400

## Overview

Pages 351–400 span two chapters and back-matter:
- **Ch. 14 (cont., pp. 351–363):** Embed: Focus+Context — superimpose, distort idioms, costs/benefits of distortion
- **Ch. 15 (pp. 341–367):** Analysis Case Studies — six full system analyses applying the book's framework
- **pp. 369–400:** Figure Credits and Bibliography (reference material, no new theory)

---

## Chapter 14 (continued): Embed — Focus+Context

### 14.4 Superimpose (p. 351)

- **Superimposed layers** integrate focus and context in a single view by placing a focus layer atop a background layer.
- Unlike global layers, the focus layer is **limited to a local region** — it does not stretch across the entire view.
- Example: **Toolglass and Magic Lenses** — a see-through lens shows color-coded Gaussian curvature in the foreground, with the rest of the 3D scene unchanged in the background (p. 351).
  - The lens occludes the region beneath it.
  - Works with many data types and encodings.

### 14.5 Distort (p. 352)

- Distortion-based focus+context uses **geometric distortion of contextual regions** to make room for focus-area detail — integrating both in one view.
- Key design choices for distortion idioms:
  1. **Number of foci:** single or multiple focus regions
  2. **Shape of focus:** radial, rectangular, or arbitrary
  3. **Extent of focus:** global (across entire scene) or local (constrained region)
  4. **Interaction metaphor:** constrained geometric navigation / moveable lens / rubber sheet / vector fields

#### Five distortion idiom examples:

**3D Perspective (p. 352–353)**
- Idiom: **Cone Trees** — 3D perspective for global distortion, single focus point (p. 353)
- Interaction: standard geometric navigation (rotation)
- Lost popularity as costs of 3D for abstract data became better understood
- Data type: Trees. Scale: thousands of nodes.

**Fisheye Lens (p. 353–354)**
- Single focus, local radial region, moveable lens metaphor
- Radial magnification: high at lens center, continuous gradient outward
- Works on any data/layout
- Example: poker player dataset — scatterplot and dense matrix views with fisheye lens applied (p. 353–354)
- Anti-pattern: continuous magnification change introduces cognitive load; can be disorienting for unfamiliar structures (p. 360–361)

**Hyperbolic Geometry (p. 354–356)**
- Single radial global focus; interaction: hyperbolic translation
- Exploits non-Euclidean geometry: infinite non-Euclidean plane mapped to finite Euclidean circle
- Excellent for exponentially growing structures (trees, networks)
- Example: **H3** — 3D hyperbolic layout for file system tree (p. 355–356)
- Cost: 3D version has partial occlusion in any single frame

**Stretch and Squish Navigation (p. 356–358)**
- Multiple rectangular foci of global extent; rubber sheet metaphor
- Enlarging one region causes others to shrink; borders stay fixed — all items stay visible
- Example: **TreeJuxtaposer** — comparing phylogenetic trees (p. 357)
- **Guaranteed visibility** — important items always visible even at sub-pixel scale via custom aggregation (p. 357–358)
  - High-importance items (e.g., red diff marks) never disappear even in very squished regions
- Example: **PRISequenceJuxtaposer** — comparing gene sequences 16,000+ nucleotides wide in 700 pixels (p. 357)

**Nonlinear Magnification Fields (p. 358–359)**
- Multiple foci of arbitrary shape and magnification level, local or global scope
- General computational framework: calculates implicit magnification fields for desired transformations
- Supports lens, stretchable surface, and data-driven interaction metaphors
- Can expose magnification fields directly for data-driven trails (moving objects)

### 14.6 Costs and Benefits: Distortion (p. 359–362)

- Distortion is one of five strategies for handling complexity (alongside: derive new data, manipulate changing view, facet into multiple views, reduce data shown)
- Trade-offs between these five approaches are **not fully understood** (p. 359)

**Measured costs of distortion:**
- **Distance/length judgements severely impaired** — poor match for comparison tasks requiring metric precision (p. 359)
- Best use case: topological exploration of networks/trees, where exact metric judgements are not needed
- Users may **not notice distortion** — risk of misunderstanding object structure; highest with unfamiliar/sparse structures (p. 359)
- Mitigations: explicit distortion indicators (enclosing circles for hyperbolic, superimposed grids for magnification fields)
- **Object constancy overhead**: tracking that an item before/after transformation is the same object — cost increases with distortion magnitude (p. 360)
- Constrained and predictable distortion is better tolerated than drastic distortion (p. 360)
- Fisheye metaphor need not be geometric: can apply directly to structured data (e.g., hierarchical document with collapsed sections) (p. 360)

**Comparison of four graph exploration approaches (p. 361–362):**
1. **Fisheye lens** — continuous magnification gradient, can be disorienting
2. **Magnifying lens** — discrete two-level jump (full mag vs. periphery), causes occlusion but simpler to interpret
3. **Neighborhood highlighting** — no distortion, opacity reduction for items outside 1–2 hop neighborhood; good for path tracing (p. 362)
4. **Bring and Go** — temporary selective relocation of one-hop neighbors to target node; minimizes disorientation by moving only specific items (p. 362)

**Key rule of thumb:** Fisheye benefit (no occlusion) may not justify the cost of interpreting continuous magnification — depends on task (p. 361).

---

## Chapter 15: Analysis Case Studies

### 15.1 The Big Picture (p. 341/366)

- Six full vis system case studies showing complete framework application
- Analyses are **descriptive, not prescriptive** — they show one good solution, not the only one (p. 342)
- Real-world systems often have complex data abstractions: combinations of types, multiple levels, significant data transformation

### 15.2 Why Analyze Case Studies? (p. 341–342)

- Concise system descriptions provide a foundation for generating new design alternatives
- Uses the full framework: data abstraction + task abstraction + encoding idiom + faceting + reduction + scale

### 15.3 Graph-Theoretic Scagnostics (p. 342–345)

**Concept:** Scalable exploration of scatterplot matrices (SPLOMs) — a "scatterplot of scatterplots."
- SPLOM scalability challenge: matrix grows quadratically; each cell needs enough pixels for distinction (p. 344)
- **Nine scagnostics measures** classify the shape of point distributions within each scatterplot (p. 344):
  - *Outlying* (outlier detection)
  - *Skewed, clumpy, sparse, striated* (distribution/density)
  - *Convex, skinny, stringy* (shape)
  - *Monotonic* (association)
- Result: a **scagnostics SPLOM** where each point represents a full original scatterplot
- Linked highlighting: selecting a point shows the corresponding original scatterplot in a popup detail view (p. 344–345)
- Guides user toward unusually shaped (potentially interesting) scatterplots

**Framework summary:**
- What: Table → Derived: nine quantitative attributes per scatterplot (pairwise of originals)
- Why: Identify, compare, summarize distributions and correlations
- How: Scatterplot + SPLOM; select; juxtaposed small-multiple views with linked highlighting + popup detail
- Scale: Dozens of original attributes

### 15.4 VisDB (p. 347–350)

**Concept:** Dense, space-filling visualization of large database tables with query relevance.
- Computes derived relevance score per item per attribute + overall relevance (p. 348)
- Uses **spiral spatial ordering** from center (not standard rectilinear/radial) (p. 348)
- **Sequential colormap** with multiple hues + monotonically increasing luminance: dark red → purple → blue → cyan → green → bright yellow (p. 348)

**Two layouts:**
1. **Attribute-based (small multiples):** one view per attribute, items ordered identically and colored by relevance for that attribute. Supports: distribution characterization, within-attribute grouping, outlier detection, inter-attribute correlation (p. 348–349)
2. **Item-based (glyph):** one glyph per item showing all attributes. Supports: cross-item comparison, finding similar items (p. 349)

**Scalability:**
- Both layouts use filtering by relevance when items exceed display space
- Small-multiples: handles 10–12 attributes, ~100,000 items per view, ~1M total across views
- Glyph-based: only ~100,000 total items (glyph elements need to be salient, require borders)

**Key insight:** Different space-partitioning strategies support different tasks (p. 350).

**Framework summary:**
- What: Table (k attributes) + query → Derived: k+1 relevance attributes
- Why: Distribution, grouping, outliers, correlations, similar items
- How: Dense area marks in spiral layout; colormapped; small-multiples or glyph
- Reduce: Filtering. Scale: several million items total; 1M visible

### 15.5 Hierarchical Clustering Explorer (HCE) (p. 351–354)

**Concept:** Scalable interactive exploration of large multidimensional tables with associated hierarchical clustering.
- Original domain: genomics (genes × conditions × activity level)
- Key scalability: aggregation + filtering + navigation + coordinated multiple views (p. 352)
- Scalability target: 100–20,000 genes; 2–80 conditions (p. 352)

**Views:**
- **Overview cluster heatmap** (top): aggregated, ~1500 pixels for 3614 genes; interactive density control
- **Detail cluster heatmap** (bottom): selected cluster from overview; shows second dendrogram for row clustering
- **Scatterplot and histogram views** for alternative encodings
- **Minimum Similarity slider**: interactive filtering control on dendrogram; dragging filters columns and changes cluster count (p. 352–353)
- **Rank-by-feature idiom**: augments data with derived orderings for each attribute and pairwise combination; multiple views with list alignment + area mark coloring; supports systematic exploration (p. 353–354)

**Framework summary:**
- What: Multi-dim table (2 categorical keys + 1 quantitative value) → Derived: cluster hierarchy + ranking criteria attributes
- Why: Find correlations, clusters, gaps, outliers, trends
- How: Cluster heatmap, scatterplots, histograms, boxplots; diverging colormaps; reorderable 2D matrix or 1D list
- Reduce: Dynamic filtering + aggregation; Manipulate: pan/scroll; Facet: multiform with linked highlighting; overview-detail
- Scale: 20,000 genes × 80 conditions = 1.6M values

### 15.6 PivotGraph (p. 355–358)

**Concept:** Summarize networks by deriving an aggregate network via roll-up on categorical node attributes.
- Aggregates groups of nodes and links into single aggregate nodes/links based on 1 or 2 categorical attributes (p. 355)
- For 2 attributes: nodes laid out on a grid; links drawn as curves
- Node positions minimize link-crossing clutter
- **Animated transitions** when user changes roll-up choice
- Additional quantitative attribute can be encoded via diverging colormap on aggregate nodes (p. 357)
- Highly scalable: visual complexity depends only on attribute levels, not original network size — handles thousands to millions of nodes (p. 357)

**Best for:** cross-attribute comparison at aggregate level
**Worst for:** understanding topological features (use node-link views for those) (p. 358)

**Framework summary:**
- What: Network → Derived: aggregate network by roll-up on 2 chosen attributes
- Why: Cross-attribute comparison of node groups
- How: Connection marks + node size + link width + diverging color
- Reduce: Aggregation, filtering; Manipulate: animated transitions
- Scale: Original nodes/links unlimited; roll-up levels: up to ~1 dozen per attribute

### 15.7 InterRing (p. 358–360)

**Concept:** Space-filling radial hierarchy view with distortion-based focus+context interaction.
- Base layout: radial, space-filling (like a sunburst), without distortion (p. 358–359)
- Distortion: enlarging one subtree shrinks siblings (multiple foci)
- **Structure-based coloring** redundantly encodes hierarchy; can be replaced by attribute coloring if hierarchy is the only view; especially useful for shared coloring across linked views (p. 358–359)
- Supports: selection, rollup/drilldown, and **direct hierarchy editing** (unlike many tree browsers) (p. 359)
- ~3× more legible labels than classical node-link layout at the same label size (p. 360)

**Framework summary:**
- What: Tree
- Why: Selection, rollup/drilldown, hierarchy editing
- How: Radial space-filling layout; color by tree structure
- Facet: Linked coloring + highlighting; Reduce: Embed distort, multiple foci
- Scale: Hundreds of labeled nodes; thousands of dense nodes; dozens of tree levels

### 15.8 Constellation (p. 360–366)

**Concept:** Specialized multilevel linguistic network browser with spatial encoding of query relevance.
- Data: 3-level network — paths (ordered word sequences), subgraphs (dictionary definitions), nodes (word senses) (p. 360–361)
- Edge-crossing minimization done via **dynamic foreground layering** rather than algorithmic layout — frees spatial position for encoding (p. 360)
- **Nodes duplicated** across multiple subgraphs to maximize subgraph readability; duplicates are "proxies" drawn in gray, connected to black "master" by long slanted line (p. 360, 365)
- Designed to "work itself out of a job" — highly specialized, intended for small audience for limited period (p. 361)

**Key layout choices:**
- High-level: curvilinear grid — paths flow vertically (source→sink); horizontal = plausibility rank; more room for plausible paths on left (p. 362–363)
- Empty grid cells eliminated (first horizontally then vertically) to increase information density (p. 363)
- Mid-level: containment marks show hierarchical relationship between path word and its definitions (p. 363)
- Low-level: ladder-like rectilinear structure; vertical lines = hierarchy (white); horizontal lines = link type (color coded) (p. 363)
- **Semantic zooming**: space allocation per word class changes dynamically with zoom level; 3 viewing levels: global (interpath), intermediate (path segments), local (individual definitions) (p. 366)

**Link type binning**: 8 bins from dozens of types — 7 most frequent + 1 "other" category (p. 361)

**Framework summary:**
- What: Three-level network (paths, subgraphs, nodes)
- Why: Discover/verify — browse and locate types of paths, identify, compare
- How: Containment + connection marks; horizontal position = plausibility; vertical = path order; color links by type
- Manipulate: Semantic zooming; animated transitions; Reduce: Superimpose dynamic layers
- Scale: 10–50 paths; 1–30 subgraphs/path; several thousand nodes

---

## Key Cross-Cutting Themes and Rules of Thumb

- **Five strategies for handling complexity** (p. 359): (1) derive new data, (2) manipulate a changing single view, (3) facet into multiple views, (4) reduce data shown, (5) embed focus in context. Trade-offs not fully understood.
- **Distortion is most valuable for topological exploration** where precise metric judgements are not needed (p. 359).
- **Guaranteed visibility** (p. 357–358): items with high importance values are always visible regardless of scale — a custom aggregation strategy for abstract data where geometric distance is a poor proxy for importance.
- **Space-partitioning strategy determines task support** (VisDB, p. 350): partition by attribute → compare distributions; partition by item → compare items.
- **Linked highlighting + overview-detail** is a powerful scalability pattern for large tables (HCE, p. 352).
- **Animate transitions** when changing derived data representation to maintain object constancy (PivotGraph, p. 357).
- **Node duplication** can improve subgraph readability at the cost of layout complexity — useful when the structure is multilevel and cross-referenced (Constellation, p. 360).
- **Scagnostics principle** (p. 344): when the display itself becomes too large to explore directly, compute a meta-display summarizing shape features — a "display of displays."
