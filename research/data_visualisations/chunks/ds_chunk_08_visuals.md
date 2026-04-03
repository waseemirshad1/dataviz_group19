# [agent_13] Data Sketches — pages 351-400

## Coverage
Pages 351–400 contain three major original visualization projects: Nadieh's "Figures in the Sky" (star/constellation map), Shirley's "Legends" (3D crystal glyph display), and the opening of Nadieh's CCS radial visualization. Each project produces multiple chart types; all are described below.

---

### Stereographic Sky Map with Donut Ring Overlays (p.353–368)

- **What it shows:** A circular sky map centered on a single star, showing all constellations (across multiple world cultures) that include that star. Mini donut charts are drawn around each star that participates in at least one constellation, with each colored arc representing one constellation.
- **When to use:** When showing membership of an item in multiple overlapping groups, especially when spatial context (the actual positions of stars) carries meaning. Avoid for datasets without a meaningful spatial embedding.
- **Interesting properties:** Combines a scientific base map (stereographic projection) with a data visualization overlay (donut charts per node) and ornamental elements (ecliptic line, zodiac sign annotations, dashed boundary circle). The background uses D3.js contour functions to simulate a Milky Way-like texture.
- **Marks:** Circles (stars, sized by magnitude); arc segments (donut slices, one per constellation per star); lines (constellation stick figures); background contour patches (simulated nebulosity).
- **Channels:** Size of circle → stellar magnitude; color of arc segment → culture/constellation identity; angular position of arc → relative ordering of constellations; opacity/glow → star brightness reinforcement; color hue of star → temperature.
- **Annotation options:** Zodiac symbols at 12 major right-ascension lines on the boundary circle; degree labels for declination and RA on the boundary; North/South compass pointers.
- **Data types suited for:** Spatial point data with group-membership attributes (set membership); ordered quantitative (magnitude); categorical (culture, constellation).
- **Interesting feature extraction/manipulation of data:** Normal vector math used to offset parallel lines between the same two stars (when multiple constellations share an edge), keeping them visually distinct without overlapping. Per-star radial gradients (lighter center, darker edge) created programmatically using `chroma.js` lightness/darkness functions.

---

### Full Equirectangular Sky Map (All Constellations of One Culture) (p.362)

- **What it shows:** The complete celestial sphere in a rectangular projection, showing all constellations of a selected culture simultaneously.
- **When to use:** When comparing the overall density and distribution of constellations across an entire sky for one culture; or as a header/overview image. Less suitable for comparing individual stars in detail.
- **Interesting properties:** Background "fuzzy patches" are aligned with the approximate shape of the Milky Way. Switching between cultures dynamically updates the map (interactive filter).
- **Marks:** Dots (stars), lines (constellation edges), area fills (background contour patches for Milky Way).
- **Channels:** Position → actual sky coordinates (RA, declination); size → stellar magnitude; color → star temperature.
- **Annotation options:** Culture name; graticule grid lines.
- **Data types suited for:** Spatial/astronomical data with cultural categorical grouping.
- **Interesting feature extraction/manipulation of data:** Automatic optimal zoom, rotation, and center calculation per constellation — a function that fits any shape to a display area without manual adjustment.

---

### Ring of Mini Sky Map Thumbnails (p.360–361)

- **What it shows:** A ring of small circular sky map thumbnails surrounding a central larger map — one thumbnail per constellation — all built around the same central star.
- **When to use:** Overview + detail-on-demand for a collection of related spatial items. Clicking a thumbnail loads its full-detail version in the center. Avoid if the thumbnails need fine detail — they are too small to show everything.
- **Interesting properties:** Thumbnails contain only the essential layer (constellation stick figures) — stars and background are stripped for performance. Clicking a thumbnail triggers a transition to a full-resolution central view.
- **Marks:** Small circular maps (thumbnails); large central circular map; interactive click targets.
- **Channels:** Spatial position in ring → no inherent order (spatial, not ordered); visual content of each thumbnail → shape of the constellation.
- **Annotation options:** Constellation name on hover or click.
- **Data types suited for:** Collections of spatial sub-items (constellations) associated with a common reference item (shared star).
- **Interesting feature extraction/manipulation of data:** Performance optimization: reduce layer count in thumbnails (keep constellation lines only, drop stars and background) to maintain responsiveness when rendering many small maps simultaneously.

---

### Scatter Plot: Star Brightness vs. Number of Constellations (p.363, p.368)

- **What it shows:** Each of the ~2,200 stars that belong to at least one constellation is plotted as a point. X-axis = number of constellations using that star; Y-axis = apparent brightness (magnitude). Color matches the star's temperature-based color, as used in the sky maps.
- **When to use:** Showing correlation or lack thereof between two continuous variables for a large set of items; spotting outliers (bright stars that appear in many cultures). Avoid when visual consistency with a companion spatial view is not needed.
- **Interesting properties:** Uses canvas for the ~2,200 data points (performance), with an SVG overlay for axes, annotations, and interactivity. `multiply` blend mode applied to overlapping points to reveal density. Colors made more vibrant than in the sky map, with an added glow effect, because the white background made the realistic star colors appear too soft.
- **Marks:** Points (one per star).
- **Channels:** X-position → number of constellations; Y-position → apparent magnitude (brightness); color hue → temperature; size (small and consistent) → presence.
- **Annotation options:** Named annotations with d3-annotation library for notable stars (those appearing in unusually many constellations, or unusually bright outliers).
- **Data types suited for:** Quantitative × quantitative with a categorical color channel. Large N (thousands of items).
- **Interesting feature extraction/manipulation of data:** Canvas + SVG hybrid: compute-heavy drawing in canvas, annotation/axis/interaction layer in SVG on top — best-of-both-worlds approach for large datasets.

---

### Small Multiple Sky Maps per Star (p.362–363)

- **What it shows:** A grid of smaller sky map circles, each centered on a different star, showing that star's network of constellations. Allows comparison of many stars side by side.
- **When to use:** Comparing the constellation-membership structure of multiple stars simultaneously. Avoid for more than ~15–20 stars (space and clutter).
- **Interesting properties:** Stars are manually curated to select the ~15 most interesting and diverse examples from ~100 candidates. The reusable sky-map function that handles any star/constellation combination makes generating these cheap once the base function exists.
- **Marks:** Circular sky maps (each a complete visualization instance).
- **Channels:** Layout position → star identity; visual content → constellation structure.
- **Annotation options:** Star name; number of constellations.
- **Data types suited for:** Same schema as the central sky map, applied to multiple items simultaneously.
- **Interesting feature extraction/manipulation of data:** Manual curation of "interesting" cases from a large candidate set — a valuable curatorial/editorial step in the design process.

---

### Mini Bar Charts Within Culture Cards (p.363–364)

- **What it shows:** Each world culture that has a constellation catalog is shown as a card; within each card, a small inline bar encodes the average number of stars per constellation for that culture.
- **When to use:** When a single summary statistic per category is sufficient and the cards already carry most of the information. Avoid when more than one dimension of comparison is needed — use a full bar chart or scatter plot instead.
- **Interesting properties:** A bar chart that was originally planned as a standalone visual was redesigned as an embedded sparkline within an information card — reducing visual complexity while retaining the quantitative comparison.
- **Marks:** Horizontal bar (one per culture card).
- **Channels:** Bar length → average stars per constellation.
- **Annotation options:** Culture name; exact value label optional.
- **Data types suited for:** One quantitative value per categorical item, displayed in context with other information about each item.
- **Interesting feature extraction/manipulation of data:** Aggregation: compute mean(n_stars) grouped by culture.

---

### 3D Crystal Glyph Field — "Legends" (p.371–377, p.379–382)

- **What it shows:** Each of 51 women Nobel Laureates is represented as a 3D gem/crystal shape in a WebGL scene. Male Nobel Laureates are shown as stars (background points). The viewer can walk through the crystals (ground-level view: individual details) or fly above (bird's-eye view: temporal distribution revealed).
- **When to use:** When encoding 3–4 variables per item and artistic, experiential presentation is appropriate. Especially effective for showing a large comparison (53 crystals vs. 866 background stars) that generates emotional impact. Not suited for precise quantitative reading — this is a statement piece.
- **Interesting properties:** Size encodes influence (Wikipedia backlinks); number of faces encodes depth of documentation (Wikipedia sources); color gradient encodes award category (two gradient families: humanities vs. natural sciences); z-axis position encodes decade of award. The temporal dimension is only revealed from above — progressive disclosure via camera angle.
- **Marks:** 3D polyhedra (one per woman); small point-light objects (one per male laureate).
- **Channels:** 3D size → influence; face count → documentation depth; color gradient family → discipline category; z-axis → time (decade); spatial density → gender imbalance (866 stars vs. 53 crystals — visually striking).
- **Annotation options:** Text labels rendered as canvas textures on `PlaneGeometry` objects — positioned near each crystal. Landing page legend explains all channels.
- **Data types suited for:** Multi-attribute categorical/quantitative data where impact and aesthetics matter more than precision. Temporal data encoded spatially (z-axis).
- **Interesting feature extraction/manipulation of data:** `Three.js SphereGeometry` with `flatShading: true` + programmatic face count variation + vertex jitter = unique organic crystal shapes per item. Fragment shader with GLSL `mix()` and shaping functions (`power()`, `sine()`, `smoothstep()`) creates rich color gradients per crystal.

---

### Radial Manga Visualization — CCS Layout (p.389–400)

- **What it shows:** A complex multi-ring radial visualization for a 50-chapter manga series. Inner circle: character relationship network; outer ring: 50 chapter "pills" colored by K-means color clusters extracted from cover images; outermost ring: volume groupings. Curved arcs connect characters (inner circle) to the chapters they appear in (outer ring).
- **When to use:** When showing many-to-many relationships between two entity sets and when circular/radial organization reflects a meaningful structure (e.g., sequential chapters in a ring). The donut/ring metaphor works especially well for media with defined episodes or chapters. Avoid if straight linear ordering would be clearer — a matrix or chord diagram may communicate the same relationships more precisely.
- **Interesting properties:** Chapter pills are colored using K-means color extraction in LAB space from cover images — the color of each chapter arc reflects the actual dominant color palette of that chapter's artwork. Lines between characters and chapters run along circular arc paths rather than straight or arbitrary curves — "subway map" style. On hover: only the connections belonging to the hovered item are shown; all others fade.
- **Marks:** Arcs (chapter pills; volume grouping); circles (characters in inner donut); curved paths (connections, routed along radii and arcs); central image area (chapter cover image shown on hover).
- **Channels:** Angular position → sequential order (chapters 1–50 around the ring); arc color → dominant color palette of chapter cover; inner segment → character identity; line color → relationship type (family, love, friend); arc thickness → optional.
- **Annotation options:** Story annotations placed radially outward from the center using `d3-annotation.js`; custom radial annotation lines coded separately; legend diagram (created in Illustrator) explaining all rings.
- **Data types suited for:** Many-to-many relationship data (characters × chapters); image-derived color data; categorical sequence data.
- **Interesting feature extraction/manipulation of data:** K-means clustering in LAB color space applied per cover image; k chosen visually (inspect 3–11 clusters per image, pick best by eye); output = hex codes + percentage share per color cluster → drives the colored arc fill.

---

### Color Distribution Bar Chart (per Image, K-means Output) (p.387–388)

- **What it shows:** For each chapter cover image, a horizontal bar chart where each segment represents one K-means color cluster. Segment width = percentage of pixels assigned to that cluster. Segment color = the cluster's representative color. Used to evaluate the quality of clustering for different values of k.
- **When to use:** Evaluating and comparing color extraction results across different k values (3 to 11 clusters) and choosing the best k visually. Also useful as a standalone encoding of an image's color composition. Avoid as a main visualization — it is primarily a diagnostic/processing tool.
- **Interesting properties:** Generated for every chapter image at every k value — a grid of 50 × 9 = 450 small charts used purely for calibration. The final k per chapter is chosen manually by human comparison to the original image.
- **Marks:** Horizontal bar segments.
- **Channels:** Segment width → proportion of pixels; fill color → the cluster's color (self-referential — the color IS the data).
- **Annotation options:** k value label; chapter number.
- **Data types suited for:** Proportional part-of-whole data where the value IS the color (self-describing color channel).
- **Interesting feature extraction/manipulation of data:** Converting RGB pixel arrays → LAB color space → K-means clustering → hex + percentage export. The LAB conversion is the key manipulation that makes the clustering perceptually meaningful.

---

### CMYK Halftone Circle (Aesthetic Texture) (p.391–393)

- **What it shows:** A colored circle rendered with a CMYK halftone dot pattern — dots get smaller toward the edges instead of being clipped, creating a natural fade-out. Used as a fill style for chapter circles in the CCS visualization.
- **When to use:** When the subject matter (a manga, a printed medium) calls for a printing-process aesthetic that reinforces the content's identity. The technique is more decorative than analytically necessary. Avoid when fine color precision is needed — CMYK halftoning introduces visual noise.
- **Interesting properties:** Canvas-based implementation allows smooth dot fade at circle boundaries (unlike SVG which clips abruptly). When two CMYK circles overlap, the dot patterns mix, creating additive color blending effects. Final compromise: used SVG CMYK pattern with a thick stroke to approximate smooth edges at smaller sizes.
- **Marks:** CMYK dot pattern fills within circular shapes.
- **Channels:** Base hue → K-means cluster color; dot density at edges → fade-out (spatial encoding of circle boundary).
- **Annotation options:** Chapter number label overlay.
- **Data types suited for:** Color proportion data displayed in a context where printing aesthetics are thematically appropriate.
- **Interesting feature extraction/manipulation of data:** SVG pattern-based CMYK using separate angle-rotated dot patterns for C, M, Y, K channels. Canvas version uses halftoning algorithms from open-source references.
