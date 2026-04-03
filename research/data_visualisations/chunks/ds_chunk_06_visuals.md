# [agent_11] Data Sketches — pages 251-300

## Visualization Catalogue

---

### Generative Butterfly Path Visualization — "Marble Butterflies" (p.251–260)
- **What it shows:** Each butterfly species is represented as a flowing, smoky path across a canvas, with multiple butterflies active simultaneously. The dataset has 86 butterfly species with attributes: main color, wing shape, size (wingspan category).
- **When to use / avoid:** Use for exploratory/artistic data art where the aesthetic experience IS the point, or when showing a collection of entities in motion. Avoid when precise comparison between entities is needed — this is a display, not an analytical chart.
- **Interesting properties:** Every viewer sees a unique version because paths are generated with controlled randomness (jittered splines). The visual is perpetually changing — a static screenshot is never the "final" state. Named "Marble Butterflies" because the smoky lines resemble marble patterns.
- **Marks:** Curved lines (splines) with jitter applied on each redraw; some species (Skippers) use scattered circles instead of lines; smallest butterflies use dotted lines.
- **Channels:**
  - Color hue → species' main color (with slight random variation among 5 similar shades)
  - Line thickness / opacity → wingspan category (small = thin/transparent; large = thick/opaque)
  - Path type (solid / dotted / circle-scatter) → species category
  - Path curvature behavior → simulated natural flutter (curves hold direction briefly before changing)
- **Annotation options:** Title spelled out in wiggled, hand-drawn-style letters along the center; a central butterfly-like shape and the Data Sketches logo hexagon/circle serve as focal anchors.
- **Data types suited for:** Categorical (species, color, size group); continuous (wingspan mapped to thickness/opacity).
- **Interesting feature extraction/manipulation:** Wingspan was discretised into three categories (small / medium / large) to simplify the encoding. Brown-colored butterflies were filtered out by the designer because the color performed poorly aesthetically — an explicit subjective data filter in the service of visual quality.

---

### Generative Watercolor Flower-Tree Visualization — "Send Me Love" (p.262–276)
- **What it shows:** Each text message sent to SFMOMA is represented as a flower (positive sentiment) or leaf (neutral/negative sentiment), arranged on fractal tree branches. Each tree represents one day's worth of text messages for an individual. Five individuals are shown across multiple days.
- **When to use / avoid:** Use when you want to convey emotional texture and individual journeys over time — particularly effective when the "story" behind the data is personal or narrative. Avoid when precise quantitative comparison is the goal. High implementation complexity (watercolor effects, fractal branching, canvas layers).
- **Interesting properties:**
  - Cutout effect: watercolor canvas is behind a white-filled canvas with CSS `destination-out` blend mode, so flowers drawn on the second layer punch through as cutouts, revealing the watercolor underneath. A third SVG layer draws petal outlines.
  - The fractal branching metaphor (flowers grow on branches) solved a layout problem organically — the computer science concept of fractals matched the natural visual form.
  - Hover interaction reveals arrows showing the sequence of texts before and after any given message, plus the artwork SFMOMA sent back — creating a navigable personal narrative.
- **Marks:** Flower shapes (SVG petal paths colored by the artwork's dominant color) for positive messages; leaf shapes for neutral/negative messages; fractal branches as structural scaffolding.
- **Channels:**
  - Color → most dominant color in the artwork SFMOMA sent back (continuous/perceptual)
  - Shape (flower vs. leaf) → sentiment (positive vs. neutral/negative)
  - Position on branch → temporal sequence within a day
  - Branch scale → volume of messages (busier days have more flowers/leaves on larger branches)
- **Annotation options:** A keyword log displayed below each tree ("soil from which the tree sprouts") showing raw text keywords and timestamps; legend explaining flower = positive, leaf = neutral/negative, color = artwork received; hover arrows linking messages in sequence.
- **Data types suited for:** Temporal (messages over time), categorical (sentiment, artwork color), relational (sequence of interactions).
- **Interesting feature extraction/manipulation:** Sentiment scoring (positive/negative score per keyword via Node.js "sentiment" package) transformed unstructured text into a binary categorical variable for the shape encoding. Shannon Entropy of each artwork (how visually "chaotic" it is) was computed from the SFMOMA API as a potential additional variable.

---

### Tree Ring / Radial Arc Chart — "Beautiful in English" (p.282–295)
- **What it shows:** Top 10 most-translated words (nouns/adjectives) per language, displayed as concentric arcs. Each arc level = one rank (1st = innermost or most prominent, 10th = outermost). Each arc segment shows the original word in the source language alongside the English translation.
- **When to use / avoid:** Use for ranked lists where you want a compact, visually distinctive display that emphasizes order without a linear bar chart. Works well for single-language focus. Avoid when you need to compare multiple languages simultaneously in one view — too much visual weight.
- **Interesting properties:** The tree ring metaphor (growth rings of a tree) implies accumulation and hierarchy. Switching between languages is animated by rotating the text rings out of view and back in (rather than physically moving elements), which is cleaner than a position swap.
- **Marks:** Arcs (SVG arc paths), text labels placed along the arc path.
- **Channels:**
  - Radial position (arc ring level) → rank (1st most translated = innermost/prominent position)
  - Text on arc → the actual word (in source language, smaller/grey; English translation, larger/black in center)
  - Arc color → subtle differentiation
- **Annotation options:** Three layered `textPath` SVG elements per arc: grey original word left, black English translation center, grey original word right — making the English translation stand out without a separate legend.
- **Data types suited for:** Categorical (words), ordinal (rank), nominal (language).
- **Interesting feature extraction/manipulation:** Rankings were combined across all 10 languages using a point system (top word = N points, second = N-1, etc.) to derive an overall cross-language ranking. Synonyms mapping to the same English translation were manually merged per language before ranking — a critical data cleaning step.

---

### Word Snake / Beads on a String (p.282–295)
- **What it shows:** The top 100 most translated words overall, arranged as a string of "beads" (circles) connected by a swirling line. Each bead represents one language's top-translated word; the string winds down the page connecting all 10 language circles.
- **When to use / avoid:** Use for showing a ranked sequence of items where the "path through" them matters — especially for linguistic/textual data where the words themselves serve as the marks. Avoid if you need precise value comparison (no common scale).
- **Interesting properties:** The swirling layout (2, 3, or 4 beads per row depending on screen width) is fully responsive, recalculating the path geometry for each screen size. Hovering a language bead reveals an elaborate tooltip: a 5-year Google Trends line chart for that word + a word cloud of related queries — the most extensive tooltip described in the book.
- **Marks:** Circles (language beads) connected by a curved SVG path; text labels on/around each bead.
- **Channels:**
  - Position along the path → relative ranking / popularity
  - Circle size → distinguishes selected/highlighted language from others
  - Tooltip on hover → Google Trends time series + related query word cloud
- **Annotation options:** Hover tooltip with annotated trend line (using d3-annotation.js) and word cloud; hand-lettered section headers for visual personality.
- **Data types suited for:** Categorical (words, languages), ordinal (rank), temporal (trend over time in tooltip).
- **Interesting feature extraction/manipulation:** Word frequencies from multiple source terms were aggregated to a single English translation target before ranking. NLP tagging (R with NLP/OpenNLP packages) was used to filter only nouns and adjectives.

---

### Language Similarity Network (p.289–296)
- **What it shows:** Each of 10 languages is a circle node. A line connects two languages if they share a word in common within their respective top 10 most-translated words. Multiple shared words = multiple lines, each progressively more curved to avoid overlap.
- **When to use / avoid:** Use for showing pairwise similarity or shared membership between a modest number of nodes. Avoid when nodes are numerous (>15–20) — the network becomes a hairball. Avoid when replacing link lines with text labels — this was tried and caused chaos.
- **Interesting properties:** Multiple links between two nodes use progressively increasing curvature rather than thicker lines — because the lines were eventually meant to carry text. Clicking a language circle moves it to the center and animates all its connected links; hovering highlights all lines attached to that language. Interestingly, Spanish, Portuguese, and Italian formed the highest-similarity cluster; Russian and Polish also clustered.
- **Marks:** Circles (language nodes), curved lines (shared-word links), single English word label centered on each link.
- **Channels:**
  - Number of lines between two nodes → degree of lexical overlap (shared vocabulary in top 10)
  - Line curvature → disambiguation of multiple links between the same pair
  - Node position → click/animate to center for detail view
  - Color/highlight on hover → focus on one language's connections
- **Annotation options:** English translation word as text label on each link line; language names on the circle nodes; circular layout on desktop, rectangular on mobile.
- **Data types suited for:** Relational (shared vocabulary), categorical (languages, words).
- **Interesting feature extraction/manipulation:** The "shared word" link was computed from top-10 ranked lists per language — a join operation on ranked word tables. Only the English translation (not the original-language word) was used as the link label, keeping the visual minimal.

---

### Google Trends Travel Map + Time Breakdown (p.298–300)
- **What it shows:** For a selected "target" country (e.g., Brazil), which "source" countries searched for it most, shown on a world map by volume of search interest. A second view breaks down search interest per year since 2004. Topics (cities, landmarks, people) further detail what aspects of the country were searched.
- **When to use / avoid:** Use when geographic distribution of interest/behavior is the primary question. The choropleth/dot map gives immediate spatial intuition. Pair with a time view when temporal change matters.
- **Interesting properties:** The data was gathered in reverse — starting from "target" countries and working back to find "source" countries — because of how Google Trends' API works. Categories for topics were built from 252 Google Knowledge Graph "types" collapsed to 8 meaningful categories (city, region, attraction, nature, person, history, arts, other).
- **Marks:** Geographic regions/countries (choropleth or sized symbols on map); topic marks (dots or icons by category).
- **Channels:**
  - Geographic position → source country location
  - Color saturation / size → search interest volume
  - Color hue → topic category (city / nature / person / etc.)
- **Annotation options:** Topic names as labels; year-by-year time series for drill-down; Google-defined topic images in detail view.
- **Data types suited for:** Spatial (countries), temporal (yearly since 2004), categorical (topic categories), quantitative (search interest score 0–100).
- **Interesting feature extraction/manipulation:** Relative popularity scores (Google Trends outputs 0–100, not absolute counts) were used — important caveat for comparisons. Eight summary categories were manually derived from 252 Knowledge Graph types, with automated mapping for ~95% and manual assignment for the remaining 45.
