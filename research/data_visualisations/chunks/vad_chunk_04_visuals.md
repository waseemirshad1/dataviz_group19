# [agent_19] Visualization Analysis and Design — pages 151-200

## Visualization Catalogue: Chapter 6 (Rules of Thumb) and Chapter 7 (Arrange Tables)

---

### Linked 2D Views with Calendar (p.126–128)
- **What it shows:** Time-series data over multiple days/years shown through derived aggregate curves + calendar heat-map; linked with shared color coding
- **When to use:** Multi-scale temporal data where both fine-grained (daily) and coarse-grained (seasonal) patterns matter; use instead of 3D extruded time-series when comparison is the task
- **Avoid when:** Single time scale, or when the goal is only rough overview (simple line chart may suffice)
- **Interesting properties:** Hierarchical clustering produces representative aggregate curves (average per cluster); calendar layout exploits culturally understood time structure; linked views share colors so patterns map across both
- **Marks:** Line marks (curves in main view), area marks (calendar cells)
- **Channels:** Position (value along curve), color hue (cluster identity, shared), spatial position in calendar (date/day-of-week)
- **Annotation options:** Color legend linking cluster ID to curve; labeled axes for time and value; calendar week/month labels
- **Data types suited for:** Ordered (time), quantitative (measurement), categorical (cluster/day type)
- **Interesting feature extraction/manipulation of data:** Hierarchical clustering of time-series curves into a small set of representative aggregate curves as derived data; this reduces a year of data to a handful of interpretable patterns

---

### Blink Comparator (p.133)
- **What it shows:** Localized changes between exactly two frames/images by rapidly toggling back and forth
- **When to use:** When detecting whether a specific localized change exists between two configurations; classic use is astronomy (found Pluto)
- **Avoid when:** Changes are distributed across many areas simultaneously; more than 2 frames to compare
- **Interesting properties:** Exploits the visual system's sensitivity to motion at focus of attention; enables detection of subtle changes invisible in static side-by-side comparison
- **Marks:** Whole-frame images (each frame is a mark)
- **Channels:** Temporal position (which frame), spatial position of changes
- **Annotation options:** Frame labels; timestamps
- **Data types suited for:** Any dataset with exactly two states to compare; spatial data, astronomical images
- **Interesting feature extraction/manipulation of data:** None; the interaction pattern itself IS the idiom

---

### Scatterplot (p.146–148)
- **What it shows:** Relationship and correlation between two quantitative value attributes; distributions, clusters, outliers, extremes
- **When to use:** Two quantitative attributes; want to see correlation, clusters, outliers, distribution; primary task is finding trends or patterns between two variables
- **Avoid when:** One or both attributes are categorical (use bar/dot chart); need precise value lookup (use table or bar chart); too many items (overplotting above hundreds)
- **Interesting properties:** Diagonal pattern shows correlation strength; positive slope = positive correlation; negative slope = negative correlation; log transformation of axes often reveals hidden linear relationships
- **Marks:** Point marks (one per item)
- **Channels:** Horizontal spatial position (value attribute 1), vertical spatial position (value attribute 2), color hue (optional categorical attribute), size (optional quantitative attribute → "bubble plot")
- **Annotation options:** Regression line (derived); axis labels; data labels on selected points; reference lines; confidence intervals
- **Data types suited for:** Two quantitative values; augmented with categorical (color) or quantitative (size)
- **Interesting feature extraction/manipulation of data:** Log transformation of original attributes creates derived attributes that may show linear correlation when originals do not; regression line as derived overlay; contour lines for density

---

### Bar Chart (p.150–151)
- **What it shows:** One quantitative value per category, enabling direct comparison across levels of a categorical key attribute
- **When to use:** One categorical key + one quantitative value; tasks are lookup by category and comparison; want high-accuracy position encoding
- **Avoid when:** Key attribute is ordered and trend is the main task (use line chart); too many categories to display (switch to dense layout or hierarchy)
- **Interesting properties:** Line marks aligned to a common baseline → highest accuracy position-against-common-scale channel; default alphabetical ordering should be replaced with data-driven ordering (by value) to reveal dataset trends
- **Marks:** Line marks (bars)
- **Channels:** Vertical spatial position (value attribute, aligned), horizontal spatial position (category separation)
- **Annotation options:** Value labels on bars; reference lines; color coding for secondary categorical attribute; sorted order annotation
- **Data types suited for:** One quantitative value, one categorical key; extensible with color for second categorical
- **Interesting feature extraction/manipulation of data:** Ordering bars by value (derived attribute = rank) reveals trends; sorting by derived aggregates (e.g., mean across groups) is common

---

### Stacked Bar Chart (p.151–153)
- **What it shows:** Part-to-whole relationships across categories; total value per primary category AND breakdown by secondary category within each bar
- **When to use:** Two categorical keys + one quantitative value; interested in both totals AND composition; up to ~12 levels in the stacked dimension
- **Avoid when:** The primary task is comparing sub-categories across bars (unaligned position is inaccurate); too many categories in the stacked dimension (>12 causes visual confusion)
- **Interesting properties:** Bottom sub-bar uses aligned position (accurate); other sub-bars use unaligned position (less accurate); ordering of stacking layers significantly affects what patterns are visible; typically requires color to distinguish sub-components
- **Marks:** Composite glyph of stacked sub-bars (line marks for each sub-component)
- **Channels:** Vertical spatial position (total height = total value, aligned baseline); length (each sub-bar height = sub-value); color hue (secondary key category)
- **Annotation options:** Color legend for secondary key; value labels on sub-bars; normalized variant shows percentage instead of absolute
- **Data types suited for:** 1 quantitative value, 2 categorical keys; works for absolute counts (standard) or proportions (normalized variant)
- **Interesting feature extraction/manipulation of data:** Normalizing to 100% creates a part-to-whole view; choosing which sub-category goes at the bottom determines which comparisons are most accurate

---

### Normalized Stacked Bar Chart (p.170)
- **What it shows:** Relative proportions of sub-categories (parts to whole), equivalent to many pie charts in a single view
- **When to use:** Proportional data across multiple groups; comparing composition across many categories simultaneously
- **Avoid when:** Absolute counts are needed (use regular stacked bar); too many sub-categories (>12)
- **Interesting properties:** Each bar = one pie chart's worth of information, but with more accurate length channel instead of angle; allows direct comparison across many groups
- **Marks:** Line marks (sub-bars, each normalized to fill full height)
- **Channels:** Length (proportion, normalized); color hue (sub-category); horizontal position (primary category)
- **Annotation options:** Percentage labels; color legend
- **Data types suited for:** Proportional/percentage data; two categorical keys + one quantitative value
- **Interesting feature extraction/manipulation of data:** Normalization operation converts absolute counts to relative percentages

---

### Streamgraph (p.153–155)
- **What it shows:** Evolution of many categories over time; emphasizes continuity of each stream and its changing magnitude; organic silhouette reveals overall shape of the data
- **When to use:** Multiple time series with categorical breakdown; when the continuous flow and changing relative proportions matter more than precise value lookup; many categories that don't all span the full time range
- **Avoid when:** Precise value reading is important (aligned baseline missing); categories are few (regular stacked bar chart may be clearer)
- **Interesting properties:** Baseline is organic/curved (not flat) — optimized trade-off between multiple factors; layer order is derived from data (e.g., volatility or onset time); scales to more categories than stacked bar because sparse layers don't occupy full timeline
- **Marks:** Area marks (each stream); derived geometry from global computation
- **Channels:** Height of layer (quantitative value); horizontal position (time); color hue (categorical entity); layer ordering (derived quantitative attribute)
- **Annotation options:** Category labels on streams; tooltips; interactive highlighting of individual streams
- **Data types suited for:** One quantitative value (counts), one ordered key (time), one categorical key (entity/artist/etc.)
- **Interesting feature extraction/manipulation of data:** Derived layer ordering attribute (volatility, onset time, alphabetical); derived geometry computation for optimal baseline and silhouette shape

---

### Dot Chart (p.155)
- **What it shows:** One quantitative value per item using point marks with aligned position; similar to bar chart but uses points
- **When to use:** One quantitative value, one ordered or categorical key; when exact position is more important than showing bar extent
- **Avoid when:** Trend-following is the main task (use line chart); many items crowded (bars may be easier to count)
- **Interesting properties:** Point marks rather than line marks; aligned position = same high-accuracy channel as bar chart; can be thought of as scatterplot where one axis is categorical
- **Marks:** Point marks
- **Channels:** Vertical spatial position (value, aligned), horizontal position (key/category)
- **Annotation options:** Value labels; reference lines; grid
- **Data types suited for:** One quantitative value, one ordered key
- **Interesting feature extraction/manipulation of data:** Ordering by value to reveal ranking

---

### Line Chart (p.155–158)
- **What it shows:** Trend in a quantitative value over an ordered key (usually time); connection marks emphasize ordering and imply continuous relationship
- **When to use:** One quantitative value, one ordered key; primary task is spotting trends; time-series data
- **Avoid when:** Key is categorical (expressiveness violation; falsely implies trend); too few data points (bar or dot chart clearer)
- **Interesting properties:** Connection marks between points strongly imply trend; aspect ratio matters critically — "banking to 45°" maximizes angle accuracy; multiscale banking reveals structure at multiple frequencies; Zacks & Tversky found line charts for categorical data elicited false trend language
- **Marks:** Point marks + connection line marks between them
- **Channels:** Vertical spatial position (value), horizontal spatial position (ordered key); color hue/shape for second categorical attribute
- **Annotation options:** Trend line (regression); confidence bands; annotations at notable events; aspect ratio adjustment
- **Data types suited for:** One quantitative value, one ordered key (time, ordinal)
- **Interesting feature extraction/manipulation of data:** Banking to 45° as aspect ratio derivation; locally weighted regression (LOESS) as derived trend overlay; power spectrum derivation for multiscale banking

---

### Heatmap (p.158–161)
- **What it shows:** A quantitative value for all combinations of two categorical key attributes; patterns of similarity, clusters, outliers across a large matrix
- **When to use:** Two categorical keys + one quantitative value; need compact overview of many values; want to spot clusters or outliers; high information density needed
- **Avoid when:** Only a few rows/columns (bar chart clearer); color perception needed for many distinct levels (max 3–11 bins distinguishable in small non-contiguous areas)
- **Interesting properties:** Very compact — handles millions of items; widely used in bioinformatics; colormap choice critical (diverging for +/- data; sequential for one-sided); red-green colormap common in genomics but bad for colorblind users
- **Marks:** Area marks (cells)
- **Channels:** Color (quantitative value — limited to 3–11 distinguishable bins); horizontal position (key attribute 1); vertical position (key attribute 2)
- **Annotation options:** Color legend with scale; row/column labels; row/column dendrograms (cluster heatmap); highlighted cells
- **Data types suited for:** Two categorical keys + one quantitative value
- **Interesting feature extraction/manipulation of data:** Matrix reordering by hierarchical clustering of rows and columns simultaneously (biclustering); clustering algorithm produces dendrogram as derived data showing merge history

---

### Cluster Heatmap (p.160–161)
- **What it shows:** Heatmap with rows and columns reordered by hierarchical clustering; dendrograms on periphery show the derived cluster hierarchy
- **When to use:** Same as heatmap, plus when discovering structure/groupings in both row and column dimensions is the goal
- **Avoid when:** Cluster structure is not expected or irrelevant (plain heatmap); very small matrices
- **Interesting properties:** Dendrograms align leaves so interior branch heights are comparable; leaf order in final matrix = dendrogram traversal order; each leaf = cluster of one item; root = cluster of all items; juxtaposition of heatmap + two dendrograms is a composite visualization
- **Marks:** Area marks (heatmap cells); connection line marks (dendrograms)
- **Channels:** Color (quantitative value); spatial position (matrix rows/columns ordered by cluster); length of dendrogram branches (merge distance)
- **Annotation options:** Row/column labels; dendrogram branch labels; cluster highlight boxes
- **Data types suited for:** Two categorical keys + one quantitative value; clustered/grouped data
- **Interesting feature extraction/manipulation of data:** Hierarchical clustering as derived data; two separate cluster hierarchies (one for rows, one for columns); traversal of tree leaves determines final ordering

---

### Scatterplot Matrix / SPLOM (p.161–162)
- **What it shows:** All pairwise combinations of attributes as individual scatterplots in a matrix layout; comprehensive correlation overview
- **When to use:** Exploring correlation structure across many quantitative attributes; finding which pairs of variables are related; up to ~12 attributes
- **Avoid when:** More than ~12 attributes (too small to see individual cells); categorical attributes dominant (use other idioms); looking for specific values (use table)
- **Interesting properties:** Only lower or upper triangle shown (upper is redundant); diagonal cells replaced with attribute labels; each cell is a complete scatterplot; "scagnostics" extensions can characterize each cell with derived attributes
- **Marks:** Point marks (within each scatterplot cell); the matrix structure itself as containment marks
- **Channels:** Position within each cell (pairwise value attributes); spatial position in matrix (which pair of attributes = which cell)
- **Annotation options:** Correlation coefficients per cell; regression lines; color coding of points by a separate categorical attribute; highlighting of specific clusters
- **Data types suited for:** Table with many quantitative attributes; derived key = list of attribute indices
- **Interesting feature extraction/manipulation of data:** Derived key attribute = index of original attributes; matrix can be reordered by any ordered attribute; "scagnostics" = derived attributes characterizing scatterplot shape (monotone, clumpy, striated, convex, etc.)

---

### Parallel Coordinates (p.163–166)
- **What it shows:** Many quantitative attributes at once using parallel vertical axes; trends, outliers, ranges, pairwise correlation between neighboring axes
- **When to use:** Many quantitative attributes (more than 2-3); overview of all attributes simultaneously; range selection; outlier detection; often used alongside scatterplots in linked views
- **Avoid when:** Thousands of items (severe overplotting); correlation task is primary (SPLOM is easier); users are unfamiliar with the encoding (training required)
- **Interesting properties:** Each item = polyline (jagged/connected line) crossing all axes; positive correlation = parallel line segments between adjacent axes; negative correlation = all lines crossing at single point; axis ordering critically affects visible patterns; interactive axis reordering needed; training time is real cost
- **Marks:** Polyline marks (one per item, crossing all axes)
- **Channels:** Vertical spatial position on each axis (quantitative value); horizontal spatial position (which attribute); line opacity/color for additional categorical attributes
- **Annotation options:** Axis labels; range brushes (interactive selection of value range on one axis); color coding by category; density contours for overplotted data; interactive axis reordering
- **Data types suited for:** Table with many quantitative value attributes
- **Interesting feature extraction/manipulation of data:** Hierarchical parallel coordinates scale to larger datasets; brushing-and-linking selects item subsets; axis ordering computed by correlation or other derived attributes

---

### Radial Bar Chart (p.168)
- **What it shows:** Same as bar chart but with radial layout; length of each bar from center encodes quantitative value
- **When to use:** When cyclic/periodic data must be shown and radial layout helps; one categorical attribute + one quantitative value
- **Avoid when:** Rectilinear bar chart is available and task requires accurate comparison (rectilinear is more accurate); no periodicity in data
- **Interesting properties:** Mathematically equivalent to bar chart; perceptually inferior for comparison (length along radial axis harder to judge accurately than aligned bars); creates visually appealing circular shape
- **Marks:** Line marks (radial bars)
- **Channels:** Length (quantitative value, radial); angle (categorical separation)
- **Annotation options:** Category labels at each bar; radial scale grid
- **Data types suited for:** One quantitative + one categorical attribute
- **Interesting feature extraction/manipulation of data:** None unique over bar chart

---

### Pie Chart (p.168–170)
- **What it shows:** Relative proportions of parts to a whole (percentages) for one categorical attribute
- **When to use:** Part-to-whole relationship is the primary task; small number of categories (~12 max); audiences are very familiar with the encoding
- **Avoid when:** Precise comparison between individual categories is needed (angle judgements are inaccurate); many categories (>12); side-by-side comparison of multiple groups (use normalized stacked bar instead)
- **Interesting properties:** Sum of angles = 360° → must encode normalized (percentage) data; wedge width varies radially (narrow at center, wide at edge) making area judgement hard; pie charts require roughly square space; competing encoding: angle + area both vary, both inaccurate
- **Marks:** Area marks (wedges)
- **Channels:** Angle (primary quantitative value); area (secondary, also varies with value but less accurate); color hue (categorical identity of each wedge)
- **Annotation options:** Percentage labels; category labels; color legend; explosion of slices for emphasis
- **Data types suited for:** One quantitative value (normalized/percentage), one categorical key
- **Interesting feature extraction/manipulation of data:** Normalization to 100% is required; exploded slice = spatial emphasis technique

---

### Polar Area Chart / Rose Plot / Coxcomb (p.169–170)
- **What it shows:** Same data as pie chart but varies the length of each wedge (like a bar chart in polar coordinates) rather than angle; more accurate than pie chart
- **When to use:** Same use cases as pie chart; more accurate encoding than pie; useful for cyclic/directional data (compass directions, months)
- **Avoid when:** Rectilinear bar chart available (still more accurate than polar area); many categories
- **Interesting properties:** Popularized by Florence Nightingale for Crimean War mortality data; encodes quantitative value with length channel (more accurate than angle); wedge width is constant; visual appeal of radial layout maintained
- **Marks:** Area marks (wedges, variable length)
- **Channels:** Length (quantitative value, from center); angle (categorical separation — equal per category)
- **Annotation options:** Category labels; radial scale; color hue for categories
- **Data types suited for:** One quantitative value, one categorical key
- **Interesting feature extraction/manipulation of data:** Useful for cyclic attributes (month, compass direction, time of day)

---

### Dense Layout / Dense Software Overview (p.172–174)
- **What it shows:** Overview of very large text or structured datasets using one-pixel marks; spatial structure from original data preserved; color encodes derived attributes
- **When to use:** Extremely large datasets needing overview (10,000+ items); spatial order of items is semantically meaningful (e.g., source code line order); tasks are orientation and navigation, not precise value reading
- **Avoid when:** Precise text reading is required at a specific location (combine with detail view); marks need to encode size or shape (impossible at 1 pixel)
- **Interesting properties:** Only planar position and color available as channels at pixel scale; indentation/line length preserved as spatial landmark; multiple columns created by wrapping; combined with detail view for overview+detail pattern
- **Marks:** Point or line marks (1 pixel each)
- **Channels:** Planar spatial position (reflects source order); color hue (derived categorical attribute, e.g., pass/fail); brightness/luminance (derived quantitative attribute, e.g., coverage %)
- **Annotation options:** Detail view pane with full resolution; color legend; hover tooltip for specific items
- **Data types suited for:** Ordered text/code with hierarchical structure; derived quantitative attributes from test results
- **Interesting feature extraction/manipulation of data:** Deriving quantitative attributes from test execution results (coverage %, pass:fail ratio); wrapping linear list into multi-column layout

---

### Space-Filling Layout (p.174–175)
- **What it shows:** Any dataset where items fill all available display space; maximizes area available for color coding and embedded labels
- **When to use:** Hierarchical data (treemaps); when every pixel of screen space is valuable; when labels need to fit inside marks
- **Avoid when:** White space is needed for readability/emphasis; the geometry of containment doesn't match the data semantics
- **Interesting properties:** Does not imply space efficiency — space-filling is a layout property, not an efficiency guarantee; examples: treemaps (containment marks), icicle trees, concentric circle trees
- **Marks:** Area marks (items) or containment marks (relationships)
- **Channels:** Area (size/magnitude where applicable); color; spatial position
- **Annotation options:** Labels embedded within area marks; color legend; hierarchical outlines
- **Data types suited for:** Hierarchical/tree data; large tables
- **Interesting feature extraction/manipulation of data:** Area proportional to quantitative attribute (e.g., file size in treemap)

---

### Glyphmap / Small Multiples in Rectilinear vs. Radial (p.170–171)
- **What it shows:** A matrix of small charts (line charts or other glyphs) comparing patterns across 12 iconic time-series shapes in either rectilinear or radial form
- **When to use:** Comparing multiple patterns side by side; rectilinear for linear/non-linear trend detection; radial for cyclic pattern detection
- **Avoid when:** Individual detail is more important than pattern comparison
- **Interesting properties:** Figure 7.19 explicitly shows that rectilinear outperforms radial for showing differences between linear and nonlinear trends; radial outperforms rectilinear for cyclic patterns
- **Marks:** Line marks within each small chart
- **Channels:** Spatial position (value within each chart); arrangement in matrix (small multiples)
- **Annotation options:** Chart titles; axis labels; baseline markers
- **Data types suited for:** Multiple time series with ordered key (time)
- **Interesting feature extraction/manipulation of data:** Standardizing scales across small multiples for fair comparison
