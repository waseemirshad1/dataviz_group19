# [agent_22] Visualization Analysis and Design — pages 301-350

## Overview of Chapters Covered

Pages 301-350 span three chapters:
- **Ch. 12 (continued): Facet into Multiple Views** (pp. 301-322) — coordination, partitioning, superimposition
- **Ch. 13: Reduce Items and Attributes** (pp. 323-346) — filtering and aggregation strategies
- **Ch. 14 (intro): Embed: Focus+Context** (pp. 347-350) — embedding design choices

---

## Chapter 12 (continued): Facet into Multiple Views

### 12.3 Coordinate Views — Share Navigation (p.301)

- **Linked navigation**: moving the viewpoint in one view synchronizes movement in others (p.301)
- Common example: bird's-eye overview window + large detail view; interaction in small window changes viewpoint in large one
- Navigation covered in Section 11.5

### 12.3.4 Combinations of Coordination (p.301)

- Six combinations of (same/different encoding) × (same/subset/partition of data) — two are useless: fully shared (redundant) and fully unshared (no linkage) (p.301)
- These terms are non-exclusive — "multiform" means at least one pair of views differs, not that every view has a different encoding

**Design matrix for coordinating views:**
| Encoding | Data | Result |
|---|---|---|
| Same | Same | Redundant (useless) |
| Same | Subset | Overview–detail |
| Same | Partition | Small multiples |
| Different | Same | Multiform, overview–detail |
| Different | Subset | Multiform, overview–detail |
| Different | Partition | Multiform |
| Different | No linkage | No linkage (useless) |

### Example: Improvise Census Vis (p.302-303)

- Multivariate census data with geographic, scatterplot, parallel coordinate, tabular, and matrix views
- All views share the same bivariate sequential–sequential color encoding
- Views are linked by highlighting (blue selected items)
- Small-multiple reorderable list views partition data by attribute
- Overview map + large geographic detail view linked with navigation
- System: Improvise [Weaver 04]

### 12.3.5 Juxtapose Views (p.303)

- Default: all views permanently visible for glancing between them
- Option: views pop up temporarily in response to user action
- Arrangement choices: window system default, linear list, 2D matrix
- Matrix alignment gives higher-precision comparison for partitioned data (p.303)

---

### 12.4 Partition into Views (p.304-313)

**Core principle**: partitioning encodes association between items using **spatial proximity** — a highly ranked channel (p.304)

**Three design choices in partitioning** (p.304):
1. How many splits to carry out (one per attribute down to individual items, or stop earlier)
2. Order in which attributes are used to split
3. How many views to use (data-driven or predetermined)

**Partitioning attributes** (p.304):
- Typically categorical variables with limited unique values (levels)
- Can be derived: e.g., a quantitative attribute divided into bins
- Can use key attributes (separating to item level) or value attributes (multiple items share same bin)

### 12.4.1 Regions, Glyphs, and Views (p.305-306)

- Region: a partition of space that receives encoded data
- **Glyph**: an object with internal structure from multiple marks. Can be:
  - **Macroglyph**: large, complex structure (e.g., schematic bar chart embedded in map)
  - **Microglyph**: so small that individual structure is not directly perceivable; used in dense 2D arrays forming visual texture
- **View**: large, stand-alone, highly detailed region; regions may be called views or glyphs depending on size and context
- No strict dividing line between region, glyph, and view (p.305)

### 12.4.2 List Alignments — Grouped vs. Small-Multiple Bar Charts (p.306-307)

**Key task-encoding trade-off** (p.307):
- **Grouped bar chart**: interleaved second-level regions within first-level regions → facilitates comparison **between attributes**
- **Small-multiple bar charts**: contiguous second-level regions within one first-level region → facilitates comparison **within a single attribute**
- Both can be interpreted as two levels of partitioning or as glyph structures

### 12.4.3 Matrix Alignments — Trellis (p.307-309)

**Trellis** [Becker et al. 96]:
- Partitions multiattribute data into a 2D matrix of views
- Key technique: **main-effects ordering** — order rows/columns by median value of derived attribute to make outliers visible against general trends (p.308)
- Alphabetical ordering reveals no trends; main-effects ordering reveals both trends and outliers
- Dataset: barley yields with three categorical keys + one quantitative value

**Rule of thumb**: Use main-effects ordering to spatially sort data so both general trends and outliers can be spotted simultaneously (p.308)

### 12.4.4 Recursive Subdivision — HiVE (p.310-313)

- **HiVE** [Slingsby et al. 09]: supports exploration through flexible partitioning choices
- Order of partitioning dramatically changes visible patterns (p.311)
- Same data, same layout type, different partitioning order → radically different insights
- Sizing regions by count → **treemap** layout emerges (p.312-313)
- Using geographic layout at second level → **choropleth maps** emerge (p.313)
- Structural similarity between heatmaps, treemaps, choropleth maps: all use color-coded area marks (p.313)

**Anti-pattern**: Changing only the order of partitioning — not the encoding — can look like a completely different visualization type (p.311)

---

### 12.5 Superimpose Layers (p.313-320)

**Definition**: Multiple simple drawings combined on top of each other in a single composite view, sharing the same spatial frame (p.313)

**Design choices** (p.313-314):
1. How many layers?
2. How are layers visually distinguished?
3. Static (predetermined) or dynamic (user-driven) layers?
4. How to partition items into layers?

**Key limitation**: Maximum ~2-3 layers if layers contain substantial area marks. Many layers only work if each layer has very few marks (e.g., single lines) (p.314)

### 12.5.1 Visually Distinguishable Layers (p.314)

- Use **non-overlapping ranges** of visual channels per layer
- Common: foreground vs. background using luminance contrast
- The "Get It Right in Black and White" principle: check luminance contrast explicitly (p.314)

### 12.5.2 Static Layers (p.314-319)

**Cartographic Layering** (p.314-315):
- Area marks: background layer (water, parks, land) — unsaturated colors
- Line marks: foreground layer (roads) — saturated colors, varying widths
- Works via luminance contrast between layers
- Idiom: area marks for regions, line marks for roads, categorical colormap

**Superimposed Line Charts** (p.315-316):
- Multiple lines sharing the same frame, one per data item
- Works well for ~dozen lines; fails at hundreds of items
- Scale: ordered key attribute → hundreds; categorical key → ~dozen items
- Data: multidimensional table with one ordered key (time), one categorical key (machine), one quantitative value

**Empirical study: Superimposed vs. Juxtaposed (p.317)**:
- **Superimposed line charts** best for **local tasks** (finding max at a specific time point) within small visual span
- **Juxtaposed small multiples** better for **global tasks** (finding highest increase across the whole series) especially as number of series increases
- Trade-off: less vertical space in small multiples vs. more visual clutter in superimposed

**Hierarchical Edge Bundles** (p.317-319) [Holten 06]:
- Shows compound network: base network + cluster hierarchy over nodes
- Three layers: (1) gray containment circles for tree, (2) red-green connection links for graph, (3) gray nodes in front
- Bundling edges reduces occlusion with underlying tree
- Works because color and mark type distinguish layers
- Anti-pattern: if all network edges were also gray/opaque, image would be very hard to interpret

### 12.5.3 Dynamic Layers (p.319-320)

- Layer created interactively in response to user selection (e.g., cursor position)
- **Cerebral system**: one-hop neighborhood layer activates when cursor is over a node
- Foreground layer: fully saturated red, larger linewidth
- Background layer: low-saturation colors
- The number of possible layers is huge (constructed on-the-fly)

---

## Chapter 13: Reduce Items and Attributes

### 13.1-13.2 The Big Picture and Why Reduce? (p.323-325)

**Five strategies for managing complexity** (reduction is one of five):
1. Derive new data (Ch. 3)
2. Change a view over time (Ch. 11)
3. Facet into multiple views (Ch. 12)
4. **Reduce items and attributes** (Ch. 13) ← this chapter
5. Embed focus+context (Ch. 14)

**Two reduction methods** (p.324):
- **Filtering**: eliminates elements entirely
- **Aggregation**: combines multiple elements into a single stand-in element

**Trade-off filtering vs. aggregation** (p.325):
- Filtering: straightforward, but "out of sight, out of mind" — users forget about filtered-out elements
- Aggregation: safer cognitively (stand-in conveys summary info), but cannot convey all omitted detail; challenge is what to summarize

### 13.3 Filter (p.325-329)

**Dynamic queries** principle (p.325):
- Tightly coupled loop between visual encoding and interaction
- Display updates immediately when user changes a filter setting
- Users cannot be expected to know what numbers to type — show them visually!
- Standard widgets: sliders, buttons, comboboxes, text fields

### 13.3.1 Item Filtering (p.326-328)

**FilmFinder** [Ahlberg and Shneiderman 94]:
- Interactive scatterplot: movies as items, year vs. popularity axes, color = genre
- Dynamic queries via sliders and buttons with immediate update
- Marks auto-enlarge and label when enough items filtered out to allow room
- Multiform overview–detail: click mark → popup detail view
- Alpha sliders for text-string selection (not just numbers)
- Dual sliders for selecting both min and max of a range

**Scented Widgets** [Willett et al. 07] (p.328):
- Standard filter widgets augmented with concise visual info about dataset
- Uses no or minimal additional screen real estate → high information density
- Ways to add info: insert statistical graphic (bar/line chart), icons, text labels, or use widget parts as marks with extra channels (hue, saturation, opacity)
- Alludes to "information scent": cues helping searcher decide whether to drill down further

### 13.3.2 Attribute Filtering (p.328-329)

- Eliminate attributes (dimensions), not items
- Can combine with item filtering
- **DOSFA** idiom [Yang et al. 03a]: Dimensional Ordering, Spacing, and Filtering Approach
  - Orders attributes by similarity, filters by similarity and importance thresholds
  - Used with star plots: with 215 attributes, patterns invisible; after filtering → clear structure
- Attribute filtering often used with **attribute ordering**: order by derived similarity measure, then filter out low/high-scoring ones
- Similarity measures: variance, global similarity, partial matches

### 13.4 Aggregate (p.329-346)

**Aggregation operators** (p.330): average, minimum, maximum, count, sum
- Anscombe's Quartet illustrates the danger of over-aggregating (p.330)
- Full power comes with interactive aggregation where user changes level on-the-fly

### 13.4.1 Item Aggregation (p.330-335)

**Histograms** (p.331-332):
- Aggregates items by binning a quantitative attribute
- Derived: one ordered key attribute (bin) + one quantitative value (count per bin)
- Key difference from bar charts: no spaces between bars (imply continuity); show derived data not original data
- **Bin size choice is crucial and tricky**: same data can look very different with different bins
- Solutions: compute bins from dataset characteristics, or let user interactively change bin count

**Continuous Scatterplots** (p.332-333):
- Solves occlusion in scatterplots by plotting aggregate density at each pixel
- Derived attribute: overplot density; visualized with sequential log-scale colormap
- Generalization: discrete scatterplot → continuous (density function in 2D); discrete histogram → continuous (density in 1D)

**Boxplot Charts** (p.333-335):
- Aggregates distribution to 5 derived values: median, lower quartile, upper quartile, lower fence, upper fence
- Outliers beyond fences shown explicitly as dots
- Scale: items → unlimited; attributes → dozens
- Task support: characterize distribution, find outliers/extremes/averages, identify skew
- **Vase plot variant**: width encodes density → allows checking for multimodal distributions (p.334-335)
- Standard boxplots assume **unimodal** data — this is an anti-pattern to watch for

**Interactive/Dynamic Aggregation**:
- **SolarPlot** [Chuah 98] (p.335-336): radial histogram with user-controlled circle radius → indirectly controls bin count (aggregation level)
  - Small circle: high aggregation, shows trend; large circle: lower aggregation, shows seasonal patterns
  - Aggregation operator: count

**Hierarchical Parallel Coordinates** [Fua et al. 99] (p.336-337):
- Scalability solution for parallel coordinates: hierarchical clustering of items
- Each cluster shown as band of varying width and opacity (mean = center, width = min-max range)
- Proximity-based coloring for cluster hierarchy
- Interactive slider controls global level of detail
- Scale: 10,000–100,000 items, ~dozen clusters visible at once

### 13.4.2 Spatial Aggregation (p.337-339)

**Modifiable Areal Unit Problem (MAUP)** (p.338):
- Changing aggregation region boundaries → dramatically different analysis results
- Even same number/size of units, any change of spatial grouping → significant change
- Scale changes also lead to different results
- Gerrymandering is a well-known instance of MAUP

**Geographically Weighted Boxplots (geowigs)** [Dykes and Brunsdon 07] (p.338-339):
- Geographically weighted interactive graphics
- Supports comparison between global and local distributions at chosen scale
- Superimposed layers: gray boxplot = global distribution (background), green boxplot = local scale (foreground)
- Scale parameter interactively adjustable

### 13.4.3 Attribute Aggregation / Dimensionality Reduction (p.339-345)

**Dimensionality Reduction (DR)** (p.340):
- Synthesize new attributes to replace multiple original ones
- Assumes hidden structure + significant redundancy in original data
- MDS (multidimensional scaling): linear and nonlinear variants; minimize distance differences between high-D and low-D space

**Document Collection DR** (p.340-344):
1. Transform documents → bag-of-words (word count vectors) → high-D table (up to 10,000 attributes)
2. Apply MDS → 2D or low-D table
3. Show as scatterplot colored by conjectured clustering
4. User verifies/discovers cluster structure; annotates clusters
- Scale: 100,000 items, 10,000 attributes → 2 derived attributes

**How to show DR data** (p.344-345):
- 2 new synthetic attributes → **scatterplot**
- More than 2 → **SPLOM (scatterplot matrix)** may be good choice
- **Only relative distances matter** in DR scatterplots — absolute position is not meaningful
- DR scatterplots should only be used to find/verify **large-scale cluster structure** — fine-grained structure is unreliable
- **Anti-pattern**: Using 3D scatterplots for DR data — susceptible to all 3D perception problems; 3D landscapes similarly problematic
- Empirical evidence: 2D scatterplots/SPLOMS are safest idiom for DR data [Sedlmair et al. 13]

---

## Chapter 14 (intro): Embed: Focus+Context (p.347-350)

### 14.1 The Big Picture (p.348)

**Focus+context** idiom family: embed detailed information about a selected focus within a single view that also contains overview/context information

**Three embedding design choices** (p.348):
1. **Elide**: filter some items completely; summarize others via dynamic aggregation for context; only focus items in full detail
2. **Superimpose layers**: local focus region moveable against background context layer
3. **Distort geometry**: compress context regions to make room for magnified focus regions

**Design space variables for geometric distortion**: region shape, region extent, interaction metaphor; single or multiple focus regions

### 14.2 Why Embed? (p.349)

- Mitigates disorientation from standard navigation (zooming loses context)
- Provides contextual landmarks using **external memory** to reduce internal cognitive load
- Focus+context is a form of nonliteral navigation (like semantic zooming)
- Focus set changes dynamically; visual representation changes dynamically
- Often uses indirect control: focus set inferred from user navigation + dataset structure

### 14.3 Elide (p.350)

**Degree of Interest (DOI) function** [Furnas 86]:
- DOI = I(x) − D(x, y)
- I = interest function; D = distance (semantic or spatial); x = item location; y = current focus point
- Continuous function; threshold values determine what is shown in detail vs. aggregated vs. elided
- Exploits knowledge about dataset structure (especially hierarchical relationships)

**DOITrees Revisited** [Heer and Card 04]:
- Shows 600,000-node tree with multiple foci
- Shaded triangles aggregate elided subtrees
- Context computed via tree traversal from focus nodes to common ancestors
- Distance computed topologically (hops through tree), not geometrically
- Focus chosen by clicking or indirectly through searching

---

## Key Rules of Thumb (pages 301-350)

- Partitioning encodes association via spatial proximity — a highly ranked channel (p.304)
- Order of partitioning decisions changes visible patterns radically — always explore multiple orderings (p.311)
- Main-effects ordering (by median) makes both trends and outliers visible simultaneously (p.308)
- Superimposed layers: max ~2-3 with area marks; many layers only feasible if each has very few marks (p.314)
- Check luminance contrast explicitly — "Get It Right in Black and White" (p.314)
- Superimpose for local comparison tasks; juxtapose for global/dispersed comparison tasks (p.317)
- Filtering: users tend to forget about filtered-out items ("out of sight, out of mind") (p.325)
- Aggregation: cognitively safer than filtering, but risks hiding signals — Anscombe's Quartet (p.330)
- Bin size for histograms is crucial and tricky — offer interactive control (p.331)
- Standard boxplots assume unimodal distributions — use vase plots for multimodal (p.334)
- For DR scatterplots: only relative distances matter; only large-scale structure is reliable; avoid 3D (p.344-345)
- Focus+context idioms require understanding both visual encoding and interaction together — they are fundamentally a synthesis (p.349)
