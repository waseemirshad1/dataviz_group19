# [agent_10] Data Sketches — pages 201-250

## Coverage
Pages 201–250 cover three projects: the DDR (Dance Dance Revolution) spiral visualization (Shirley, music theme), the Dragon Ball Z fights network (Nadieh, nostalgia theme), and the Harry Potter fanfiction project (Shirley, nostalgia theme). The final page introduces the "Nature" theme (Marble Butterflies). These are primarily process narratives; the visual types described below are inferred from the text descriptions and figure captions.

---

### Spiral Step-Chart (per song) (p.209–211)

- **What it shows:** The sequence of dance steps in a DDR song (Dance Dance Revolution), where each step is a dot placed equidistantly along an Archimedean spiral. Each dot represents one beat/step event.
- **When to use:** When you want a compact, continuous, circular representation of a sequential event sequence — especially when comparing many sequences side by side. Avoid when within-sequence pattern recognition is the primary goal (spirals make it hard to see repeating patterns vs. a linear layout).
- **Interesting properties:** The spiral is "continuous" — unlike a multi-row layout, it never breaks the sequence. Compact enough to show 645 songs on one page. Varying arc length between dots would be uneven in a naive implementation; equidistant placement requires a brute-force iterative algorithm.
- **Marks:** Filled circles (dots), one per step event.
- **Channels:** 
  - Position along spiral = temporal sequence (beat order in the song)
  - Color hue = arrow direction (left=orange, up=red, right=green, down=blue)
  - Circle radius = difficulty level (higher difficulty → smaller circle — a deliberate pun: harder to see at higher difficulty)
  - Spiral size (total radius) = song length (longer songs → larger spiral)
- **Annotation options:** Color legend for arrow directions and sizes; expand button for detail view; filter by arrow direction and difficulty.
- **Data types suited for:** Temporal/sequential (event sequences), categorical (arrow directions, difficulty levels).
- **Interesting feature extraction/manipulation:** Mapping the six difficulty/mode combinations (single-basic, single-trick, single-maniac, double-basic, double-trick, double-maniac) on top of each other using an overlay blend mode — allows simultaneous view of all levels, though blend mode corrupts color encoding accuracy.

---

### Dot Histogram / Stacked Dot Timeline (p.236–237)

- **What it shows:** Volume of fanfiction stories published per month over a multi-year period, where each dot represents up to 100 stories. Dots are stacked vertically for each month, creating a histogram silhouette. The color of each dot encodes the average number of reviews (popularity) for the stories within that dot.
- **When to use:** When you have a large number of items (tens of thousands) you want to show as a volume-over-time distribution, while also encoding a secondary continuous variable (like average quality or rating) per bin. Avoid when you need to show individual items (too many), or when precise reading of the secondary variable matters (color is hard to read precisely).
- **Interesting properties:** Combines a histogram (frequency distribution over time) with a color-encoded heatmap layer. The stacking makes the "height" of the histogram visible as dot count. The color gradient (deep blue → magenta → orange → yellow on a navy background) distinguishes between high-review and low-review periods visually.
- **Marks:** Circles (dots), binned.
- **Channels:**
  - x-position = publication month/year (temporal)
  - y-position (stacking height) = count of stories in that month bin
  - Color hue + saturation/brightness = average number of reviews (continuous, sequential color scale)
- **Annotation options:** Book and film release dates marked as separate circles on the timeline (filled = book, outlined = film); GIFs/images for qualitative context at notable spikes.
- **Data types suited for:** Temporal, quantitative (counts + averages), event markers.
- **Interesting feature extraction/manipulation:** Aggregating 80,000 stories into bins of 100 before plotting — essential for making the large dataset tractable. The color then re-introduces per-bin detail (average quality) without individual-level clutter.

---

### Stacked Area Chart / Step Area Chart (p.239–240)

- **What it shows:** Volume of fanfiction stories per pairing per month, stacked on top of each other to show relative share of each pairing over time. Each area is colored by the average number of reviews (popularity).
- **When to use:** For comparing multiple time series that share a common baseline, where you care more about the total volume and relative shares than the exact values. Avoid for more than 5–6 categories (areas blend together). Step-curve variant (d3.curveStep) works best when adjacent areas are hard to distinguish.
- **Interesting properties:** The step-curve style creates clean rectangular steps instead of smooth curves — makes boundaries between adjacent areas more distinct. Color encodes a second variable (average reviews) on top of the area shape, creating a heat-map-within-area effect. Used to compare canon vs. non-canon pairings (pink vs. purple gradient palettes).
- **Marks:** Filled areas.
- **Channels:**
  - x-position = time (month/year)
  - y-position (area height) = count of stories
  - Color hue + gradient = average number of reviews (popularity), with pink for canon, purple for non-canon
- **Annotation options:** Hover interaction reveals titles, authors, and review counts for individual blocks of stories. Legend maps color gradient to review count.
- **Data types suited for:** Temporal, quantitative, categorical (pairing type).
- **Interesting feature extraction/manipulation:** Converting raw story counts into color-coded blocks (each "block" = a set of 100 stories stacked for a given month) — the block color is the average review count within those 100 stories.

---

### Character Relationship Network Graph (as navigation) (p.241)

- **What it shows:** Characters linked to their romantic pairings — a node-link graph where nodes are characters and edges indicate a pairing relationship exists.
- **When to use:** When you need to show many-to-many relationships between entities and allow the user to select a focal entity to drive another visualization. Unusual use: doubles as interactive navigation rather than just a static display.
- **Interesting properties:** The graph serves dual purpose — it shows relationship structure AND acts as a click-to-filter navigation element. Clicking a character node switches the main timeline visualization to center on that character. This is a strong example of using a structural visualization as a UI control.
- **Marks:** Nodes (circles or illustrated character icons), edges (lines).
- **Channels:** Node identity = character (illustrated icon); edge presence = pairing exists; possibly size or label for popularity.
- **Annotation options:** Character illustrations (custom icons by Catherine Madden) replace plain circles, adding aesthetic and identity signal.
- **Data types suited for:** Relational, categorical.
- **Interesting feature extraction/manipulation:** Defaulting the selection to the most-connected node (Hermione, with the most pairings) — an implicit ranking that guides the user's first exploration.

---

### Fight Sequence Network / Parallel Timeline with Bezier Connectors (p.219–226)

- **What it shows:** All fights in Dragon Ball Z across all sagas. Each fight is a cluster of overlapping circles (one circle per fighter). Fights are arranged vertically in chronological order within each saga column. Characters are connected across consecutive fights they appear in by SVG Bézier curves of varying thickness — creating a "flow" of each character through the story.
- **When to use:** When you want to show how individual entities (characters) move through a sequence of events, and how those events cluster. Effective for narrative data where temporal order and group membership per event both matter. Avoid when the number of entities or events is so large that the connecting lines become an indistinguishable mass.
- **Interesting properties:**
  - Lines vary in thickness (thin at fight circles, broad at the bend between fights) — achieved by creating a closed SVG path (going down one side and back up the other with slightly different Bézier parameters) rather than a simple stroke.
  - Swoosh direction encodes alignment: good guys' lines swoosh left, bad guys' right — spatial encoding of a binary categorical variable. This allows viewers to instantly identify allegiance shifts (e.g., Vegeta migrating from right to left over time).
  - Transformation levels (Super Saiyan etc.) encoded as concentric rings around fighter circles.
  - Animated GIFs embedded at key fights link to YouTube videos of the exact episode.
  - Mini-map panel shows the full visual at reduced scale with a viewport indicator for context during scrolling.
- **Marks:** Overlapping circles (fighters in a fight), closed Bézier path areas (character trajectories), concentric rings (transformation level), animated GIF thumbnails.
- **Channels:**
  - x-position = saga (story arc column)
  - y-position = fight order within saga (chronological)
  - Color hue = character identity
  - Number of concentric rings = transformation level
  - Line thickness profile = visual emphasis / dynamic quality (not a data variable, purely aesthetic)
  - Swoosh direction (left vs. right) = alignment (good/bad)
- **Annotation options:** Hover expands the fight cluster with a tooltip naming characters and fight details. Manual annotations on key fights. Animated GIFs linked to episode timestamps.
- **Data types suited for:** Sequential/temporal, relational (who fought whom), categorical (good/bad, transformation), hierarchical (saga > fight > fighter).
- **Interesting feature extraction/manipulation:** Manually extracting fight data from a wiki into Excel, then reshaping from one-row-per-fight to one-row-per-character-per-fight in R — a reshape operation essential for the visual structure.

---

### Genre Timeline (Small Multiple Timelines per Pairing) (p.239–241)

- **What it shows:** For each character pairing (e.g., Hermione/Draco, Hermione/Ron), a set of small timeline strips — one per genre — stacked vertically and aligned to a shared time axis. Each strip shows the volume of stories in that genre over time, colored by average popularity.
- **When to use:** When you want to show how multiple categories (genres) evolve over time for multiple groups (pairings), and compare the genre profiles between groups. Works well for a moderate number of categories (5–8 genres) and groups.
- **Interesting properties:** The small-multiple structure allows side-by-side genre comparison across pairings. Aligned x-axis (time) allows spotting synchronous events (e.g., book/film releases driving genre spikes).
- **Marks:** Filled step-curve area blocks.
- **Channels:** x = time; y = story count; color = average reviews (popularity gradient).
- **Annotation options:** Hover reveals individual story titles and authors within a block.
- **Data types suited for:** Temporal, categorical (genre, pairing), quantitative (counts, reviews).
- **Interesting feature extraction/manipulation:** Organizing genres qualitatively along a "dark/serious to light/fluffy" spectrum was attempted but abandoned — no principled quantification was possible, illustrating the limits of forcing ordinal encoding on subjective categories.
