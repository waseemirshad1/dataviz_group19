# [agent_12] Data Sketches — pages 301-350

## Overview of Pages 301–350

These pages cover three projects:
- **"Culture" (ch.9, Shirley):** Visualizing Google Trends travel search data — a detailed account of many failed prototypes before finding an effective design (pp.301–316).
- **"Breathing Earth" (ch.10, Nadieh):** Animating global vegetation health data as pulsating circles on a map (pp.320–332).
- **"Community / 655 Frustrations" (ch.10, Shirley):** Visualizing a data visualization community survey using beeswarm plots (pp.333–342).
- **"Myths & Legends" (ch.11, Nadieh):** Introduction — visualizing constellation figures from 25+ world cultures (pp.348–350).

---

## Goal and Function of Visuals

- **Visuals should enable analysis, not just look interesting.** Shirley repeatedly abandoned "visually interesting" prototypes (the arc-circle, the plunger, the heatmap) because they were too hard to extract insights from. (p.303–304, p.309)
- **Prioritize the reader's understanding over visual flair.** "I began to realize the importance of prioritizing the reader and their understanding of my visualizations, instead of just doing whatever was visually flashy and technically interesting." (p.311)
- **Familiar chart types (line chart, map) are easy to analyze** and let the story come through. Shirley's final "Culture" piece used a line chart + world map because "they were easy to analyze." (p.309)
- **Data exploration visuals serve a different purpose than final presentation visuals.** Exploration is about finding what's interesting; final visuals are about communicating it clearly. (pp.304–305, p.336–337)

---

## Design Process Guidance

### Iterate, Abandon, and Restart
- The "Culture" chapter is a masterclass in iterative failure: bar charts → pie charts on maps → arc circles → "The Plunger" → overlapping circles → heatmaps → seasonal blocks → finally a line chart + map. Each iteration taught something new. (pp.301–310)
- When stuck, switch gears: "I've found that if I've been banging my head for a while, it's often more helpful to give it some space and work on something else." (p.307)

### Ask Questions Before Designing
- Mark interesting data attributes first; those naturally generate questions to explore. (p.305)
- Having a specific set of questions prevents getting distracted by interesting tangents in large datasets. Note tangents for later. (p.305)
- Shirley's process: (1) list survey questions of interest, (2) group by theme, (3) form hypotheses, (4) explore with quick charts. (p.335)

### Use Charting Libraries for Exploration
- Use tools like Vega-Lite / Observable for rapid hypothesis testing — not custom code. Build quick bar charts, histograms, scatterplots first. (p.336–337)
- "I list data types (quantitative, nominal, ordinal, temporal, spatial) next to the attributes in my first step, because they inform the charts I should use for exploration." (p.337)
- Common exploration charts: **bar charts** for comparisons, **box plots/histograms** for distributions, **scatterplots** for correlations, **node-link diagrams** for relationships, **line charts** for temporal trends. (p.337)

### Design With Code for Large/Multi-Part Projects
- For large datasets, get data on screen first, explore it, then let findings inform design. Sketching on paper alone doesn't work for complex data. (p.307)
- For multi-part narratives: finish and code one section before sketching the next, as earlier sections influence later ones. (p.307)
- Nowadays, sketch only to work out design kinks or interaction details. (p.307)

### Prioritize Individual Data Points
- "I really like showing individual data points and layering summary metrics on top of them." (p.340)
- Showing individual responses (beeswarm) was more revealing than aggregates (stacked bar). (p.338)

---

## Marks and Channels

### Channel Appropriateness
- **Size/area (circles):** Hard to judge relative sizes with circles. Use sparingly; pie charts should only be used for a few values that are part of a whole. (p.301)
- **Width of bars:** Encoding an extra dimension in bar width creates confusion — "The Plunger" anti-pattern: adding search interest to bar width alongside year (x) and category (color) produced an unreadable visual. (p.303)
- **Color hue:** Used for categorical grouping (topic categories, frustration vs. no-frustration). (pp.302–305, p.338)
- **Color opacity:** Used for quantitative magnitude (vegetation greenness mapped to circle opacity + size). (p.324)
- **Circle radius:** Used for search interest magnitude; overlapping circles indicate more countries searching. (p.303)
- **Position (x/y axis):** Year on x-axis, categorical grouping on y-axis — the most readable combination in the final "Culture" design. (p.309)
- **Height of bars:** Mapping search interest to block height (y = time on shelf, height = interest) finally revealed seasonal trends. (p.305)

### Visual Metaphors as a Channel
- **Vertical position as emotional valence:** Respondents with frustrations "drip down" (below center), those without "rise up" (above center). Reinforces what the data communicates. Suggested by RJ Andrews. (p.339)
- Visual metaphors take advantage of familiar associations (negative = downward) to reduce the learning curve for unfamiliar chart types. (p.339)

---

## Task-Encoding Fit

| Task | Encoding Used | Notes |
|------|--------------|-------|
| Compare time trends | Line chart (x=time, y=value) | Clear, familiar, easy to analyze (p.309) |
| Show geographic origin | World map with sized circles | Circle size = search interest (p.309) |
| Show seasonal patterns | Bar/block chart with height = interest, grouped by season | Only visible when height mapped to interest, not just presence (p.305) |
| Explore individual survey responses | Beeswarm plot | Shows individuals + distribution in one compact view (p.338) |
| Compare distributions across groups | Box-and-whisker overlaid on beeswarm | Median + quartiles on top of individual dots (p.339) |
| Filter and cross-reference two questions | Linked beeswarms + brush interaction | Brush one chart to filter both simultaneously (p.339–340) |
| Explore categorical breakdowns | Bar chart / histogram | Quick, unambiguous for nominal/ordinal data (p.336) |

---

## Data Manipulation

- **Aggregation vs. individual:** Aggregate (stacked bar) hid the story; showing individual survey responses (beeswarm) revealed patterns. (p.338)
- **Proxy variables:** When the direct question wasn't in the survey, Shirley used "answered with frustration" as a proxy for "might leave the field." (p.338)
- **Filtering before visualizing:** Filter stars by naked-eye visibility (apparent magnitude < 6.5) to reduce 22M+ data points to a meaningful subset. (p.350)
- **Resolution reduction:** Satellite vegetation data reduced from ~22 million pixels/week to ~50,000 non-water pixels — "small enough for the browser to handle, but high enough to still see interesting details." (p.322)
- **Cross-dataset linking:** Star data from HYG database linked to constellation data from Stellarium via HIP IDs (unique key). (p.349–350)
- **Scatter plot for outlier discovery:** Plotting star brightness vs. number of constellations using a quick R/ggplot2 scatter revealed which stars deviated from the general trend — a useful exploratory step before designing the final visual. (p.350)

---

## Interaction Design

### Scrollytelling vs. Steppers
- **Scrollytelling:** User scrolls to advance through a story. Uses vertical space heavily — Shirley's first iteration was scrapped because it took too much vertical space for simple concepts. (p.307–308)
- **Steppers:** User clicks to step through sections. All visualizations contained in one place, but clicking through each step was "too much to ask." Solution: auto-animate through steps with Greensock, but still allow clicking a step to replay from that point. Reader retains control of pacing. (p.310)
- **Start animations on scroll-into-view:** Animations automatically start only when the visualization comes into view — a small but important detail for user experience. (p.311)

### Brush Filtering
- A **brush interaction** (D3.js) lets users draw a bounding box to filter data points. Used to cross-reference two survey questions: brush on one beeswarm fades out non-matching dots in both linked charts. (p.339–340)

### Dropdown for Question Switching
- Dropdowns let users switch between different survey questions in the same beeswarm frame — enables comparison without requiring multiple charts visible at once. (p.339)

---

## Common Mistakes and Anti-Patterns

- **Pie charts on maps:** Placing pie charts above country centroids on a map is potentially misleading and confusing; avoid. (p.301)
- **Pie charts with many values:** Pie charts should only be used for a few values that are part of a whole. (p.301)
- **Adding width as an extra dimension to bars ("The Plunger"):** Mapping a third variable to bar width alongside x-axis and color created an unreadable chart. (p.303)
- **Arc/radial layouts for time comparison:** Arranging topics as arcs in a circle made it hard to compare years not adjacent to each other, or see trends over time. (p.301)
- **Too many dimensions before testing readability:** Mashing three survey questions together without considering readability produced a prototype that was "really hard to understand." (p.338)
- **Aggregating when you should show individuals:** Stacked bar chart hid the individual variation that was the real story. (p.337–338)
- **Coding custom visualizations for every hypothesis:** Extremely time-consuming; use charting libraries for exploration instead. (p.337)
- **Over-engineering performance (SVG for 50,000 animated elements):** Standard D3.js SVG approach failed for large animated datasets; Canvas/WebGL required. (p.324)

---

## Practical Rules of Thumb

- When a visualization looks interesting but you can't extract insights from it efficiently, start over. (p.304)
- Use simple, familiar chart types (line chart, bar chart) when the story is in the data, not the form. (p.309)
- Layer summary statistics (box-and-whisker) on top of individual data points (beeswarm) — best of both worlds. (p.339)
- Annotate trigger moments in time series (e.g., global recession 2008–2011 dip in search trends). (p.305)
- For very large datasets (50,000+ animated elements), use Canvas or WebGL (regl, Pixi.js) instead of SVG. (p.324)
- D3.js's utility functions (scales, color interpolation, min/max/mean, d3.delaunay, d3.stratify) are valuable even when the rendering is done with Canvas or WebGL. (p.326)
- Ask for help publicly (Twitter, Slack, Stack Overflow) when stuck on technical problems — community response can be decisive. (p.330)
- When data exploration reveals that a hypothesis is unprovable (e.g., too few people wanted to leave), abandon it and reformulate. (p.337–338)
