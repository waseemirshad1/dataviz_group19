# Visualization Catalogue — Synthesized from 25 Source Chunks

**Sources:** Cool Infographics (CI), Data Sketches (DS), Visualization Analysis and Design / Tamara Munzner (VAD), Example Reports from Class (EC), Student Reports (ER)

**Scope:** General-purpose reference catalogue. Not scoped to any specific dataset. Entries are merged from all sources — the richest description is preserved and supplementary details folded in.

**Organization:**
1. Quantitative / Magnitude Data
2. Categorical / Nominal Data
3. Temporal / Time-Series Data
4. Relational / Network / Hierarchical Data
5. Spatial / Geographic Data
6. Multivariate / High-Dimensional Data
7. Custom / Creative / Domain-Specific

Within each group, entries are sorted alphabetically.

Student report entries are marked **[from student report]** in the header.

---

## 1. Quantitative / Magnitude Data

### Arc Timeline (Search Interest Rise/Fall)
- **What it shows:** For a single item or topic, the trajectory of a quantitative value over time. Each time unit is a circle on an axis scaled by value; an arc above the axis = value increased that year; arc below = value decreased.
- **When to use:** When direction of change (increase/decrease) year-by-year is more important than absolute value. Good for artistic/exploratory views. Avoid when the reader needs precise value extraction quickly.
- **Interesting properties:** The arc direction explicitly encodes the year-over-year delta (derivative), which is invisible in a standard line chart that shows only absolute values. Revealed that many topics peaked in 2004 and declined, with a dip during 2008–2011 (global recession).
- **Marks:** Circles (one per year/time unit), arcs (connecting consecutive years, above or below axis).
- **Channels:** X-position (quantitative value on scale), arc direction (up = increase, down = decrease), arc shape/length (magnitude of change).
- **Annotation options:** Year labels on circles, reference lines for notable events, topic label.
- **Data types suited for:** Quantitative (value), temporal (time/year), single series.
- **Interesting feature extraction/manipulation:** The arc direction encodes the first derivative of the time series — a derived attribute that the raw line chart hides.

---

### Back-to-Back Opposing Bar Chart
- **What it shows:** Two related but distinct quantities for each item, displayed as bars extending in opposite directions from a central axis. Example: annual sales (left) vs. annual profit (right) for top 10 products.
- **When to use:** When comparing two quantities per item and revealing that the ranking on one does not match the ranking on the other. Avoid for more than ~15 items.
- **Interesting properties:** The opposing layout makes it visually obvious when the rank order on one side diverges from the other (e.g., highest sales but not highest profit). Not natively in Excel — must be built manually.
- **Marks:** Horizontal bars (extending left and right from a central spine).
- **Channels:** Length (monetary/quantitative amount), color hue (metric type — e.g., blue=sales, green=profit), position on vertical axis (item identity), label inside bar (exact value and percentage).
- **Annotation options:** Values inside bars, percentage margin shown at bar ends, central axis labels.
- **Data types suited for:** Quantitative (two metrics per item), categorical (items).
- **Interesting feature extraction/manipulation:** Pre-computing a derived ratio (e.g., profit margin %) and displaying it alongside absolute values reveals the rate dimension that pure absolute comparison misses.

---

### Bar Chart
- **What it shows:** A quantitative value for each level of a categorical key attribute. Enables comparison of magnitude across categories.
- **When to use:** One categorical key, one quantitative value. Ideal for lookup, ranking, and comparison. Avoid for continuous ordered keys (use line chart); avoid when part-to-whole is the question (use stacked or pie instead); avoid for hundreds of categories without interaction. Never use 3D bar charts.
- **Interesting properties:** All bars share a common baseline (aligned spatial position) — this is the highest-accuracy magnitude channel. Ordering bars by value reveals trends; alphabetical ordering aids lookup but hides patterns. Horizontal orientation is better when labels are long. Marks can be replaced with icons to eliminate the legend (CI p.215).
- **Marks:** Bars (line marks / area rectangles).
- **Channels:** Length (quantitative value, aligned to common baseline), horizontal or vertical position (category identity), color hue (optional second categorical attribute for grouped bars).
- **Annotation options:** Value labels above/inside bars, reference lines, error bars, icon clusters embedded at bar base (replaces legend), sorted order.
- **Data types suited for:** Table: one quantitative value, one categorical/ordinal key. Extensible with color for a second categorical.
- **Interesting feature extraction/manipulation:** Sort by value to reveal ranking; normalize for proportion comparison; derive aggregates (sum, mean, count) per category before encoding.

---

### Boxplot / Box-and-Whisker Chart
- **What it shows:** Statistical distribution summary using five derived values (median, Q1, Q3, lower fence/min, upper fence/max) plus explicit outliers. Compares distributions across many categories simultaneously.
- **When to use:** Comparing distributions across many groups (dozens) where spread, skew, and outliers are the key tasks. Avoid for multimodal data (use violin or vase plot instead); avoid when showing all individual values is important.
- **Interesting properties:** Highly scalable — compresses any number of values to 5 numbers. Assumes unimodal distribution. Can be combined with beeswarm overlaid to show both the distribution shape and individual points. Geographically weighted boxplots adapt this for spatial data (two overlaid: global=gray, local=green). Notches can show median confidence intervals.
- **Marks:** Line marks (whiskers), rectangle (interquartile box), horizontal line (median), point marks (outlier dots).
- **Channels:** Vertical spatial position (all 5 derived values), horizontal position (categorical key, 1D list alignment).
- **Annotation options:** Axis labels, outlier value annotations, mean markers, notches for CI, jittered data overlay, overlaid beeswarm.
- **Data types suited for:** Table: one quantitative value per group, one categorical key. Derived: 5-number summary per group.
- **Interesting feature extraction/manipulation:** Derive median, quartiles, fences; compute IQR; sort groups by median; overlay raw data points (beeswarm) for detail.

---

### Bubble Chart / Proportional Circle Comparison
- **What it shows:** Quantitative magnitudes compared through circle area. Can show 3–4 variables simultaneously: two via position (x/y), one via size, one via color.
- **When to use:** Comparing magnitudes where a bar chart would be too wide, or where spatial layout matters. Avoid when exact comparison is critical (area perception is compressed — Stevens' exponent ~0.7). Avoid when points are many and overlap is severe.
- **Interesting properties:** Circles MUST be sized by area (π × r²), not diameter — incorrect diameter-based sizing makes a 3× difference appear as ~9× visually. Combining proportional circles with logo fills allows logo identity to serve as the categorical channel, eliminating any legend (CI p.184). Used frequently for demographic data (population, GDP, life expectancy, continent).
- **Marks:** Filled circles (area marks).
- **Channels:** Area/size (quantitative magnitude — must be computed correctly), color hue (categorical — second variable), horizontal/vertical position (two quantitative variables or categorical groupings), text label inside circle (direct annotation).
- **Annotation options:** Value labels inside circle, area calculation shown, size legend, color legend.
- **Data types suited for:** Quantitative magnitudes (1–3 variables) + optional categorical. Ratio-scale data required for size encoding.
- **Interesting feature extraction/manipulation:** Log-scale size mapping prevents very large values from dominating. Normalize/index values to a baseline year for change comparison over time.

---

### Bubble Grid / Proportional Circle Matrix [from student report]
- **What it shows:** Two quantitative variables compared across a two-dimensional categorical space. Each cell in the grid contains one mark; two variables are encoded per mark (size + saturation).
- **When to use:** When two quantitative variables need to be compared across two categorical dimensions simultaneously, with moderate cell count (up to ~100 cells). Avoid when cell count is very high or when values are very similar in magnitude.
- **Interesting properties:** Can simultaneously reveal which categories dominate on one dimension (size) while also flagging anomalies on a second dimension (saturation). Can surface cases like "low revenue but high price per order" that bar charts would not show at a glance.
- **Marks:** Points (circles), sized and coloured.
- **Channels:** Size (area) → primary quantitative variable; saturation → secondary quantitative variable; vertical position → one categorical dimension; horizontal position → second categorical dimension.
- **Annotation options:** Tooltip on hover (exact values); checkboxes for filtering dimensions.
- **Data types suited for:** Two quantitative variables × two categorical variables. Quantitative variables must be ratio-scale for size encoding.
- **Interesting feature extraction/manipulation:** The secondary variable must be aggregated to the cell level (e.g., average order value, not individual records). Grouping to a manageable number of categories is the key data manipulation that makes the encoding viable.

---

### Cumulative Line Chart
- **What it shows:** Total accumulated quantity over time. The line never decreases. Slope reveals rate; steep sections = high-rate periods.
- **When to use:** When total burden over time is the question, not instantaneous rate. Pairs well with showing seasonal intensity. Avoid when the audience expects a standard time series and the cumulative transformation may confuse.
- **Interesting properties:** Converts volatile time-series into a smooth, always-rising curve. Seasonal spikes appear as steeper rises rather than peaks. Multiple years can be overlaid on the same axes to compare cumulative trajectories.
- **Marks:** Line.
- **Channels:** X-position (time), Y-position (cumulative total), slope (implied rate of consumption/accumulation).
- **Annotation options:** Vertical reference lines for seasons/events, slope annotations, labels at key inflection points.
- **Data types suited for:** Quantitative (consumption or accumulation) over ordered time.
- **Interesting feature extraction/manipulation:** Transform daily/weekly readings into running sum. Can overlay multiple years for trajectory comparison.

---

### Gauge / Dial Chart
- **What it shows:** A single quantitative value shown as a needle position on a circular dial, relative to a known min–max range.
- **When to use:** Status monitoring — showing current value against a range. Avoid for precise value comparison between multiple items; avoid when trend over time matters.
- **Interesting properties:** Dual-ring gauges (CI p.177) allow two different product types or groups to be compared on the same face (outer ring = one product, inner ring = another). Multiple color-coded needles on one dial can show several metrics simultaneously. Nesting gauges answers two questions in one visual frame.
- **Marks:** Circular dial face, needle/pointer, arc fills.
- **Channels:** Needle angle (quantitative value on scale), color zones on dial face (green/yellow/red for good/warning/danger ranges), needle color (metric identity in multi-needle versions), gauge radius (product/group in nested versions).
- **Annotation options:** Numeric value below dial, label above dial, min/max values at dial ends, legend for needle colors.
- **Data types suited for:** Quantitative (single or few values against a range). Best for operational KPI monitoring.
- **Interesting feature extraction/manipulation:** Joins multiple datasets to compare expected vs. actual quantities; alarm logic as derived categorical state.

---

### Histogram
- **What it shows:** Distribution of a single quantitative attribute, aggregated into bins; shows count per bin.
- **When to use:** Summarizing distribution for large datasets where individual items would overplot. Avoid for small datasets; avoid when bin count is contentious and not interactively adjustable.
- **Interesting properties:** No gaps between bars (implies continuity, unlike bar charts). Bin size choice radically changes appearance. A smoothed density curve (KDE) overlaid helps compare shape at a glance. Generalizes to a continuous scatterplot in 2D. SolarPlot variant uses radial layout for cyclic time data (circle radius controls bin count interactively — small = high aggregation/trend; large = low aggregation/seasonal).
- **Marks:** Line marks (bars touching without gaps).
- **Channels:** Length/height (count per bin), horizontal position (bin range = ordered key).
- **Annotation options:** Bin edge annotations, frequency labels, overlaid KDE curve, mean/median lines.
- **Data types suited for:** Table: one quantitative value attribute → derived: one ordered key (bin) + one quantitative value (count).
- **Interesting feature extraction/manipulation:** Derive bin boundaries; count items per bin; interactive bin-size control (Freedman-Diaconis rule for optimization); overlay multiple distributions for comparison.

---

### Isotype / Unit / Pictogram Chart
- **What it shows:** A count or quantity using repeated unit icons; especially effective for "how many of X" comparisons where the unit icon is meaningful.
- **When to use:** When showing a count and you want the mark to carry semantic meaning (the image IS the category). Avoid when the number is too large to count visually (n > ~50 becomes unwieldy). Use literal count for small-sample qualitative data to prevent false statistical conclusions.
- **Interesting properties:** The grid format naturally communicates quantity through count. Highlighting one subset in a different color/border makes comparisons visceral (CI p.25). Person-icon arrays make small sample size self-evident — no false impression of statistical power.
- **Marks:** Icons / pictograms (semantic shapes: newspaper, person, flame, lightning bolt) arranged in rows.
- **Channels:** Count of icons (quantitative frequency), color highlight (comparison group or category), icon shape (the semantic unit of what is being counted).
- **Annotation options:** Quantity labels below each group, color highlight/border on comparison group, title text.
- **Data types suited for:** Quantitative (small counts), categorical (time period, category), part-to-whole (unit charts).
- **Interesting feature extraction/manipulation:** Converting raw data into a relatable human-scale unit (e.g., newspapers per day instead of gigabytes). Deliberately NOT computing a percentage when n is small — showing literal count.

---

### Nested Area / Square Size Comparison
- **What it shows:** Relative sizes of values as rectangles or squares positioned or nested together. Effective when the ratio between values is so extreme a bar chart would be unreadable.
- **When to use:** When the ratio between values is extreme and the visceral sense of scale is the message. Avoid when precise reading is needed.
- **Interesting properties:** Nested or corner-aligned squares make multiplicative relationships immediately comprehensible (e.g., gigabyte/terabyte/petabyte where each is 1024× the previous). Color differentiates the units.
- **Marks:** Rectangles/squares (areas).
- **Channels:** Area/size (relative magnitude), color hue (unit/category identity), position (lower-left anchored for fair comparison).
- **Annotation options:** Unit labels, text callouts with arrows.
- **Data types suited for:** Quantitative (large ratio comparisons, two or three values).
- **Interesting feature extraction/manipulation:** None — the visual is the ratio itself.

---

### Proportional Circle with Change Arrows
- **What it shows:** Hierarchical budget or quantity breakdown — one large central circle for total, satellite circles for sub-items, arrows encoding year-over-year change direction.
- **When to use:** Showing budget allocations with multiple hierarchy levels and change over time. Avoid when more than ~15 leaf nodes (becomes cluttered).
- **Interesting properties:** Arrow color (red/yellow/green) encodes budget change direction as a third variable without adding a separate chart — viewers scan both magnitude and trend simultaneously. A "NEW" label can flag items appearing for the first time.
- **Marks:** Circles (areas), directed arrows.
- **Channels:** Circle area (dollar amount), arrow color hue (change direction: red=decrease, yellow=unchanged, green=increase), arrow direction (hierarchical relationship), label text (dollar value and percentage).
- **Annotation options:** Dollar value and percentage change inside or adjacent to circles, parent category name.
- **Data types suited for:** Quantitative (budget amounts), categorical (departments), ordinal (change direction).
- **Interesting feature extraction/manipulation:** Computing year-over-year percentage change and encoding it as a discrete three-category variable (red/yellow/green) rather than a continuous scale simplifies reading considerably.

---

### Ranked Fan / Pie Chart with Extended Legend Lines
- **What it shows:** Ranking and proportion simultaneously for many categories. Pie slices are numbered and ordered by rank; large slices carry embedded labels while small slices use extended leader lines to a ranked list below.
- **When to use:** When both rank and proportion matter and there are many categories. Avoid for simple part-to-whole comparisons where a standard pie is clearer.
- **Interesting properties:** Solves the small-slice legibility problem by linking thin slices to a text list. The pie acts as a visual anchor while full detail appears in the ranked list. A key statistic (e.g., "97% of revenue = advertising") is often best shown as a large separate callout rather than embedded in the pie.
- **Marks:** Pie slices (wedges), extended leader lines, ranked list below, large number callout.
- **Channels:** Arc angle (percentage of total), color hue (category identity), rank number embedded in large slices, line extensions from small slices to text list.
- **Annotation options:** Rank numbers inside large slices, price-per-click or other metric annotations, leader lines to ranked list for small slices.
- **Data types suited for:** Categorical (categories), quantitative (percentage share, secondary metric), ordinal (ranking).
- **Interesting feature extraction/manipulation:** The combination of pie + ranked list solves the small-slices legibility problem. The large callout is the key message, deliberately separated from the detail data.

---

### Stacked Bar Chart
- **What it shows:** Part-to-whole relationships across categories; total value per primary category AND breakdown by secondary category within each bar. Normalized variant shows proportions (each bar = 100%).
- **When to use:** Two categorical keys + one quantitative value; interested in both totals AND composition; up to ~12 levels in the stacked dimension. Avoid when comparing non-baseline segments (only the bottom segment has an aligned baseline, making it accurate). Avoid more than 12 stacked categories (visual confusion).
- **Interesting properties:** Bottom sub-bar uses aligned position (accurate); other sub-bars use unaligned position (less accurate). The ordering of stacking layers significantly affects what patterns are visible. Normalized variant shows percentage instead of absolute — like many pie charts in a single view but with the more accurate length channel.
- **Marks:** Rectangles (composite glyph of stacked sub-bars).
- **Channels:** Vertical position/length (total value or proportion), color hue (secondary key category), length of each sub-bar (sub-value contribution).
- **Annotation options:** Color legend for secondary key, value/percentage labels on sub-bars, sorted order.
- **Data types suited for:** 1 quantitative value, 2 categorical keys. Absolute counts (standard) or proportions (normalized variant).
- **Interesting feature extraction/manipulation:** Normalizing to 100% creates a pure part-to-whole view; choosing which sub-category goes at the bottom determines which comparisons are most accurate; reorder segments to move segment of interest to the baseline.

---

### Vase Plot
- **What it shows:** Boxplot variant where the width of the central box varies with density — allows detection of multimodal distributions.
- **When to use:** When checking whether a distribution is unimodal vs. bimodal/multimodal. Use when standard boxplot assumptions are violated.
- **Interesting properties:** Adds one additional spatial dimension (width) to standard boxplot encoding. Makes bimodal distributions visible where a boxplot would show only one apparent center.
- **Marks:** Variable-width line/area marks for box body, line marks for whiskers.
- **Channels:** Vertical position (quantitative value), horizontal width (density at each value), horizontal position (categorical key).
- **Annotation options:** Same as boxplot.
- **Data types suited for:** Continuous quantitative distributions, especially when shape is uncertain.
- **Interesting feature extraction/manipulation:** Derive density function; compute KDE or histogram-derived widths per value level.

---

### Waffle Chart / Grid Unit Chart
- **What it shows:** Percentage values shown as fractions of a whole using a 10×10 grid (or other grid) of colored and grey squares. Each square = 1% in a 100-cell grid.
- **When to use:** Showing percentages as fractions of a whole when you want the visual to be proportional and countable. More honest than pie charts for comparing two percentages. Use rows of 10 for immediate Base-10 readability. Avoid when values are not percentages or the audience expects precise comparison.
- **Interesting properties:** Side-by-side waffle charts allow direct comparison of two percentages without a shared axis. Grey squares represent the "remaining" portion, giving immediate context for headroom. Statistical significance can be encoded as small colored dots beneath each grid (CI p.190), adding inferential information without disrupting the primary reading.
- **Marks:** Small squares in a grid (100 per chart for percentages).
- **Channels:** Color fill of squares (percentage value — count of filled squares = the percentage literally), position (each cell = 1% unit), secondary small dots (statistical significance against a comparator).
- **Annotation options:** Percentage value printed below/alongside the grid, category labels, brand logos or labels at row start.
- **Data types suited for:** Quantitative (percentages), part-to-whole, comparative (two or more groups against the same total).
- **Interesting feature extraction/manipulation:** Encoding statistical significance as secondary small-dot markers adds inferential information. Multiple grids arranged as small multiples (3 brands × 7 attributes = 21 grids) can fit on one page.

---

## 2. Categorical / Nominal Data

### Annotated Graduated Scale / Strip Plot
- **What it shows:** Ranking of items along a single continuous quantitative scale, with item icons placed at their value position. Effective for comparing items against thresholds.
- **When to use:** When you want to show where many items fall on a single dimension, especially with strong visual icons for each item. Good for comparing items to thresholds (danger levels, safety limits). Avoid when items cluster too tightly to be legible.
- **Interesting properties:** Central vertical or horizontal scale with color gradient (e.g., red at danger/high, green at low/safe). Items (product photos, logos) placed at exact scale positions on left and right. Threshold annotations placed at relevant scale levels. Splitting left/right by type adds one categorical dimension without visual complexity.
- **Marks:** Graduated bar (the scale), product icon images at scale positions, horizontal arrows pointing from icon to scale.
- **Channels:** Position along axis (quantitative value), color saturation of scale bar (danger level), side of axis (categorical grouping), icon identity (brand/product recognition).
- **Annotation options:** Threshold labels at specific scale values, fact boxes at key positions, chemical structure or other supplementary info in corner.
- **Data types suited for:** Quantitative (single continuous dimension), categorical (item type/brand).
- **Interesting feature extraction/manipulation:** Data deliberately reduced to single dimension only — a simplification that makes the one key comparison immediately clear.

---

### Category Wheel / Radial Category Map
- **What it shows:** A large taxonomy of entities grouped into radial sectors by category. Items (icons, logos) are placed within their category sector.
- **When to use:** For showing a large taxonomy of entities grouped by categories, where the relationship between items is membership in a category. Avoid when precise quantitative comparison is needed.
- **Interesting properties:** Can double as a navigation interface (CI p.47 — clickable wine app wheel). The circular layout creates a sense of a complete ecosystem. Hundreds of company logos in concentric rings create an immediately scannable landscape (CI p.100 — Conversation Prism). Each category is a distinct color segment.
- **Marks:** Icons/logos (item identity), circular sector regions (category boundary).
- **Channels:** Angular position (category membership), color hue (category identity), radial distance from center (informally — smaller/newer items further out), icon identity (brand recognition).
- **Annotation options:** Category labels on outer rim, item names below icons, center label for the overall taxonomy title.
- **Data types suited for:** Categorical (item type), nominal (item identity), relational (membership).
- **Interesting feature extraction/manipulation:** Grouping by functional category rather than alphabetically — the category is the key insight, not the individual rank.

---

### Flower / Petal Diagram
- **What it shows:** Multiple components or sub-categories of a whole, displayed as petals radiating from a center. Petal size is proportional to the value for each activity or component.
- **When to use:** When showing composition of a whole across several named parts in a visually engaging way, especially in infographic or public-facing contexts. Avoid when precise comparison of petal sizes is needed (area perception is inaccurate).
- **Interesting properties:** Highly memorable and visually distinctive. Each entity can have its own flower, enabling small-multiples comparison across entities. Can also show communication modes (petal/wheel chart variant in CI p.67) where each petal carries an icon for the category.
- **Marks:** Petals (custom shapes or arcs radiating from center).
- **Channels:** Size/area of petal (magnitude per activity or category), angular position (which activity/category), color hue (activity type, optional).
- **Annotation options:** Labels on each petal, size scale reference, title per flower for small-multiples, percentage labels.
- **Data types suited for:** One entity with multiple quantitative sub-components (part-of-whole), or categorical membership.
- **Interesting feature extraction/manipulation:** Normalize petal sizes within each flower to show relative composition; keep absolute scale across flowers for cross-entity comparison.

---

### Pie Chart / Donut Chart
- **What it shows:** Relative proportions of parts to a whole (percentages) for one categorical attribute. Donut variant frees the center for a summary label or icon.
- **When to use:** Part-to-whole relationship is the primary task, with very few categories (~2–4 maximum). Only when approximate shares are sufficient. Avoid for comparison across individual segments; avoid for more than 12 categories; avoid side-by-side multiple pies (use normalized stacked bar instead).
- **Interesting properties:** Angle and area both vary with value — both are inaccurate channels. Ranked pie variant (CI p.208) numbers the slices and adds extended leader lines for small slices. Polar area chart (Nightingale coxcomb) is a more accurate alternative that uses bar-like length instead of angle. Globe pie (CI p.31) adds geographic metaphor when the global scope is meaningful.
- **Marks:** Area marks (wedges/arcs).
- **Channels:** Angle (primary quantitative value), area (also varies — less accurate), color hue (categorical identity of each wedge).
- **Annotation options:** Percentage labels, category labels, color legend, explosion of slices for emphasis, center label in donut.
- **Data types suited for:** One quantitative value (normalized/percentage), one categorical key.
- **Interesting feature extraction/manipulation:** Normalization to 100% is required; donut center freed for summary metric or icon anchor.

---

### Word Cloud
- **What it shows:** Frequency distribution of words in a text corpus. Font size encodes word frequency. Best used as an exploratory step rather than a final presentation.
- **When to use:** Qualitative text data where overall themes and relative frequencies matter more than exact counts. Avoid when precise frequency comparison is needed; avoid when the audience might mistake it for quantitative data.
- **Interesting properties:** Color separation of two clouds by sentiment (one green, one red) makes contrast immediately visible without reading individual words (CI p.194). Hypernym-mapping (replacing "wizard" with "magic") is an interesting semantic generalization that makes the word cloud thematically meaningful rather than literally noisy (DS p.153). Position and angle carry no meaning.
- **Marks:** Text words at varying sizes and positions.
- **Channels:** Font size (word frequency), color hue (optional sentiment category or categorical grouping), spatial arrangement (no data meaning — decorative layout).
- **Annotation options:** Title identifying sentiment category, source note.
- **Data types suited for:** Textual/qualitative data, categorical (word types), quantitative (frequency).
- **Interesting feature extraction/manipulation:** Splitting a single text corpus into two sentiment clouds by first filtering positive vs. negative reviews — the comparison between the two clouds is the insight. Prior text cleaning (removing stop words, digits, punctuation) is required. Phrase-level analysis separates "love" from "don't love."

---

## 3. Temporal / Time-Series Data

### Beeswarm Plot
- **What it shows:** Individual items as dots, spread horizontally using force simulation to avoid overlap, positioned along a quantitative x-axis. Shows distribution while preserving individual item identity.
- **When to use:** When showing the distribution of individual data points across categories matters more than summary statistics alone. Better than a histogram when individual item identity should be preserved. Good for medium-sized datasets (hundreds to low thousands). Avoid for very large datasets where dots overlap unresolvably.
- **Interesting properties:** Can be combined with box-and-whisker overlay to show both the forest (summary) and the trees (individuals). Linked dual beeswarm (DS p.339) enables cross-referencing two different questions across the same respondents using brush interaction. The "bounded force layout" split can encode sentiment through vertical position (dripping below = frustration, rising above = no frustration).
- **Marks:** Circles/dots (one per item), optional box-and-whisker overlay.
- **Channels:** X-position (continuous variable), Y-position (categorical or ordinal grouping), color hue (categorical grouping), fill vs. outline (binary attribute), opacity (selection state in linked views).
- **Annotation options:** Box-and-whisker overlaid for summary statistics, category labels on Y-axis, color legend, median line label, quartile values, brushing box for linked filtering.
- **Data types suited for:** Quantitative (continuous variable), categorical (groups), ordinal (levels). Works well for survey data.
- **Interesting feature extraction/manipulation:** D3.js force simulation (forceX, forceY, forceCollide) positions dots to avoid overlap while respecting categorical groupings. Brush-and-filter links two views of the same individuals across two questions.

---

### Climate Stripes / Deviation Stripe Chart
- **What it shows:** Deviation of a quantity from its average over time. Each stripe = one time unit; color encodes direction and magnitude of deviation (e.g., dark red = far above average, dark blue = far below).
- **When to use:** When the trend of deviation over time is the message and you want a visually striking, axis-free format. Best for communication and advocacy contexts. Avoid when readers need exact values.
- **Interesting properties:** No axes needed — the pattern itself communicates the trend. Derived from Ed Hawkins' climate warming stripes — carries strong visual precedent and emotional impact. Semantically novel when applied to non-climate data (e.g., energy consumption patterns).
- **Marks:** Rectangles (vertical stripes, one per time unit).
- **Channels:** Color hue (direction: red = above, blue = below average), color saturation (magnitude of deviation), position on x-axis (time).
- **Annotation options:** Minimal by design; optional year labels at start/end; color scale legend.
- **Data types suited for:** Quantitative deviation from a reference value over ordered time.
- **Interesting feature extraction/manipulation:** Calculate deviation = actual − rolling mean (or long-term mean); map to diverging color scale centered at zero.

---

### Compressed / Non-Linear Timeline (Vacation Timeline)
- **What it shows:** Sparse events over a long time range where the events themselves are the focus, not the gaps. Months with no events are compressed; event months have full space.
- **When to use:** Showing sparse events over a long time range where events are the focus, not the gaps. Also for personal/biographical data. Avoid when precise temporal positioning matters or when the audience needs to compare exact dates.
- **Interesting properties:** The compressed time axis is the key innovation — non-linear time scale that distorts empty periods to give prominence to the data of interest. Internal texture patterns within event rectangles can encode secondary categorical variables (trip type, companions). Blur filter on rectangle edges encodes uncertainty (horizontal blur = uncertain dates; vertical blur = uncertain enjoyment).
- **Marks:** Colored rectangles (one per event), internal texture patterns and person icons overlaid, curved month-dividing lines connecting rows, text annotations for major life events.
- **Channels:** Horizontal position (time within year — compressed/non-linear), vertical position (year/age row), rectangle width (event duration), internal texture/pattern (event type), icon overlay (companion identity), blur direction and intensity (uncertainty).
- **Annotation options:** Life event annotations on side, legend explaining all visual touches, hover tooltip highlighting same month across all years.
- **Data types suited for:** Temporal (dates, duration), categorical (event type, companions), binary (uncertainty), biographical narrative.
- **Interesting feature extraction/manipulation:** Non-standard time scale transformation compressing months by vacation presence/absence. Uncertainty (forgotten details) encoded as a visual property rather than excluded.

---

### Line Chart / Time-Series
- **What it shows:** Trends in a quantitative value over an ordered key (usually time). Connection marks strongly imply trend.
- **When to use:** One quantitative value, one ordered key. Primary task is spotting trends. Avoid for categorical x-axis (falsely implies trend — Zacks & Tversky found line charts for categorical data elicited false trend language). Avoid too few data points (bar or dot chart clearer).
- **Interesting properties:** Aspect ratio matters critically — "banking to 45°" maximizes angle accuracy (lines near 45° angle are most perceptually accurate). Multiscale banking reveals structure at multiple frequencies. Superimposed lines: up to ~dozen series on one shared frame; best for local maximum tasks. Multiple small line charts in a grid (small multiples) compare across categories.
- **Marks:** Point marks + connection line marks between them.
- **Channels:** Vertical spatial position (value), horizontal spatial position (ordered time key), color hue/shape (additional categorical attribute for multiple series), opacity (density in crowded displays).
- **Annotation options:** Trend lines (LOESS/regression), confidence bands, annotations at notable events, aspect ratio adjustment (banking to 45°), highlighted time points.
- **Data types suited for:** One quantitative value, one ordered key (time, ordinal). Time-series tables.
- **Interesting feature extraction/manipulation:** Banking to 45° as aspect ratio derivation; locally weighted regression (LOESS) as derived trend overlay; derive difference attribute (e.g., trade balance = exports − imports) and encode directly rather than both raw series — reduces perceptual demand for comparison.

---

### Multi-Track Horizontal Timeline
- **What it shows:** A long horizontal timeline with multiple parallel horizontal tracks (themes, actors, categories). Each track has annotated image or text blocks at specific dates.
- **When to use:** Historical topics with multiple parallel narrative threads evolving over the same time period. When both sequence and thematic grouping of events matter. Long-lifespan topics are ideal.
- **Interesting properties:** Three simultaneous tracks allow the viewer to follow one strand or read across all tracks at a given time period for context (CI p.121 — "Visual History of Halloween"). The track metaphor is borrowed from music notation — each "instrument" plays its own melody along the same time axis.
- **Marks:** Image thumbnails, text annotation blocks, horizontal track lines, date markers.
- **Channels:** Horizontal position (time), vertical position (thematic track — categorical), color coding per track.
- **Annotation options:** Date labels, event names, descriptive paragraphs, source citations.
- **Data types suited for:** Temporal, categorical (track/theme), qualitative/narrative.
- **Interesting feature extraction/manipulation:** Editorial curation — selecting which events are significant enough to include requires abstracting a large body of historical knowledge.

---

### Scrollytelling Dot Stream
- **What it shows:** Individual items (dots) that animate between layouts on scroll, guiding the reader through a narrative sequence of analytical steps. Each scroll event transitions from one organizational frame to another.
- **When to use:** Narrative-driven data essays where pacing and viewer guidance through a sequence of analytical steps matters. Avoid for analytical audiences who need free exploration — animation can disorient and stable reference frames are preferred.
- **Interesting properties:** The transition between layouts IS the insight — watching items reorganize from one frame to another reveals structural change. Force simulation positions dots dynamically on scroll. Delight-focused animation (non-informational) increases engagement. Progress bar animates in sync with audio playback for linked media experiences.
- **Marks:** Dots (each = a set of aggregated items or events).
- **Channels:** Dot size (count of items represented), color (categorical identity), position (changes per scroll event to support the narrative).
- **Annotation options:** Hover shows detail. Song lyrics or other text in the article are clickable to trigger audio + progress bar. Songs or categories highlighted and faded on/off as story references them.
- **Data types suited for:** Temporal/sequential, categorical, quantitative (count).
- **Interesting feature extraction/manipulation:** Aggregating many individual items into runs of consecutive same-category items (e.g., consecutive same-character lyric lines) was the key abstraction that made the visualization manageable.

---

### Small Multiple Histograms with Smoothed Density Overlay
- **What it shows:** Distribution of a variable across multiple discrete panels (time points, groups, conditions), displayed side by side to show how the distribution has shifted.
- **When to use:** Comparing how the shape of a distribution changes across discrete conditions. Overlaying a smoothed density curve on top of the histogram helps compare overall shape at a glance.
- **Interesting properties:** The smoothed density curve (KDE) layered over the histogram provides shape comparison affordance that raw histograms alone do not. Keeping all panels the same color reduces visual competition with the primary message.
- **Marks:** Bars (histogram bins), smooth curve (density estimate).
- **Channels:** X-position (quantitative attribute), bar height (count per bin), curve shape (smoothed distribution), panel position (condition/time grouping).
- **Annotation options:** Panel labels for the conditioning variable.
- **Data types suited for:** Quantitative (distribution variable), categorical/ordinal (the faceting condition).
- **Interesting feature extraction/manipulation:** Appending data across time periods or groups before faceting; kernel density estimation as the smoothing manipulation.

---

### Spiral Step-Chart (per event sequence)
- **What it shows:** A sequence of events in order along an Archimedean spiral. Each event is a dot placed equidistantly along the spiral. Compact enough to show many sequences side by side on one page.
- **When to use:** When a compact, circular representation of a long sequential event sequence is needed — especially for comparing many sequences simultaneously. Avoid when within-sequence pattern recognition is the primary goal (spirals make repeating patterns hard to see vs. a linear layout).
- **Interesting properties:** The spiral is continuous — unlike a multi-row layout, it never breaks the sequence. Varying arc length between dots requires a brute-force iterative algorithm for equidistant placement. Circle size can encode difficulty level (smaller = harder), creating a visual pun. Spiral total radius can encode sequence length. Overlay blend modes allow stacking multiple event types.
- **Marks:** Filled circles (one per event).
- **Channels:** Position along spiral (temporal sequence), color hue (event type/direction), circle radius (difficulty or level), spiral total size (sequence total length).
- **Annotation options:** Color legend, expand button for detail view, filter by event type.
- **Data types suited for:** Temporal/sequential (event sequences), categorical (event types, difficulty levels).
- **Interesting feature extraction/manipulation:** Mapping multiple difficulty/mode combinations on top of each other using blend modes allows simultaneous view of all levels. Equidistant placement along the spiral requires pre-computation.

---

### Streamgraph / Stacked Area Chart
- **What it shows:** Evolution of multiple categorical components over an ordered axis (usually time). Total and part-whole proportions simultaneously. Streamgraph variant centers the baseline for a flowing, organic visual appearance.
- **When to use:** Showing how composition of a total changes over time; multiple time series that sum to a meaningful total; when the continuous flow and changing relative proportions matter more than precise value lookup. Avoid when precise value reading is important; avoid when there are few categories.
- **Interesting properties:** Bottom layer uses aligned position (accurate); upper layers use unaligned position (less accurate). Streamgraph variant uses an organic curved baseline optimized for overall silhouette shape. Layer order derived from data (volatility or onset time). ThemeRiver variant scales to many categories because sparse layers don't occupy the full timeline.
- **Marks:** Area marks (one area per category, stacked).
- **Channels:** Area (quantitative — part of total at each time point), color hue (categorical — which component), position x (ordered time key), layer height (quantitative value per layer).
- **Annotation options:** Category labels at end of bands, interactive highlighting of individual streams, hover tooltips.
- **Data types suited for:** Tables with a categorical key (component) + temporal key (time) + quantitative value (amount).
- **Interesting feature extraction/manipulation:** Aggregate by time period; normalize to percentage of total for relative view; derive layer ordering by volatility or onset time; step-curve variant (d3.curveStep) creates clean rectangular steps that make boundaries more distinct.

---

## 4. Relational / Network / Hierarchical Data

### Adjacency Matrix View
- **What it shows:** Network adjacency as a 2D matrix, with one node per row and column. A filled area mark = link exists; empty = no link. Can encode link weights with color.
- **When to use:** Dense networks (edges up to N²) where node-link becomes a hairball. When node label lookup, degree inspection, or clique detection are important tasks. Perceptually scalable to 1M+ edges.
- **When to avoid:** When path tracing between nodes is the primary task (node-link is better). When users lack matrix-reading training. When the network is sparse and small.
- **Interesting properties:** Completely eliminates edge-crossing occlusion. Stable and predictable screen space. Reordering rows/columns reveals structure: cliques = diagonal square blocks; bicliques = off-diagonal blocks; degree = row/column fill count. Can be combined with node-link in hybrid views (NodeTrix).
- **Marks:** Area marks (cells in 2D matrix alignment).
- **Channels:** Spatial position (row = node, column = node — matrix alignment), color/luminance (link presence/absence or weight).
- **Annotation options:** Row/column labels, color of cells for additional attributes, reordering controls, cluster dendrograms alongside.
- **Data types suited for:** Network data; social networks; biological interaction networks; co-occurrence matrices.
- **Interesting feature extraction/manipulation:** Network → derived table (two key attributes: node lists; one value: link indicator). Reordering by hierarchical clustering is a critical transformation that reveals block structure.

---

### Bipartite / Connection Matrix Flow Diagram
- **What it shows:** Many-to-many connections between two categorical sets (food and wine, food and ingredients, species and sites) shown as curved lines connecting items on two rows or columns.
- **When to use:** Showing many-to-many relationships between two categorical sets where the number of connections is moderate. Avoid when connections are too dense (lines become unreadable).
- **Interesting properties:** Using illustrated icons (realistic food and bottle drawings) instead of abstract marks makes connections semantically legible without reading labels. Colored lines group by one set. A "hard to match" or "no connection" footer section is an elegant way to show absence.
- **Marks:** Illustrated icon glyphs (items in each set), curved colored lines (connections).
- **Channels:** Horizontal position (item identity in each set), color of line (category within one set), line presence/absence (compatibility relationship).
- **Annotation options:** Description labels within marks, category labels, footer section for exceptions.
- **Data types suited for:** Categorical (two sets), relational (compatibility/occurrence links).
- **Interesting feature extraction/manipulation:** Binary simplification — either a connection exists or it does not. Degree of connection or weight is often abstracted away for clarity.

---

### Chord Diagram (Standard)
- **What it shows:** Flows or connections between a group of entities; quantitative flow strength between pairs. Outer arcs show each entity's total flow volume; inner chords connect pairs with thickness encoding flow magnitude.
- **When to use:** When you have bidirectional or directional flows between a fixed set of entities (N × N matrix). Works well when N is small (4–10 entities). Use when which pairs are most strongly connected is the primary question.
- **When to avoid:** When N is large (too many arcs); when flows are all similar in magnitude; when the audience needs to read exact values.
- **Interesting properties:** "Often tricky to understand but can display a wealth of information" (DS p.34). The outer arcs show total flow volume; inner chords show pairwise magnitudes. Radial arrangement conveys the sense of a closed system.
- **Marks:** Arcs (outer segments), filled curved bands/chords (inner connections).
- **Channels:** Arc length (total flow volume for that entity), chord thickness (bidirectional flow magnitude), color (entity identity), position on circle (entity).
- **Annotation options:** Labels on arcs, value annotations, hover highlights.
- **Data types suited for:** Quantitative (flow volumes), categorical (entities), relational (pairwise connections).
- **Interesting feature extraction/manipulation:** Underlying data is an N×N matrix of flows; the matrix must be aggregated from raw transaction data before use.

---

### Chord Diagram — Custom Variant: "Loom and Strings"
- **What it shows:** How many of something (e.g., words spoken) each entity in a central group distributed across a set of peripheral contexts (e.g., locations). All strings flow from the outer ring toward the center, where the inner group is placed. Derived from the standard chord diagram but invented for this specific semantic.
- **When to use:** When showing how a set of actors distributes across a set of contexts, where one group is "central" and the other "peripheral." Good for showing how a small set of entities (characters, species) distributes across a larger set of categories (locations, time periods).
- **When to avoid:** When the connection data is symmetrical (standard chord diagrams handle that better). Not suitable when exact values are needed rather than relative magnitudes.
- **Interesting properties:** Named "Loom and Strings" by Nadieh Bremer (named with input from Mike Bostock). The center is split into two halves (left/right) to give the strings room to flow naturally. Locations are ordered clockwise by when they first appear — adding a temporal layer. Font choices can reinforce thematic identity (Elvish/Dwarvish scripts for Lord of the Rings).
- **Marks:** Curved strings (Cubic Bézier curves), outer arcs per context, text labels in center per entity.
- **Channels:** Thickness of string (quantitative: amount per entity per context), color of string/arc (context identity), position on outer ring (context, ordered by narrative chronology), position in center (entity identity).
- **Annotation options:** Hover tooltip on entity shows text paragraph of insights, hover on context highlights which entities appear there, outer arc values show totals per context.
- **Data types suited for:** Quantitative (word count or flow), categorical (entities, contexts), relational (who did what where).
- **Interesting feature extraction/manipulation:** Underlying data must be aggregated to entity × context level. Context variable may need to be manually added to the dataset. Filtering to key entities simplifies without losing the core story.

---

### Fight Sequence Network / Parallel Timeline with Bezier Connectors
- **What it shows:** How individual entities (characters, items) move through a sequence of events, showing which events they cluster into and how they connect across consecutive events. Events are circles/clusters; entities are connected across events by Bézier curves of varying thickness.
- **When to use:** When you want to show how individual entities move through a sequence of events, and how those events cluster. Effective for narrative data where temporal order and group membership per event both matter.
- **When to avoid:** When the number of entities or events is so large that connecting lines become an indistinguishable mass.
- **Interesting properties:** Lines vary in thickness (thin at event circles, broad at the bend between events) — achieved by creating a closed SVG path rather than a simple stroke. Swoosh direction can encode alignment/allegiance: good vs. bad sides of a conflict (left vs. right swoosh), allowing viewers to instantly identify allegiance shifts. Transformation levels or status can be encoded as concentric rings around entity circles. Embedded GIF thumbnails link to source media at key events.
- **Marks:** Overlapping circles (entities in an event), closed Bézier path areas (character trajectories), concentric rings (status level), animated GIF thumbnails.
- **Channels:** X-position (story arc/saga column), Y-position (event order within saga), color hue (entity identity), number of concentric rings (status level), swoosh direction (good/bad alignment).
- **Annotation options:** Hover expands the event cluster with tooltip; manual annotations on key events; animated GIFs linked to timestamps; mini-map panel for navigation context.
- **Data types suited for:** Sequential/temporal, relational (who participated in which event), categorical (alignment, status), hierarchical (arc > event > participant).
- **Interesting feature extraction/manipulation:** Reshape data from one-row-per-event to one-row-per-entity-per-event before visualization.

---

### Hierarchical Edge Bundles
- **What it shows:** A compound network (call graph, dependency graph) where edges are routed along a hierarchical spine to reduce visual occlusion. Three superimposed layers: tree structure (back), network edges (middle), nodes (front).
- **When to use:** Compound networks where both a base network and a cluster hierarchy over nodes exist, and distinguishing tree structure from network connections is important. When edge crossings in a plain network create visual confusion.
- **When to avoid:** No underlying hierarchy; few nodes (overkill); sparse networks where edges don't benefit from bundling.
- **Interesting properties:** Bundling reduces occlusion the way cable ties bundle physical wires. Color distinction between the tree/nodes layer (gray) and network edges (red/green) ensures all layers remain readable. The edge tension parameter controls how tightly edges follow the hierarchy.
- **Marks:** Containment circle marks (hierarchy/tree, back layer), connection link marks (network edges, middle layer), point marks (nodes, front layer).
- **Channels:** Color hue (gray = tree/nodes vs. hue = network edge type), line curvature (bundling), color saturation (foreground vs. background distinction).
- **Annotation options:** Node labels at leaf positions, hover to highlight incident edges, color coding by direction.
- **Data types suited for:** Compound graph: network + hierarchy whose leaves are network nodes.
- **Interesting feature extraction/manipulation:** Edge bundling uses tree hierarchy to route edges; back-to-front rendering order via z-planes.

---

### Language Similarity Network
- **What it shows:** Pairwise similarity between entities (languages, species, sites) as a node-link network where lines connect pairs that share something in common. Multiple shared items between a pair = multiple lines with progressively increasing curvature.
- **When to use:** For showing pairwise similarity or shared membership between a modest number of nodes (under ~15–20). Avoid when nodes are numerous — the network becomes a hairball. Avoid when similarity is gradational (use a heatmap instead).
- **Interesting properties:** Multiple links between two nodes use progressively increasing curvature rather than thicker lines, allowing each link to be individually labeled. Clicking a node moves it to center and animates all connected links. Interactivity reveals cluster structure (e.g., Romance languages form the highest-similarity cluster).
- **Marks:** Circles (nodes), curved lines (pairwise links), text label on each link.
- **Channels:** Number of lines between nodes (degree of overlap/similarity), line curvature (disambiguation of multiple links), node position (click/animate to center for detail), color/highlight (hover state).
- **Annotation options:** Link text label (the shared item or dimension), node labels, language/entity names.
- **Data types suited for:** Relational (pairwise shared attributes), categorical (entities, shared items).
- **Interesting feature extraction/manipulation:** The similarity link is computed from a join operation on ranked lists per entity — only the shared items appear as links.

---

### Node-Link Network Diagram
- **What it shows:** Network or tree topology — nodes as items, links as relationships. Spatial layout encodes proximity/grouping via layout algorithm.
- **When to use:** Networks up to ~hundreds of nodes (simple algorithms) or thousands (multilevel). Tasks involving topology: path tracing, neighborhood exploration, finding bridges/cliques. Trees with all depth levels to show.
- **When to avoid:** Dense networks (L > 4N) — degenerates into hairball. Very large networks (10,000+ nodes). When node label lookup speed matters (adjacency matrix is better). Genealogy networks require temporal embedding to "pull apart" the hairball.
- **Interesting properties:** Force-directed placement is nondeterministic; spatial proximity can indicate clustering but may be an artifact. Spatial position does NOT directly encode attributes in force-directed layouts. Strahler number (a derived centrality metric) can filter peripheral nodes to show the structural skeleton even from 500,000+ nodes. Genealogy visualization (DS p.119) embeds birth year on the horizontal axis and family proximity on vertical — a forced layout that gives interpretable axes.
- **Marks:** Point/glyph marks (nodes), line marks (links/edges).
- **Channels:** Position (layout algorithm or deliberate encoding of tree depth/time), size (node degree or importance), color hue (node category or cluster), line width (edge weight), line style (edge type — solid=blood/dotted=marriage), opacity (distance from focus node).
- **Annotation options:** Node labels, edge weight via line width, color coding, size coding, interactive highlighting on search, hover for detail.
- **Data types suited for:** Network data (general graphs), tree data (hierarchical), genealogical, social, biological networks.
- **Interesting feature extraction/manipulation:** Derive centrality (Strahler number, hop distance to key nodes) to filter and color edges. Multilevel approach for compound networks. Birth date estimation for missing records (death date minus 60 years, or inferred from family relationships).

---

### Process Flow / Flowchart
- **What it shows:** Sequential or branching processes, without necessarily any numerical data. Standard flowcharts use shape conventions: rounded rectangles = start/end, rectangles = process steps, diamonds = decision points.
- **When to use:** Formal process documentation; when precision and standardization matter; when explaining steps to a non-technical audience. Avoid when you want engagement — standard flowcharts become generic at scale.
- **Interesting properties:** Illustrated character process paths (CI p.187) replace abstract process boxes with human figure glyphs performing each action — the viewer immediately understands the activity by seeing a person do it. Color coding of actors (blue=Affiliate, orange=Merchant) makes who-does-what immediately readable.
- **Marks:** Rectangles, diamonds, rounded rectangles, directed arrows; optionally human figure glyphs and isometric path tiles.
- **Channels:** Shape (step type), arrow direction (flow sequence), color hue (actor identity or process phase).
- **Annotation options:** Step name inside shape, Yes/No labels on decision arrows, character name labels, step description callouts.
- **Data types suited for:** Sequential/ordinal (process steps), categorical (actor roles, step types).
- **Interesting feature extraction/manipulation:** Reducing a complex multi-party process to color-coded actor roles; collapsing decision branching into simplified paths.

---

### Radial Manga / CCS Multi-Ring Circular Layout
- **What it shows:** Many-to-many relationships between two entity sets (characters × episodes/chapters) where one set is arranged as pills on an outer ring and the other as segments in an inner ring. Curved arcs connect the two sets. Color of outer ring elements derived from K-means color extraction on source images.
- **When to use:** When showing many-to-many relationships between two entity sets and when circular organization reflects a meaningful structure (e.g., sequential chapters in a ring). The donut/ring metaphor works especially well for media with defined episodes.
- **When to avoid:** When the number of entities or episodes is very large (lines become unreadable). When straight linear ordering would be clearer.
- **Interesting properties:** Chapter arc colors derived from K-means color extraction in LAB space from cover images — the color of each chapter arc reflects the actual dominant color palette of that chapter's artwork. On hover: only connections belonging to the hovered item are shown; all others fade. Inner character segments carry annotated relationship text on hover (a third layer of data). Bidirectional hover (character → chapters and chapter → characters) gives two perspectives on the same data.
- **Marks:** Arcs (chapter pills; volume groupings), circles (character segments in inner donut), curved connection paths, central image area (chapter cover on hover), CMYK dot clusters (color palette encoding on outer ring).
- **Channels:** Angular position (sequential order of chapters), arc color (dominant color palette of chapter cover art), inner segment (character identity), line color (relationship type), arc thickness (optional).
- **Annotation options:** Story annotations placed radially using d3-annotation.js; legend diagram explaining all rings; hover-reveal text on relationship lines.
- **Data types suited for:** Many-to-many relationship data (characters × chapters), image-derived color data, categorical sequence data.
- **Interesting feature extraction/manipulation:** K-means clustering in LAB color space applied per cover image; k chosen visually (inspect 3–11 clusters per image, pick best by eye). Output = hex codes + percentage share per color cluster → drives the colored arc fill.

---

### Sankey Diagram [from student report]
- **What it shows:** Flows or transformations between two sets of categories (source → destination). Thickness of links encodes flow quantity. Nodes identify individual sources and destinations.
- **When to use:** Showing flows or transformations between two categorical sets (supply chain, resource allocation, material flows, energy systems). When shared dependencies between destinations need to be visible. Avoid when there are many crossing flows creating visual clutter.
- **Interesting properties:** When multiple materials are shared between two product types, the Sankey makes shared dependencies immediately visible as flows touching multiple destination nodes. Icons on destination nodes add semantic clarity without extra text. Works for 10–50 source nodes; degrades with more.
- **Marks:** Rectangles (nodes for sources and destinations), flowing bands/links (flows).
- **Channels:** Width/thickness of links (flow quantity), position (left = sources, right = destinations), color of nodes (source/material type or identity).
- **Annotation options:** Node labels with source/destination names, icon overlay on destination nodes, thickness legend.
- **Data types suited for:** Flow data between two categorical sets. Best when flows can be quantified.
- **Interesting feature extraction/manipulation:** Identifying which source items are shared between multiple destinations requires a join across product-level data. Shared dependencies become a primary visual signal.

---

### Treemap
- **What it shows:** Hierarchical data using nested rectangles. Area of each rectangle encodes a quantitative value (e.g., file size, budget, species count). Color encodes a second attribute.
- **When to use:** Hierarchies with important leaf-level attributes; shallow hierarchies; spotting outliers of large attribute values. When space-filling is important. When part-of-whole proportions at multiple levels matter.
- **When to avoid:** Deep hierarchies (nested rectangles become tiny); when path-based navigation through the hierarchy is primary (containment marks are weaker than connection marks for this); when exact area comparisons are needed.
- **Interesting properties:** Space-filling layout uses all available pixels. Squarified treemap algorithm optimizes aspect ratios for readability. BBC-o-Gram (CI p.182) uses color coding to separate categories without a separate legend panel. Interactive drill-down enables zoom to subtrees. Spatially ordered treemaps can embed geographic ordering.
- **Marks:** Area marks (nested rectangles with rectilinear layout), containment marks.
- **Channels:** Spatial position (nesting structure + rectilinear area allocation), area/size (quantitative leaf attribute), color (additional attribute — category or continuous value).
- **Annotation options:** Color coding by attribute or cluster, label overlays when rectangles are large enough, hover tooltips, zoom to subtree, color scale legend.
- **Data types suited for:** Tree/hierarchical data with quantitative leaf attributes; file systems; biological taxonomies; budget hierarchies; species richness nested by group.
- **Interesting feature extraction/manipulation:** Area is derived from a quantitative attribute (normalizing to proportion of total). Layout algorithm distributes rectangular space proportionally. Editorial filtering reduces cognitive load while preserving the proportional story.

---

### Tree Visualization — Icicle Tree
- **What it shows:** Tree hierarchy with depth encoded by one spatial dimension (vertical) and parent–child relationships + sibling order by the other (horizontal). No connection marks — relationships inferred from spatial alignment.
- **When to use:** When both depth and sibling ordering matter; when containment or connection marks are not desired. Better than indented outline for spatial comparison of sizes across levels.
- **When to avoid:** Very deep or very wide trees (cells become too small).
- **Interesting properties:** Uses only spatial position channels (both axes), no connection or containment marks needed for structure. Proportional width allocation can encode node size attribute simultaneously.
- **Marks:** Area marks (rectangular cells, one per node).
- **Channels:** Vertical spatial position + size (tree depth), horizontal spatial position (parent–child + sibling order).
- **Annotation options:** Color by attribute, labels inside cells, zoom/filter for subtrees.
- **Data types suited for:** Tree/hierarchical data; file systems; biological taxonomies.
- **Interesting feature extraction/manipulation:** Width allocation proportional to subtree size can encode a second quantitative attribute.

---

### Tree Visualization — Concentric Circles / Radial Space-Filling (InterRing)
- **What it shows:** Radial version of icicle. Depth encoded as radial distance from center; sibling relationships encoded by angular position. Interactive distortion enlarges selected subtrees while shrinking siblings.
- **When to use:** Exploring hierarchies; navigation, selection, rollup/drilldown. When radial layout is aesthetically or spatially preferable; for relatively shallow trees.
- **When to avoid:** Very deep or wide trees. When precise size comparison is needed (arc areas harder to compare than rectangles).
- **Interesting properties:** ~3× more legible labels than classical node-link at the same label size. No connection marks — parent–child relationship conveyed by angular containment within the parent's arc sector. Interactive distortion dynamically reallocates space; supports rollup/drilldown as an in-place operation. Angular width can be proportional to subtree size.
- **Marks:** Area marks (arc sectors / concentric rings).
- **Channels:** Radial spatial position (tree depth), angular spatial position (link relationships + sibling order), arc size (tree depth proportional to ring width), color (attribute or structure).
- **Annotation options:** Color by attribute, labels along arcs, interactive zoom, focus indicators.
- **Data types suited for:** Tree data; evolutionary phylogenies; hierarchical cluster results.
- **Interesting feature extraction/manipulation:** Angular width allocation can be proportional to subtree size or node count. Enables rollup/drilldown interactivity.

---

### Viral Sharing / Radial Tree
- **What it shows:** Exponential diffusion or network propagation — one source node at center, expanding rings of nodes connected by edges showing sharing/branching.
- **When to use:** When the message is about reach and growth structure, not about which specific nodes are connected. Avoid when you need to show real network topology.
- **Interesting properties:** All nodes are identical (no differentiation), so visual emphasis is entirely on structural growth pattern. The radial layout makes exponential explosion visually immediate. Abstracting real social network data into a uniform tree model removes complexity but makes the core exponential principle legible.
- **Marks:** Person-icon glyphs or circles (nodes), thin lines (edges/connections).
- **Channels:** Position (radial distance from center = generation number), structure (number of connections = branching factor).
- **Annotation options:** Generation labels, count of nodes per ring, percentage reach estimates.
- **Data types suited for:** Network/relational, temporal (generation sequence).
- **Interesting feature extraction/manipulation:** Abstracting real network data into a uniform tree model to make the exponential principle legible.

---

### Word Tree
- **What it shows:** A hierarchical tree of keywords laid out horizontally, preserving context of keyword usage within original text. Shows patterns of how a keyword appears in different contexts.
- **When to use:** Understanding the context and patterns of keyword usage in a text corpus. When semantic context matters more than frequency.
- **When to avoid:** Very large corpora with many divergent contexts (visual clutter). When frequency comparison is the primary task.
- **Interesting properties:** Combines a visual encoding idiom (horizontal hierarchical tree) with an interaction idiom (navigation by keyword selection). The encoding and interaction idioms are tightly coupled. Text is transformed into a tree structure — an example of dataset-type transformation.
- **Marks:** Text labels arranged as tree nodes, lines connecting branches.
- **Channels:** Position (horizontal = depth/proximity in text context), indentation (hierarchy level), branch direction (context variation).
- **Annotation options:** Selected keyword highlighted, navigable branching paths.
- **Data types suited for:** Text corpus (derived as a tree structure via parsing).
- **Interesting feature extraction/manipulation:** Text → tree structure transformation with quantitative frequency attributes per node.

---

## 5. Spatial / Geographic Data

### Animated Dot Map
- **What it shows:** Spatial change over time for continuous surface data, encoded as many circles pulsating across an animated sequence of time frames. Each geographic location = one circle; size and opacity encode the field value.
- **When to use:** When showing spatial change over time, especially when animation communicates temporal pattern better than static small multiples. Avoid for precise value reading — animation is for impression, not measurement.
- **Interesting properties:** Circle size AND color opacity both encode the same variable (e.g., vegetation health), creating redundant encoding that reinforces the signal. Multiply color blend mode darkens overlapping circles. No country borders — geography emerges from the data pattern alone. The animation gives a "breathing" impression for seasonal data.
- **Marks:** Circles (one per sampled geographic location, ~50k locations).
- **Channels:** Size (field value), color (green intensity mapped to health value), opacity (also field value — redundant), position (geographic, fixed).
- **Annotation options:** Minimal — only title, legend, brief text. The visual is self-explanatory.
- **Data types suited for:** Quantitative (continuous field value 0–1), spatial (geographic), temporal (weekly/seasonal, animated).
- **Interesting feature extraction/manipulation:** Downsampling from millions of pixels to ~50k non-water locations while preserving spatial resolution for pattern legibility. Color blend mode (multiply) creates natural-looking color layering.

---

### Choropleth Map
- **What it shows:** Geographic regions colored or shaded by a quantitative or categorical attribute; one region = one item.
- **When to use:** Showing spatial distribution of an attribute across regions; identifying geographic clusters or patterns; when the geographic distribution IS the insight.
- **When to avoid:** When region size is highly variable (large regions dominate visually regardless of their values — MAUP problem); for precise quantitative comparison; when attributes are raw counts rather than normalized values.
- **Interesting properties:** Sequential segmented colormap provides discrete levels that aid region comparison. "Shift from 2008" view (CI p.58) shows change rather than absolute values, revealing where opinion moved. Design choice of region granularity significantly affects visual interpretation. Cartogram variant distorts region area to normalize by population.
- **Marks:** Filled areas (region boundaries from given geometry).
- **Channels:** Color saturation/hue (ordered quantitative magnitude or categorical winner), geographic position (fixed by given geography).
- **Annotation options:** Text labels on regions, legend, reference lines, highlighted region outlines, separate ranked bar or table with values.
- **Data types suited for:** Quantitative (normalized) per-region attributes, categorical (regional classification), geographic/spatial datasets.
- **Interesting feature extraction/manipulation:** Spatial aggregation — choosing region granularity (country, county, grid cell) changes what patterns are revealed. Normalizing counts by area or population is a critical derived attribute step. Derive a "change" or "deviation from national average" attribute for a more insightful encoding.

---

### EU Map with Overlay Bar Chart Boxes [from student report]
- **What it shows:** A geographic map as base layer with small overlay boxes positioned near specific locations, each containing a bar chart of metrics for that location.
- **When to use:** When geographic position is meaningful and you want detail-on-demand for specific locations without cluttering the map itself. A "small multiples in geographic space" approach.
- **When to avoid:** When overlay boxes obstruct each other or important geographic features. When the number of locations is very large.
- **Interesting properties:** The blend of two visual idioms (map + bar chart) is uncommon but effective. A "blur transition" from a wider map to a detailed regional map on clicking a location is a novel navigation mechanism.
- **Marks:** Rectangles (entity markers), bars within overlay boxes (metric values), splines connecting vendors/plants.
- **Channels:** Color hue (entity type), geographic position (real-world location), bar length (performance metrics), color within bars (on-time vs. late breakdown).
- **Annotation options:** Hover on rectangles for name and location; return button for transition; percentage labels in bar charts.
- **Data types suited for:** Geographic point data with associated quantitative metrics; bipartite relationships between two sets of entities.
- **Interesting feature extraction/manipulation:** Derived composite metrics from multiple date fields (e.g., total inbound lead time = production + transportation + receipt processing).

---

### Globe Pie / Proportional Globe Segment
- **What it shows:** One value as a proportion of a global total, shown as a partial globe colored vs. grey. The globe metaphor reinforces global scope.
- **When to use:** When one value is a subset of a global total and geographic/worldwide framing adds meaning. Avoid when the ratio is not globally meaningful.
- **Interesting properties:** Using a 3D globe instead of a flat pie chart adds geographic metaphor weight. The grey-vs-color contrast is stark. Semantically novel — the shape carries meaning beyond the data.
- **Marks:** Globe area (3D sphere segment or 2D globe illustration).
- **Channels:** Color hue (connected/not-connected, or included/excluded), area proportion (fraction of sphere).
- **Annotation options:** Large numerals, labels for each segment.
- **Data types suited for:** Quantitative ratio (part-to-whole), spatial (global).
- **Interesting feature extraction/manipulation:** None — the ratio is the data; the globe form is a semantic choice.

---

### Google Trends Travel Map + Time Breakdown
- **What it shows:** For a selected target entity, which source entities (countries, regions) show the most interest, displayed on a geographic map by volume. A second view breaks down interest by year. Topic categories further detail what aspects are most searched.
- **When to use:** When geographic distribution of interest/behavior is the primary question. Pair with a time view when temporal change also matters.
- **Interesting properties:** Data gathered in reverse — starting from "target" entities and working back to "source" entities to match how the API works. Hundreds of Knowledge Graph "types" collapsed to ~8 meaningful categories through automated + manual mapping. Both views animate simultaneously through time in the linked version.
- **Marks:** Geographic regions/countries (choropleth or sized symbols on map), topic marks (dots by category).
- **Channels:** Geographic position (source entity location), color saturation or size (interest volume), color hue (topic category: city/nature/person/etc.).
- **Annotation options:** Topic names as labels, year-by-year time series for drill-down, source-entity labels on hover.
- **Data types suited for:** Spatial (countries), temporal (yearly), categorical (topic categories), quantitative (search interest score 0–100).
- **Interesting feature extraction/manipulation:** Relative popularity scores (0–100) are used — not absolute counts. Eight summary categories manually derived from 252 Knowledge Graph types, with automated mapping for ~95% and manual assignment for the remaining 5%.

---

### Interactive Choropleth with Real-Time Updates
- **What it shows:** Geographic map data updated in real time (e.g., election results by county as they come in). Filter controls change the view (by size of lead, shift from prior period, etc.).
- **When to use:** Live events where data streams in over time; when showing change relative to a prior baseline adds analytical value. Avoid when precise value comparison is needed.
- **Interesting properties:** "Shift from 2008" view (CI p.58) shows change rather than absolute values, revealing where opinion moved. Zoom is supported. Summary tallies shown at top alongside the map. Animated transitions as results update.
- **Marks:** Filled polygons (counties/states).
- **Channels:** Color hue (categorical winner — party), color saturation (margin of victory / ordered magnitude), geographic position (given).
- **Annotation options:** State borders, numeric vote totals at top, filter labels on sidebar, zoom controls.
- **Data types suited for:** Spatial (geographic), categorical (party/winner), quantitative (vote share, margin).
- **Interesting feature extraction/manipulation:** Derived "shift" attribute (change from prior period) as an alternative to absolute values; monthly aggregation of individual transactions.

---

### Proportional Circle Map / Cartogram
- **What it shows:** Revenue, quantity, or other quantitative values by geographic unit, using circle size rather than geographic area to represent magnitude. Hierarchical structure (area → nation/region) can be encoded through spatial grouping.
- **When to use:** When geographic hierarchy is important and you want quantity to drive visual weight (not geographic area). When the number of entities is too large for a standard map but too structured for a plain treemap.
- **Interesting properties:** Tile-within-sector layouts (CI student report p.6) are a non-standard hybrid between treemap and pie chart. Adding a "dot on tile" overlay for a secondary variable is an elegant multi-channel design that avoids overplotting because size and dot operate on different visual channels.
- **Marks:** Sector slices (area groupings), tiles within sectors (individual entities), dots on tiles (secondary variable).
- **Channels:** Tile area (primary quantitative variable), color hue (group/area identity), dot size (secondary quantitative variable), spatial position within circle (area/group identity).
- **Annotation options:** Area labels, entity name labels on tiles, dot size legend, hover tooltips.
- **Data types suited for:** Hierarchical quantitative data (value by area and entity). Requires pre-computation of tile areas proportional to quantity.
- **Interesting feature extraction/manipulation:** Threshold for secondary variable (e.g., "high-value orders") determined empirically from the distribution shape. Revenue aggregated by entity; high-value orders filtered by threshold.

---

### Stereographic Sky Map with Donut Ring Overlays
- **What it shows:** A circular sky map centered on a single star, showing all groups (constellations across cultures) that include that star. Mini donut charts are drawn around each participating star, with each colored arc representing one group membership.
- **When to use:** When showing membership of an item in multiple overlapping groups, especially when spatial context carries meaning. Avoid for datasets without a meaningful spatial embedding.
- **Interesting properties:** Combines a scientific base map (stereographic projection) with a data visualization overlay (donut charts per node) and ornamental elements. Background texture simulates a Milky Way-like field via D3.js contour functions. The concept is generalizable: any set of overlapping group memberships for spatially embedded items can use this approach.
- **Marks:** Circles (stars sized by magnitude), arc segments (donut slices per group per star), lines (group stick figures), background contour patches (simulated texture).
- **Channels:** Circle size (stellar magnitude), color of arc segment (group/culture identity), angular position of arc (relative ordering of groups), opacity/glow (brightness reinforcement), color hue of star (temperature).
- **Annotation options:** Group labels, compass pointers, degree labels for coordinate systems, zodiac symbols at key positions.
- **Data types suited for:** Spatial point data with group-membership attributes (set membership), ordered quantitative (magnitude), categorical (group/culture).
- **Interesting feature extraction/manipulation:** Normal vector math used to offset parallel lines between the same two stars (when multiple groups share an edge). Per-item radial gradients created programmatically.

---

### Topographic / Isocontour Map
- **What it shows:** Contour lines (isolines) derived from a 2D spatial scalar field, showing lines of equal value (elevation, temperature, pressure).
- **When to use:** When showing spatial variation of a continuous scalar field where understanding spatial extent and gradient (rate of change) is the task. Well-suited for terrain elevation, temperature, precipitation.
- **When to avoid:** Very many levels causing visual clutter; when the scalar field changes discontinuously.
- **Interesting properties:** Line density encodes rate of change (closely spaced = steep gradient; widely spaced = slow change). Small closed contours indicate local extrema. Lines can never overlap. Color fill between levels (contour plot) can add a sequential channel.
- **Marks:** Line marks (isolines), underlying geography as point/line/area marks.
- **Channels:** Spatial position (given geography), implicit magnitude via line density, color coding of contour levels (optional sequential channel).
- **Annotation options:** Elevation/value labels on contour lines, color fill between levels, color-coded contour lines by level.
- **Data types suited for:** 2D scalar spatial fields; geographic data with a continuous quantitative field attribute.
- **Interesting feature extraction/manipulation:** Derived geometry — the isoline is computed from the raw scalar field, not directly observed. Contour level selection determines which structure is revealed.

---

### Vendor-to-Production Network / Geographic Relationship Map [from student report]
- **What it shows:** Geographic relationships between two sets of entities (e.g., vendors and production plants), with link thickness or annotations showing quantitative relationship attributes (lead time, quantity).
- **When to use:** When the relationship between two sets of entities matters and geographic position is meaningful. For supply chain or logistics analysis.
- **When to avoid:** When the graph is too dense (many vendors × many plants) creating crossing link clutter. When geographic position is not meaningful.
- **Interesting properties:** The spatial distribution itself is a data encoding — vendors far from plants visually suggest longer lead times even before reading annotations. Using both color AND shape for entity type (red circles vs. green rectangles) provides redundant encoding for accessibility.
- **Marks:** Circles (external vendors), rectangles (production plants), splines/curved lines (material flows / lead time relationships).
- **Channels:** Color hue (entity type), shape (entity type — redundant encoding), spline presence (relationship exists), lead time annotation on spline (quantitative attribute), geographic position.
- **Annotation options:** Hover tooltip (name, location), material dropdown filter (highlights relevant splines), animated spline movement (intended for showing flow direction).
- **Data types suited for:** Bipartite network data with geographic coordinates, quantitative edge attributes (lead time, quantity).
- **Interesting feature extraction/manipulation:** Total Inbound Lead Time = production time + transportation + receipt processing — a computed composite metric joining multiple date fields across datasets.

---

## 6. Multivariate / High-Dimensional Data

### Beeswarm + Box-and-Whisker Combined
- **What it shows:** Both individual data points (beeswarm) and distributional summary (box-and-whisker) simultaneously on the same chart. Gives the reader both the forest and the trees.
- **When to use:** When both individual variation and distributional summary are important. Especially powerful when comparing whether groups differ in central tendency AND spread.
- **When to avoid:** If the box-and-whisker occludes too many individual dots; if N is too large for individual dots to be meaningful.
- **Interesting properties:** The combination gives two levels of detail simultaneously. The IQR box acts as a visual "anchor" for understanding distribution shape at a glance while individual outliers remain identifiable.
- **Marks:** Dots (individuals), rectangles + lines (box-and-whisker).
- **Channels:** Position (all channels from beeswarm), box/whisker extent (IQR and range), color for group identity.
- **Annotation options:** Median line label, quartile values, outlier markers.
- **Data types suited for:** Quantitative + categorical (same as beeswarm).
- **Interesting feature extraction/manipulation:** Calculating quartiles as a separate derived layer on top of individual-level data; the IQR box serves as the summary while dots preserve the detail.

---

### Cluster Heatmap (with Dendrogram)
- **What it shows:** A matrix of quantitative values between two categorical axes, with rows and columns reordered by hierarchical clustering. Dendrograms on the periphery show the derived cluster hierarchy.
- **When to use:** Revealing clusters and patterns in a data matrix (species × sites, genes × conditions). When both row and column ordering matters and discovering natural groupings is the goal.
- **When to avoid:** When precise quantitative reading is needed (color is a less accurate channel); when the matrix is not meaningful to cluster; when color perception is needed for many distinct levels (max 3–11 distinguishable bins for non-contiguous small areas).
- **Interesting properties:** Dendrograms align leaves so interior branch heights are comparable. The leaf order in the final matrix = dendrogram traversal order. Widely used in bioinformatics. Colormap choice is critical: diverging for +/- data; sequential for one-sided; red-green colormap is common but bad for colorblind users.
- **Marks:** Area marks (one rectangle per cell), connection line marks (dendrograms).
- **Channels:** Color saturation/luminance (ordered quantitative value), horizontal position (categorical key 1), vertical position (categorical key 2), dendrogram branch length (merge distance).
- **Annotation options:** Row/column labels, color scale legend, dendrogram branch annotations, cluster highlight boxes.
- **Data types suited for:** Two categorical keys + one quantitative value; clustered/grouped multivariate data; species × site presence/absence matrices; correlation matrices.
- **Interesting feature extraction/manipulation:** Hierarchical clustering as derived data; two separate cluster hierarchies (one for rows, one for columns); row/column normalization (z-scores) for comparable color encoding; biclustering.

---

### Dimensionality Reduction Scatterplot (PCA / t-SNE / MDS / UMAP)
- **What it shows:** Items from a high-dimensional space projected into 2D coordinates that preserve relative distance structure. Each point = one item; color codes conjectured cluster membership.
- **When to use:** Very high-dimensional data (thousands of attributes) where cluster structure is the goal. Document collections, image collections, when direct multi-attribute comparison is infeasible.
- **When to avoid:** When only a few attributes exist (scatterplot or SPLOM suffices); when absolute positions must be interpretable (they are not — only relative distances matter); when fine-grained structure matters (DR loses detail).
- **Interesting properties:** Only large-scale cluster structure is reliable; fine-grained distances may not be meaningful. Rotation, reflection, and rescaling do not change meaning. t-SNE is preferred over K-means and PCA for text/book data when visual separation is clearest. The output x/y coordinates become "visual variables baked into the dataset." Hotspot ovals can be drawn manually in Adobe Illustrator over the scatter output.
- **Marks:** Points (one per item), optional filled blob-ovals for thematic regions, text labels for regions.
- **Channels:** Position x/y (derived synthetic dimensions — encodes similarity), color hue (conjectured cluster membership or categorical group), blur (on manual overlay ovals, encodes gradient/fuzzy region membership).
- **Annotation options:** Text labels for verified clusters, popup detail view on click (showing keywords or document text), manually drawn region labels at average position of items in that region.
- **Data types suited for:** High-dimensional table → derived: 2 or few synthetic attributes via dimensionality reduction.
- **Interesting feature extraction/manipulation:** Bag-of-words transformation for text; MDS/UMAP/t-SNE; two-stage chained derivation (raw → high-D table → low-D table); "average position" of items per theme to place region labels.

---

### Hierarchical Parallel Coordinates
- **What it shows:** Parallel coordinates where clusters of items are shown as bands/ribbons of varying width and opacity rather than individual polylines. A slider controls the level of aggregation detail.
- **When to use:** Very large multidimensional tables (10,000–100,000 items) where standard parallel coordinates would show too many individual lines; when cluster structure is the goal.
- **When to avoid:** Small datasets (standard parallel coordinates work fine); when individual item tracing is important.
- **Interesting properties:** In the limit (one item per cluster), reduces to standard parallel coordinates — the idiom is a generalization, not a replacement. Proximity-based coloring distinguishes clusters. Interactive aggregation dial from highly aggregated (one broad band) to detailed (dozens of narrow bands).
- **Marks:** Band marks (variable width and opacity per cluster), line marks (individual items at finest level).
- **Channels:** Vertical position (value range at each axis), width (min-max span of cluster at each axis), opacity (cluster size/level), color (proximity in cluster hierarchy), horizontal position (attribute identity).
- **Annotation options:** Axis labels, cluster identity legend, level-of-detail slider.
- **Data types suited for:** Table with many quantitative attributes → derived: hierarchical clustering with per-cluster stats (count, mean, min, max, depth).
- **Interesting feature extraction/manipulation:** Compute hierarchical clustering; derive per-cluster mean, min, max, count, depth; interactive LOD slider.

---

### Linked Multiple Views / Coordinated Multiple Views
- **What it shows:** Multiple different visualizations of the same dataset, linked so that selections or highlights in one view propagate across all others. No single view captures all relevant aspects — the combination does.
- **When to use:** Large multidimensional tables where no single encoding captures all relevant relationships. When users need to compare across many attributes simultaneously. Limit to 2–4 coordinated views to avoid cognitive overload.
- **When to avoid:** Low-information tasks, small datasets, or when one view suffices; when excessive linking confuses users.
- **Interesting properties:** Linked highlighting (brushing) is the core interaction primitive. Overview–detail is a common linked-view pattern. Cross-filtering means selections in one view filter data in others. Features invisible in one view (e.g., physical space) can be selected and followed through all derived-attribute views.
- **Marks:** Varies per individual view.
- **Channels:** Varies per view; color highlight indicates selection state across views.
- **Annotation options:** Selection bands, tooltips, linked cursors or brushes.
- **Data types suited for:** Any multidimensional dataset. Particularly powerful for spatial fields, multivariate tables, network + attribute data.
- **Interesting feature extraction/manipulation:** Must first derive many new quantitative attributes from the original data, then facet them into multiple linked views. The cross-filtering itself dynamically creates sub-group views.

---

### Node-Matrix Conceptual Diagram [from student report]
- **What it shows:** Cities and building types (or any two entity sets) as nodes in a matrix layout, connected by lines encoding relationships. Node size encodes total quantity. Line color and thickness encode relationship type and quantity. Optional embedded stacked bars within each node for breakdown.
- **When to use:** Multi-dimensional relationships between two sets of entities (city × building type) and a quantitative variable, simultaneously. Answers questions that no single basic chart could.
- **When to avoid:** When the audience is unfamiliar with network-style diagrams; when the matrix is so large it becomes unreadable.
- **Interesting properties:** A hybrid visualization combining matrix layout + proportional symbols + line encoding + optional stacked bars within nodes. High information density. The embedded stacked bars within nodes add a third level of encoding — composition within each node — without requiring a separate chart.
- **Marks:** Circles (nodes), lines (connections), stacked bar segments within nodes (optional).
- **Channels:** Node size/area (total quantity), line thickness (relationship quantity), line color hue (relationship type), position in matrix (entity pair identity), stacked segment (sub-breakdown within each node).
- **Annotation options:** Node labels, line labels or legend, stacked segment legend, size scale reference.
- **Data types suited for:** Two categorical dimensions (city, building type) + quantitative (consumption) + categorical sub-breakdown (energy type).
- **Interesting feature extraction/manipulation:** Aggregate quantity per entity pair; compute proportional breakdown by type per node; sort both entity sets by total quantity for clearest layout.

---

### Parallel Coordinates
- **What it shows:** Many quantitative attributes at once using parallel vertical axes. Each item = one polyline crossing all axes. Reveals trends, outliers, ranges, and pairwise correlation between neighboring axes.
- **When to use:** Many quantitative attributes (more than 2–3); overview of all attributes simultaneously; range selection; outlier detection. Often used alongside scatterplots in linked views.
- **When to avoid:** Thousands of items (severe overplotting without filtering or aggregation); when correlation tasks are primary (SPLOM is easier to read); when users are unfamiliar with the encoding (training time is a real cost).
- **Interesting properties:** Each item = polyline; positive correlation = parallel line segments between adjacent axes; negative correlation = all lines crossing at a single point. Axis ordering critically affects visible patterns — interactive axis reordering is needed. Star plots (radial variant) require ordering by similarity to reveal structure from 215 unordered attributes.
- **Marks:** Polyline marks (one per item, crossing all axes).
- **Channels:** Vertical spatial position on each axis (quantitative value per attribute), horizontal spatial position (which attribute), line opacity/color (additional categorical attribute).
- **Annotation options:** Axis labels, range brushes for interactive value selection on one axis, color coding by category, density contours for overplotted data, interactive axis reordering.
- **Data types suited for:** Table with many quantitative value attributes.
- **Interesting feature extraction/manipulation:** Compute similarity measure between attributes; order axes by correlation or similarity; filter by importance threshold; brushing-and-linking selects item subsets.

---

### Scatterplot
- **What it shows:** Joint distribution of two quantitative attributes; each item is a point positioned by its two attribute values. Reveals correlation, clusters, outliers, distributions, and trends.
- **When to use:** Exploring correlations, dependencies, clusters, outliers between two quantitative variables. Anscombe's Quartet demonstrates that four structurally different datasets can have identical summary statistics but completely different visual scatter patterns — scatterplots reveal what summaries hide.
- **When to avoid:** When items are so dense they overlap into an unreadable mass (use continuous scatterplot or KDE instead); when one or both attributes are categorical.
- **Interesting properties:** A regression line superimposed makes correlation immediately clear. Log-transform of one or both axes reveals nonlinear/power-law relationships. Applied to derived attributes (vorticity vs. enthalpy; pressure vs. temperature) reveals spatial structures invisible in the original physical view. In linked views, brushing in one scatter selects the same items in all others.
- **Marks:** Points (one per item).
- **Channels:** Horizontal position (quantitative value 1), vertical position (quantitative value 2), color hue (optional categorical attribute), size/area (optional quantitative attribute → "bubble plot"), shape (optional categorical).
- **Annotation options:** Regression line overlay, axis labels, color legend, size legend, data labels on individual points, reference lines, marginal distributions (rug plots or histograms) along axes.
- **Data types suited for:** Two quantitative value attributes. Categorical and additional quantitative attributes via color, size, and shape channels.
- **Interesting feature extraction/manipulation:** Apply log-transform to linearize power-law or exponential relationships. Compute and overlay regression line. Add marginal distributions along axes. Create many derived attributes and plot each pair in separate linked scatterplots for multi-attribute feature detection.

---

### Scatterplot Matrix / SPLOM
- **What it shows:** All pairwise scatterplots of a multivariate dataset in a matrix layout; diagonal shows distribution of each individual attribute.
- **When to use:** Initial exploration of correlation structure in a multivariate dataset; identifying which attribute pairs are most interesting. For up to ~12 attributes.
- **When to avoid:** When there are many attributes (matrix grows as n²); when individual plots become too small to read.
- **Interesting properties:** Only lower or upper triangle needs to be shown (upper is redundant). Diagonal cells can show univariate distributions (histograms or KDE). "Scagnostics" extensions can automatically characterize each cell with derived attributes (outlying, skewed, clumpy, sparse, striated, convex, skinny, stringy, monotonic) to rank which pairs are most interesting — a "meta-display" of displays.
- **Marks:** Points within each scatterplot cell, containment marks (matrix structure).
- **Channels:** Position x and y within each cell (two attributes per cell), color/size for additional attributes, spatial position in matrix (which pair of attributes = which cell).
- **Annotation options:** Correlation coefficients per cell, regression lines, color coding of points by categorical variable, highlighting of specific clusters.
- **Data types suited for:** Tables with multiple quantitative attributes.
- **Interesting feature extraction/manipulation:** Reorder rows/columns by attribute cluster; derive scagnostic measures per attribute pair to automatically surface interesting relationships; filter to subset of attributes.

---

### Small Multiples / Trellis
- **What it shows:** The same visualization type repeated across a grid of panels, each showing a different subset, time point, group, or condition.
- **When to use:** Comparing patterns across many conditions while keeping scales consistent; as an alternative to animation when all frames need to be visible simultaneously. Preferred over animation for detailed multi-frame comparison tasks (exploits "eyes beat memory" — all panels are simultaneously visible).
- **When to avoid:** When the number of panels exceeds what can be legibly displayed at sufficient detail; when each panel requires significant interaction.
- **Interesting properties:** All panels simultaneously visible means comparison uses the perceptual system rather than memory. Main-effects ordering (sorting panels by a summary statistic like median) is critical — without it, no patterns emerge even when they exist in the data (Morris anomaly in barley dataset).
- **Marks:** Whatever the repeated idiom uses.
- **Channels:** Same as repeated idiom + panel position encodes the faceting variable.
- **Annotation options:** Panel labels (faceting variable value), shared or per-panel axes, consistent scale, connecting lines across panels.
- **Data types suited for:** Any data type with a categorical or ordinal partitioning attribute. Time series faceted by time period. Spatial data faceted by season/condition.
- **Interesting feature extraction/manipulation:** Key manipulation: faceting/slicing by a categorical or temporal attribute into small equal panels. Main-effects ordering = derive median per partition and sort panels accordingly.

---

### Spider / Radar / Star Chart
- **What it shows:** Multiple quantitative attributes per item on radial axes, forming a polygon. Multiple items can be overlaid or shown as small multiples for comparison.
- **When to use:** Comparing multiple quantitative variables across a small number of categories (3–8) where no single variable is primary and no ranked comparison is needed.
- **When to avoid:** More than ~6–8 variables (axes become unreadable); when precise comparison between non-adjacent axes is needed; when more than ~5 items are overlaid (polygons overlap and become unreadable).
- **Interesting properties:** The area of the polygon encodes an "overall performance" shape. Axis ordering matters — adjacent variables are easiest to compare. Axes with different scales must be normalized to [0,1] for fair comparison. Inverting an axis (e.g., delivery time: shorter is better) so higher axis values always mean better performance is a semantically important transformation.
- **Marks:** Lines/polygons connecting axis points, points on each axis.
- **Channels:** Radial distance on each axis (metric value), axis direction (metric identity), color of polygon (item identity), area of polygon (overall "performance" shape).
- **Annotation options:** Axis labels, legend for items, note that inversion on one axis transforms the semantics of the direction.
- **Data types suited for:** Multiple quantitative metrics (4–8) across a small number of categorical items. All metrics should be normalized to a common scale.
- **Interesting feature extraction/manipulation:** Delivery time inverted (1/delivery_time) so higher axis values always mean better performance. Normalization to [0,1] is required for cross-axis comparison. DOSFA variant orders/filters axes by similarity and variance to reveal structure in high-dimensional data.

---

### tSNE Scatter Map with Labeled Hotspot Regions
- **What it shows:** A 2D layout of items (documents, books, sites) where similar items cluster together, based on tSNE dimensionality reduction. Manually drawn ovals mark thematic hotspot regions.
- **When to use:** Exploring clustering and similarity structure in high-dimensional text or feature data. Especially useful as a first-pass before building a more precise visualization.
- **When to avoid:** When exact positions need to be interpretable (tSNE positions are relative, not absolute). Ovals are appropriate only when hotspot membership is approximate.
- **Interesting properties:** tSNE was chosen over K-means and PCA when visual separation was clearest. Hotspot ovals drawn manually in Adobe Illustrator over the tSNE output — a hybrid algorithmic + manual design process. Blurring the ovals with SVG blur filters makes them blend smoothly into a colored landscape that serves as background. Region labels placed at average position of all items belonging to that theme.
- **Marks:** Points (item circles), filled blob-ovals for thematic regions, text labels for regions.
- **Channels:** Position (tSNE-derived x/y — encodes textual similarity), color of background ovals (theme category), blur (gradient/fuzzy nature of theme regions).
- **Annotation options:** Region labels at average item position, interactive highlighting of items by theme.
- **Data types suited for:** High-dimensional categorical/textual data collapsed to 2D for layout.
- **Interesting feature extraction/manipulation:** Converting text into a Document Term Matrix → running tSNE → taking output x/y as "visual variables baked into the dataset." Computing "average position" of items per theme to place region labels.

---

## 7. Custom / Creative / Domain-Specific

### 3D Crystal Glyph Field
- **What it shows:** Each item (e.g., a person, a site) is represented as a 3D gem/crystal shape in a WebGL scene. Multiple variables are encoded in the shape and spatial position of each crystal.
- **When to use:** When encoding 3–4 variables per item and artistic, experiential presentation is appropriate. Effective when the comparison itself (e.g., 53 crystals vs. 866 background stars) generates emotional impact. Not suited for precise quantitative reading.
- **Interesting properties:** Size encodes one quantitative variable (e.g., influence/Wikipedia backlinks); number of faces encodes another (depth of documentation); color gradient encodes category (humanities vs. natural sciences); z-axis position encodes temporal dimension (decade). The temporal dimension is only revealed from above — progressive disclosure via camera angle. Spatial density conveys the gender imbalance without explicit encoding.
- **Marks:** 3D polyhedra (one per primary item), small point-light objects (one per secondary comparison item).
- **Channels:** 3D size (primary quantitative variable), face count (second quantitative variable), color gradient family (discipline category), z-axis (time/decade), spatial density (gender or group imbalance between primary and comparison items).
- **Annotation options:** Text labels rendered as canvas textures, landing page legend explaining all channels.
- **Data types suited for:** Multi-attribute categorical/quantitative biographical data where impact and aesthetics matter more than precision. Temporal data encoded spatially.
- **Interesting feature extraction/manipulation:** Wikipedia backlink count as a proxy for "renown" — a derived quantitative measure extracted from hyperlink structure. Year of accomplishment cross-referenced across multiple sources.

---

### Annotated Narrative Infographic (Multi-Section)
- **What it shows:** A complex multi-section visual combining: a timeline, a spatial/geographic illustration, a social media or event feed, and photographic thumbnails with time-stamped captions.
- **When to use:** Breaking news events or complex narrative topics where sequence, geography, and social reaction must all be shown simultaneously. Avoid for data requiring precision.
- **Interesting properties:** The spatial illustration (e.g., isometric building or compound) serves as a geographic anchor that grounds the timeline in physical space. The social feed beside it adds a real-time emotional/social layer. Multi-day and multi-minute timescales require a time-scale break, handled by visually separating sections.
- **Marks:** Event dots on timeline, isometric building illustration, photo thumbnails, text blocks.
- **Channels:** Position (horizontal = time), spatial layout (left panel = narrative, center = spatial/geographic, right = social reaction), color (aesthetic theme reinforcing subject matter).
- **Annotation options:** Timestamps, location labels, social handles, photo captions.
- **Data types suited for:** Temporal, spatial, qualitative/narrative.
- **Interesting feature extraction/manipulation:** Collapsing multi-scale timelines (days + minutes) into a single continuous visual requires a time-scale break handled by section separation.

---

### Battery-Shape Distribution Visualization [from student report]
- **What it shows:** Forecast quantities per distribution center and product type, as a proportion of a user-selected threshold. A semantic/metaphorical mark (battery cylinder) represents each distribution center, with fill level as the key channel.
- **When to use:** When an immediately legible "fill level" metaphor is appropriate for the domain and audience. Particularly effective in dashboards for quick anomaly detection. Avoid for precise comparison — cylindrical 3D perspective distorts proportional judgements.
- **Interesting properties:** The mark is semantically novel — a battery shape is used not to represent a battery as an object, but as a metaphorical vessel whose fill level encodes a percentage of forecast. This creates immediate domain resonance for a supply chain company making batteries. An alarm dot (green/orange/red) at the battery top adds a pre-attentive alert layer above the quantitative encoding.
- **Marks:** Vertical cylinders (batteries), colored sections within; colored dot at top (alarm indicator).
- **Channels:** Fill height (percentage of forecast quantity), color (product type), position (distribution center identity), alarm dot color (inventory status vs. threshold).
- **Annotation options:** Hover tooltip, y-axis percentage scale, responsive legend, year dropdown, threshold dropdown.
- **Data types suited for:** Proportional/percentage quantities across a small number of categories. Works best when the proportional metaphor is semantically meaningful to the audience.
- **Interesting feature extraction/manipulation:** Quantities normalized as percentage of forecast for cross-DC comparability. Alarm logic joins forecast with inventory data across two datasets.

---

### Beeswarm with Fisheye Timeline
- **What it shows:** A dense horizontal timeline of events or captions with fisheye distortion that magnifies the hovered region while keeping context visible.
- **When to use:** When a timeline has too many items to read individually at normal scale, but you don't want to lose the overview. Particularly useful for long-duration time series with discrete events.
- **When to avoid:** When the distortion would mislead quantitative comparisons. When the user needs to compare distances across the timeline.
- **Interesting properties:** The fisheye creates a lens effect — the region under the mouse expands, adjacent regions compress, and the full timeline remains visible. Hovering shows the actual image or detailed record (e.g., video screenshot with emotion overlays) for that moment. The timeline serves as both a navigation tool and a data display.
- **Marks:** Segments/slices (each = one event/moment), image thumbnail (on hover).
- **Channels:** X-position (time within sequence), color or marking on segment (category detected), fisheye distortion magnitude (proximity to cursor).
- **Annotation options:** Caption text shown on hover, full screenshot or detail image with overlaid annotations.
- **Data types suited for:** Temporal (moment within sequence), categorical (event type), qualitative (caption/text).
- **Interesting feature extraction/manipulation:** Caption timestamps from source files converted to JSON; images extracted at those timestamps; faces or events detected and scored at frame level; all joined by timestamp.

---

### Circular Timeline with Pop-Up Hover Detail
- **What it shows:** A timeline arranged as a circular or spiral path with illustrated icons at each historical milestone. Hovering over a milestone reveals a pop-up text block with detailed information. A secondary chart (e.g., bar chart) is embedded within the circular design.
- **When to use:** When a timeline has many events that would clutter a single view if all detail was shown simultaneously. Circular format works for long-span histories or cyclical narratives. Pop-up detail manages information density.
- **Interesting properties:** The primary design is visually clean — only icons and dates on the circular path; all textual detail hidden in hover states. Decorative border elements integrate the data and the aesthetic. Embedding a secondary chart within the circular space is a space-efficient way to add a quantitative dimension.
- **Marks:** Circular/spiral path (timeline), icons/illustrations (events), pop-up rectangles (hover detail), embedded bar or sub-chart.
- **Channels:** Position along the arc (temporal), icon identity (event type), color of icons (event category), size (event prominence).
- **Annotation options:** Date labels along path, event titles at icon positions, full detail text in hover pop-ups.
- **Data types suited for:** Temporal (historical progression), categorical (event type), narrative.
- **Interesting feature extraction/manipulation:** Separating primary vs. secondary information into two layers (visible vs. hover) is a key complexity management technique.

---

### Color Palette Bar Chart (K-means Output)
- **What it shows:** For each item (e.g., a chapter cover image), the color palette extracted via K-means clustering — each segment of the bar is one color cluster, segment width = percentage of pixels assigned to that cluster, fill color = the cluster's representative color.
- **When to use:** Evaluating and comparing color extraction results across different k values and choosing the best k visually. Also useful as a standalone encoding of an image's color composition.
- **When to avoid:** As a main visualization — primarily a diagnostic/processing tool. When color blindness is a concern (encoding relies entirely on hue discrimination).
- **Interesting properties:** Uses color as a direct encoding of color — the segments are the thing they represent. Self-referential color channel: the fill color IS the data value. Can be generated for every item at every k value for calibration (e.g., 50 images × 9 k values = 450 diagnostic charts). The final k per item is chosen manually by human comparison to the original image.
- **Marks:** Horizontal bar segments (one per cluster).
- **Channels:** Segment width (proportion of pixels), fill color (the cluster's color — self-referential).
- **Annotation options:** k value label, item number.
- **Data types suited for:** Proportional part-of-whole data where the value IS the color.
- **Interesting feature extraction/manipulation:** Converting RGB pixel arrays → LAB color space → K-means clustering → hex + percentage export. The LAB conversion is the key step that makes clustering perceptually meaningful.

---

### Dive Fractals / Generative Flow Visualization
- **What it shows:** Multi-round sequential scores for multiple competing teams, where each team's performance across rounds is shown as a sweeping fractal line flow. The shape encodes score; the texture encodes execution variability.
- **When to use:** When showing multi-round sequential scores across multiple competitors where the aesthetic metaphor reinforces the subject matter. Avoid when precise numerical comparison is the goal.
- **Interesting properties:** Based on Dan Gries' "Sweeping Fractal Lines" algorithm. The fractal morphs from one round to the next, creating a flowing animation. Execution scores seed the fractal subdivision — the data controls the shape of the fractal noise, making texture a data channel. Colors are the two primary colors of each team's national flag.
- **Marks:** Fractal line drawn to canvas (one per round transition per team); each set of fractal lines forms a "flow" (one per team).
- **Channels:** Height of each fractal zone (score for that round), radius of circular fractal (difficulty score), squiggliness/texture (execution variability), color hue (team identity/national colors), vertical position (round number).
- **Annotation options:** Team name, country, score per round; hover reveals detailed breakdown; click filters all flows by round.
- **Data types suited for:** Quantitative (scores, difficulty), ordinal (rounds), categorical (teams/countries).
- **Interesting feature extraction/manipulation:** Three types of score (total, difficulty, execution) mapped to three different visual channels (height, radius, texture noise) — each answering a different question about performance.

---

### Film Flowers / Custom Flower Glyph
- **What it shows:** Multiple attributes of individual items (movies, sites, species) encoded into a single flower-shaped glyph per item. Each petal represents one genre, species group, or category; size, color, number of petals, and petal shape all encode different variables.
- **When to use:** When 4–5 attributes of many individual items need to be shown simultaneously in a visually engaging, dense layout. When the "item" metaphor (flower = a movie, a site) adds meaning. Avoid when precise quantitative comparison across items is required.
- **Interesting properties:** The flower metaphor is motivated by both aesthetics and domain appropriateness (summer films, growth). Petal shape encodes a categorical variable (4 distinct shapes for 4 categories). Number of petals encodes a quantitative variable via discretization. This is an unorthodox encoding of a quantitative variable into a count-based mark property. CSS blend modes (multiply) create a blending effect for multi-category items showing overlap visually. Leaf count can encode a personal binary (seen/not seen) hidden within the mark shape.
- **Marks:** Flower glyphs (custom SVG path shapes), each petal duplicated and rotated at equal intervals around center.
- **Channels:** Petal shape (categorical: e.g., parental guidance rating), petal radius/size (quantitative: item rating), number of petals (quantitative discretized: popularity/vote count), color hue (categorical: genre), position in layout (temporal: release year), opacity + blend mode (genre overlap/blending effect).
- **Annotation options:** Title labels per flower, color legend for genres, shape legend for categories.
- **Data types suited for:** Quantitative (rating, count), categorical (genre, rating), temporal (release year).
- **Interesting feature extraction/manipulation:** d3.scaleQuantize() to convert continuous count to discrete petal count. Filtered to top N items per time period. Multiple API sources combined. Aggregated by genre combination.

---

### Generative Butterfly Path / Marble Visualization
- **What it shows:** Each item (butterfly species) is represented as a flowing, smoky path across a canvas, with multiple items active simultaneously. Variables encoded in path thickness, color, curvature behavior, and mark type.
- **When to use:** For exploratory/artistic data display where the aesthetic experience IS the point, or for showing a collection of items "in motion." Avoid when precise comparison between items is needed.
- **Interesting properties:** Every viewer sees a unique version because paths are generated with controlled randomness (jittered splines). The visual is perpetually changing. Named "Marble Butterflies" because the smoky lines resemble marble patterns. Different species categories use distinct mark types (solid lines, dotted lines, circle scatters), adding categorical signal through mark choice.
- **Marks:** Curved lines (splines) with jitter applied on each redraw; some categories use scattered circles; smallest items use dotted lines.
- **Channels:** Color hue (species' main color with slight random variation), line thickness/opacity (size category: small=thin/transparent, large=thick/opaque), path type (solid/dotted/circle-scatter = species category), path curvature behavior (simulated natural motion).
- **Annotation options:** Title spelled out in wiggled hand-drawn-style letters; central focal anchor shape; data source logo.
- **Data types suited for:** Categorical (species, color, size group), continuous (size mapped to thickness/opacity).
- **Interesting feature extraction/manipulation:** Size discretized into three categories to simplify encoding. Brown-colored items filtered out for aesthetic reasons — an explicit subjective data filter in the service of visual quality.

---

### Generative Watercolor Flower-Tree ("Send Me Love")
- **What it shows:** Each text message or data item is represented as a flower (positive sentiment) or leaf (neutral/negative sentiment), arranged on fractal tree branches. Each tree represents one day's worth of items for one individual.
- **When to use:** When conveying emotional texture and individual journeys over time — particularly effective when the story behind the data is personal or narrative. Avoid when precise quantitative comparison is the goal.
- **Interesting properties:** Cutout effect: watercolor canvas behind a white-filled canvas with CSS `destination-out` blend mode, so flowers punch through as cutouts revealing the watercolor underneath. The fractal branching metaphor (flowers grow on branches) solved a layout problem organically. Hover interaction reveals arrows showing the sequence of items before and after any given message.
- **Marks:** Flower shapes (positive items), leaf shapes (neutral/negative items), fractal branches (structural scaffolding).
- **Channels:** Color (most dominant color in an associated artwork), shape (flower vs. leaf = sentiment), position on branch (temporal sequence within day), branch scale (volume of items).
- **Annotation options:** Keyword log below each tree ("soil from which the tree sprouts"); legend explaining flower=positive, leaf=neutral/negative, color=associated artwork; hover arrows linking items in sequence.
- **Data types suited for:** Temporal (items over time), categorical (sentiment, associated color), relational (sequence of interactions).
- **Interesting feature extraction/manipulation:** Sentiment scoring transformed unstructured text into a binary categorical variable for shape encoding. Shannon Entropy of associated artwork (visual "chaos") was computed as a potential additional variable.

---

### Honeycomb / Hexagon Tile Chart
- **What it shows:** Items or categories arranged as hexagonal tiles, with proximity and arrangement encoding relationships. Can be used for personality traits (positive radiate outward, negative point inward), skill taxonomies, or categorical landscapes.
- **When to use:** When the spatial clustering of categories into a memorable, non-rectilinear layout is desired. When a visual metaphor (honeycomb, molecular structure) is appropriate for the domain.
- **Interesting properties:** Personality trait encoding (CI p.214): hexagons where positive traits radiate outward and negative traits (dislikes) point inward — a spatial proximity encoding of valence. Periodic Table of Visualization Methods (CI p.232) uses a periodic-table grid of hexagon-like tiles to organize a taxonomy of ~100 visualization types by category — a reference/ideation tool, not a data display.
- **Marks:** Hexagon tiles (positioned as a connected mesh).
- **Channels:** Hexagon position (proximity = relatedness or valence), color hue (category), text label (item identity).
- **Annotation options:** Labels within hexagons, category grouping by color.
- **Data types suited for:** Categorical (taxonomy, traits, cluster membership). Can encode ordinal valence through spatial arrangement.
- **Interesting feature extraction/manipulation:** Spatial proximity encodes qualitative relatedness rather than a quantitative variable — a non-standard semantic use of position.

---

### Multi-Attribute Product Timeline Table
- **What it shows:** Multiple product generations or items organized in parallel vertical columns by category, with time as the y-axis. Each column tracks one product lineage; each row is a time period.
- **When to use:** For a comprehensive historical taxonomy of a single entity's product line or evolution across multiple parallel categories. Works as a large poster. When both the sequence and the parallel evolution of categories must be visible simultaneously.
- **Interesting properties:** Each product category is a color-coded vertical column; items within columns are placed at their time position with thumbnail images. Lines connect successor products within a column — a product family tree. Reading horizontally reveals what co-existed; reading vertically reveals how a lineage evolved.
- **Marks:** Product image thumbnails, connecting lines (succession), colored column backgrounds (category).
- **Channels:** Position y (time), column position x (product category), color of column (category hue), connecting line (product succession within category).
- **Annotation options:** Product names, year labels on y-axis, category headers.
- **Data types suited for:** Temporal (release year), categorical (product type), relational (succession).
- **Interesting feature extraction/manipulation:** Separating one entity's history into parallel product lineages makes simultaneous evolution across categories visible — impossible in a single timeline.

---

### Multi-Layer Area Chart Career / Resume Timeline
- **What it shows:** A horizontal timeline (years) showing work history above the date line and academic history below, with multiple overlapping colored area bands representing concurrent activities. Additional embedded mini-charts (donut, bar) show skill profiles.
- **When to use:** Career histories with concurrent activities, overlapping roles, and transitions that all need to be shown simultaneously. Used in infographic resumes where visual encoding itself demonstrates design skill.
- **Interesting properties:** Y-axis can be labeled with a self-defined qualitative metric (e.g., "Area represents relative energy expenditure over time") — honest about its qualitative nature while using quantitative visual form. Milestone dots overlaid on the timeline add a discrete event layer on top of the continuous area. Geographic location encoded as background gray columns behind skill areas (CI p.140 — Mike Wirth resume).
- **Marks:** Overlapping area fills (career/skill bands), milestone dots, background columns (locations), donut arcs (skill profiles).
- **Channels:** Horizontal position (time), vertical height (accumulated experience or self-assessed energy), color hue (activity/skill type), left/right side (education vs. employment in butterfly layout), background column width (time at location).
- **Annotation options:** Role names with dates, location names above columns, skill labels within color bands, year labels.
- **Data types suited for:** Temporal, quantitative (relative or self-assessed), categorical (job types, skills, locations).
- **Interesting feature extraction/manipulation:** Values are self-assigned and qualitative rather than measured — the visual conveys relative patterns, not absolute measurement.

---

### Name Voyager / Stacked Stripe Chart
- **What it shows:** Popularity of many categorical items over time (1900–present); each item = one horizontal stripe, stripe height = popularity at each year. Brighter = currently popular. Interactive text search filters to matching items.
- **When to use:** Showing trends over time for many categorical items simultaneously; combining temporal trend with magnitude. Particularly effective for exploratory "enjoy" tasks (browsing, discovering patterns).
- **Interesting properties:** Originally designed for one user goal (expectant parents choosing names), widely adopted for entirely different goals (historical trend analysis for enjoyment) — illustrates how real user goals can diverge from designer intent. Interactive prefix filtering dynamically narrows the dataset in real time.
- **Marks:** Areas (one stripe per item).
- **Channels:** Height of stripe (popularity), color luminance/brightness (recency/current popularity), color hue (categorical distinction — e.g., gender), position x (temporal key — year).
- **Annotation options:** Interactive label on hover, text search input to filter.
- **Data types suited for:** Tables with categorical key (item) + temporal key (year) + quantitative value (popularity). Plus additional categorical attribute for color distinction.
- **Interesting feature extraction/manipulation:** Filter to items starting with a typed prefix; aggregate annual counts into smoothed trends; normalize by total per year.

---

### Network Genealogy / Force-Layout with Temporal Axis
- **What it shows:** Genealogical or network relationships among many nodes, structured so that a temporal attribute determines horizontal position and a proximity metric determines vertical clustering and opacity.
- **When to use:** Relational data with both hierarchy and lateral connections (family trees, org charts, citation networks). Particularly powerful when a temporal axis can be embedded to "pull apart" the network hairball.
- **When to avoid:** Without a meaningful axis, force-directed layouts produce uninterpretable hairballs for large networks. When the network is too dense even with the temporal axis.
- **Interesting properties:** The "constellation" metaphor — dark background, glowing star-like nodes, star temperature color scale — transforms a genealogy chart into an aesthetic night-sky visualization. Opacity encodes distance from power rather than filtering it out (close = opaque, distant = transparent). Line style encodes edge type (solid = blood relation, dotted = marriage). Click interaction shows shortest path to a focal node.
- **Marks:** Circles (nodes = people), lines (edges = family connections).
- **Channels:** Horizontal position (temporal: birth year), vertical position (categorical: which royal family is closest), node size (importance: hereditary leader vs. other), node color (temporal: birth year gradient), node opacity (hop distance to nearest key node), line style (edge type: solid vs. dotted).
- **Annotation options:** Named labels for historically famous nodes, introduction/legend, hover for name and generation count, click for shortest path.
- **Data types suited for:** Relational (network), temporal (birth/death dates), categorical (family membership), quantitative (hop distance).
- **Interesting feature extraction/manipulation:** Birth dates estimated for 40% of missing records; hop distance pre-calculated to each of 10 focal nodes; non-linear time scale compression for older periods; squishing old centuries to focus on recent 200 years.

---

### Olympic Feathers / Radial Arc Chart
- **What it shows:** Every item in a temporal collection (Olympic gold medals, one per arc segment) organized as five concentric "feather" circles, one per major category group. Time (year/edition) encoded as radial distance from center; continent/origin encoded as color.
- **When to use:** Showing temporal change across many parallel categories simultaneously, where categories have a natural grouping into a small number of super-categories. Excellent for revealing which categories dominated which eras. Avoid for precise quantitative comparison.
- **Interesting properties:** Each medal occupies the same arc length regardless of how many medals a sport has — white space in some feathers encodes historical gaps. Inner symmetry: men's events on one side of each feather, women's on the other. Radial gradient background distinguishes gender without color-encoding each individual mark. Hover reveals individual item detail AND highlights all items from that time period across all categories simultaneously.
- **Marks:** Arc segments (one per item), feather outline (custom SVG path), text annotations, white circle overlay (marks record-setting items).
- **Channels:** Radial distance from center (temporal: year/edition), angular position within circle (categorical: sub-category/sport), color hue of arc (categorical: origin/continent), arc length (constant = one item), background gradient (binary: gender), white circle overlay (binary: record status).
- **Annotation options:** Sub-category name labels around feather, textual annotations for unusual historical events, hover tooltips, highlighted time period on hover.
- **Data types suited for:** Temporal (year), categorical (sub-category, origin/continent, gender), binary (record status).
- **Interesting feature extraction/manipulation:** Each item = equal arc regardless of category size — a deliberate simplification that favors historical overview over proportionality. Origin → broad grouping mapping required as data transformation. Sorted by origin winning most items per edition.

---

### Physical / Tangible Data Installation
- **What it shows:** Data encoded in physical, interactive objects that visitors can pick up, touch, or walk through. Variables encoded in 3D spatial position, light, and interaction state.
- **When to use:** When the goal is immersive, emotionally resonant storytelling with a live audience; when embodied interaction adds meaning; when the dataset is small (16–20 items) and richly qualitative. When the subject matter (e.g., invisible people in history) benefits from a metaphor about visibility/invisibility.
- **When to avoid:** Large datasets; remote audiences (requires a digital counterpart for remote access); when reproducibility or scalability is required.
- **Interesting properties:** Y-axis (height from floor) encodes renown — more famous = higher = "out of reach" — a metaphor built into the physical space. Z-axis (depth in room) encodes time — visitors physically walk through history. Group-triggered staggered lighting: interacting with one object causes others in the same category to light up with a time delay, communicating categorical membership through temporal animation. A participation board near the exit lets visitors add a sticker to their preferred category — the audience becomes data contributors.
- **Marks:** Physical orbs/objects (3D points/glyphs), hanging wires (implicit position channels), laser-etched information cards inside objects.
- **Channels:** Position-y (renown/backlinks), position-z (time/year), light brightness (interaction state/accumulated engagement), stagger timing (categorical group membership).
- **Annotation options:** Information card inside each object, participation board outside, digital counterpart website for remote access.
- **Data types suited for:** Small biographical datasets with temporal and quantitative attributes; data with strong narrative or emotional dimension; data about visibility/invisibility.
- **Interesting feature extraction/manipulation:** Wikipedia backlink count as proxy for "renown" — derived from hyperlink structure, not traditional metrics. Year of accomplishment manually extracted by cross-referencing multiple sources.

---

### Radial Color Scatter
- **What it shows:** Distribution of colors (extracted from images) across a circular layout, organized by time-of-day angle and hue radius. Each point = one color from one image.
- **When to use:** When the data IS color (image datasets) and you want to show both temporal structure (time of day) and chromatic structure (hue spectrum) simultaneously.
- **Interesting properties:** Each trip or dataset subset is its own radial cluster; colors are positioned using force simulation to de-overlap while nudging toward calculated x/y positions. Hue → radius encoding creates a natural rainbow gradient from center outward. Hover arcs reveal per-day metadata (where/with whom/enjoyment rating).
- **Marks:** Colored circles/dots (each = one color extracted from one image).
- **Channels:** Angle (time of day the image was taken), radius (hue value), color fill (the actual extracted color — self-referential), spatial cluster grouping (which trip/subset).
- **Annotation options:** Per-group hover arcs showing metadata, annotations for where/with whom/rating per subset.
- **Data types suited for:** Quantitative (color values as hue/saturation/value), temporal (time of day, day of trip), categorical (trip/subset identity).
- **Interesting feature extraction/manipulation:** Colors extracted via image analysis from resized thumbnail images; top 5 colors per image; sorted by HSV hue value rather than raw RGB order.

---

### Scale Scrolling Infographic
- **What it shows:** True proportional scale of extreme distances or magnitudes, using the user's scrolling action as the data experience. The user physically scrolls through vast empty space before reaching the comparative element.
- **When to use:** When the core insight IS the scale itself — when numbers alone fail to convey magnitude. Requires web/interactive medium; does not work in print.
- **Interesting properties:** The visual effort of scrolling IS the data — the distance becomes experiential, not just numerical. All scale elements are anchored to a common reference unit (e.g., Earth = 100 pixels) so all other distances are derived from this anchor. Works for any extreme ratio comparison (distance, volume, time).
- **Marks:** Circles (planets, objects), dotted orbit rings, star field background.
- **Channels:** Position on scroll axis (distance/scale), size of circle (object diameter), color (object identity).
- **Annotation options:** Orbital or positional labels at correct relative distances.
- **Data types suited for:** Quantitative (extreme ratios), spatial.
- **Interesting feature extraction/manipulation:** Normalization of a reference object diameter to a human-readable pixel unit; all other distances derived from this anchor. The scroll distance becomes the data channel.

---

### Scrolled Headshot Grid → Timeline Transition
- **What it shows:** The same items (photo headshots) first grouped by category (grid layout) and then rearranged by date (timeline layout), with scroll driving the animated transition between layouts.
- **When to use:** When the same items need to be viewed through multiple organizational lenses (by category, then by time). Scrollytelling is best when there is a narrative progression and a general audience.
- **When to avoid:** For analytical audiences who need stable reference frames — animation can disorient. When free exploration rather than guided narrative is appropriate.
- **Interesting properties:** The same marks (photo headshots) serve as both categorical identifiers (which show/category) and temporal markers (when it occurred). The transition itself is the insight — watching items reorganize reveals the structural change. Links between items in one category and their matches in another appear during the timeline view.
- **Marks:** Photographic headshots (each = one event/item).
- **Channels:** Grid position (categorical grouping), x-position in timeline (temporal), y-position (another categorical grouping), links (relational: matching between groups).
- **Annotation options:** Hover on one item highlights all corresponding matches; text annotations per section describe what the layout reveals.
- **Data types suited for:** Categorical (show/host, person identity), temporal (date of event), relational (pairwise matching).
- **Interesting feature extraction/manipulation:** Cross-referencing multiple data sources (IMDb credits + Wikipedia + YouTube API) for item collection; missing data shown transparently rather than hidden.

---

### Subway Map Applied to Information / Anatomy / Network
- **What it shows:** A network of nodes and routes organized using the visual grammar of a subway map — colored lines as categories/themes, circles/nodes as junctions, labels as identities. The key innovation is applying this visual grammar to a non-geographic subject.
- **When to use:** When a large relational network of items needs to be organized by multiple overlapping categories, and the "route" (theme) and "junction" (multi-category membership) metaphors add clarity. Strong for information networks, biological systems, or institutional relationships.
- **Interesting properties:** Semantic novelty — subway map applied to a blogroll (CI p.50), human body anatomy (CI p.34), or social media taxonomy. The same visual grammar repurposed for information categorization. Multi-theme nodes (blogs, organs) appear where lines intersect. The abstract network is "grounded" by a spatial or conceptual frame (body silhouette, conceptual proximity).
- **Marks:** Lines (one per thematic category/route), circles/nodes (individual items), intersection nodes (multi-category members).
- **Channels:** Color hue (thematic category/line), position (spatial layout by conceptual proximity or anatomical location), line overlap (multi-category membership).
- **Annotation options:** Node labels, line/category name labels at terminals, numbered terminal circles, color-coded legend.
- **Data types suited for:** Relational (network of items), categorical (theme/category), nominal (item identity).
- **Interesting feature extraction/manipulation:** Abstracting the messy real-world structure into clean geometric lines and nodes — the schematic simplification is what makes the information readable.

---

### Tower / Height Metaphor Comparison Infographic
- **What it shows:** A large quantitative result made viscerally tangible by translating it into familiar physical objects at human scale. Stacked physical objects (beer cases, paperwork, money) are drawn to scale alongside known reference heights (buildings, landmarks).
- **When to use:** When a large quantitative result needs to be made tangible by converting it into a physical unit. When the comparison to known scales (buildings, human height) contextualizes the magnitude.
- **Interesting properties:** The financial or abstract concept is translated into a ridiculous but relatable physical unit (beer cases); height comparison to famous buildings provides immediate scale; the vertical orientation reinforces the metaphor. The unit conversion is the creative act — choosing WHICH physical unit to convert to determines the emotional impact.
- **Marks:** Stacked rectangular blocks (physical objects), building or reference silhouettes.
- **Channels:** Height/length (quantity — after unit conversion), color and texture (object identity vs. reference), position (shared ground line for fair height comparison).
- **Annotation options:** Height labels, dollar/unit amounts, reference object names and heights.
- **Data types suited for:** Quantitative (savings, count, area — convertible to a physical height), temporal (progression of accumulation).
- **Interesting feature extraction/manipulation:** Converting financial data (dollar savings + compound interest) into a physical height measurement using the size of a common object as the unit.

---

### Tree Ring / Radial Arc Rank Chart
- **What it shows:** Ranked lists where each rank level is a concentric arc. The inner arc = rank 1 (most prominent), the outer arc = rank N. Text labels placed along the arc paths show the actual items at each rank.
- **When to use:** For ranked lists where a compact, visually distinctive display emphasizing order is desired without a linear bar chart. Works well for single-category focus.
- **When to avoid:** When comparing multiple categories simultaneously in one view — too much visual weight. When more than ~10 rank levels are needed.
- **Interesting properties:** The tree ring metaphor implies accumulation and hierarchy. Switching between categories is animated by rotating the text rings out of view and back in (rather than physically moving elements). Three layered textPath SVG elements per arc: grey original on left, black translation centered, grey original on right — making the translation stand out without a separate legend.
- **Marks:** Arcs (SVG arc paths), text labels placed along the arc path.
- **Channels:** Radial position (arc ring level = rank), text on arc (the actual item/word), arc color (subtle differentiation).
- **Annotation options:** The labels ARE the annotation; animated transition between categories.
- **Data types suited for:** Categorical (items), ordinal (rank), nominal (category/group).
- **Interesting feature extraction/manipulation:** Rankings combined across multiple sub-groups using a point system (rank 1 = N points, rank 2 = N-1, etc.) to derive an overall cross-group ranking. Synonyms mapping to the same translation manually merged before ranking.

---

### Video Emotion Glyph (Bubble with Dual Radii + Dot Ring)
- **What it shows:** Three variables shown simultaneously for each item on a single circle glyph: filled circle (one quantitative), outer ring (second quantitative), small dots on ring (discrete events within the item).
- **When to use:** When three variables need to be shown simultaneously for many items, and those variables naturally correspond to a center quantity, an outer boundary, and discrete events on the boundary. Avoid when all three channels are difficult to decode simultaneously.
- **Interesting properties:** A composed glyph that stacks three encodings. Author noted this can be "overwhelming and confusing" — a cautionary example for glyph design. The temporal placement on a shared x-axis maintains continuity with adjacent views in a scrollytelling context.
- **Marks:** Filled circles (inner radius), ring/arc (outer radius), small dots on ring (event markers).
- **Channels:** Filled circle radius (primary quantitative variable), outer ring radius (second quantitative variable), dot position on ring (temporal position within item), x-position (shared temporal axis).
- **Annotation options:** Caption describing events per category.
- **Data types suited for:** Quantitative (two magnitude variables), temporal (date and position within item), categorical (item identity).
- **Interesting feature extraction/manipulation:** Emotion detection via computer vision API on screenshots taken at regular intervals; emotion moments extracted from frame-level scores.

---

### Word Snake / Beads on a String
- **What it shows:** A ranked sequence of items (words, entities) arranged as a string of "beads" (circles) connected by a swirling line. Each bead represents one item; the string winds down the page connecting all beads.
- **When to use:** For showing a ranked sequence of items where the "path through" them matters. Especially for linguistic/textual data where the words themselves serve as the marks. Good for lists of ~10–100 items.
- **When to avoid:** When precise value comparison is needed (no common scale). When the winding path obscures rank order.
- **Interesting properties:** The swirling layout is fully responsive, recalculating path geometry for each screen width. Hovering a bead reveals an elaborate tooltip — in DS p.282, a Google Trends line chart + a word cloud of related queries. The tooltip is itself a nested visualization.
- **Marks:** Circles (beads) connected by a curved SVG path, text labels on/around each bead.
- **Channels:** Position along the path (relative ranking), circle size (highlights/emphasis), tooltip content on hover (nested time series + word cloud).
- **Annotation options:** Hover tooltip with annotated trend line and word cloud; hand-lettered section headers.
- **Data types suited for:** Categorical (items), ordinal (rank), temporal (trend over time in tooltip).
- **Interesting feature extraction/manipulation:** Word frequencies from multiple source terms aggregated to a single target before ranking. NLP tagging used to filter only nouns and adjectives. TSP (Traveling Salesman Problem) used to determine optimal connection order for linked items by shortest total path length.

---

*End of catalogue. Total entries: 90 visualization types across 7 groups.*
*Sources: CI = Cool Infographics (agents 01–05), DS = Data Sketches (agents 06–14), VAD = Visualization Analysis and Design / Munzner (agents 16–24), EC = Examples from class (agent 15), ER = Example student reports (agent 25).*
