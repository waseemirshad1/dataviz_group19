# [agent_07] Data Sketches — pages 51-100

## Overview of Content
Pages 51-100 cover three chapters: the tail end of "Movies" (Film Flowers, Shirley), the "Olympics" chapter (Olympic Feathers by Nadieh; Dive Fractals by Shirley), and the "Travel" chapter (My Life in Vacations by Nadieh). These pages are primarily process narratives — data gathering, sketching, coding — with embedded design lessons.

---

## Marks and Channels

- **Visual channels** explicitly defined (p.65): position, color, size, shape. The author advises to use "remaining visual channels" to add context after the main encoding is complete — but keep extras to a minimum.
- **D3 scales as the bridge between data and channels** (p.54): scales (scaleTime, scaleLinear, scaleOrdinal) map raw data domain → visual range. This is the code equivalent of the marks-and-channels framework.
- **Discrete categorical mapping** (p.53): `d3.scaleOrdinal()` maps a categorical variable (movie genre) to a color — correct channel for categorical identity.
- **Opacity as a secondary channel** (p.68): decreasing medal opacity helped the author debug layout — also a legitimate channel for de-emphasizing secondary items.

---

## Task-Encoding Fit

- **Sorted order encodes rank** (p.67): continents sorted from most to fewest medals won per edition. Sorting is a manipulation that encodes rank into position — most accurate channel for ordered comparisons.
- **Radial position encodes time** (p.65–67): distance from center = Olympic edition/year. Radial position is less precise than linear position but allows the circular metaphor (feathers) to work.
- **Arc length / angular width encodes count** (p.65): each medal occupies the same arc length regardless of sport size — a deliberate choice for consistency over proportionality.
- **Color encodes continent** (p.65): five Olympic colors mapped to five continents — categorical identity task, correct use of color hue.
- **Blur filter encodes uncertainty** (p.97): horizontal blur = uncertain start/end date; vertical blur = uncertain enjoyment level; both = both uncertainties. Novel and semantically apt use of a visual effect as a data channel.
- **Pattern texture encodes category within a rectangle** (p.97): different line patterns inside vacation blocks encode trip purpose (nature, culture, sun, snow). Texture used for categorical identity within small bounded areas.

---

## Design Process Guidance

### Sketch Before You Code
- "If you can't make your design work logically on paper, it's definitely not going to work on the computer with the actual data." (p.67)
- Sketching to a friend or colleague is a useful technique — the act of explaining reveals logical errors in your own design (p.65).
- Each sketch iteration should build on lessons from the previous version; expect multiple rounds (p.67).
- Sketching is also how you catch data-structure mismatches early: Nadieh discovered that 56 sports in one circle would make each medal only a few pixels wide — caught through calculation on paper (p.66).

### Diverge — Prototype — Converge
- Start with a metaphor or inspiring image (peacock tail, fractal lines), then map data to that metaphor (p.65, p.80).
- Prototype with dummy/partial data first, then verify with full dataset (p.69).
- Get the broad structure working first, then refine details. (p.71)

### Check Your Data
- "Checking the accuracy of your data is a standard practice...not the most fun activity, is a lesson we have to constantly relearn." (p.64)
- Strategies: check sums/counts/averages against common sense; compare against a second data source; use a proxy dataset to find gaps (p.64).
- Missing data is harder to find than wrong data — wrong data shows up as outliers in summary stats; missing data requires knowing what *should* be there (p.64).

### Add Context Incrementally
- After the main encoding is working, look for remaining unused channels to add secondary variables (p.65).
- Keep secondary encodings subtle; they should reward interested readers without cluttering the primary message.

### Precalculate Visual Variables
- For complex layouts, compute placement, rotation, offsets, and sizes as separate "visual variables" attached to the data — do this in the language you find easiest (R, Python), not necessarily in the rendering tool (D3) (p.69).
- Visual variables are distinct from data variables — they have no meaning in the original dataset, only in the layout.

---

## Interaction Design

- **Hover to reveal detail** (p.75): hovering a medal in Olympic Feathers shows event name, edition, winner, and whether it was a record. Key principle: interaction reveals detail without cluttering the main view.
- **Hover to highlight context** (p.75, p.98-100): hovering a year in Olympic Feathers highlights all events from that edition across all sports. In "My Life in Vacations," hovering a month highlights the same month across all years — manages the complexity of a non-aligned time axis.
- **Click to filter** (p.88): in Dive Fractals, clicking a round filters all team flows by that round — drill-down interaction.
- **Minimal interaction principle** (p.98): "I kept the interactions to a minimum, limiting it to help the viewer understand the most difficult aspect of the viz" — interaction should solve specific comprehension problems, not be added for its own sake.

---

## Data Manipulation

- **Aggregation to make data manageable** (p.63): from full medal list → only gold medals; only winning country for team events (not individual members). Simplification justified by the story being told.
- **Derived categorical variable** (p.63): mapping country NOC code → ISO code → continent. Creating a new categorical variable for encoding purposes.
- **Pre-filling empty data for live updates** (p.63): creating an empty 2016 dataset in advance so the visualization structure remains stable during live updates.
- **Squeezing the time axis** (p.94): compressing months with no vacation so vacation periods are more legible. A deliberate distortion of the time scale to serve the story — acceptable when explicitly acknowledged.
- **Flatten then re-nest** (p.79): data gathered flat (spreadsheet) should then be programmatically restructured into nested JSON for rendering — the gathering format and the rendering format need not be the same.

---

## Common Mistakes and Anti-Patterns

- **Overloading one visual form** (p.66): 56 sports in one circle would make each medal too small to see. Always calculate whether your chosen form can physically accommodate your data.
- **Using wrong angle units** (p.68): mixing degrees (CSS rotate) and radians (Math.cos/sin) causes catastrophic layout errors — a practical coding pitfall with visual consequences.
- **Nested JSON for data gathering** (p.79): manually writing nested JSON for data entry is error-prone; use flat structure + programmatic nesting instead.
- **Forgetting channel limits** (p.97): SVG elements can only have one gradient applied — use filters instead when multiple uncertainty encodings are needed on the same element.
- **Too little data density** (p.94): an initial design showed vacation periods as colored blocks in a full-year timeline — vacations occupy <10% of the year so 90% of the chart would be white. The solution was to compress empty time.

---

## Practical Rules of Thumb

- SVG is best for static or lightly interactive visualizations with a small number of elements; Canvas is best for large datasets, animation, or frequent updates (p.83-84).
- Use scales (D3 or equivalent) as the explicit link between data values and visual positions/sizes (p.54).
- Test your layout math before coding: "Even a medal in the outermost ring would barely be a few pixels wide" — discovered by calculation, not trial and error (p.66).
- The tool you render with is not necessarily the tool you compute layout in — use whichever language is easiest for the computation (p.69).
- Metaphor-driven design (feathers, fractals, flowers) works when there is a structural match between the metaphor's geometry and the data's structure. The mismatch causes problems (feather tips did not work with data structure — removed after feedback) (p.71).
- Annotations that explain *how to read* the visualization are essential for non-standard charts (p.71): "these types of annotations typically help to 'teach' your reader how to actually understand the visual."
- A personal dataset can produce a visualization that is less interesting to others but deeply meaningful to the creator — and that is a valid goal (p.98).
