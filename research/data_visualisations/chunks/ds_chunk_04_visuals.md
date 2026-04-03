# [agent_09] Data Sketches — pages 151-200

## Pages covered
- pp. 151–168: "Magic is Everywhere" (Nadieh) — fantasy book title visualization
- pp. 169–188: "Every Line in Hamilton" (Shirley) — musical lyrics interactive visualization
- pp. 189–200: "The Top 2000 — the 70s & 80s" (Nadieh) — Dutch music chart beeswarm poster

---

### Word Cloud (p. 153–154)
- **What it shows:** Frequency of words (or word categories) in a text corpus — here, 862 fantasy book titles after stop-word removal.
- **When to use / avoid:** Use for quick exploratory overview of which terms dominate a text corpus. Avoid when precise frequency comparison is needed (size perception of irregular shapes is inaccurate). Best as an *exploratory* step, not a final presentation.
- **Interesting properties:** Word size scales with frequency. Position and angle carry no meaning. Useful as a first-pass check before building a more precise visualization.
- **Marks:** Text labels (words as marks).
- **Channels:** Size (font size) encodes frequency; color can be added for categories. Position is arbitrary.
- **Annotation options:** None standard — the words themselves are the labels.
- **Data types suited for:** Textual / categorical (word frequencies).
- **Interesting feature extraction/manipulation:** Prior text cleaning (removing stop words, digits, punctuation) is required. Hypernym-mapping (replacing "wizard" with "magic," "forest" with "location") is an interesting semantic generalization step that makes the word cloud thematically meaningful rather than literally noisy.

---

### tSNE Scatter Map with Labeled Hotspot Regions (p. 155–158)
- **What it shows:** A 2D layout of 862 fantasy books where similar titles cluster together, based on tSNE dimensionality reduction on a Document Term Matrix. Overlaid ovals (manually drawn) mark thematic hotspot regions.
- **When to use / avoid:** Use when you want to explore clustering and similarity structure in high-dimensional text/feature data. Avoid when exact positions need to be interpretable (tSNE positions are relative, not absolute). Ovals/blobs are appropriate only when hotspot membership is approximate.
- **Interesting properties:** tSNE was chosen over K-means and PCA because its visual output showed the clearest separation. The hotspot ovals were drawn manually in Adobe Illustrator over the tSNE output — a hybrid algorithmic + manual design process. Blurring the ovals with SVG blur filters makes them blend smoothly into a colored landscape that serves as a background rather than a foreground element.
- **Marks:** Points (book circles); filled blob-ovals for thematic regions; text labels for regions.
- **Channels:** Position (tSNE-derived x/y) encodes textual similarity; color of background ovals encodes theme category; blur encodes the gradient/fuzzy nature of the theme regions.
- **Annotation options:** Region labels (theme names: "magic," "blood," "time," etc.) placed at their average position across all books containing that term.
- **Data types suited for:** High-dimensional categorical/textual data collapsed to 2D for layout.
- **Interesting feature extraction/manipulation:** Converting text into a Document Term Matrix → running tSNE → taking the output x/y as "visual variables" baked into the dataset. Also computing the "average position" of books per theme to place region labels.

---

### Custom Circular Title Glyph (p. 156–160)
- **What it shows:** Encodes an individual book's title as a custom mark: a central circle (the book) surrounded by 26 small dots evenly distributed around it (one per letter of the alphabet), with dots placed at the position of each letter in the title, and curved SVG arcs connecting the letters of each word.
- **When to use / avoid:** Use when marks need to simultaneously encode an item's identity (title) visually without text labels crowding the chart. Best suited for an interactive or large-format poster where small details can be seen. Avoid for dense displays where marks are too small to read the arcs.
- **Interesting properties:** The glyph is entirely derived from the item's own textual content — the shape of each book mark is unique and literally "spells out" its title. This is a semantic novelty: a scatter-plot mark that is also a data encoding in its own right. The arcs "swoosh" to give an organic, flowing feel.
- **Marks:** Central circle (the book); small peripheral dots (letter positions); curved arcs (words connecting their constituent letters).
- **Channels:** Central circle size encodes number of Goodreads ratings; arc/line thickness connecting books encodes author's Amazon rank; color of circle + connecting paths encodes author identity (five highlighted authors); position encodes thematic similarity via tSNE.
- **Annotation options:** Hover interaction highlights all books by the same author. Animated legend explains how to "read" a glyph. Book title text label placed near the circle.
- **Data types suited for:** Text (title) encoded as a visual shape; quantitative (ratings, rank); categorical (author).
- **Interesting feature extraction/manipulation:** TSP (Traveling Salesman Problem) used to determine the optimal order in which to connect an author's books by the shortest total path length — a combinatorial optimization turned into a visual design decision.

---

### Scrollytelling Dot Stream with Force Simulation (p. 177–183)
- **What it shows:** Each dot represents a set of consecutive lyrics in Hamilton sung by the same character. On scroll, the dots animate (explode out, dance, re-assemble) to guide the reader through the narrative.
- **When to use / avoid:** Use for narrative-driven data essays where you want to control pacing and guide the viewer through a sequence of analytical steps. Avoid for analytical tools where the user needs stable reference — animation can disorient.
- **Interesting properties:** The force simulation (D3.js force module) positions dots dynamically on scroll, transitioning between layouts. Delight-focused animation (dots dancing) is explicitly non-informational but increases engagement. A progress bar animates in sync with audio playback when the reader clicks a lyric.
- **Marks:** Dots (each = a set of consecutive lyric lines by one character).
- **Channels:** Dot size encodes number of lines represented; color encodes character identity; position changes by scroll event to support the narrative.
- **Annotation options:** Hover shows singer name + lyrics. Lyric text in the article is clickable → plays corresponding audio + shows progress bar. Songs are highlighted and faded on/off as the story references them.
- **Data types suited for:** Temporal/sequential (lyrics in order), categorical (character), quantitative (line count).
- **Interesting feature extraction/manipulation:** Aggregating individual lines into runs of consecutive same-character lines was the key abstraction that made the visualization manageable. Without this, ~1,700 individual dots were uninterpretable.

---

### Interactive Lyrics Filter Tool (p. 173–176, 183–184)
- **What it shows:** All songs of Hamilton laid out as rows of dots (character sets), with a multi-category filter panel allowing the user to filter by characters, character conversations, and recurring phrases simultaneously.
- **When to use / avoid:** Use when the dataset is a rich structured collection and users need to perform their own exploratory analysis. Requires complex filter logic design to avoid dead-ends. Avoid if the user population is non-technical or if the exploration space is too large without guidance.
- **Interesting properties:** Filter logic uses AND within characters (to narrow down) but OR within conversations/phrases (to expand matches). Dead-end prevention: options that would cause zero results are disabled. Four visual states per filter item: selected / partially-highlighted / present-but-unrelated / absent (dotted outline). This visual state system is a careful UX design for filter tools.
- **Marks:** Horizontal bars (each bar = a set of consecutive lyric lines); musical notation arcs over bars (recurring phrases); diamonds (earlier iteration, replaced).
- **Channels:** Bar width/length encodes number of lines in the set; color encodes character; arc + shorthand label encodes recurring phrase (domain-appropriate metaphor: musical notation symbols).
- **Annotation options:** Hover on dot shows singer + lyrics. Selected filters highlighted in color at full opacity. Unselected-but-relevant items shown in partial opacity.
- **Data types suited for:** Sequential + categorical (lyrics, characters, recurring phrases).
- **Interesting feature extraction/manipulation:** The decision to use musical notation arcs (domain metaphor) instead of color for recurring phrases elegantly solved the dual-encoding problem — when color is already used for characters, borrowing a symbol system from the domain avoids channel conflict.

---

### Beeswarm Plot (p. 193–199)
- **What it shows:** 2,000 songs from the Dutch Top 2000 chart arranged along a horizontal time axis (year of release, 1950s–2016), with circles clustered around their release year using a force simulation that prevents overlap. Shows which decade dominates the list.
- **When to use / avoid:** Use when you have many items with a continuous x-axis variable and want to show density/distribution while still being able to identify individual items. Better than a histogram when you want to preserve individual item identity. Avoid when item count is so high that individual items become invisible (though force simulation helps by spreading items vertically).
- **Interesting properties:** The beeswarm was rotated 25 degrees in Adobe Illustrator purely for aesthetic effect — a reminder that non-data-encoding stylistic choices can improve visual appeal. Top 10 songs were rendered as tiny vinyl records (red circle + small white circle on top) — a thematic mark that makes the top items stand out while fitting the musical domain. Chart was deliberately kept black-and-white (vinyl record aesthetic) with red accents matching the Top 2000 logo.
- **Marks:** Circles (songs); colored outer rings for notable songs; vinyl record marks for top 10.
- **Channels:** Position x-axis = year of release; circle size = Top 2000 ranking (bigger = higher ranked); color/stroke = categorical labels (David Bowie: yellow; Prince: purple; artist with most songs: blue; notable songs: red); grey = songs absent from Top 40 (missing data convention).
- **Annotation options:** Notable songs annotated with text labels; artist names; interesting facts. Hover tooltip shows song title and artist in the interactive version.
- **Data types suited for:** Quantitative (year, ranking), categorical (artist, presence/absence in Top 40), temporal (release year as x-axis).
- **Interesting feature extraction/manipulation:** Two-source data matching (Top 2000 Excel + Top 40 scrape) using exact match → partial match → fuzzy Levenshtein distance → manual correction. The matching itself is the primary data manipulation challenge. Key insight: assign circle size to the *primary* variable (Top 2000 rank), not a secondary one — so the biggest/most visible marks correspond to the most important data points.

---

### Small Multiple Histograms with Smoothed Density Overlay (p. 200)
- **What it shows:** Distribution of song release years across four historical editions of the Top 2000 (1999, ~2005, ~2012, 2016), displayed as four small panels side by side to show how the distribution has shifted from older decades (dominated by 70s songs in 1999) toward more recent decades over time.
- **When to use / avoid:** Use when comparing how the shape of a distribution changes across discrete panels (time points, groups). Overlaying a smoothed density curve on top of the histogram helps compare overall shape at a glance rather than requiring exact bar-height comparison.
- **When to avoid:** Don't use color to encode a second variable in small multiples if it conflicts with the purpose — in this case, the color-by-height experiment was abandoned in favor of uniform grey to avoid drawing attention away from the main visualization.
- **Interesting properties:** The smoothed density curve (ggplot2) layered over the histogram provides shape comparison affordance that raw histograms alone do not. All four panels made the same color (grey) to reduce visual competition with the main beeswarm.
- **Marks:** Bars (histogram bins); smooth curve (density estimate).
- **Channels:** Position x = release year; height = count of songs in that year bin; curve shape = smoothed distribution; small multiples panel = edition year.
- **Annotation options:** Panel labels for edition year. Minimal — the point is the shape change across panels.
- **Data types suited for:** Quantitative (year, count), temporal (edition year as panel variable).
- **Interesting feature extraction/manipulation:** Appending 18 years of Top 2000 history data to compare across editions. Smoothing (kernel density estimate) is the key manipulation that makes shape comparison easy.
