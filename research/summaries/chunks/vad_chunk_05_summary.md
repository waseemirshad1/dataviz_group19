# [agent_20] Visualization Analysis and Design — pages 201-250

## Overview

Pages 201–250 span three chapters:
- **Ch. 8 (cont.):** Arrange Spatial Data — geometry, scalar fields (isocontours, direct volume rendering), vector and tensor fields
- **Ch. 9:** Arrange Networks and Trees — node–link diagrams, adjacency matrix views, containment/treemaps
- **Ch. 10 (intro):** Map Color and Other Channels — color theory, colormaps (categorical, sequential, diverging, bivariate)

---

## Chapter 8: Arrange Spatial Data (pp. 179–198)

### 8.1 The Big Picture (p. 179)

- For datasets with **spatial semantics**, the usual choice is to use the **given spatial information** to guide the layout.
- The position channel is not available for directly encoding other attributes — it is "used up" by the spatial data.
- Two main spatial data types:
  - **Geometry:** shape information conveyed directly through spatial elements (not necessarily with attributes).
  - **Spatial fields:** attributes associated with each cell in the field.
- For **scalar fields** (one value per cell): isocontours and direct volume rendering.
- For **vector and tensor fields** (many values per cell): flow glyphs (local), geometric (sparse seeds), textures (dense seeds), features (globally derived).

### 8.2 Why Use Given? (p. 179–180)

- The effectiveness principle: the most effective channel (spatial position) is used to show the most important aspect — spatial relationships.
- If spatial relationships are NOT the primary task, then other attributes can compete for the position channel.

### 8.3 Geometry (p. 180–182)

- **Geographic data:** cartographic generalization = abstraction (filtering, aggregation, level of detail). Cities as point marks at country scale; area marks at city scale.
- **Thematic cartography:** integration of non-spatial data (e.g., population) with base spatial data.

#### Choropleth Maps (p. 181)

- **What:** Quantitative attribute encoded as color over regions (area marks) using given geometry.
- **How:** Sequential segmented colormap (e.g., white-to-blue, 9 levels).
- **Region granularity** is a major design choice.
- The problem of spatial aggregation is linked to region boundaries (see Section 13.4.2).

### 8.4 Scalar Fields: One Value (pp. 182–188)

- Three families of idioms:
  1. **Slicing** — 2D image from a 2D cross-section of a 3D field.
  2. **Isocontours** — derived geometry (isolines/isosurfaces) computed from the field.
  3. **Direct volume rendering** — image from full 3D field without intermediate geometry.

#### Isocontours / Isolines (p. 183)

- Lines/surfaces representing contours of a particular scalar level.
- Isolines far apart = slow change; close together = fast change; never overlap.
- Color-coding regions between isolines with a sequential colormap → **contour plot**.
- **Topographic terrain maps** are a familiar example (equal elevation contours).
  - Scale: dozens of contour levels.

#### Flexible Isosurfaces (pp. 185–186)

- Uses a derived **simplified contour tree** (under 100 edges from 1.5M edges) to help users find structure hidden by standard single-level isosurfaces.
- Supports interactive exploration via filtering and coloring.
- Multiple coordinated views allow understanding shape + relative position simultaneously.

#### Direct Volume Rendering (pp. 186–188)

- Creates an image directly from the 3D spatial field without intermediate geometry.
- Crucial design choice: **transfer function** — maps scalar value changes to opacity and color.
- Problem: features of interest may share data value ranges with uninteresting regions.
- **Multidimensional Transfer Functions (Simian system):** derived 2D space using data value (horizontal) and gradient magnitude (vertical). The 2D joint histogram (like a heatmap with 1-pixel area marks, grayscale sequential colormap) reveals material boundaries not visible in 1D histogram.

### 8.5 Vector Fields: Multiple Values (pp. 189–194)

- Often from computational fluid dynamics (CFD): **velocity fields** with direction and magnitude.
- **Critical points:** saddle, circulating sinks, circulating sources, noncirculating sinks/sources (p. 189).
- Four families of idioms:
  1. **Flow glyphs** — local, e.g., arrow glyphs (stem length = magnitude, orientation = direction, arrowhead = disambiguation). Weakness: occlusion in 3D.
  2. **Geometric flow** — derived geometry from sparse seed points (streamlines, pathlines, streaklines, timelines, stream surfaces). Seeding strategy is a critical design choice.
  3. **Texture flow** — dense seeds, e.g., Line Integral Convolution (LIC).
  4. **Feature flow** — global computation to explicitly detect critical points, vortices, shock waves.

- Empirical study [Laidlaw et al. 05]: compared 6 idioms for 2D vector fields; arrow glyphs (local) fared worst; none dominated all tasks. (p. 190)

#### Similarity-Clustered Streamlines (p. 192)

- Derived attributes per streamline: curvature, torsion, tortuosity → signature → similarity matrix → cluster hierarchy.
- User controls which clusters to show and opacity layering.
- Scale: Field = millions of samples; Geometry = hundreds of streamlines.

### 8.6 Tensor Fields: Many Values (pp. 194–196)

- Tensors: matrix at each cell (stress, conductivity, curvature, diffusivity).
- Same four idiom families as vector fields.
- **Tensor glyphs:** shape + orientation of 3D geometric shapes encode tensor information.
  - Three shapes: isotropic (sphere), partially anisotropic planar, fully anisotropic linear (cigar/ellipsoid).
  - **Ellipsoid tensor glyphs** weakness: ambiguity from single viewpoint → superquadric glyphs resolve this.
- **Geometric tensor flow:** hyperstreamlines/tensorlines.

---

## Chapter 9: Arrange Networks and Trees (pp. 201–217)

### 9.1 The Big Picture (p. 201)

Three major approaches to encoding network data:
1. **Node–link diagrams** (connection channel): point marks for nodes, line marks for links.
2. **Matrix views** (adjacency): derived table from network, area marks in 2D alignment.
3. **Treemaps / containment marks**: containment channel for hierarchical structure.

### 9.2 Connection: Link Marks (pp. 201–208)

#### Node–Link Diagrams

- Nodes = point marks, links = line/connection marks.
- **Vertical spatial position** often encodes tree depth.
- **Horizontal position** is often an artifact of the layout algorithm (not directly encoding attributes).
- Layouts: triangular vertical, spline radial, rectangular horizontal, BubbleTree (radial, subtrees in full circles).
- Well-suited for **topological tasks**: finding paths, shortest paths, adjacent nodes, bridges between components. (p. 203–204)
- 3D node–link layout is rarely effective (perceptual problems). (p. 204)

#### Force-Directed Placement (p. 204–207)

- Nodes repel each other; links act as springs pulling endpoints together.
- Strength: easy to implement and explain; tends to show cluster structure through spatial proximity.
- **Weakness 1:** Spatial position does not directly encode attributes — proximity is sometimes meaningful, sometimes arbitrary (can mislead). (p. 204)
- **Weakness 2:** Nondeterministic — layout changes each run, preventing spatial memory exploitation. (p. 205)
- **Weakness 3:** Scalability — degenerates into "hairball" with more than a few hundred nodes. Upper limit for node/link density: L < 4N. (p. 206)
- **Weakness 4:** Brittle parameters requiring tuning per dataset. (p. 206)
- Continuous bouncing should be halted to avoid distracting peripheral vision in multi-view contexts. (p. 206)

#### Multilevel Force-Directed Placement (sfdp) (p. 207–208)

- Augments network with derived cluster hierarchy (compound network).
- Coarsens network into simpler versions, lays out simplest first, then refines.
- Improves speed and avoids local minimum problem.
- Scale: Nodes: 1,000–10,000; Links: 1,000–10,000; L < 4N.

### 9.3 Matrix Views (pp. 208–209)

#### Adjacency Matrix View

- Network nodes along rows and columns; area marks indicate link presence.
- Derived dataset: table with two key attributes (node lists), one value attribute (link existence).
- Can encode additional attributes with color or size.
- Undirected networks: only half the matrix needed (symmetry).
- Scale: Nodes: 1,000; Links: 1 million.

### 9.4 Costs and Benefits: Connection vs. Matrix (pp. 209–212)

#### Node–Link Strengths:
- Extremely intuitive for small networks.
- Best for topological tasks: path tracing, neighborhood inspection.

#### Node–Link Weaknesses:
- Past link density ~3–4× nodes → unreadable hairball.
- Variable screen space requirements (unknown in advance).
- Unstable (especially with dynamic data).

#### Matrix View Strengths:
- **Perceptual scalability** to very high densities (up to 1M edges single-level, 10B aggregated multilevel).
- No occlusion problem.
- **Predictable, stable** screen space; supports reordering.
- Fast node lookup by label.
- Excellent for estimating node/edge counts.

#### Matrix View Weaknesses:
- **Unfamiliarity** — requires training.
- Weak support for topological structure (path tracing is harder).

#### Empirical finding [Ghoniem et al. 05] (p. 211–212):
- Node–link best for small networks, matrix best for large networks.
- Tasks always better in matrix: approximate node/edge count, most connected node, finding a node by label, direct link between two nodes, common neighbor.
- Task always better in node–link: finding multiple-link path.
- Hybrid multiple-view systems (e.g., MatrixExplorer) combine complementary strengths.

#### Key visual patterns in matrix vs. node–link (p. 211):
- **Clique** → square block of filled cells along diagonal (matrix) vs. completely interconnected lines (node–link).
- **Biclique** → rectangular off-diagonal block (matrix).
- **Node degree** → count of filled cells in a row/column (matrix).

### 9.5 Containment: Hierarchy Marks (pp. 213–216)

#### Treemaps (p. 213–214)

- Alternative to node–link trees: hierarchical relationships shown with containment.
- All children enclosed within parent's area.
- Node size mapped to an attribute (e.g., file size).
- Best for: attribute values at leaves; shallow rather than deep hierarchies; spotting outliers of large attribute values.
- Less effective than connection marks for topological tasks (path tracing).
- Scale: 1 million leaf nodes.

#### Seven tree idioms compared (Figure 9.9, p. 214–215):
1. **Rectilinear vertical node–link** — connection; vertical = depth, horizontal = sibling order.
2. **Icicle** — vertical position + size = depth; horizontal = links + sibling order.
3. **Radial node–link** — connection; radial depth = depth; radial angle = sibling order.
4. **Concentric circles** — radial depth + size = depth; angular = links + sibling order.
5. **Nested circles** — containment; nesting level + size = depth.
6. **Treemap** — containment (rectilinear); nesting + size = depth.
7. **Indented outline** — horizontal = depth + links; vertical = sibling order.

#### GrouseFlocks — Compound Networks (p. 215–216)

- Combination of network + cluster hierarchy (compound network).
- Connection marks for original network links; containment marks for cluster hierarchy.
- Users can investigate multiple possible hierarchies.

---

## Chapter 10: Map Color and Other Channels (pp. 219–225)

### 10.1 The Big Picture (p. 219)

Three separable color channels:
- **Luminance** (magnitude channel): ordered data.
- **Saturation** (magnitude channel): ordered data.
- **Hue** (identity channel): categorical data.

Other channels covered: size, angle, curvature (magnitude), shape, motion (identity).

### 10.2 Color Theory (pp. 219–224)

#### 10.2.1 Color Vision (p. 219–220)

- Retina: rods (low-light, black/white) and cones (three types, different wavelength peaks).
- Visual system processes signals into **three opponent color channels**: red–green, blue–yellow, luminance.
- Luminance = high-resolution edge information; red–green and blue–yellow = lower resolution.
- **Color deficiency** (affects ~8% of men): most common form reduces red–green discrimination.

#### 10.2.2 Color Spaces (p. 220–222)

- **RGB:** computationally convenient but poor perceptual match — not separable channels (integral perception).
- **HSL (Hue-Saturation-Lightness):** intuitive for artists, but only pseudoperceptual. The L value is wildly inconsistent with perceived luminance. (p. 221)
- **L\*a\*b\*:** perceptually uniform space — L\* = perceptually linear luminance (nonlinear transform of physical luminance, based on brightness power law n=0.5). Better match for perceptual experience. Well-suited for interpolation and color difference computations. (p. 222)
- Human spectral sensitivity peaks at green/yellow wavelengths; we are less sensitive to red and blue. (p. 222)

#### 10.2.3 Luminance, Saturation, and Hue as Channels (pp. 222–224)

**Luminance:**
- Magnitude channel, suitable for ordered data.
- Low accuracy for noncontiguous regions (contrast effects).
- Discriminable steps: typically fewer than 5 when background is not uniform (Ware: avoid if more than 2–4 bins needed). (p. 222)
- Crucial: luminance contrast is the ONLY way to resolve fine detail and crisp edges — hue/saturation contrast does not provide detectable edges.
- Text readability: 10:1 luminance contrast ratio recommended; 3:1 minimum. (p. 223)
- Using luminance for data encoding "uses it up" — can no longer use it for detail/text.

**Saturation:**
- Magnitude channel, suitable for ordered data.
- Low accuracy for noncontiguous regions.
- Discriminable steps: around 3 bins. (p. 223)
- Strongly interacts with size: harder to perceive in small marks. Use only 2 levels for point/line marks.
- Saturation and hue are not separable in small regions for categorical coding.

**Hue:**
- Identity channel — extremely effective for categorical data (highest ranked after spatial position). (p. 224)
- Discriminable steps: ~6–7 bins for small separated regions.
- Harder to distinguish in small regions vs. large ones.
- No implicit perceptual ordering — people do not agree on ordering of red/blue/green/yellow. Conventions (rainbow, traffic lights) are learned, not perceptual.
- For small marks: use bright, fully saturated colors.
- For large background regions: use low-saturation (pastel) colors.

#### 10.2.4 Transparency (p. 224–225)

- A fourth color-related channel.
- Cannot be used independently: fully transparent marks convey no information.
- Strong interaction with luminance and saturation — do NOT combine transparency with these.
- Can be used with hue, but very few discriminable steps (usually just 2: foreground/background).
- Most often used redundantly (same info encoded with another channel too).
- Primarily for layering: foreground vs. background.

### 10.3 Colormaps (p. 225–)

- Colormap = mapping between colors and data values.
- Taxonomy mirrors data types:
  - **Categorical colormaps** (qualitative)
  - **Sequential ordered colormaps** (minimum to maximum)
  - **Diverging ordered colormaps** (zero-point center, diverge to negative/positive)
  - **Bivariate colormaps** (two attributes simultaneously)
- Must match colormap to data type (expressiveness principle).
- Ordered data → use luminance/saturation (magnitude channels), NOT hue (no implicit ordering).
- Continuous vs. segmented colormaps: quantitative → continuous; categorical → segmented; ordinal → choice reveals emphasis.

#### 10.3.1 Categorical Colormaps (p. 225–)

- Use color as integral identity channel (not three separate channels for hue/saturation/luminance).
- 6–12 discriminable bins maximum for small separated regions.
- Remember to include background color in count.
- Use easily nameable colors (memorability, discussion).
- Good starting point: fully saturated, easily nameable opponent colors.

---

## Key Design Rules of Thumb (from this section)

1. **Spatial position is "used up" by spatial data** — do not re-encode other attributes with it if spatial relationships are primary (p. 180).
2. **L < 4N rule**: node–link layouts become unreadable when link count exceeds ~4× node count (p. 206, 208).
3. **Force-directed placement is nondeterministic** — spatial memory cannot be relied on across runs (p. 205).
4. **Matrix views scale to 1M edges (single level) / 10B edges (multilevel)** vs. node–link tops out at hundreds–thousands (p. 211).
5. **Path tracing is always better in node–link** — matrix views cannot support it well (p. 212).
6. **Luminance contrast is required for text readability** — do not encode data with luminance unless you have spare contrast budget (p. 223).
7. **Saturation: only ~3 discriminable bins; hue: ~6–7 bins for separated regions** (p. 223–224).
8. **For small marks: bright saturated colors; for large background areas: pastels** (p. 224).
9. **Treemaps excel for leaf-level attribute outliers; poor for path tracing** (p. 213–214).
10. **Bivariate colormaps are safe with one binary attribute, difficult with two multi-level attributes** (p. 225).

---

## Common Mistakes and Anti-patterns

- Using HSL lightness L as if it were perceptually linear luminance — it is not (p. 221).
- Using RGB for perceptual comparisons or interpolation — perceptually non-uniform (p. 221).
- Encoding ordered data with hue — hue has no implicit ordering (p. 224).
- Combining transparency with luminance or saturation coding (p. 224–225).
- Using force-directed layout for networks with more than ~4× links-to-nodes (p. 206).
- Using 3D node–link layouts without strong justification (p. 204).
- Using spatial proximity in force-directed layouts as a reliable indicator of network closeness — it can be an artifact (p. 204).
- Using saturation for more than ~3 levels, or for point/line marks with more than 2 levels (p. 223).
