# [agent_19] Visualization Analysis and Design — pages 151-200

## Overview

Pages 151–200 span the end of **Chapter 6: Rules of Thumb** (pp. 126–141) and all of **Chapter 7: Arrange Tables** (pp. 143–176). Chapter 6 finishes the practical design heuristics introduced earlier. Chapter 7 provides a systematic taxonomy of spatial encoding idioms for tabular data.

---

## Chapter 6: Rules of Thumb (continued from p.126)

### 6.3 No Unjustified 3D (continued, p.126–130)

- **3D versus 2D example:** van Wijk & van Selow compared a 3D time-series surface of office building energy consumption with linked 2D views. The 3D version suffered occlusion and perspective distortion; the 2D version (aggregate curves + calendar view with shared color coding) revealed finer patterns including the Dutch holiday "Sinterklaas Day" (p.126–128).
- **Careful use of 3D:** Lopez-Hernandez et al. — oscilloscope eye diagrams opened like a "drawer" in 3D, but with orthographic projection and automatic zooming to constrain navigation complexity (p.128–129).
- **Empirical evidence against 3D for abstract data (p.129–130):**
  - 3D interfaces better for shape understanding; 2D better for relative position tasks (judging distances/angles between objects) [St. John et al. 01]
  - 3D cone trees vs. 2D browser: significant time cost for 3D [Cockburn and McKenzie 00]
  - Data Mountain: a later study found no benefit from 3D perspective over 2D version [Cockburn and McKenzie 01]
  - Information landscapes: point clouds outperform 3D landscapes for search and point estimation tasks; 2D landscapes outperform 3D landscapes [Tory et al. 07]
- **Key anti-pattern:** inferring 3D was responsible for benefits when the comparison wasn't controlled (other variables differed too)

### 6.4 No Unjustified 2D (p.131)

- 2D spatial layout (e.g., node-link network diagrams) must also be justified versus the simpler alternative of 1D lists
- **Strengths of lists:** higher information density (more text labels in less space), excellent for lookup tasks with appropriate ordering (e.g., alphabetical)
- **When 2D is justified:** when understanding topological structure is the true task

### 6.5 Eyes Beat Memory (p.131–134)

- Looking at two simultaneously visible views is far lower cognitive load than comparing current view with remembered previous view (p.131)
- **Working memory is severely limited** — cognitive load builds when limits are exceeded (p.132)
- **Human attention limits:** visual search degrades rapidly; vigilance worsens after hours of work (p.132)

#### 6.5.2 Animation versus Side-by-Side Views (p.132–133)

Three types of "animation":
1. Narrative storytelling (movies) — requires choreography; unsuitable directly for vis
2. Transitions between two states — very effective for maintaining context
3. Video-style playback (play/pause/rewind) — cognitively demanding

- **Animated transitions** between two configurations are beneficial because they help users track changes in position; most useful when only a few things change (p.132–133)
- **Blink comparator idiom:** rapidly jumping back and forth between two frames effective for detecting localized changes (p.133)
- **Multi-frame animation weakness:** comparisons between non-adjacent frames rely on internal memory; if many objects change across many frames, tracking is very difficult even with pause/replay (p.133)
- **Small multiples vs. animation:** for detailed comparison across many frames, side-by-side is often more effective; suitable for dozens but not hundreds of frames (p.133)

#### 6.5.3 Change Blindness (p.134)

- Humans have no detailed internal memory of the visual field; eyes dart to gather information just-in-time
- **Change blindness:** we fail to notice dramatic changes when attention is elsewhere
- Implication for vis: complex widespread changes across multi-frame animations are very hard to follow

### 6.6 Resolution over Immersion (p.134–135)

- **Pixels are precious:** resolution usually more important than immersion
- Immersive environments (VR, CAVE) trade resolution for sense of presence
- Additional costs of immersion: requires special physical location, users stand rather than sit, no access to standard workflow (keyboard, mouse, email, etc.)
- Justified only for 3D spatial data where presence matters; essentially never for nonspatial abstract data (p.135)

### 6.7 Overview First, Zoom and Filter, Details on Demand (p.135–137)

- **Shneiderman's influential mantra [Shneiderman 96]** — heavily cited design guideline (p.135)
- **Overview goals:** show all items simultaneously, find regions worth drilling into; used throughout exploration (not just at start) (p.136)
- **Creating overviews:** geometric zoom-out; or explicit design using dynamic aggregation driven by navigation (p.136)
- **Three idiom families** for overview+detail:
  1. Separate overview view + detail view (can be side-by-side or pop-up on demand)
  2. Single view that changes dynamically via zoom/filter
  3. Focus+context: embed detailed focus and overview context in a single view (p.137)
- **Alternative for enormous datasets:** Search, Show Context, Expand on Demand [van Ham and Perer 09] (p.137)

### 6.8 Responsiveness Is Required (p.137–140)

- **Latency is categorical, not continuous:** human response changes dramatically at discrete thresholds (p.137)

| Time Constant | Value | Relevant for |
|---|---|---|
| Perceptual processing | 0.1 s | Screen updates |
| Immediate response | 1 s | Visual feedback for selection, animated transitions |
| Brief tasks | 10 s | Breaking complex tasks into simpler pieces |

- **Visual feedback rule:** show confirmation of completed action within ~1 second; use progress indicator when crossing from one latency class to another (p.138–139)
- **Interaction mechanism speed:** mouseover (no dwell) > mouseover (dwell) > click (p.139)
- **Feedback mechanism trade-offs:** fixed side pane (high latency to read) vs. popup at cursor (fast, but occludes) vs. in-view highlight (fastest, but limited info) (p.139)
- **Fluid interaction** enables focus on high-level mental model building; mismatch in latencies "jars" users out of flow [Csikszentmihalyi] (p.139)

#### 6.8.3 Interactivity Costs (p.140)

- Interaction has both power and cost: exhaustive manual search = human-powered search
- Balance: automatic feature detection to bring interesting things to attention, but not so automatic that vis is unnecessary

### 6.9 Get It Right in Black and White (p.140)

- **Maureen Stone's guideline [Stone 10]:** ensure most crucial aspects are legible in black and white
- Method: literally print/transform to grayscale to check
- **Practical implication:** encode the most important attribute with the luminance channel first; treat hue and saturation as secondary

### 6.10 Function First, Form Next (p.140–141)

- Given effective but ugly design, form can be improved later (by collaboration with graphic designers)
- Given beautiful but ineffective design, must start from scratch
- Beauty does matter given that vis uses human visual perception — but only as a secondary concern
- This book focuses on function/effectiveness rather than graphic design principles

---

## Chapter 7: Arrange Tables (p.143–176)

### 7.1 The Big Picture (p.145)

Four design choices for arranging tabular data spatially (Figure 7.1):
1. **Express values** — spatial position encodes quantitative values
2. **Separate regions** — spatial regions encode categorical attributes
3. **Order regions** — ordered attributes control region ordering
4. **Align regions** — alignment of regions supports comparison

Axis orientations: **rectilinear**, **parallel**, or **radial**
Layout density: **dense** or **space-filling**

### 7.2 Why Arrange? (p.145)

- Arrange is the most critical encoding choice because **spatial position dominates the user's mental model** (p.145)
- Top-ranked effectiveness channels for quantitative/ordered attributes are all spatial:
  1. Planar position against common scale
  2. Planar position along unaligned scale
  3. Length
- Top-ranked channel for categorical: grouping items within the same **region** — also spatial (p.145)
- No nonspatial channel is highly effective for all attribute types — channels split into ordered vs. categorical

### 7.3 Arrange by Keys and Values (p.145–146)

- **Key:** independent attribute used as unique index to look up items (categorical or ordinal)
- **Value:** dependent attribute (can be categorical, ordinal, or quantitative)
- **Levels:** unique values for a categorical or ordered attribute (to avoid confusion with "value")
- Core design question: how many keys and how many values?
  - 0 keys, 2 values → scatterplot
  - 1 key, 1 value → bar chart
  - 2 keys, 1 value → heatmap
  - Many keys, many values → recursive subdivision (e.g., scatterplot matrix)

### 7.4 Express: Quantitative Values (p.146–148)

- Simple case: each item encoded as mark at position along an axis
- Complex case: **composite glyph** — multiple marks with internal structure, one per subregion
- Additional non-spatial channels (color, size) can augment expression

#### Scatterplot (p.146–148)

- Two quantitative value attributes → horizontal and vertical spatial position; marks are points
- Effective for: overview, distribution characterization, finding outliers/extremes, **judging correlation** between two attributes
- Correlation visible as diagonal pattern: positive = upward slope, negative = downward
- Augmentation: color (categorical attribute), size (quantitative → "bubble plot")
- Derived attribute use: log transformation to reveal hidden linear relationships
- Regression line often superimposed when correlation-finding is primary task
- Scalability: dozens to hundreds of items

**Summary table (p.148):**
| Idiom | Data | Encode | Task | Scale |
|---|---|---|---|---|
| Scatterplots | 2 quantitative values | H+V position, point marks | Trends, outliers, distribution, correlation, clusters | Hundreds of items |

### 7.5 Separate, Order, Align: Categorical Regions (p.149–155)

- Spatial position is an ordered magnitude channel → **expressiveness principle** violated if categorical attributes mapped directly to position
- Categorical attributes match well with **spatial regions** (contiguous, distinct bounded areas)
- Three operations: separate (by categorical), align (optional, by ordered), order (by ordered)

#### 7.5.1 List Alignment: One Key (p.149)

Categorical key → one region per item → 1D list alignment (horizontal or vertical)

**Bar Charts (p.150–151):**
- Line marks, one quantitative value (aligned spatial position), one categorical key (separate horizontal regions)
- Key insight: **aligned marks → highest accuracy position channel** (vs. unaligned)
- **Default alphabetical ordering hides patterns**; ordering by value attribute reveals trends (Figure 7.4)
- Task: lookup and compare values
- Scalability: dozens to hundreds of categories

**Stacked Bar Charts (p.151–153):**
- One quantitative value, **two categorical keys**
- Composite glyph: sub-bars stacked vertically, each colored by secondary key
- Bottom sub-bar: aligned to baseline → easy position comparison
- Other sub-bars: unaligned → harder to compare across bars
- **Order of stacking matters** for what patterns are visible
- Tasks: part-to-whole relationship, lookup values, find trends
- Scalability: main axis dozens–hundreds; stacked axis several to ~12

**Streamgraphs (p.153–155):**
- Complex generalized stacked graph [Byron and Wattenberg 08]
- One quantitative value (counts), one ordered key (time), one categorical key (artist/entity)
- Derived geometry: organic silhouette emphasizing continuity of layers over time
- Layer order computed algorithmically (e.g., by volatility or onset time)
- Baseline deliberately organic (not flat) to improve layer legibility
- Scales to more categories than stacked bar charts (layers don't all span full timeline)

**Dot Charts (p.155):**
- Point marks, one quantitative value expressed with aligned vertical position, one ordered/categorical key
- Like scatterplot with one categorical axis, or bar chart with point marks instead of line marks

**Line Charts (p.155–157):**
- Dot chart augmented with connection marks between points
- Connection marks imply trend/ordering relationship
- Must use **only for ordered keys** (not categorical) — violates expressiveness otherwise
- Zacks & Tversky study: line charts for categorical data elicit false "trend" answers (p.157)
- **Aspect ratio matters:** "banking to 45°" idiom maximizes segments near diagonal for most accurate angle perception; multiscale banking finds multiple informative aspect ratios using power spectrum analysis (p.157–158)

#### 7.5.2 Matrix Alignment: Two Keys (p.158)

Two keys → 2D matrix: one key distributed along rows, other along columns; rectangular cell shows item values

**Cluster Heatmaps (p.158–161):**
- Basic heatmap: each cell = area mark colored by quantitative value; **diverging colormap common**
- Very compact → high information density; good for overview
- Cluster heatmap adds **matrix reordering**: rows and columns rearranged by hierarchical clustering (dendrograms shown on periphery)
- Dendrogram: tree with leaves aligned so branch heights are comparable
- Tasks: find clusters, outliers; summarize
- Scalability: up to 1 million items (200×200 area marks at several pixels each); quantitative attribute: only 3–11 distinguishable bins due to color perception limits in small non-contiguous regions

**Scatterplot Matrix / SPLOM (p.161–162):**
- 2D matrix where each cell contains a complete scatterplot
- Shows all pairwise combinations of attributes
- Typically show only lower or upper triangle (upper is redundant)
- Diagonal cells often omitted (attribute vs. itself) or used for labels
- Tasks: find correlations, trends, outliers
- Scalability: ~12 attributes, dozens–hundreds of items
- Key is derived: index of all attributes in dataset

#### 7.5.3 Volumetric Grid: Three Keys (p.162)

- 3D volumetric alignment possible but not recommended for non-spatial data (occlusion, perspective distortion)
- Alternative for three+ keys: recursive subdivision

#### 7.5.4 Recursive Subdivision: Multiple Keys (p.162)

- Extend list/matrix approaches by recursively subdividing cells
- Ordering, alignment, containment combined

### 7.6 Spatial Axis Orientation (p.162–170)

#### 7.6.1 Rectilinear Layouts (p.162)

- Two perpendicular axes (horizontal + vertical); heavily used; all examples above
- Default for most statistical charts

#### 7.6.2 Parallel Layouts (p.162–165)

**Parallel Coordinates (p.163–166):**
- Multiple quantitative attributes shown at once using spatial position
- Each axis is vertical; axes placed parallel to each other
- Each item = polyline (jagged line) that crosses each axis once at item's value
- Correlation patterns: positive correlation = mostly parallel lines between two axes; negative correlation = lines cross at single point between axes; uncorrelated = mixed crossing angles
- In practice, **SPLOMs are typically easier for correlation tasks**; parallel coordinates more used for: overview of all attributes, finding ranges, selecting ranges, outlier detection
- **Key limitation:** axis ordering is critical; all pairs visible only for neighboring axes; interactive reordering needed but combinatorially explodes
- **Training time:** users need explicit instruction on pattern meaning
- Often used alongside scatterplots in multiple views with linked highlighting
- Scalability: dozens of attributes; hundreds of items (not thousands — severe overplotting)

#### 7.6.3 Radial Layouts (p.166–170)

- Items distributed around circle using angle channel + one linear spatial channel (polar coordinates)
- Mathematically equivalent to rectilinear under transformation; **perceptually not equivalent**
- **Two perceptual consequences:**
  1. Angle channel is less accurate than rectilinear spatial position
  2. Angle channel is inherently cyclic (start = end) → misleading for non-periodic data
- **When radial is better:** showing periodicity/cyclic patterns (p.170)
- **Guideline:** if two attributes have unequal importance, radial is justifiable; more important attribute in sectors, less important in rings

**Radial Bar Charts (p.168):**
- Same as bar chart but with radial layout; line marks with length channel; generally inferior to rectilinear

**Pie Charts (p.168–170):**
- Area marks (wedges), angle channel; very popular but perceptually problematic
- Angle judgements less accurate than length judgements; wedge width varies radially (hard area judgement)
- Useful property: shows relative contribution of parts to a whole (sum = 360°)
- But normalized stacked bar chart does same thing with more accurate length channel
- **Polar Area Chart** (rose plot / coxcomb): varies length of wedge rather than angle → more accurate than pie chart; popularized by Florence Nightingale for Crimean War data

**Empirical comparison (p.171):** Diehl et al. compared rectilinear grids vs. radial grids for object position memorization — rectilinear generally faster and more accurate; radial justified when one attribute is more important than the other

### 7.7 Spatial Layout Density (p.171–175)

#### 7.7.1 Dense Layouts (p.172–174)

- Use small, densely packed marks for maximum information density
- Maximally dense: point marks = 1 pixel; line marks = 1 pixel wide
- Available channels at that scale: **planar position and color only** (size, shape, tilt unavailable)
- **Tarantula system example:** dense overview of software source code, 1-pixel lines colored by test pass/fail; indentation preserved as spatial landmark; combined with zoomable detail view; derived attributes of test execution coverage (brightness = coverage %, hue = pass:fail ratio)
- Scales to ~10,000 lines of code

#### 7.7.2 Space-Filling Layouts (p.174–175)

- Fill all available space in view; typically use area marks or containment marks
- **Advantages:** maximizes room for color coding (larger areas = more perceptually salient); space for embedded labels
- **Disadvantage:** cannot use white space (graphic design tool for readability, emphasis, balance)
- Space-filling ≠ space-efficient: additional metrics needed (e.g., smallest node size, label area for trees)

---

## Key Rules of Thumb (Consolidated)

| Rule | Page | Core Insight |
|---|---|---|
| No unjustified 3D | p.126 | 3D adds occlusion, distortion; costs must be justified by spatial task needs |
| No unjustified 2D | p.131 | 1D lists beat 2D layouts for lookup and text density |
| Eyes beat memory | p.131 | Simultaneous visible views << memory comparison |
| Resolution over immersion | p.134 | Pixels are precious; VR rarely justified for abstract data |
| Overview first, zoom/filter, details on demand | p.135 | Shneiderman's mantra; show all then drill |
| Responsiveness required | p.137 | 0.1s/1s/10s latency thresholds; give visual feedback |
| Get it right in black and white | p.140 | Luminance encodes primary attribute; hue/saturation secondary |
| Function first, form next | p.140 | Effective > beautiful; beauty enhances but cannot replace effectiveness |

---

## Data Types → Encoding Mappings (Chapter 7)

| Data Type | Spatial Encoding | Idiom |
|---|---|---|
| Quantitative value (2 attrs) | H+V position | Scatterplot |
| 1 quant + 1 categorical | Length + aligned position | Bar chart |
| 1 quant + 2 categorical | Matrix cells + color | Heatmap |
| Many quantitative | Multiple parallel axes | Parallel coordinates |
| Quant + cyclic/time | Radial position | Radial bar, pie, polar area |
| High-dimensional with rows/cols | SPLOM matrix | Correlation exploration |

---

## Anti-Patterns and Mistakes (p.126–175)

- Using 3D for abstract data without justification (p.126)
- Using line charts for categorical key attributes → implies false trend (p.156)
- Pie charts for precise value comparison → angle judgements are inaccurate (p.168)
- Default alphabetical ordering of bar charts hides dataset patterns (p.150)
- Overplotted parallel coordinates with thousands of items → nearly unreadable (p.165)
- Animation with many simultaneous changes → change blindness and memory overload (p.133)
- Immersive displays for abstract/non-spatial data (p.135)
- Radial encoding for non-periodic data → misleading cyclic implication (p.167)

---

## Derived Attributes and Data Transformation (p.146–165)

- **Log transformation** of scatterplot axes to reveal hidden linear correlations (p.147)
- **Regression line** as derived data overlaid on scatterplot when correlation is the primary task (p.148)
- **Alphabetical ordering** is a derived attribute; prefer data-driven ordering by value attribute (p.150)
- **Hierarchical clustering** as derived data for cluster heatmap matrix reordering (p.160)
- **Dendrograms** encode cluster hierarchy derived from rows/columns of heatmap (p.160)
- **Streamgraph layer order** derived from volatility or onset time of categories (p.154)
- **Power spectrum** as derived variable for multiscale banking to 45° in line charts (p.158)
- **Test coverage percentages** as derived attributes in Tarantula dense display (p.173)
