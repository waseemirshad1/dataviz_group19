# [agent_10] Data Sketches — pages 201-250

## Coverage
Pages 201–250 span three chapters: the end of the "Music" theme (Dutch Top 2000 infographic by Nadieh; Dance Dance Revolution spiral visualization by Shirley), the "Nostalgia" theme (Dragon Ball Z fights network by Nadieh; Harry Potter fanfiction by Shirley), and the opening of the "Nature" theme (Marble Butterflies by Nadieh). These pages are predominantly process narrative and visual examples rather than systematic theory. Practical design and process lessons are embedded in reflection sections.

---

## Tool Strategy: Combine Tools for Best Results

- Use R (or Python) for data loading, cleaning, initial statistics, and simple exploratory plots. (p.201)
- Switch to D3.js / JavaScript for interactive, web-based final outputs when more creative control is needed. (p.201)
- Finish static visuals in Adobe Illustrator or other vector tools for legends, annotations, and final polish — things that are slow to add in code. (p.201)
- Key rule: **no single tool does everything best**. Learn multiple tools and understand each tool's strengths and weaknesses. (p.201)

---

## Static vs. Interactive Visuals

- Static visuals are faster to produce: no need to handle browser bugs, performance, responsive design, or interactivity. (p.201)
- Interactive visuals require significantly more engineering effort. Consider whether the interaction is truly necessary for the insight. (p.201)
- When performance is critical (many elements changing at once), prefer **canvas over SVG**. SVG is slow when many paths and circles change opacity simultaneously. (p.211, p.226)

---

## Compactness vs. Pattern Visibility Trade-off

- Spirals are compact and continuous — good for showing all beats of a song in one glance, and for comparing multiple songs. But compactness sacrifices within-item pattern visibility. (p.211)
- Rule of thumb: **compactness and pattern visibility are in tension**. Choosing one means sacrificing the other. Design explicitly for which matters more for your user task. (p.211)
- If compactness wins, consider an **expand/detail-on-demand interaction** to let the user zoom in on a single item. (p.211)

---

## Overlay Blend Modes as a Double-Edged Sword

- Overlay blend modes can create beautiful, glowing aesthetics. But they **change the perceived color of overlapping elements**, making it misleading if color encodes a meaningful variable. (p.211)
- Anti-pattern: using blend mode on top of color-encoded data — the blend corrupts the color channel. (p.211)

---

## Interaction Design Principles

- **Filter interaction**: adding a filter to select by a categorical variable (arrow direction, difficulty) can help users focus on subsets. But if the underlying data is too dense, the filter may not reveal patterns anyway. (p.211)
- **Expand / detail-on-demand**: a button or click to scale up a compact view — useful for both detail and for items cut off at the compact scale. (p.211)
- **Hover transition**: making a hovered item bigger and pushing neighboring items outward helps the user focus on one item at a time. Works best for datasets of moderate size. (p.226)
- **Mini-map / context panel**: for very long scrollable visuals, a persistent small-scale overview panel showing the viewer's current position in the whole is highly effective. Suggested by peer feedback during the DBZ project. (p.225)
- **Sidebar navigation / graph as navigation**: a character relationship graph that doubles as navigation for selecting which character's data to display — clicking a node switches the main visualization to center on that character. (p.241)

---

## Design Process Guidance

- **Start with a list of available metadata** before sketching. Write down all variables, then identify which ones might correlate with the main outcome you care about. (p.235)
- **Exploratory logging/statistics are useful but shallow**: logging min/max and medians gives a basic overview but won't surface deep insights. Simple exploratory plots are more effective than terminal statistics. (p.235)
- **Peer feedback as ideation catalyst**: the most interesting angle in the Harry Potter project (canon vs. non-canon) was spotted by a friend looking at an intermediate version of the visualization. Design reviews with others are high-value. (p.237)
- **Sketches can be abstract**: for the DBZ project, sketches were very basic — just abstract shapes on paper. The real design decisions happened during programming. This is valid; sketch to capture the structure, not the final aesthetic. (p.221)
- **Iterate incrementally in code**: build the simplest version first (straight lines, basic circles), then add complexity step by step (curves, varying thickness, randomness, color). (p.223)
- **Delight matters**: animated GIFs, illustrated character icons, careful annotation, and small interactive surprises increase engagement with complex visuals — but these should be additions, not the center. (p.220, p.227)

---

## Common Mistakes and Anti-Patterns

- **Too many elements on screen at once**: with 645 songs each visualized as a spiral, even a filter interaction could not surface patterns — the density was just too overwhelming. An overview page with simplified versions + drill-down on click would have helped. (p.211)
- **Monotony of chart type**: using only timelines for every section of a visualization creates visual monotony, even if the data within each timeline varies. Vary chart types across sections. (p.241)
- **Matrix redundancy**: a character-pairing matrix mirrors itself across the diagonal — redundant. If space is tight, consider only showing half the matrix or switching to a network graph. (p.236)
- **Overlapping area charts**: overlapping (non-stacked) area charts are hard to read at a glance; lines are thin and indistinct. Stacking improves clarity but minor categories still blend into others. The step-curve style (d3.curveStep) can help distinguish adjacent areas. (p.239)
- **Quantifying the unquantifiable**: attempting to place genres on a continuous dark-to-light spectrum was scrapped because there was no principled way to assign positions. Don't force a continuous encoding on an inherently subjective ordering. (p.239)

---

## Data Manipulation Worth Visualizing

- **Aggregation into bins**: grouping 80,000 fanfiction stories into bins of 100 stories each, then stacking those bins by publication month — creates a dot histogram that shows volume over time without individual-level clutter. (p.236)
- **Color-encoding averages within aggregated bins**: coloring each bin of 100 stories by the average number of reviews (popularity) within that bin — combining frequency (position/height) with average quality (color) in one mark. (p.236)
- **Per-character timelines with stacked area**: showing the volume of stories per pairing per month as stacked area charts — allows comparison of relative popularity of pairings over time. (p.239)
- **Ranking / sequencing fights**: ordering fights chronologically within sagas, and grouping sagas into columns — a temporal sequence structure that shows the arc of a narrative. (p.219-220)

---

## Practical Rules of Thumb

- Test a visual with peers before calling it done — they will spot angles and interactions you missed. (p.225, p.237)
- For very long/tall visuals that cannot fit on one screen, **always add a mini-map**. (p.225)
- Varying line thickness (thin at nodes, thick in the middle of a curve) is more visually dynamic than uniform strokes. Achievable with a closed SVG path that loops back with slightly different curve values. (p.224)
- Good guys vs. bad guys (or any binary opposition) can be encoded spatially: lines swooshing left vs. right to instantly communicate alignment. (p.226)
- **Attention to detail is cumulative**: small touches (links to YouTube clips, manually annotated fight descriptions, character illustrations) make the difference between a visualization that is looked at once and one that is explored deeply. (p.227)
- When using color gradients for two related dimensions (e.g., canon pink vs. non-canon purple), pick colors that are meaningfully associated with the concept (e.g., warmer tones for relationships) and that look good together. (p.238)
