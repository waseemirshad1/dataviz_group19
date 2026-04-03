# [agent_12] Data Sketches — pages 301-350

## Visualization Catalogue

---

### Pie Charts on Country Centroids (Map Overlay) (p.301)
- **What it shows:** Breakdown of a metric (search interest) by sub-category (year) for each geographic entity (country), displayed spatially.
- **When to use / avoid:** AVOID — described explicitly as "potentially misleading" and confusing by the author's art director. Placing pie charts on maps conflates two encodings (size of pie = total interest; slices = yearly breakdown) and the spatial position of each pie is the country centroid, which adds a third encoding that competes. Avoid unless the geographic comparison is the primary task and the categorical breakdown is secondary and simple.
- **Interesting properties:** The size of the pie represents total search interest; colors represent years. Reveals which countries started searching recently vs. long ago.
- **Marks:** Pie slices (filled arcs).
- **Channels:** Position (geographic centroid), size (total magnitude), color hue (year/category).
- **Annotation options:** Country labels, year legend.
- **Data types suited for:** Quantitative (magnitude), temporal (year), spatial (geographic).
- **Interesting feature extraction/manipulation:** Grouping by year within a spatial context reveals temporal adoption patterns geographically; but the encoding is too busy to be readable.

---

### Arc-Circle Radial Layout per Country (p.301–302)
- **What it shows:** Travel topics per country, with each topic as an arc around the country, colored by category, arranged clockwise by year.
- **When to use / avoid:** Avoid for trend/comparison tasks. Looks aesthetically interesting but makes it hard to compare years not adjacent to each other or to see category trends over time. Use only if aesthetic impression and rough pattern are the goal, not precise comparison.
- **Interesting properties:** Each country is represented as a cluster of arcs in a circle; the density of arcs shows which countries are most popular travel destinations. Clockwise arrangement attempts to encode time, but fails for non-sequential comparison.
- **Marks:** Arcs.
- **Channels:** Angular position (year), color hue (topic category), presence/count of arcs (popularity of destination).
- **Annotation options:** Country labels, year annotations at clock positions, color legend for categories.
- **Data types suited for:** Categorical (topic, category), temporal (year), spatial (country).
- **Interesting feature extraction/manipulation:** Nothing meaningful can be derived from time comparisons due to the circular non-linear layout.

---

### "The Plunger" — Multi-Dimension Bar Chart (p.303)
- **What it shows:** Travel topics plotted by year (x-axis), colored by category, with bar width mapped to search interest.
- **When to use / avoid:** AVOID — explicitly identified as a mistake ("The Plunger"). The width encoding for a third variable makes bars jagged and misshapen, impossible to read. Width should not be used as a data channel in standard bar charts.
- **Interesting properties:** Named by the author for its plunger-like appearance. A useful cautionary example of over-encoding.
- **Marks:** Rectangular blocks.
- **Channels:** Position (x = year), color hue (category), width (search interest — the anti-pattern).
- **Annotation options:** Year labels, category color legend.
- **Data types suited for:** Categorical, temporal, quantitative — but the encoding combination fails.
- **Interesting feature extraction/manipulation:** None useful. The lesson is that width is not a reliable quantitative channel alongside position.

---

### Overlapping Circles per Topic (Source-Country View) (p.303–304)
- **What it shows:** For each travel topic on a timeline, circles represent "source" countries searching for that topic. Overlapping circles indicate more international interest. Circle radius = a source country's interest level.
- **When to use / avoid:** Use when showing the number and intensity of contributing entities (countries) per item is the primary interest. Avoid if precise comparison of individual entities matters — overlap makes individual circles hard to read.
- **Interesting properties:** The degree of overlap serves as a rough proxy for total international interest. Clicking a topic reveals source country proximity and year.
- **Marks:** Circles (one per source country per topic).
- **Channels:** Position (x = year/time), radius (search interest of source country), overlap density (total international interest), color (could encode country/region).
- **Annotation options:** Topic labels, country labels on hover/click.
- **Data types suited for:** Quantitative (interest), categorical (country, topic), temporal (year).
- **Interesting feature extraction/manipulation:** Aggregating circles by overlap creates an implicit "sum of interest" without explicit aggregation — the visual density itself is informative.

---

### Heatmap — Source Country × Year (p.303–304)
- **What it shows:** For a selected travel topic, which source countries searched for it and in which years, with color opacity encoding search interest.
- **When to use / avoid:** Use when the primary task is spotting which cells have high/low values across a two-dimensional matrix (countries × years). Avoid when absolute values or precise comparison across many cells is needed — color opacity is a weak quantitative channel.
- **Interesting properties:** Compact encoding of a country × year matrix. Replaces overlapping circles with a cleaner grid.
- **Marks:** Filled rectangles (cells).
- **Channels:** Position (x = year, y = country), color opacity (search interest magnitude).
- **Annotation options:** Country labels, year labels, value labels in cells if needed.
- **Data types suited for:** Quantitative (interest), temporal (year), categorical (country).
- **Interesting feature extraction/manipulation:** Sorting countries by geographic proximity to the target country (y-axis) reveals spatial patterns in who searches for a destination.

---

### Seasonal Block Chart (Grouped by Season and Continent) (p.305–306)
- **What it shows:** Travel topics grouped first by season (spring/summer/fall/winter), then by continent of destination, with block height mapped to search interest.
- **When to use / avoid:** Use when comparing magnitude across many categorical groups arranged in a meaningful order (seasonal + geographic). The key insight: encoding height (not just presence) reveals seasonal differences that weren't visible when all blocks were the same height.
- **Interesting properties:** The breakthrough came when block height was made proportional to search interest — flat height showed nothing, but variable height revealed that US users search most in spring. Continent order (by geographic proximity to USA) adds implicit spatial meaning to the x-axis ordering.
- **Marks:** Rectangular blocks (variable height).
- **Channels:** Height (search interest magnitude), color hue (topic category), x-position (continent group, then topic), grouping/faceting (season).
- **Annotation options:** Season labels, continent labels, topic labels, search interest axis.
- **Data types suited for:** Quantitative (interest), categorical (topic, category, continent), temporal (season).
- **Interesting feature extraction/manipulation:** Grouping by season first, then continent, makes seasonal patterns primary. The ordering of continents by geographic proximity adds an implicit spatial variable.

---

### Arc Timeline (Search Interest Rise/Fall per Topic) (p.305–307)
- **What it shows:** For a single travel topic, the trajectory of search interest from 2004 to 2016. Each year is a circle on an x-axis scaled by search interest (0–100). An arc above the axis = interest increased that year; an arc below = interest decreased.
- **When to use / avoid:** Use when showing the direction of change (increase/decrease) year-by-year is more important than the absolute value. Avoid when the reader needs to extract precise values quickly — it requires effort to read. Good for artistic/exploratory views.
- **Interesting properties:** The arc direction encodes the sign of change; the arc length/shape encodes the magnitude of change. Revealed that many topics peaked in 2004 and declined, with a notable dip between 2008–2011 (global recession).
- **Marks:** Circles (years), arcs (connecting consecutive years, above or below axis).
- **Channels:** X-position (search interest value 0–100), arc direction (up = increase, down = decrease), arc shape (magnitude of change).
- **Annotation options:** Year labels on circles, reference lines for notable events (recession), topic label.
- **Data types suited for:** Quantitative (search interest), temporal (year).
- **Interesting feature extraction/manipulation:** The arc direction explicitly encodes year-over-year delta (derivative), which is lost in a standard line chart that only shows absolute values.

---

### Line Chart + Animated World Map with Sized Circles (p.309)
- **What it shows:** For a selected travel topic, (1) a line chart showing search interest across years, and (2) a world map with circles on source countries sized by search interest, both animated through time.
- **When to use / avoid:** Use when temporal trend (line chart) AND geographic distribution (map) are both important for the same dataset. The combined animation through time links both views. Avoid if the animation is too fast to process — pacing matters.
- **Interesting properties:** Both charts animate simultaneously through time, so the reader sees the geographic origin of searches evolve as the line chart progresses. Familiar chart types make analysis easy. Revealed an interesting story: searches for Qin Shi Huang and his Terracotta Army show similar seasonal patterns.
- **Marks:** Line (time series), circles (countries on map).
- **Channels:** Position (x = time for line chart; geographic position for map), y-position (search interest on line chart), circle radius (search interest for source country), color (could differentiate regions).
- **Annotation options:** Year labels, country labels on hover, event annotations on line chart.
- **Data types suited for:** Quantitative (interest), temporal (year), spatial (geographic country).
- **Interesting feature extraction/manipulation:** Animating both charts through time creates a linked temporal-spatial view without requiring a complex combined chart type.

---

### Beeswarm Plot (Survey Responses) (p.338–340)
- **What it shows:** Individual survey respondents as dots, spread horizontally to avoid overlap, positioned vertically by a categorical variable (dataviz focus: primary/secondary/one of several). Color and x-position encode years of experience or percent of day on dataviz.
- **When to use / avoid:** Use when showing the distribution of individual data points across categories matters more than summary statistics alone. Great for medium-sized datasets (hundreds to low thousands of items). Avoid for very large datasets where dots overlap unresolvably.
- **Interesting properties:** Compact yet individual — each dot = one person. Combines distribution (like a histogram) with individual visibility. The "bounded force layout" split: respondents with frustrations drip below center, those without rise above — a visual metaphor encoding sentiment through vertical position.
- **Marks:** Circles/dots (one per respondent).
- **Channels:** X-position (continuous variable: years of experience or % day on dataviz), Y-position (categorical: dataviz focus level; also encodes frustration vs. no-frustration via above/below split), color hue (categorical grouping), fill vs. outline (whether dataviz was intended career path).
- **Annotation options:** Box-and-whisker overlaid for median and quartiles, category labels on y-axis, color legend.
- **Data types suited for:** Quantitative (continuous variables), categorical (groups), ordinal (levels of focus).
- **Interesting feature extraction/manipulation:** The "bounded force layout" using D3.js force simulation (forceX, forceY, forceCollide) positions dots to avoid overlap while respecting categorical groupings. Overlaying box-and-whisker on top of individual dots combines summary + detail in one view.

---

### Beeswarm with Overlaid Box-and-Whisker (p.339)
- **What it shows:** As above (beeswarm), but with a box-and-whisker plot overlaid to show median and first/third quartiles for each group.
- **When to use / avoid:** Use when both individual variation and distributional summary are important. Especially powerful when comparing whether groups differ in central tendency AND spread. Avoid if the box-and-whisker occludes too many individual dots.
- **Interesting properties:** The combination gives the reader both levels of detail simultaneously: the forest (box-and-whisker) and the trees (individual dots).
- **Marks:** Dots (individuals), rectangles + lines (box-and-whisker).
- **Channels:** Position (all channels from beeswarm), box/whisker extent (IQR and range).
- **Annotation options:** Median line label, quartile values, outlier markers.
- **Data types suited for:** Quantitative + categorical (same as beeswarm).
- **Interesting feature extraction/manipulation:** Calculating quartiles as a separate layer on top of an individual-level view; the IQR box acts as a visual "anchor" for understanding the distribution shape at a glance.

---

### Linked Dual Beeswarm with Brush Interaction (p.339–340)
- **What it shows:** Two beeswarm plots side by side, each showing a different survey question. A brush on either chart filters both, enabling cross-question correlation analysis.
- **When to use / avoid:** Use when cross-referencing two different categorical/ordinal variables across the same set of individuals matters. Especially useful for exploratory analysis of multi-question surveys. Avoid when the connection between the two questions is unclear — linking will confuse rather than reveal.
- **Interesting properties:** The brush-filter link means selecting "people whose primary focus is dataviz" in one chart simultaneously highlights those same people in the other chart. Implemented with D3.js brush + React.js for state linking.
- **Marks:** Dots in two panels.
- **Channels:** As per beeswarm, plus visual fade (opacity) for non-selected items.
- **Annotation options:** Selection count display, category labels, brush bounding box.
- **Data types suited for:** Quantitative + categorical + ordinal survey data.
- **Interesting feature extraction/manipulation:** The brush operation is itself a form of dynamic filtering/aggregation — you see the sub-group distribution in both charts simultaneously.

---

### Animated Dot Map — "Breathing Earth" (p.322–331)
- **What it shows:** Global vegetation health (NDVI "greenness") for every week of the year, encoded as ~50,000 circles pulsating across 52 weeks of data.
- **When to use / avoid:** Use when showing spatial change over time for continuous surface data, especially when animation communicates the temporal pattern better than static small multiples. Avoid for precise value reading — animation is for impression, not measurement.
- **Interesting properties:** Each pixel of satellite data becomes a circle. Circle size AND color opacity both encode vegetation health ("greenness"). Multiply color blend mode darkens overlapping circles. The animation gives a "breathing" impression as circles grow and shrink seasonally. No country borders — the earth's geography emerges from the vegetation pattern alone.
- **Marks:** Circles (one per 50k sampled geographic locations).
- **Channels:** Size (vegetation health / greenness), color (green intensity mapped to health value), opacity (also greenness), position (geographic, fixed).
- **Annotation options:** Minimal by design — only title, legend, and brief text. The visual is self-explanatory.
- **Data types suited for:** Quantitative (continuous greenness value 0–1), spatial (geographic), temporal (weekly, animated).
- **Interesting feature extraction/manipulation:** Downsampling from 22M pixels to 50,000 non-water pixels while preserving enough spatial resolution for the pattern to be legible. Color blend mode (multiply) creates natural-looking color layering where circles overlap.

---

### Scatter Plot — Star Brightness vs. Number of Constellations (p.350)
- **What it shows:** For ~2,200 naked-eye-visible stars, the relationship between apparent magnitude (brightness) and the number of constellations (across 25 world cultures) that each star is part of.
- **When to use / avoid:** Use for correlation / outlier detection. Revealed that brighter stars tend to appear in more constellations, with interesting outliers (stars used in many constellations despite being dimmer, or vice versa).
- **Interesting properties:** Made in R/ggplot2 as a quick exploratory step, not the final visual. The outliers drive the storytelling in the final visualization.
- **Marks:** Points (one per star).
- **Channels:** X-position (apparent magnitude — note: smaller = brighter in astronomy), Y-position (number of constellations that use this star), possibly size or color for named stars.
- **Annotation options:** Labels for notable outlier stars, trend line.
- **Data types suited for:** Quantitative (magnitude, count), categorical (named vs. unnamed stars).
- **Interesting feature extraction/manipulation:** Filtering to apparent magnitude < 6.5 (naked-eye visibility threshold) before plotting. The outlier stars from this scatter plot became the focal points of the final "Myths & Legends" visualization.
