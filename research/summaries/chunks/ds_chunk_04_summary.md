# [agent_09] Data Sketches — pages 151-200

## Pages covered
- pp. 151–168: "Magic is Everywhere" (Nadieh) — fantasy book title visualization
- pp. 169–188: "Every Line in Hamilton" (Shirley) — musical lyrics interactive visualization
- pp. 189–200: "The Top 2000 — the 70s & 80s" (Nadieh) — Dutch music chart beeswarm poster

---

## Data Sources and Collection

- **Scraping as a legitimate data source** (p. 153): When no structured dataset exists, scraping (web) combined with APIs is a valid strategy. Amazon's author list + Goodreads API were combined to build a dataset of 862 fantasy book titles.
- **Combining multiple imperfect data sources** (p. 193): Top 2000 Excel file + 50 years of Top 40 chart scraping required multi-step matching: exact match (~60%), partial match (~10%), fuzzy Levenshtein distance (~2.5%), then manual checking.
- **Manual data entry as a valid last resort** (p. 171): Hamilton's lyrics metadata (characters, conversations, recurring phrases) were manually entered because automated approaches were too slow or inaccurate. Two days of manual work beat algorithmic complexity in this case.

---

## Data Manipulation

- **Text cleaning pipeline** (p. 153–154): Removing digits, punctuation, stop words; word count; word cloud exploration as a first exploratory step.
- **Semantic generalization / manual hypernym mapping** (p. 154): Replacing ~800 unique title words with ~10–15 general categories ("magic," "name," "location," etc.) to make clustering meaningful. Automated hypernyms failed; manual mapping worked. Key lesson: automated routes don't always win.
- **Dimensionality reduction for layout** (p. 155): Compared K-means, PCA, and tSNE on the book title matrix. tSNE gave the most visually insightful separation — spread + clear clusters.
- **Shortest path for connecting related items** (p. 155): Used the Traveling Salesman Problem (TSP package in R) to order books by the same author so connecting lines have minimum total length.
- **Precalculating visual variables** (p. 162): Computed x/y pixel positions, clustering order, and author-path order *before* rendering. This avoids making each user's browser recompute the same invariant layouts.
- **Granularity decision** (p. 171): Started encoding every individual lyric line as a dot; realized it was too many (~1,700+ dots). Switched to encoding *sets of consecutive lines sung by the same character* — the right level of abstraction for the task.

---

## Design Process Guidance

- **Iterative tool exploration** (p. 155): Trying multiple clustering algorithms (K-means, PCA, tSNE) and visually inspecting results is part of the design process — not just data analysis. Choose the algorithm whose *visual output* best serves the goal.
- **Manual fine-tuning as a design step** (p. 161): After algorithmic placement, Nadieh dragged ~850 book circles one by one to reduce label overlap. Saved positions in `localStorage` so the layout persisted across browser refreshes. Manual intervention is not a failure — it is a valid finishing step.
- **Hybrid toolchain** (p. 201): R for data exploration and simple plots → D3.js for interactive/web rendering → Adobe Illustrator for annotation and print finalization. No single tool is optimal for all stages.
- **Static vs. interactive trade-off** (p. 201): Static visuals require far less engineering (no browser bugs, no responsive design, no performance tuning). For time-constrained projects, print/static may be better.
- **Story-led writing** (p. 179–180): Shirley found that writing about her personal emotional connection to Hamilton (rather than just reciting numbers) made the piece far more resonant and well-received.
- **Taking a break to reset** (p. 179): A deliberate break between projects helped Shirley solve a creative problem she'd been stuck on. Cognitive rest is part of the design process.

---

## Interaction Design

- **Filter logic design** (p. 175): For the Hamilton tool, filtering used different Boolean logic per category:
  - Characters: AND (every selected character must appear)
  - Conversations + Phrases: OR (any selected item qualifies)
  - Between categories: AND
  - Rationale: AND for frequent items (to narrow results) and OR for rare items (to avoid empty states).
- **Dead-end prevention** (p. 176): When a filter combination would lead to zero results, *disable* the options that cause it rather than showing an empty state. Four UI states per item: selected / highlighted-but-not-selected / in-song-but-not-highlighted / absent (dotted outline).
- **Scroll-triggered animation for delight** (p. 177): Dots "exploding out" and re-assembling on scroll added no information but increased engagement and kept readers scrolling. Lesson: delight can justify cost.
- **Hover highlighting** (p. 164, 167): Hovering a book highlights all books by the same author — a lightweight interaction that transforms a static scatter into an exploration tool without adding visual clutter by default.
- **Linked text + audio** (p. 187): In the Hamilton piece, clicking on lyric text in the narrative actually played the corresponding portion of the song and animated a progress bar. This cross-modal interaction deepened engagement.

---

## Marks and Channels

- **Size encoding** (p. 159, 196–197): Circle area encodes a quantitative variable (book ratings count; Top 2000 ranking). Key insight from the Top 2000 project: the variable encoded in size should be the *primary* variable of interest, so that the largest circles are the most important items — not a secondary detail.
- **Line thickness as channel** (p. 159): Path thickness between books of the same author encodes the author's rank in the Amazon Top 100. Thicker = higher rank.
- **Color as categorical identifier** (p. 160, 197): Assigning distinct colors to five specific authors in "Magic is Everywhere"; using red/yellow/purple strokes to mark specific artists in the Top 2000 poster. Color hue for categorical identity.
- **Color stroke (outer ring)** (p. 197–198): A colored outer circle behind the main circle mimics an outside stroke in SVG (which cannot natively do outside strokes). This adds a categorical channel without occluding the circle area.
- **Shape as semantic metaphor** (p. 197): Top 10 songs in the Top 2000 were rendered as tiny vinyl records (small white circle on red circle). The shape carries thematic meaning beyond just marking top rank — it fits the musical domain.
- **Custom glyph as mark** (p. 156–160): Each book is represented by a custom circular glyph: a main circle with 26 positions around its edge (one per alphabet letter), small dots at each letter's position in the title, and curved arcs connecting letters of each word. The shape of the glyph encodes the book's title.
- **Symbol as categorical encoding** (p. 179): For recurring phrases in Hamilton, Shirley replaced color (already used for characters) with musical notation symbols (arcs and shorthand labels from sheet music). A domain-appropriate symbol set avoids channel conflict.

---

## Channel Rankings and Rules of Thumb

- **Don't overload visual channels** (p. 179): In the first Hamilton iteration, diamonds for recurring phrases were colored by theme AND color was already used for characters. This caused confusion. Never use the same channel for two different variables.
- **Assign primary importance to the most salient channel** (p. 196–197): In the Top 2000 beeswarm, initially circle size encoded Top 40 rank (a secondary variable) and color encoded Top 2000 rank (the primary variable). Switching them — size for Top 2000, color for Top 40 — immediately improved clarity because the largest circles became the most important songs.
- **Use remaining free channels for context, not noise** (p. 194–195): After the main encoding is set, audit which channels are still available and use them to add context rather than leaving them empty. "Think about which visual channels are still free."
- **Grey for missing data** (p. 197): Songs that never appeared in the Top 40 were encoded in light grey. Grey is a culturally understood signal for absent/null values and avoids the missing data looking like a category.

---

## Common Mistakes and Anti-Patterns

- **Too many individual data items without abstraction** (p. 171): Rendering every lyric line as a dot (~1,700+) created unmanageable visual noise. Solution: aggregate into sets of consecutive lines.
- **Encoding secondary variable in size while primary variable gets color** (p. 196–197): Made the visual harder to read because the most visible marks (large circles) didn't correspond to the most important data points.
- **Cluttered marks from too much visual complexity** (p. 160): Book glyph arcs "were getting much too big, obscuring titles and other books." The solution was to reduce arc size — each decorative element must be tuned so it doesn't interfere with legibility.
- **Over-ambitious filters causing empty states** (p. 175–176): Without dead-end prevention, overly specific filter combinations left the user with no data — a frustrating experience. Design must account for edge cases.
- **SVG performance with many animated elements** (p. 181): At ~1,700 animated SVG path elements, performance degraded. Canvas is preferable for large animated datasets.

---

## Practical Rules of Thumb

- **Start with simple plots** (p. 153): Before committing to a complex visualization, do a word count, run a word cloud, make a quick scatter — these quick explorations reveal what's interesting.
- **Try multiple algorithms and choose by visual output** (p. 155): K-means, PCA, tSNE — don't pick an algorithm by theoretical reputation; pick the one whose output looks most insightful for your specific dataset.
- **Use smoothed density curves over histograms for shape comparison** (p. 200): When comparing distributions across small multiples, overlaying a smoothed density curve on a histogram makes the overall shape more comparable across panels.
- **Combine tools by their strengths** (p. 201): R for exploration/transformation, D3.js for interactive web rendering, Adobe Illustrator for static annotation — each tool at its best phase.
- **Rotate or tilt a chart for visual interest** (p. 199): Nadieh rotated the beeswarm 25 degrees in Illustrator purely for aesthetic effect. Non-data-encoding stylistic choices are acceptable when they don't mislead.
- **Delight is a legitimate design goal** (p. 177, 197): Subtle animated effects, thematic shapes (vinyl records), and playful touches increase engagement and keep viewers exploring, even if they add no information.
