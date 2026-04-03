# [agent_06] Data Sketches — pages 1-50

## About This Book

Data Sketches (Nadieh Bremer & Shirley Wu, 2021) is a practitioner's book documenting 24 data visualization projects across 12 thematic topics. Each project is written up as a first-person account covering data gathering, sketching, coding, and reflections. Pages 1-50 cover the introduction, foreword, tech/tools overview, and the first two projects (LotR chord diagram and Film Flowers).

---

## Goal and Function of Visuals

- Visuals serve to explore curiosities about the world, find stories buried in data, and share them in a beautiful way that excites people (p.15)
- The most successful projects turn spreadsheets full of numbers into visualizations that "entice people to dive in, explore, and learn all that it has to reveal" (p.15)
- Visualization is not one fixed orthodoxy — purpose matters. For exploratory analysis, standard forms and clarity first; for expressive/artistic pieces, uniqueness and experimentation are valid (p.13-14)
- There is no single "right" answer: "many possible answers — each of them beautiful, provocative, and shaped by the unique lens of its creator" (p.4)
- Reflecting on purpose before designing (or critiquing) is paramount (p.14)

---

## Marks and Channels

Explicit definition given in the "Film Flowers" project sidebar (p.48):

- **Marks** are geometries: lines, ticks, circles, bars — and even flowers, custom glyphs
- **Channels** define the appearance of marks: positions, sizes, colors, shapes
- **Mapping rules:**
  - Quantitative attributes → positions (x, y, angle), sizes (width, height, radius), continuous color scales
  - Categorical attributes → shapes and discrete colors
- An unorthodox but valid mapping: quantitative data (number of IMDb votes) → number of petals (a count-based mark property) (p.48)
- Marks and channels provide a framework that helps make unorthodox encodings more understandable to end users (p.48)

---

## Task-Encoding Fit

- Use position (x, y, angle) for the most important quantitative variables — they are the most accurately read channel (p.48)
- Size/radius works for continuous quantitative comparisons (movie rating → flower petal radius) (p.50)
- Shape works for categorical identity (parental guidance rating → distinct petal shape — 4 shapes for 4 ratings) (p.50)
- Color hue works for categorical distinctions (movie genre → discrete color) (p.49-50)
- Count/number of repeating elements (number of petals) can encode a quantitative variable when creative context allows it (p.48-49)

---

## Data Manipulation

- **Filtering**: Focus a large dataset on a meaningful subset before visualizing (e.g., filtering LotR characters down to the 9 Fellowship members for structural clarity) (p.31)
- **Aggregation**: Summarize raw scene-level word counts to character-location totals — this is what gets visualized, not individual scenes (p.31)
- **Manual variable addition**: Key variables not present in source data can and should be added manually. LotR: location variable was not in the dataset; manually added from scripts and memory, covering ~90% of rows. Do not be limited to data already in CSV form (p.31, p.32 sidebar)
- **Discretization**: d3.scaleQuantize() converts continuous numerical input (IMDb vote count) to a discrete output (number of petals: 5-15). Useful for mapping a quantitative value to a mark property that only takes whole numbers (p.50)
- **Continuous linear mapping**: d3.scaleLinear() maps continuous numerical input to continuous output (movie rating → petal size) (p.50)
- **Simple exploratory plots**: Before building the final visual, create basic plots to get a grip on data values — quick bar charts, etc. (p.22, R section)

---

## Design Process Guidance

- Start with exploring what datasets exist, then find personal connection to narrow focus (p.30, p.46)
- **Sketch multiple alternatives** before committing: For LotR, Nadieh produced at least 3 ideas: chord/string layout, timeline with circles, spirograph abstraction (p.33)
- Sketch tools: paper/pen, iPad + Apple Pencil + Tayasui Sketches or Paper app. Key: choose a tool that keeps you focused on the idea without getting lost in fine-tuning settings (p.22-23)
- **Don't plan all steps at once** — focus on the most fundamental change at each point, make it work, then think about the next step. This keeps the process flexible (p.34 sidebar)
- **Start from existing code/examples** closest to your design, then adapt; rarely start from scratch (p.39, "Remix What's Out There")
- Find the core "hardest step" first. If that step is impossible, change the design before over-investing (p.34)
- Iterate visual tweaks: colors, spacing, curves — each iteration surfaces the next problem (p.36-38)
- Use static analysis tools (R, Vega-Lite, Observable) to explore data before building the final visual (p.22, p.24)

---

## Interaction Design

- Hover to reveal detail: hovering over a character's name shows only their strings, fades out locations with no spoken lines, updates outer word counts to only theirs (p.38, p.43)
- Hover to highlight connections: hovering a location shows all Fellowship members who spoke there (p.43)
- Hover to surface textual insights: hovering a character shows a paragraph of interesting data-driven insight about them — turn patterns in data into prose stories for the user (p.38, p.44)
- Fade-out / dimming strategy: when a user selects one item, completely fade out all unrelated elements rather than removing them, so context is preserved (suggestion from Shirley, adopted by Nadieh) (p.38)
- Interaction is added at the end of the project, after the core visual is complete (p.38)

---

## Common Mistakes and Anti-Patterns

- Not enough space in the center of a circular layout → visual feels "squished" — fix by separating the two halves to create white space (p.37-38)
- Sticking only to data already in CSV form limits interesting topics — collect, scrape, and manually augment data when necessary (p.32 sidebar)
- Choosing a visually exciting idea (fireworks) over a cleaner implementable one (flowers) without assessing technical feasibility early (p.48)
- Letting aesthetic obsession slow sketching: use a tool with *limited* options so you stay focused on communicating the concept (p.23)
- Don't start full implementation before testing the most fundamental/risky design step (p.34)

---

## Practical Rules of Thumb

- Map quantitative → positions/sizes/continuous colors; map categorical → shapes/discrete colors (p.48)
- When a new variable is needed but absent from source data, manually add it — a few hours of effort can dramatically improve the story (p.31-32)
- Always try multiple sketch ideas before committing; the first idea is rarely the best (p.33)
- Use exploratory quick plots (bar charts in R, Vega-Lite notebooks) before investing in the final visual (p.22, p.24)
- Add interactivity at the end, once the static visual is solid — don't build interaction into the early prototype (p.38)
- When adapting an existing chart type (chord diagram → Loom+Strings), isolate the one hardest transformation and prove it works before continuing (p.34)
- Color-pick directly from domain imagery (movie stills) to create a palette that feels semantically connected to the data (p.37)
- When encoding with shapes, restrict to ~4 distinct shapes maximum (4 parental guidance ratings → 4 petal shapes) (p.50)

---

## On Orthodoxy vs. Eccentricity in Dataviz (Foreword, Alberto Cairo, p.13-14)

- The orthodox tradition (Bertin, Tukey, Cleveland, Munzner) favors clarity, simplicity, standard forms — still valid when the goal is exploration, insight, or decision support
- An emerging counter-orthodoxy: uniqueness is paramount, templates and conventions are viewed with skepticism
- Visualization can't be taught as rigid rules, but as *principled reasoning* about how to make decisions about what to show and how to show it
- Knowledge of vision science, cognitive science, rhetoric, graphic design should be a foundation that opens up possibilities, not a straitjacket
- Design decisions should be justified on ethics, aesthetics, and empirical evidence — then conversation determines if novelties succeed and become convention
