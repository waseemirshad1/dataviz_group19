# [agent_20] Visualization Analysis and Design — pages 201-250

## Visualization Catalogue

---

### Choropleth Map (p. 181)

- **What it shows:** A quantitative attribute encoded as color over geographic regions. Each region is an area mark with boundaries from given geometry.
- **When to use:** When showing how a quantitative value (unemployment rate, population density, coffee yield) varies across spatial regions. Use when the spatial unit (county, country, site) is the primary unit of analysis.
- **When to avoid:** When very fine spatial detail matters or region boundaries are arbitrary/misleading (MAUP problem). Avoid if attributes are counts rather than normalized values (larger areas appear inflated).
- **Interesting properties:** Design choice of region granularity significantly affects visual interpretation. Sequential segmented colormap provides discrete levels that aid comparison across regions.
- **Marks:** Area marks (region boundaries from given geometry).
- **Channels:** Color (sequential segmented colormap encoding a quantitative attribute); spatial position (fixed by given geography).
- **Annotation options:** Text labels on regions; legend for colormap; highlighted region outlines; separate bar or table with ranked values.
- **Data types suited for:** Quantitative (normalized) per-region attributes; geographic/spatial datasets.
- **Interesting feature extraction/manipulation of data:** Spatial aggregation — choosing which level of regional granularity (country, county, grid cell) changes what patterns are revealed. Normalizing counts by area or population is a critical derived attribute step.

---

### Topographic Terrain Map / Isocontour Map (p. 183–184)

- **What it shows:** Contour lines (isolines) derived from a 2D spatial scalar field, overlaid on a geographic base map. Shows equal-value lines (e.g., equal elevation).
- **When to use:** When showing spatial variation of a continuous scalar field where understanding spatial extent and gradient (rate of change) is the task. Well-suited for terrain elevation, temperature, pressure, precipitation.
- **When to avoid:** When there are very many levels that cause visual clutter; when the scalar field changes discontinuously.
- **Interesting properties:** Line density encodes rate of change (closely spaced = steep gradient; widely spaced = slow change). Small closed contours indicate local extrema (peaks). Lines can never overlap (physical property).
- **Marks:** Line marks (isolines); underlying geography as point/line/area marks.
- **Channels:** Spatial position (given geography); implicit magnitude via density of lines; color coding of contour levels can add a sequential channel.
- **Annotation options:** Elevation/value labels on contour lines; color fill between levels (contour plot); color-coded contour lines by level.
- **Data types suited for:** 2D scalar spatial fields; geographic data with a continuous quantitative field attribute.
- **Interesting feature extraction/manipulation of data:** Derived geometry — the isoline is computed from the raw scalar field, not directly observed. Contour level selection determines which structure is revealed.

---

### Isosurfaces / Flexible Isosurfaces (pp. 184–186)

- **What it shows:** 3D surface(s) derived from a 3D scalar spatial field at a specific contour value. Flexible isosurfaces use a derived simplified contour tree to navigate structure.
- **When to use:** 3D medical imaging (CT/MRI), scientific simulation data, geological data. When shape and spatial arrangement of internal structures matter.
- **When to avoid:** When many simultaneous isosurfaces cause occlusion; when the relevant structure is not surface-like.
- **Interesting properties:** Transparency can show multiple surfaces simultaneously. Contour tree (simplified from millions to under 100 edges) gives a structural overview without requiring the user to manually sweep through all values.
- **Marks:** 3D surface geometry (derived); line marks for the contour tree with vertical position encoding isovalue.
- **Channels:** 3D spatial position (given field); color/opacity (attributes of isosurface components); vertical spatial position (isovalue in contour tree).
- **Annotation options:** Labels on contour tree nodes; color coding of identified structures (brain, nasal cavity, bone, etc.); cutting planes to reveal internal structure.
- **Data types suited for:** 3D scalar spatial fields.
- **Interesting feature extraction/manipulation of data:** Contour tree simplification — compresses 1.5M edges to under 100, preserving topological structure. Allows region-based filtering and coloring by component identity.

---

### Direct Volume Rendering (pp. 186–188)

- **What it shows:** An image directly generated from the entire 3D scalar spatial field, using opacity and color transfer functions to reveal internal structure.
- **When to use:** Medical imaging, scientific visualization where seeing "through" the volume (not just surfaces) is important. When multiple material types and their boundaries need simultaneous inspection.
- **When to avoid:** When computational resources are limited; when the user cannot specify a meaningful transfer function; when surface geometry alone is sufficient.
- **Interesting properties:** Transfer function design is the critical creative and analytical challenge. 2D transfer functions using both data value and gradient magnitude can distinguish material boundaries invisible in 1D histograms.
- **Marks:** Pixel-level rendering (no explicit geometric marks); joint histogram view uses 1-pixel area marks.
- **Channels:** 3D spatial position (given field); opacity and color (mapped by transfer function from data value and gradient magnitude); grayscale sequential colormap for joint histogram (count per bin).
- **Annotation options:** Cutting planes to reveal interior; widget overlays on 2D transfer function space; separate histogram views.
- **Data types suited for:** 3D scalar spatial fields; multi-material scientific and medical data.
- **Interesting feature extraction/manipulation of data:** Derived gradient magnitude field — computed from original scalar field, enables distinguishing sharp boundaries from homogeneous regions. 2D joint histogram = derived table with counts.

---

### Flow Glyph / Arrow Glyph (pp. 190–191)

- **What it shows:** Local vector field information at each cell using an arrow (or more complex glyph). Arrow stem length = magnitude; orientation = direction; arrowhead disambiguates flow direction.
- **When to use:** 2D vector fields with modest density; when local direction and magnitude at specific points are the task.
- **When to avoid:** Dense 3D fields (occlusion problem); when global patterns or paths are more important than local values.
- **Interesting properties:** Can be placed on regular grid, jittered grid, or sparse subset. Empirical study found local arrow glyphs fared worst among six flow vis idioms for tasks involving path prediction and critical point identification.
- **Marks:** Arrow glyph objects (stem + arrowhead as compound marks).
- **Channels:** Spatial position (given field); length (magnitude); orientation/angle (direction).
- **Annotation options:** Color coding by magnitude or cluster; varying density of glyph placement.
- **Data types suited for:** 2D or 3D vector fields; flow data with direction and magnitude.
- **Interesting feature extraction/manipulation of data:** Glyph substructure encodes two attributes simultaneously (magnitude via length, direction via angle), plus implicit disambiguation of forward/backward via arrowhead.

---

### Geometric Flow (Streamlines / Pathlines) (pp. 191–193)

- **What it shows:** Trajectories of particles in a vector field, computed by numerical integration from seed points. Streamlines = steady fields; pathlines = unsteady (time-varying) fields; streaklines = trail through a point; timelines = connected front of pathlines.
- **When to use:** When understanding flow topology, path structure, and relationships between different regions of a flow field matter. Better than glyphs for path following tasks.
- **When to avoid:** When seeding strategy is poor (visual clutter/occlusion); when the field is very large and dense.
- **Interesting properties:** Similarity-clustered approach [McLoughlin et al. 13]: derives curvature, torsion, and tortuosity per streamline → signature → cluster hierarchy. Users can interactively filter by cluster and use opacity layering (emphasized cluster = full opacity; others = low opacity background).
- **Marks:** Line marks (trajectories in 3D space); point marks (seed locations).
- **Channels:** Spatial position (given + derived trajectory geometry); color (cluster membership); opacity (foreground/background layering).
- **Annotation options:** Color by cluster, by attribute (e.g., edge length); opacity layering for emphasis; separate legend for clusters.
- **Data types suited for:** 2D and 3D vector fields; CFD simulation data.
- **Interesting feature extraction/manipulation of data:** Three levels of derived data: trajectories from field → per-line attributes (curvature, torsion, tortuosity) → signatures → similarity matrix → cluster hierarchy.

---

### Line Integral Convolution (LIC) / Texture Flow (p. 193)

- **What it shows:** Dense texture representation of a 2D vector field, where white noise is smeared along particle flow directions to reveal continuous flow patterns.
- **When to use:** 2D vector fields; when full coverage of flow direction without sparse seeding is desired.
- **When to avoid:** 3D fields (impractical); when magnitude must be shown (LIC shows direction only).
- **Interesting properties:** Dense coverage across entire field; no seeding strategy issues. Shows direction everywhere without the glyph occlusion problem.
- **Marks:** Pixel-level texture (no discrete geometric marks).
- **Channels:** Spatial position (given); luminance/texture pattern encodes flow direction.
- **Annotation options:** Color overlay for magnitude; superimposed glyphs for direction disambiguation.
- **Data types suited for:** 2D vector fields; surface flows.
- **Interesting feature extraction/manipulation of data:** Dense particle tracing from every cell; smearing operation integrates directional information over local neighborhood.

---

### Ellipsoid Tensor Glyphs (pp. 194–196)

- **What it shows:** Local tensor field information (diffusion, stress, conductivity) using 3D ellipsoid shapes. Shape encodes isotropy/anisotropy; orientation encodes principal directions.
- **When to use:** Diffusion tensor imaging (DTI) for brain connectivity; material stress analysis; anywhere a symmetric 3×3 matrix field is the data.
- **When to avoid:** Large fields (occlusion); when distinction between glyph types from a single viewpoint is critical (ellipsoid ambiguity). Use superquadric glyphs instead for disambiguation.
- **Interesting properties:** Three base shapes: sphere (isotropic), flattened sphere (planar anisotropy), cigar/ellipsoid (linear anisotropy). Filtering out isotropic glyphs reduces visual noise. Color by orientation aids interpretation.
- **Marks:** 3D glyph objects (ellipsoids); derived from eigenvalue decomposition.
- **Channels:** Spatial position (given); shape geometry (tensor shape via eigenvalues); orientation (eigenvectors); color (orientation attribute).
- **Annotation options:** Color coding by anisotropy type; opacity filtering; superimposed anatomical reference geometry.
- **Data types suited for:** 3D tensor spatial fields; symmetric second-order tensor data.
- **Interesting feature extraction/manipulation of data:** Mathematical decomposition of tensor into shape (eigenvalues) and orientation (eigenvectors) before visual encoding.

---

### Node–Link Diagram (pp. 201–208)

- **What it shows:** Network or tree topology, with nodes as point marks and links as line/connection marks.
- **When to use:** Networks with up to ~hundreds of nodes (simple algorithms) or thousands (multilevel). Tasks involving topology: path tracing, neighborhood exploration, finding bridges/cliques. Trees with all depth levels to show.
- **When to avoid:** Dense networks (L > 4N) — degenerates into hairball. Very large networks (10,000+ nodes with simple algorithms). When node label lookup speed matters (matrix view is better).
- **Interesting properties:** Force-directed placement is nondeterministic; spatial proximity can indicate clustering but may be an artifact. Spatial position does NOT directly encode attributes in force-directed layouts. Multilevel variants (sfdp) improve scalability and avoid local minima.
- **Marks:** Point marks (nodes); connection marks / line marks (links).
- **Channels:** Spatial position (layout algorithm or deliberate encoding of tree depth); size (node degree, edge weight via line width); color (attribute encoding or cluster membership); opacity.
- **Annotation options:** Node labels; edge weight via line width; color coding by attribute or cluster; size coding; interactive highlighting on search.
- **Data types suited for:** Network data (general graphs); tree data (hierarchical); genealogical, social, biological networks.
- **Interesting feature extraction/manipulation of data:** Multilevel approach derives cluster hierarchy from network for compound network. Strahler centrality metric can color edges. sfdp uses coarsening → iterative refinement.

---

### Adjacency Matrix View (pp. 208–212)

- **What it shows:** Network adjacency as a 2D matrix, with one node per row and column. Filled area mark = link exists; empty = no link. Can encode link weights with color or size.
- **When to use:** Dense networks (L up to N²); when node label lookup, degree inspection, or clique detection are important tasks. Large networks where node–link becomes a hairball.
- **When to avoid:** When path tracing between nodes is the primary task. When users lack matrix-reading training. When the network is sparse and small (node–link more intuitive).
- **Interesting properties:** Perceptually scalable to 1M edges (single level) or 10B (multilevel). Completely eliminates edge-crossing occlusion. Stable and predictable screen space. Reordering rows/columns reveals structure. Characteristic patterns: cliques = diagonal square blocks; bicliques = off-diagonal blocks; degree = row/column fill count.
- **Marks:** Area marks (cells in 2D matrix alignment).
- **Channels:** Spatial position (row = node, column = node — matrix alignment); color/luminance (link presence/absence or weight); size (limited by cell pixel count, ~few levels only).
- **Annotation options:** Row/column labels; color of cells for additional attributes; reordering controls; visual cluster patterns; combination with node–link in hybrid view.
- **Data types suited for:** Network data; social networks; biological interaction networks; co-occurrence matrices.
- **Interesting feature extraction/manipulation of data:** Network → derived table (two key attributes: node lists; one value attribute: link indicator). Reordering is a critical transformation that reveals cluster structure. Half-matrix for undirected networks (symmetry exploitation).

---

### Treemap (pp. 213–215)

- **What it shows:** Hierarchical structure using containment (nested rectangles). Node size encodes an attribute (e.g., file size, yield magnitude). Nesting level encodes tree depth.
- **When to use:** Hierarchies with important leaf-level attributes; shallow hierarchies; spotting outliers of large attribute values (e.g., large files, high-yielding sites).
- **When to avoid:** Deep hierarchies (nested rectangles become tiny); when path tracing through the hierarchy is the primary task (containment marks are weaker than connection marks for this).
- **Interesting properties:** Scale: up to 1 million leaf nodes. Hierarchical structure is immediately visible from containment (nesting). Area encodes attribute value — very effective for outlier detection. Cannot show paths easily.
- **Marks:** Area marks (nested rectangles with rectilinear layout); containment marks.
- **Channels:** Spatial position (nesting structure + rectilinear area allocation); area/size (quantitative attribute at leaf or node level); color (additional attribute).
- **Annotation options:** Color coding by attribute or cluster; label overlays; hover tooltips; zoom to subtree.
- **Data types suited for:** Tree/hierarchical data with quantitative leaf attributes; file systems; hierarchical taxonomic data; species richness nested by plant group.
- **Interesting feature extraction/manipulation of data:** Area is derived from a quantitative attribute (e.g., normalizing yield or species count to a proportion of total). Layout algorithm distributes rectangular space proportionally.

---

### Icicle Tree (p. 215)

- **What it shows:** Tree hierarchy with depth encoded by one spatial dimension (vertical) and parent–child relationships + sibling order by the other (horizontal). No connection marks — relationships inferred from spatial alignment.
- **When to use:** When both depth and sibling ordering matter; when containment or connection marks are not desired. Better than indented outline for spatial comparison of sizes across levels.
- **When to avoid:** Very deep or very wide trees (cells become too small).
- **Interesting properties:** One of seven tree idioms in Figure 9.9. Uses only spatial position channels (both axes), no connection or containment marks needed for structure.
- **Marks:** Area marks (rectangular cells, one per node).
- **Channels:** Vertical spatial position + size (tree depth); horizontal spatial position (parent–child + sibling order).
- **Annotation options:** Color by attribute; labels inside cells; zoom/filter for subtrees.
- **Data types suited for:** Tree/hierarchical data; file systems; biological taxonomies.
- **Interesting feature extraction/manipulation of data:** Proportional width allocation can encode node size attribute simultaneously.

---

### Concentric Circles Tree (p. 215)

- **What it shows:** Radial version of icicle. Depth encoded as radial distance from center; sibling relationships encoded by angular position.
- **When to use:** When radial layout is aesthetically or spatially preferable; for relatively shallow trees.
- **When to avoid:** Very deep or very wide trees. When precise size comparison is needed (arc areas harder to compare than rectangles).
- **Interesting properties:** No connection marks. Parent–child relationship conveyed by angular containment within the parent's arc sector.
- **Marks:** Area marks (arc sectors / concentric rings).
- **Channels:** Radial spatial position (tree depth); angular spatial position (link relationships + sibling order); size (tree depth proportional to ring width).
- **Annotation options:** Color by attribute; labels along arcs; interactive zoom.
- **Data types suited for:** Tree data; evolutionary phylogenies; hierarchical cluster results.
- **Interesting feature extraction/manipulation of data:** Angular width allocation can be proportional to subtree size or node count.

---

### Indented Outline Tree (p. 215)

- **What it shows:** Text-based tree representation familiar from file explorers. Horizontal indentation = depth + link relationships; vertical position = sibling order.
- **When to use:** When label readability is the primary concern; when users are familiar with file-manager-style interfaces.
- **When to avoid:** Wide/deep trees with poor space efficiency; when visual pattern detection is important.
- **Interesting properties:** Only idiom in the seven that is primarily text-based. Best space efficiency for label reading; worst for visual comparison.
- **Marks:** Point marks (nodes); line marks (indentation/connecting lines, optional).
- **Channels:** Horizontal spatial position (depth + link relationships); vertical spatial position (sibling order).
- **Annotation options:** Icons; color coding; bold/italic for attributes; expand/collapse interaction.
- **Data types suited for:** Tree data; file systems; taxonomies; nested categories.
- **Interesting feature extraction/manipulation of data:** No spatial encoding of quantitative attributes — purely structural.

---

### BubbleTree (p. 202–203)

- **What it shows:** Radial node–link tree layout where subtrees are laid out in full circles. Depth encoded as relative distance to parent center.
- **When to use:** Large trees (thousands of nodes) where hierarchical clustering into circles aids visual grouping.
- **When to avoid:** When absolute depth comparisons are needed (relative not absolute distances); very irregular branching factors.
- **Interesting properties:** Full circles rather than partial arcs unlike standard radial layouts. Spatial position encodes relative depth (distance to parent center) rather than absolute screen position.
- **Marks:** Point marks (nodes); connection marks (links as lines or curves).
- **Channels:** Spatial position (relative radial depth; parent-relative distance); color (additional attribute); size (node attribute).
- **Annotation options:** Color, size coding of nodes; labels; interactive zoom/pan.
- **Data types suited for:** Large tree/hierarchical data.
- **Interesting feature extraction/manipulation of data:** Layout algorithm computes space allocation per subtree proportionally to subtree size or node count.

---

### Color Channels Overview (pp. 219–225)

- **What it shows:** Not a single visualization type, but the building blocks for all color encodings.
- **Luminance channel:** Ordered magnitude — 2–5 discriminable bins for separated regions; required for text/edge contrast; power law perception.
- **Saturation channel:** Ordered magnitude — ~3 discriminable bins; smaller effect in small marks; interacts with size.
- **Hue channel:** Categorical identity — ~6–7 discriminable bins for separated small regions; no implicit ordering; more discriminable in large regions; bright/saturated for small marks, pastels for large areas.
- **Transparency channel:** Layering — usually only 2 discriminable states (opaque/semi-transparent); must not combine with luminance/saturation encoding.

---

### Colormaps Taxonomy (p. 225–)

- **What it shows:** Framework for choosing how to map data values to colors.
- **Categorical (qualitative):** Hue-based; 6–12 bins; identity channel.
- **Sequential ordered:** Luminance/saturation progression from min to max; 9 levels common (e.g., white-to-blue choropleth).
- **Diverging ordered:** Two sequential ramps meeting at a zero/neutral point; shows both positive and negative deviations.
- **Bivariate:** Two attributes simultaneously; safe when one is binary; confusing when both have many levels.
- **Continuous vs. segmented:** Quantitative data → continuous; categorical → segmented; ordinal → choice reveals emphasis.
