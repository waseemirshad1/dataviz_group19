# [agent_14] Data Sketches — pages 401-428

## Visualization Catalogue: Pages 401–428

---

### Radial Character-Chapter Network / Chord-Style Circular Layout (pp. 401–404)
- **What it shows:** Co-occurrence and relationships between characters and chapters in a manga/anime series. The 50 chapters are arranged as "pills" around the outer ring; characters are placed along an inner circle; lines connect characters to chapters they appear in.
- **When to use:** Best for showing which entities (characters) appear across which events/episodes/categories, when both dimensions have moderate cardinality (here: ~50 chapters, ~20+ characters). Avoid when either dimension has very high cardinality — lines become unreadable.
- **When to avoid:** Very dense networks where all entities are connected to most episodes; when the primary task is counting rather than pattern exploration.
- **Interesting properties:**
  - Outer ring encodes color palette data (CMYK dotted circles) — each chapter's cover art color is encoded as a cluster of CMYK color dots (p. 404)
  - Bidirectional hover interaction: filtering from character → chapters and from chapter → characters gives two perspectives on the same data
  - Main character (Sakura) is visually identifiable by having lines to all 50 chapters — the fully-connected entity stands out
  - Relationship lines in the inner circle carry text annotation on hover, encoding a third layer of data (relationship type/description)
- **Marks:** Lines (connections), dots/circles (character nodes), arc/pill segments (chapter nodes), CMYK dot clusters (color palette encoding)
- **Channels:** Position (radial/angular — chapter and character placement), Color hue (cover art palettes via CMYK dots), Line presence/absence (co-occurrence), Size (implicit — density of lines around a character indicates frequency)
- **Annotation options:** Hover-reveal text annotations on relationship lines (p. 403); hover-reveal highlighting of connected chapters/characters; legend overlay using the visualization itself (p. 404)
- **Data types suited for:** Bipartite networks (two entity types with co-occurrence/membership data); categorical × categorical with presence/absence; supplementary quantitative data (color palette) encoded at nodes
- **Interesting feature extraction/manipulation of data:** The CMYK color of each chapter's cover art was extracted and encoded as dot clusters — transforming a visual aesthetic property of source material into a quantitative channel. Character "importance" is derivable from line density without explicit calculation.

---

### Physical Data Installation with Illuminated Orbs (pp. 406–421)
- **What it shows:** 16 women in computing, each represented as a physical illuminated orb (fillable Christmas ornament with Neopixel and tilt sensor inside). The installation encodes multiple variables in 3D space and interactive light.
- **When to use:** When the goal is immersive, emotionally resonant storytelling with a live audience; when embodied interaction (picking up, touching, walking through) adds meaning; when the dataset is small (16–20 items) and richly qualitative.
- **When to avoid:** Large datasets; remote audiences (though a digital counterpart was created with D3.js + Three.js); when reproducibility or scalability is required.
- **Interesting properties:**
  - y-axis (height from floor): encodes renown (Wikipedia backlink count) — more famous = higher = "out of reach" (p. 408)
  - z-axis (depth in room): encodes time — year of accomplishment — visitors physically walk through history (p. 408)
  - Orbs start dimmed; light up as visitors interact — metaphor for invisibility and illumination (p. 410)
  - Group-triggered staggered lighting: interacting with one orb causes others in the same category to light up with a time delay, communicating categorical membership through temporal animation (p. 415)
  - Orb brightness accumulates over the show duration — persistent state as a communal data artifact
  - Summary board near exit: visitors place a gold star sticker by the category they identify with most — audience participation as data collection (p. 409)
- **Marks:** Physical orbs (3D points/glyphs), hanging wires (implicit position channels), acrylic info cards laser-etched inside orbs (text marks)
- **Channels:** Position-y (renown/backlinks), Position-z (time/year), Light brightness (interaction state / accumulated visitor engagement), Color (initially planned but rejected due to indistinguishability at subtle hues — p. 410), Stagger timing (categorical group membership)
- **Annotation options:** Information card inside each orb (laser-etched acrylic, p. 418); summary board outside for visitor engagement; digital counterpart website for remote access (p. 421)
- **Data types suited for:** Small biographical/person datasets with temporal and quantitative attributes; data with strong narrative or emotional dimension; data about visibility/invisibility (metaphor aligns with subject matter)
- **Interesting feature extraction/manipulation of data:** Wikipedia backlink count used as proxy for "renown" — a derived quantitative measure extracted from hyperlink structure, not from traditional citation or fame metrics. Year of accomplishment manually extracted by cross-referencing multiple Wikipedia sources.

---

### Digital 3D Counterpart (Three.js / D3.js / WebGL) (p. 421)
- **What it shows:** A digital version of the physical installation, accessible to audiences who could not visit in person. Built with D3.js, Three.js, Greensock, and Vue.js.
- **When to use:** When a physical installation has been created but you need to extend reach to global audiences. Also when learning 3D visualization in the browser.
- **When to avoid:** When the embodied/tactile dimension is central to the message — the digital version is a translation, not a substitute.
- **Interesting properties:** The transition from 2D to 3D digital (using Three.js) was described as a necessary stepping stone before the physical installation — coding in 3D first helped the author "understand how to think about space and lighting in the third dimension" (p. 406)
- **Marks:** 3D geometric objects in browser space
- **Channels:** 3D position, light, color, animation
- **Annotation options:** Text overlays, hover states
- **Data types suited for:** Same biographical dataset as the physical version; any dataset where spatial metaphor adds meaning
- **Interesting feature extraction/manipulation of data:** Same data as physical installation; no additional manipulation described

---

### Summary / Participation Board (p. 409, p. 421)
- **What it shows:** A board where installation visitors place a gold star sticker in the category (mathematicians, computer scientists, creatives, other) they identify most with. Accumulates audience self-identification data over the course of the show.
- **When to use:** Live events or exhibitions where audience participation adds a communal data layer; when you want visitors to "leave something behind."
- **When to avoid:** Digital-only contexts (though digital equivalents like voting widgets exist).
- **Interesting properties:** The board is both a visualization output (showing which categories resonated most with the audience) and a data collection tool. The act of placing a sticker is an interaction that contributes to the evolving visualization.
- **Marks:** Star/gem stickers as physical points; position in category columns as categorical encoding
- **Channels:** Position (category membership), Density/accumulation (how many people chose each category)
- **Annotation options:** Category labels on the board
- **Data types suited for:** Self-reported categorical preference data; audience demographics
- **Interesting feature extraction/manipulation of data:** Transforms a live audience into data contributors; the visualization grows during the exhibition

---

### CMYK Dot Cluster as Color Palette Encoding (p. 404)
- **What it shows:** The color palette of each manga chapter's cover art, encoded as clusters of small CMYK-colored dots arranged around the outer ring of the circular layout.
- **When to use:** When you want to encode color/aesthetic properties of source material within a larger visualization; when the exact palette matters more than an average color.
- **When to avoid:** When viewers are color blind (CMYK encoding relies entirely on hue discrimination); when the encoding needs to be immediately legible rather than exploratory.
- **Interesting properties:** Uses color as a direct encoding of color — the dots are the thing they represent. Creates a beautiful decorative outer ring that also carries genuine data.
- **Marks:** Small dots (colored)
- **Channels:** Color hue and saturation (CMYK components), Position (which chapter the cluster belongs to)
- **Annotation options:** Hover reveals which character appeared on that cover (p. 404)
- **Data types suited for:** Color palette data; aesthetic metadata from visual media
- **Interesting feature extraction/manipulation of data:** Cover art images were analyzed to extract CMYK color components, which were then encoded as proportional dot sizes within each cluster
