# [agent_15] examples from class (dutch) — pages 1-3

---

### Matrix Heatmap — Building Type × Energy Type (p.1)

- **What it shows:** Magnitude of energy consumption at the intersection of every building type (row) and energy type (column). Patterns of high/low use across the full cross-product.
- **When to use:** When you have two categorical dimensions and one quantitative value and want to see all pairwise combinations at once. Avoid when one dimension has too many categories (>20) or when precise magnitude comparison is needed.
- **Interesting properties:** Supports hierarchical clustering of rows and columns to reveal natural groupings. Cell color encodes the third variable without requiring spatial position.
- **Marks:** Rectangles (cells).
- **Channels:** Color saturation/luminance (dark = high, light = low consumption).
- **Annotation options:** Cell labels with exact values; dendrograms on axes when clustering is applied; color legend bar.
- **Data types suited for:** Two categorical/ordinal dimensions + one quantitative value.
- **Interesting feature extraction/manipulation of data:** Apply hierarchical clustering (e.g., Ward linkage) to reorder rows and columns so that similar building types and similar energy types are adjacent — reveals structure invisible in alphabetical ordering.

---

### Heatmap — Days × Time of Day (p.1)

- **What it shows:** Energy consumption patterns across the week and across hours of the day simultaneously. Reveals when peaks occur (e.g., weekday daytime in offices).
- **When to use:** Cyclical or time-structured data with two temporal axes. Avoid when the dataset is sparse (many empty cells).
- **Interesting properties:** Instantly communicates "hot spots" in time. The 2D layout of time-on-time is natural and readable.
- **Marks:** Rectangles (cells).
- **Channels:** Color saturation/luminance.
- **Annotation options:** Axis labels for days and hours; color scale legend; annotations for notable cells.
- **Data types suited for:** Two ordinal time dimensions + one quantitative value.
- **Interesting feature extraction/manipulation of data:** Aggregate raw time-stamped data into day-of-week × hour-of-day bins (mean or sum). Normalizing per building type allows comparison across sites.

---

### Mirror Chart / Diverging Time Chart (JA7) (p.1)

- **What it shows:** Two groups (commercial vs. residential) plotted symmetrically on opposite sides of a shared vertical time axis (year or day). Allows direct comparison of magnitude and timing between the two groups.
- **When to use:** Exactly two groups that share the same time axis and whose comparison is the central question. Avoid for more than two groups.
- **Interesting properties:** The mirroring makes visual comparison of left vs. right intuitive. Asymmetry between sides is immediately visible.
- **Marks:** Area or bars extending from a central spine.
- **Channels:** Position along vertical axis (time); Length/distance from center (magnitude); Side (left/right) = category.
- **Annotation options:** Labels on each side; gridlines at time intervals; annotations for notable peaks.
- **Data types suited for:** Quantitative (consumption) over ordered time, for exactly two categories.
- **Interesting feature extraction/manipulation of data:** Normalize each side independently if scales differ greatly; use smoothing (rolling average) to reduce noise while keeping trend visible.

---

### Radial Bar Chart / Clock Diagram (JA6) (p.1)

- **What it shows:** Total energy consumption per hour of the day, for each building type, in a 24-hour circular layout. Each hour is a position on the clock; bars radiate outward.
- **When to use:** When the cyclical nature of the data (hours, months) is semantically important. Avoid when precise length comparison is needed — radial bars near the center are compressed.
- **Interesting properties:** The circular layout makes daily rhythm feel natural. The shape formed by all bars conveys the overall "energy profile" of a city.
- **Marks:** Bars (radial).
- **Channels:** Angle (hour of day); Length (energy magnitude); Color hue (building type).
- **Annotation options:** Hour labels at each position; concentric gridlines; legend for building types.
- **Data types suited for:** Quantitative over cyclic ordinal (hours/months) + categorical (building type).
- **Interesting feature extraction/manipulation of data:** Aggregate to hourly totals per building type; optionally normalize to show relative rather than absolute consumption.

---

### Heating vs. Cooling Monthly Clock (p.1)

- **What it shows:** Monthly energy use for heating vs. cooling on opposite sides of a 12-month radial chart. Seasonal asymmetry is the central message.
- **When to use:** When showing a seasonal split across a full year cycle. Avoid if data has more than two categories to split.
- **Interesting properties:** The opposing sides make the seasonal trade-off (more heating in winter, more cooling in summer) immediately visible as a visual balance.
- **Marks:** Bars (radial, bidirectional).
- **Channels:** Angle (month); Length (magnitude); Direction/side (heating vs. cooling).
- **Annotation options:** Month labels; scale rings; labels for the two sides.
- **Data types suited for:** Quantitative split into two categories over 12 cyclic months.
- **Interesting feature extraction/manipulation of data:** Separate energy readings by type (heating vs. cooling) and aggregate by month; optionally express as deviation from annual mean.

---

### Cumulative Line Chart (p.1)

- **What it shows:** Total gas consumption accumulated over time. The line never decreases. Slope reveals rate of consumption; steep sections = high consumption periods.
- **When to use:** When total burden over time is the question, not instantaneous rate. Pairs well with showing seasonal intensity. Avoid when the audience expects a standard time series and the cumulative transformation may confuse.
- **Interesting properties:** Converts volatile time-series into a smooth, always-rising curve. Seasonal spikes appear as steeper rises.
- **Marks:** Line.
- **Channels:** Position on x-axis (time); Position on y-axis (cumulative total); Slope (implied rate of consumption).
- **Annotation options:** Vertical reference lines for seasons/events; slope annotations; labels at key inflection points.
- **Data types suited for:** Quantitative (consumption) over ordered time (date/month).
- **Interesting feature extraction/manipulation of data:** Transform daily/weekly readings into running sum. Can overlay multiple years on same axes to compare cumulative trajectories.

---

### Pictogram Chart — Flames / Lightning Bolts (p.1–2)

- **What it shows:** Approximate magnitude of gas (flames) or electricity (lightning bolts) consumption. Size of the symbol encodes level of use. Different symbol types can encode different applications (cooking vs. heating).
- **When to use:** Communication to general audiences where memorability and engagement matter more than precision. Avoid for analytical tasks requiring accurate comparison.
- **Interesting properties:** Semantically self-explanatory — no legend needed for the symbol meaning. Works well in infographic or public-facing contexts.
- **Marks:** Icons (flames, lightning bolts).
- **Channels:** Size of icon (magnitude); Shape (application type).
- **Annotation options:** Numeric labels alongside; grouping by application type.
- **Data types suited for:** Quantitative (ordinal-ish) with meaningful categorical type distinction.
- **Interesting feature extraction/manipulation of data:** Bin continuous consumption values into discrete size categories (small/medium/large) for symbol sizing.

---

### Horizontal Bar Chart (JA1) (p.2)

- **What it shows:** Total gas consumption across all building types, broken out by category. Horizontal orientation suits long category labels.
- **When to use:** Comparing a single quantitative value across many categories. Avoid vertical bars when labels are long. Avoid when part-to-whole is the main question (use stacked or pie instead).
- **Interesting properties:** Length is the most accurate channel for magnitude after position. Easy to rank categories visually.
- **Marks:** Bars (horizontal rectangles).
- **Channels:** Length (total consumption); Color hue (optional — category distinction).
- **Annotation options:** Value labels at bar ends; reference line for mean; sorted order (descending) aids comparison.
- **Data types suited for:** One categorical dimension + one quantitative value.
- **Interesting feature extraction/manipulation of data:** Sort by value descending; optionally normalize to per-capita or per-square-meter to enable fairer comparison.

---

### Pie Chart / Taartdiagram (p.2)

- **What it shows:** Part-to-whole breakdown of energy types and applications within one city.
- **When to use:** Only when showing composition (parts of a whole) with very few slices (2–4) and approximate shares are sufficient. Avoid for comparison across multiple pies or when slices are similar in size.
- **Interesting properties:** Familiar to general audiences. Poor for precise comparison — humans judge angles and arc lengths inaccurately.
- **Marks:** Wedge/arc.
- **Channels:** Angle/arc length (proportion); Color hue (category).
- **Annotation options:** Percentage labels; direct slice labels; legend.
- **Data types suited for:** Categorical (energy type) with proportional quantitative values summing to a whole.
- **Interesting feature extraction/manipulation of data:** Calculate percentage share of each energy type; collapse small categories into "other."

---

### Bubble Chart (p.2)

- **What it shows:** Total energy consumption per location (bubble size) differentiated by building type (bubble color). Provides a geographic or scatter overview.
- **When to use:** When location matters and two quantitative or categorical variables need to be shown simultaneously. Avoid for precise magnitude comparison — area judgment is imprecise.
- **Interesting properties:** Encodes three variables (location x, location y, magnitude as size, category as color). Patterns across geographic space are visible.
- **Marks:** Circles (bubbles).
- **Channels:** Position x/y (location or two quantitative variables); Area/size (total consumption); Color hue (building type).
- **Annotation options:** Labels on large bubbles; legend for color; size legend.
- **Data types suited for:** Spatial/quantitative (x, y) + quantitative (size) + categorical (color).
- **Interesting feature extraction/manipulation of data:** Aggregate consumption to site level; scale bubble area proportionally (not radius) to avoid perceptual distortion.

---

### Flower Diagram / Bloemen-diagram (p.2)

- **What it shows:** Multiple components of electricity use (heating, cooling, cooking, etc.) as petals radiating from a center. Petal size is proportional to energy use for that activity.
- **When to use:** When showing composition of a whole across several named parts in a visually engaging way. Avoid when precise comparison of petal sizes is needed.
- **Interesting properties:** Highly memorable and visually distinctive. Each entity (building/site) can have its own flower, enabling small-multiples comparison across sites.
- **Marks:** Petals (custom shapes radiating from center).
- **Channels:** Size/area of petal (magnitude per activity); Position/angle (which activity); Color hue (activity type, optional).
- **Annotation options:** Labels on each petal; size scale reference; title per flower for small-multiples.
- **Data types suited for:** One entity with multiple quantitative sub-components (part-of-whole).
- **Interesting feature extraction/manipulation of data:** Normalize petal sizes within each flower to show relative composition; or keep absolute scale across flowers for cross-site comparison.

---

### Climate Stripes / Klimaatstrepen (p.2)

- **What it shows:** Deviation of energy consumption from average over time. Each stripe = one time unit; color encodes direction and magnitude of deviation (dark red = far above average, dark blue = far below).
- **When to use:** When the trend of deviation over time is the message and you want a visually striking, axis-free format. Best for communication/advocacy contexts. Avoid when readers need exact values.
- **Interesting properties:** No axes needed. The pattern itself communicates the trend. Derived from Ed Hawkins' climate warming stripes — carries strong visual precedent and emotional impact. Semantically novel when applied to energy data.
- **Marks:** Rectangles (vertical stripes).
- **Channels:** Color hue (direction: red = above, blue = below average); Color saturation (magnitude of deviation); Position on x-axis (time).
- **Annotation options:** Minimal by design; optional year labels at start/end; color scale legend.
- **Data types suited for:** Quantitative deviation from a reference value over ordered time.
- **Interesting feature extraction/manipulation of data:** Calculate deviation = actual − rolling mean (or long-term mean); map to diverging color scale centered at zero.

---

### Home vs. Office 24-Hour Comparison Chart (p.2)

- **What it shows:** Energy use at home vs. at the office across a full 24-hour day, with peaks at typical moments (morning = home; daytime = office).
- **When to use:** When two contexts share the same time axis and the contrast between their patterns is the story. Avoid when more than two contexts need comparison.
- **Interesting properties:** The temporal overlap and divergence of two lines tells a behavioral story. Works as a dual-line, dual-area, or mirrored chart.
- **Marks:** Lines or areas.
- **Channels:** Position on x-axis (hour of day); Position on y-axis (energy magnitude); Color hue (home vs. office).
- **Annotation options:** Peak labels; shaded time bands (morning/afternoon/evening); reference line for average.
- **Data types suited for:** Quantitative over cyclic ordinal (hours) for exactly two categories.
- **Interesting feature extraction/manipulation of data:** Aggregate to hourly means across days; optionally normalize each context to its own max for shape comparison rather than magnitude.

---

### Node-Matrix Conceptual Diagram (JA9) (p.2–3)

- **What it shows:** Cities and building types as nodes in a matrix layout, connected by lines. Node size (circle) encodes total energy consumption. Line color and thickness encode energy type and quantity. Can embed stacked bars within each node for energy type breakdown.
- **When to use:** When multi-dimensional relationships between two sets of entities (cities × building types) and a quantitative variable need to be shown simultaneously. Avoid when the audience is unfamiliar with network-style diagrams.
- **Interesting properties:** Hybrid visualization combining matrix layout + proportional symbols + line encoding + optional stacked bars. Answers questions that no single basic chart could. High information density.
- **Marks:** Circles (nodes); Lines (connections); Stacked bar segments (within nodes, optional).
- **Channels:** Node size/area (total consumption); Line thickness (quantity); Line color hue (energy type); Position in matrix (city × building type identity).
- **Annotation options:** Node labels; line labels or legend; stacked segment legend; size scale reference.
- **Data types suited for:** Two categorical dimensions (city, building type) + quantitative (consumption) + categorical sub-breakdown (energy type).
- **Interesting feature extraction/manipulation of data:** Aggregate consumption per city-building-type pair; compute proportional breakdown by energy type per node; sort cities and building types by total consumption for clearest layout.
