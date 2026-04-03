# [agent_13] Data Sketches — pages 351-400

## Coverage
Pages 351–400 span three main sections: (1) the final stages of Nadieh's "Myths & Legends" project — a star-constellation visualization called "Figures in the Sky" (pp.351–368); (2) Shirley's "Myths & Legends" entry — a 3D crystal visualization of women Nobel Laureates called "Legends" (pp.370–382); and (3) the opening and early progress of Nadieh's "Fearless" project — a radial visualization of the manga Cardcaptor Sakura (CCS) including data gathering, color clustering via K-means, and iterative construction of a complex radial layout (pp.386–400). These pages are primarily process narratives with embedded design and technical lessons.

---

## Math as a Design Tool

- Math — especially trigonometry, linear algebra, and geometry — is an essential skill for creating custom, unique data visuals. (p.351)
- Knowing when to switch from trigonometry to vector math can turn a hard problem into a simple one. Example: finding normal vectors to offset parallel lines was far simpler as vector math than as trig with four separate cases. (p.351)
- Polar coordinates (radius + angle) are especially useful for radial layouts and for reasoning about circular paths. (p.390)
- SVG Cubic Bézier Curves require understanding of anchor points and control handles; debugging by placing visible dots on anchor points is a reliable technique. (p.395)

---

## Remix vs. Copy: Starting from Existing Code

- It is mentally easier to start from a base example than from scratch, especially for unfamiliar techniques (e.g., sky map projections, Three.js, WebGL). (p.354)
- Key principle: **remix, don't copy**. Take base code as a starting point, then meaningfully transform it to reflect your specific data and your own visual style. "Inspired by" rather than "cheap knock-off." (p.354)
- This approach is distinct from "plug your data in and call it done" — the creator's unique data, unique context, and unique style should visibly transform the output. (p.354)

---

## Projections for Spatial / Astronomical Data

- Stereographic projection: used for circular sky map views focused on a single pole or region. (p.353)
- Equirectangular projection: used for full-sky maps showing all constellations of a culture. Requires adjusting width/height ratio and removing circular clip. (p.362)
- Both are available in D3.js. Choosing the right projection for the task is a core design decision for geographic/astronomical data. (p.353, p.362)
- Graticule lines (background grid) are invaluable for debugging — they confirm whether a spatial projection is correctly implemented. (p.354)

---

## Canvas vs. SVG: When to Use Each

- Canvas is preferred for large numbers of elements (e.g., 9,000 stars, 2,200+ data points) due to better rendering performance. (p.353, p.363)
- SVG is preferred for axes, interactivity, annotations, and text — it offers DOM-based event handling and accessibility. (p.363)
- Hybrid approach: use canvas for the heavy drawing layer + an SVG overlay for interactive/annotation elements. This combines performance (canvas) with interactivity (SVG). (p.363)
- Canvas offers useful capabilities: `shadowBlur` for glow effects, radial gradients per element, `multiply` blend mode for overlapping data points. (p.355, p.363)

---

## Color Encoding

- Matching star colors to their actual perceived temperature-based colors (not arbitrary hue mapping) increases realism and semantic meaningfulness of the color channel. (p.355)
- Overly saturated colors can make a visualization look garish — test with real data at realistic scale. (p.355)
- Radial gradients on individual marks (lighter center, darker edge) add depth and realism to circular marks, simulating a light source. (p.355)
- The `chroma.js` library can programmatically generate lighter/darker variants of a base color. (p.355)
- LAB color space produces perceptually better clustering results than RGB when grouping colors with K-means, because distances in LAB better match human perception. (p.387)
- Mixing colors channel-by-channel in GLSL (fragment shaders) with `mix()` + trigonometric shaping functions (`power()`, `sine()`, `absolute()`, `step()`, `smoothstep()`) enables rich, unique gradients. (p.374)

---

## Annotations Are Vital

- Annotations are one of the most underutilized yet most effective tools for making a chart understandable to an audience. (p.363)
- Annotations should guide the reader toward what the creator considers most important — they are an explicit editorial act. (p.363)
- The `d3-annotation.js` library has an "edit mode" that lets you drag annotation labels interactively, see their placement in context, and then hardcode the final positions. This saves significant time. (p.399)
- Custom annotation lines (e.g., radiating outward from a center) may be worth hand-coding when the library's defaults do not fit the visual style. (p.399)

---

## Performance Optimization

- Replace heavy live computations with pre-generated images when possible. For a scrollable article, replacing dynamically rendered sky maps with static images dramatically reduced load time. (p.364)
- When text rendering in Three.js/WebGL makes the page unresponsive (because each letter becomes a 3D object), instead render text to a canvas element, then use that canvas as an image texture on a `PlaneGeometry`. Much more performant. (p.377)
- Removing visual elements from "mini" repeated versions (ring of small constellation images) that are too small to be visible improves performance AND visual clarity. (p.361)

---

## 3D / WebGL Data Visualization

- WebGL coordinate system uses "units" (not pixels); orientation follows the right-hand rule (thumb = x, index = y, middle = z). (p.372)
- `Three.js SphereGeometry` with `flatShading: true` shows individual triangular faces, creating gem/crystal-like shapes — a technique that transforms an ordinary sphere into a faceted object. (p.375)
- `computeFlatVertexNormals()` on a Three.js geometry can fake a light source, making faces appear to have depth (bottom/back = darker). (p.376)
- Encoding data in 3D spatial position: using the z-axis for time (most recent = closest to viewer, oldest = farthest) creates a spatially intuitive time dimension. (p.377)
- Progressive disclosure via view angle: different information is revealed depending on whether the viewer is at ground level (personal details) vs. flying above (holistic patterns). This is a powerful interaction design technique unique to 3D. (p.377)

---

## Glyph Design: Encoding Multiple Variables in One Mark

- Crystal/gem glyph (Shirley's "Legends" project): encodes 3 variables simultaneously in one mark:
  - **Size** → influence (Wikipedia backlinks)
  - **Number of faces** → depth of documentation (number of Wikipedia sources)
  - **Color** → award category
  - **Z-position** → temporal dimension (year of award)
- This is a multi-channel glyph where every channel earns its place and each encodes something semantically meaningful. (p.371–372)
- Adding jitter to vertices of the geometry makes each glyph look slightly unique, reinforcing the individual-identity reading. (p.375)

---

## Interaction Design

- **Click to expand**: clicking a mini image in a ring layout triggers it to be displayed large in a central space. Allows overview + detail-on-demand. (p.361, p.367)
- **Culture selector**: selecting a culture from a list updates the full sky map to show only that culture's constellations — filter + update interaction. (p.362)
- **Hover to reveal**: hovering over a character or chapter in the radial CCS layout shows only the lines connecting that item to related items, reducing clutter. (p.397)
- **Fly-through view**: in 3D, providing controls to "walk through" vs. "fly above" reveals different encodings depending on the viewer's perspective — an interaction design pattern unique to 3D. (p.377)

---

## Data Preparation and Tool Separation

- Principle: **use each tool for what it does best**. (p.388, p.400)
  - R: data loading, cleaning, exploratory statistics, K-means clustering, exporting preprocessed JSON files
  - JavaScript/D3.js: interactive visualization
  - Adobe Illustrator / Affinity Designer / Inkscape: legends, annotations, final layout polish
- Pre-calculating "visual variables" in R (e.g., color hex codes, cluster percentages per chapter) reduces the complexity of JavaScript code. (p.388)
- Spreadsheets are excellent for light data cleaning and manual annotation tasks. (p.371)
- For static portions of interactive visuals, exporting a legend as SVG and loading it in is a hybrid approach — it keeps the legend adjustable via JavaScript (color, resize, animate) while avoiding the time cost of coding it from scratch. (p.400)

---

## Design Iteration and Accepting Failure

- Design frequently involves spending hours on a technique that does not make the final cut. This is normal, not wasteful — it teaches you what does and does not work. (p.393, p.400)
- Example: ~5 hours on a canvas-based CMYK halftone effect that was abandoned; ~15 hours on swirly Bézier lines that were replaced with a circular-arc approach. (p.400)
- Simpler approaches discovered later can outperform complex ones: replacing elaborate SVG Bézier curves with circle-arc segments resolved both visual and performance problems. (p.397)
- Peer feedback is a high-value, low-cost design intervention. Asking friends for feedback after completing a draft often yields significant improvements to interaction clarity and legend design. (p.399)

---

## Automatic Layout Calculation

- For constellations of widely varying sizes, calculating the optimal zoom level, rotation, and center position programmatically — rather than setting them manually per item — is essential for scalability. (p.360)
- General principle: wherever you have a collection of items that vary in spatial extent, write a function that automatically fits each item to its available display area. (p.360)

---

## Image-Based Data Analysis (Color Extraction)

- Loading images as pixel arrays (RGBA values) and applying K-means clustering in LAB color space extracts perceptually meaningful color groups from images. (p.387)
- When K-means requires you to pre-specify k: use your own eyes as the evaluation metric — generate cluster results for k=3 through k=11, compare against the original image, and choose the k that best captures all colors with good distinctiveness. (p.388)
- This technique is reusable: extracting color palettes from any collection of images (book covers, album art, posters) and aggregating them across items. (p.387–388)

---

## Radial Layout Design

- Radial layout with inner and outer rings allows two related datasets to be co-positioned around a shared center — inner ring for one set of entities, outer ring for another. (p.389)
- Connections between inner and outer ring entities are shown as lines swirling around the center — but these must be carefully designed to avoid overlapping each other. (p.389–395)
- "Onion-layered" approach: inner circle = characters, outer ring = chapters, connections = lines between them. Multiple concentric rings can encode different hierarchical groupings (e.g., volumes wrapping chapters). (p.389, p.397)
- Limiting visible connections to only those belonging to the currently hovered item is critical for radial layouts with many relationships — showing all at once creates an unreadable hairball. (p.397)

---

## Common Mistakes and Anti-Patterns

- **Forgetting coordinate transformation**: missing an RA/declination transformation produces an apparently random cloud of points. Always verify spatial data with a reference (e.g., graticule grid). (p.354)
- **Too many lines at once**: displaying all relationship lines simultaneously in a network embedded in a radial layout creates visual clutter. Solution: show only on hover. (p.395, p.397)
- **Tapering lines that still don't fit the design**: improving line aesthetics (e.g., tapered width) doesn't help if the line routing geometry is wrong for the overall visual style. Sometimes the geometry itself needs to change. (p.396)
- **Over-engineering annotations in code**: using a vector drawing tool for legend/annotation layout is often faster and equally effective. (p.400)
- **Not considering accessibility**: text rendered to canvas is not accessible (not a11y compliant) because it is treated as an image. Text rendered to DOM (SVG or HTML) is preferred for accessibility. (p.377)

---

## Practical Rules of Thumb

- When a star map (or any spatial visual) produces unexpected output: add graticule lines first — they immediately reveal if the projection/coordinate system is correct. (p.354)
- Scale mark size by magnitude (brightness/importance) and use radial gradients per mark for a sense of physical depth. (p.355)
- Use `multiply` blend mode to darken overlapping marks in scatter plots — prevents them from washing out to white, reveals density. (p.363)
- For CMYK halftone effects with smooth edges: canvas allows graceful fade-out at circle boundaries. SVG clips too abruptly unless a thick stroke "masks" the sharp edge. (p.392–393)
- For the outer small "ring" previews in a large radial layout: reduce the number of visible layers (keep only constellation lines, drop stars and background) to improve performance while retaining essential information. (p.361)
- When debugging complex SVG path formulas: render the anchor points and control handles as colored circles — this reveals why a curve deforms unexpectedly. (p.395)
