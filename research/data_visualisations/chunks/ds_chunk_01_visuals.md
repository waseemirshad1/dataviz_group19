# [agent_06] Data Sketches — pages 1-50

## Visualization Catalogue

---

### Loom and Strings (Custom Chord Diagram) (p.28-43)

- **What it shows:** How many words each character in the Lord of the Rings (9 Fellowship members) spoke at each location in the three films. Shows the flow / connection between two sets of entities: characters (center) and locations (outer ring).
- **When to use:** When showing flows or connections between two groups of entities where one group is "central" and the other "peripheral." Good for showing how a set of actors (characters, nodes) distributes across a set of contexts (locations, categories). Avoid when there are too many entities on either side to remain legible.
- **When to avoid:** When the connection data is symmetrical (standard chord diagrams handle that better). Not suitable when the viewer needs to read exact values rather than relative magnitudes.
- **Interesting properties:** This is a novel chart form derived from a standard chord diagram. The key innovation is that all inner strings flow towards the center (where characters are placed), rather than connecting two arcs on the outer ring as in a standard chord diagram. The center is split into two halves (left/right) to give the strings room to flow naturally. The result was named "Loom and Strings" by Nadieh Bremer (named with input from Mike Bostock, creator of D3.js). Locations are ordered clockwise by when they first appear in the film. Font choices reinforced the Middle-Earth theme (Elvish and Dwarvish scripts).
- **Marks:** Curved strings (Cubic Bézier Curves); outer arcs per location; text labels in center per character
- **Channels:**
  - Thickness of string → number of words spoken by that character at that location (quantitative)
  - Color of string/arc → location identity (categorical, color-picked from movie stills)
  - Position on outer ring → location (ordered by narrative chronology)
  - Position in center → character identity (alphabetical initially; then adjusted)
- **Annotation options:** Hover tooltip on character name shows text paragraph of insights; hover on location highlights which characters spoke there; outer arc values show total words per location
- **Data types suited for:** Quantitative (word count), categorical (characters, locations), relational (who spoke where)
- **Interesting feature extraction/manipulation:** Word counts aggregated from scene-level to character × location level. Location variable was manually added to ~700 rows (not present in the original dataset). Filtering to 9 Fellowship members simplifies without losing the core story. The "thickness" aggregation is the visual summary.

---

### Film Flowers (Flower Glyph per Movie) (p.44-50)

- **What it shows:** Multiple attributes of top US summer blockbuster movies (1990s–2016): movie rating, genre, parental guidance rating, popularity (number of votes), box office performance — all encoded into a single flower-shaped glyph per movie.
- **When to use:** When you want to show 4-5 attributes of many individual items simultaneously in a visually engaging, dense layout. When the "item" metaphor (flower = a movie, a site, a species) adds meaning. Works well for an overview gallery that invites exploration.
- **When to avoid:** When precise quantitative comparison across items is required (length/position is more accurate than petal shape or radius). If encoding rules are too complex, viewers cannot decode values. More than ~5 channels per glyph risks information overload.
- **Interesting properties:** The flower is a metaphor for summer; the mark choice is motivated by both aesthetics and domain appropriateness. Each petal is an SVG Cubic Bézier Curve shape. Petal shape encodes a categorical variable (4 parental guidance rating categories → 4 distinct petal shapes, including a cherry blossom shape). Number of petals encodes a quantitative variable via discretization (IMDb vote count → 5 to 15 petals). This is an unorthodox encoding of a quantitative variable into a count-based mark property. The entire glyph is one "mark" with 4+ channels active simultaneously.
- **Marks:** Flower glyphs (custom SVG path shapes); each petal duplicated 6 times and rotated 60° intervals around center
- **Channels:**
  - Petal shape (4 distinct shapes) → parental guidance rating (categorical: G, PG, PG-13, R)
  - Petal radius / size → movie rating out of 10 (quantitative, continuous linear scale)
  - Number of petals (5-15, discretized) → number of IMDb votes (quantitative, popularity)
  - Color hue → movie genre (categorical: Action, Adventure, Comedy, etc.)
  - Position (x, y in layout) → release year / time ordering (temporal)
- **Annotation options:** Title labels per flower; color legend for genres; shape legend for ratings
- **Data types suited for:** Quantitative (rating, votes, box office), categorical (genre, rating), temporal (release year)
- **Interesting feature extraction/manipulation:** Used d3.scaleQuantize() to convert continuous vote count to discrete petal count (5-15). Used d3.scaleLinear() for continuous rating to petal size. Multiple API sources combined (IMDb search + OMDb API). Filtered to top 5 US-grossing movies per summer per year.

---

### Standard Chord Diagram (referenced / shown as starting point) (p.34)

- **What it shows:** Flows or connections between a group of entities; quantitative flow strength between pairs. Classic use cases: import/export flows between countries, how people switch between phone brands, how students transition from degree to job type.
- **When to use:** When you have bidirectional or directional flows between a fixed set of entities (N × N matrix). Works well when N is small (4-10 entities). The visual emphasis is on which pairs are most strongly connected.
- **When to avoid:** When N is large (too many arcs); when flows are all similar in magnitude (no visual differentiation); when the viewer needs to read exact values.
- **Interesting properties:** The outer arcs show each entity's total flow volume. The inner chords connect pairs, with thickness encoding flow magnitude. Described as "often tricky to understand but can display a wealth of information" (p.34).
- **Marks:** Arcs (outer segments); filled curved bands/chords (inner connections)
- **Channels:**
  - Arc length → total flow volume for that entity (quantitative)
  - Chord thickness → bidirectional flow magnitude between two entities (quantitative)
  - Color → entity identity (categorical)
  - Position on circle → entity (categorical)
- **Annotation options:** Labels on arcs; value annotations; hover highlights
- **Data types suited for:** Quantitative (flow volumes), categorical (entities), relational (pairwise connections)
- **Interesting feature extraction/manipulation:** Underlying data is an N×N matrix of flows; the matrix must be aggregated from raw transaction data before use.

---

### Timeline with Sized Circles (Sketched / Rejected Idea) (p.33)

- **What it shows:** A sequence of scenes/events on a time axis, with circles sized to the amount of words spoken at each scene. A rejected alternative for the LotR dataset.
- **When to use:** When time ordering matters and you want to show a continuous temporal sequence with a magnitude variable.
- **When to avoid:** When connection/flow structure (who spoke where) is the primary question — a timeline loses relational information.
- **Marks:** Circles positioned along a timeline
- **Channels:** Position (x-axis) → time; Size (circle area) → word count (quantitative)
- **Data types suited for:** Quantitative (word count), temporal

---

### Spirograph / Petal Abstraction (Sketched / Rejected Idea) (p.33)

- **What it shows:** Each location represented as a spirograph-like figure. Number of "petals" = number of detailed sub-locations. Petal size = total words spoken at that location. A more abstract alternative to the chord diagram.
- **When to use:** When aesthetic abstraction and artistic impact take priority over readability. When showing magnitude and count simultaneously in a compact glyph.
- **When to avoid:** When the viewer needs to compare specific values or trace relationships between entities — the abstraction severs relational legibility.
- **Marks:** Spirograph-like radial forms; petals of varying sizes
- **Channels:** Number of petals → count of detailed sub-locations; petal size → total word count (quantitative)
- **Data types suited for:** Quantitative, categorical (grouped by location)
- **Interesting feature extraction/manipulation:** Would require pre-aggregation: count of sub-locations per broad location, total words per broad location.
