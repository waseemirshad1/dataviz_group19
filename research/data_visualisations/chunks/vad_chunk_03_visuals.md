# [agent_18] Visualization Analysis and Design — pages 101-150

## Visualization Catalogue

---

### Scatterplot (p. 146–148)

- **What it shows:** The relationship between two quantitative value attributes. Each item is a point at (x, y) coordinates. Reveals correlation, clusters, outliers, distributions, and trends.
- **When to use:** When task is to find correlation, distribution, outliers, or clusters across two continuous variables. Effective for exploratory overview.
- **When to avoid:** When items are very numerous (hundreds+) and overlap obscures individual points. Not suitable for comparing categories directly without additional channels.
- **Interesting properties:** Correlation is read as a diagonal line pattern — very intuitive perceptual judgement. Negative correlation = downward diagonal, positive = upward. A regression line superimposed makes the task even easier. Log-transform axes to reveal nonlinear relationships.
- **Marks:** Point (one per item)
- **Channels:** Horizontal spatial position (quantitative value 1), vertical spatial position (quantitative value 2); optionally color hue (categorical attribute), size/area (quantitative attribute — "bubble plot")
- **Annotation options:** Regression line overlay; axis labels; color legend; size legend; data labels on individual points; reference lines or bands
- **Data types suited for:** Two quantitative value attributes. Categorical and additional quantitative attributes via color and size channels.
- **Interesting feature extraction/manipulation of data:** Apply log-transform to one or both axes to linearize power-law or exponential relationships (see diamond price/carat example, p. 147–148). Compute and overlay a derived regression line. Add marginal distributions (rug plots or histograms) along axes.

---

### Bar Chart (p. 150)

- **What it shows:** A quantitative value for each level of a categorical key attribute. Enables comparison of magnitude across categories.
- **When to use:** One categorical key, one quantitative value. Ideal for lookup of individual values, ranking, and comparison across categories.
- **When to avoid:** Many categories (hundreds) — not enough screen space. When the task is distributional (use histogram instead). Never use 3D bar charts (perspective distortion makes bars hard to compare, p. 122).
- **Interesting properties:** All bars share a common baseline (aligned spatial position) → highest-accuracy magnitude channel. Ordering bars by value attribute reveals trends; alphabetical ordering aids lookup but hides patterns (p. 150).
- **Marks:** Line (bar = tall thin line/rectangle mark)
- **Channels:** Aligned vertical spatial position (quantitative value), spatial region along horizontal axis (categorical key)
- **Annotation options:** Value labels above/inside bars, reference line, color coding for a second categorical attribute (grouped bars), error bars for uncertainty
- **Data types suited for:** 1 categorical key + 1 quantitative value. Can extend to 2 keys with grouped or stacked bars.
- **Interesting feature extraction/manipulation of data:** Order by value rather than label to reveal ranking. Normalize values for comparison across groups of unequal size. Compute derived attributes such as ratios or differences for secondary bars.

---

### Bubble Plot / Size-coded Scatterplot (p. 148)

- **What it shows:** Three or four attributes simultaneously — two quantitative via position, one quantitative via size (area of point), optionally one categorical via color.
- **When to use:** When a third quantitative attribute needs to be shown without a third spatial axis. Common for demographic data (e.g., population + life expectancy + infant mortality + continent).
- **When to avoid:** When size differences are subtle (area perception is compressed — Stevens' exponent n ≈ 0.7, p. 104). Avoid when points are many and overlap is severe.
- **Interesting properties:** Size channel uses area, which is a lower-accuracy channel than position, so this is only suitable for showing broad magnitude differences, not precise comparisons.
- **Marks:** Point (variable-area circle)
- **Channels:** Horizontal position (quantitative), vertical position (quantitative), area/size (quantitative — third attribute), color hue (categorical — fourth attribute)
- **Annotation options:** Size legend, color legend, labels on notable points, reference lines
- **Data types suited for:** Three quantitative value attributes + one categorical. Examples: country datasets (population, GDP, life expectancy, continent).
- **Interesting feature extraction/manipulation of data:** Log-scale size mapping prevents very large values from dominating all visual space. Normalize or index values to a baseline year for change comparison over time.

---

### 3D Bar Chart (anti-pattern reference, p. 122)

- **What it shows:** Intended to show quantitative values with 3D depth — in practice, an anti-pattern demonstrating costs of unjustified 3D.
- **When to use:** Do not use for abstract data. No justified use case for bar charts.
- **When to avoid:** Always for abstract/quantitative data. Perspective distortion makes bar height comparison difficult; foreshortening adds ambiguity; occlusion hides bars (p. 122).
- **Interesting properties:** Classic example of how visual encoding suffers when 3D depth is introduced unnecessarily. The planar position channel (the most accurate) is destroyed by perspective distortion.
- **Marks:** 3D rectangular prism
- **Channels:** Height (intended quantitative), but distorted by perspective; position along ground plane (categorical)
- **Annotation options:** None that compensate for the distortion problem
- **Data types suited for:** None — use 2D bar charts instead.
- **Interesting feature extraction/manipulation of data:** N/A. Use multiple aligned 2D bar charts for multi-key data instead.

---

### 3D Time-Series / Extruded Line Chart (anti-pattern reference, p. 126–127)

- **What it shows:** Time-series data extruded into a third dimension (one curve per time unit along the depth axis). In the van Wijk & van Selow example: daily power consumption curves for one year.
- **When to use:** Not recommended for abstract data. Only shows broad seasonal/cyclical patterns.
- **When to avoid:** When fine-grained patterns (weekdays, holidays, sub-seasonal variations) need to be visible. Occlusion hides near-back curves; perspective distortion prevents direct comparison.
- **Interesting properties:** Used as contrast case to motivate the 2D linked view with hierarchical clustering. The 3D version reveals only the two largest patterns; the 2D version reveals six or more distinct patterns.
- **Marks:** 3D surface/line
- **Channels:** Position along depth axis (day of year), x-axis (time of day), y-axis (power consumption)
- **Annotation options:** Very limited due to occlusion and perspective
- **Data types suited for:** Temporal data with repeated cycles — but better shown with 2D alternatives.
- **Interesting feature extraction/manipulation of data:** The recommended approach is hierarchical clustering of time-series curves into aggregate types, then showing these in a 2D calendar linked view (p. 127).

---

### Linked Calendar + Aggregate Curve View (positive 2D alternative, p. 127)

- **What it shows:** Temporal patterns across a full year of daily data, showing both fine-grained within-day patterns (aggregate curves) and macro calendar structure (weeks, seasons, holidays).
- **When to use:** When data has repeating temporal structure (daily/weekly/seasonal cycles) and the task is to identify and compare different pattern types.
- **When to avoid:** When the number of distinct pattern types is too large to color-code meaningfully. Requires hierarchical clustering preprocessing.
- **Interesting properties:** Two linked views share color encoding. Calendar view (left) shows which days belong to which cluster. Aggregate curve view (right) shows the shape of each cluster's pattern. Together they answer "when does this pattern occur AND what does it look like."
- **Marks:** Points/lines (curves in aggregate view), colored cells (calendar view)
- **Channels:** Color hue (cluster identity, shared across both views); x-axis (time of day, in curve view); y-axis (measurement value); calendar position (day of week, week of year)
- **Annotation options:** Day/week/month labels on calendar; curve labels in aggregate view; shared color legend
- **Data types suited for:** Time series with recurring patterns; requires computing derived clustering attributes
- **Interesting feature extraction/manipulation of data:** Hierarchical clustering of daily curves → derived cluster assignment attribute. Average curve per cluster = derived representative curve. Calendar position = derived week-of-year / day-of-week attributes.

---

### Constrained / Justified 3D Layer View (p. 128)

- **What it shows:** Oscilloscope eye diagram where multiple overlapping time-series traces are spread into layers along a constrained depth axis ("drawer" metaphor).
- **When to use:** When separating overlapping signals into layers aids understanding AND the depth axis is kept orthographic (no perspective distortion), layers always face the viewer, and navigation is constrained.
- **When to avoid:** When unconstrained 3D navigation is required; when the task is precise magnitude comparison.
- **Interesting properties:** Example of justified 3D — depth used only to separate layers, not to encode magnitude. Orthographic projection prevents perspective distortion. Automatic framing/zooming during interaction reduces navigation complexity.
- **Marks:** Lines (traces)
- **Channels:** Position along depth (layer index), x-axis (time), y-axis (signal value)
- **Annotation options:** Layer labels, time axis labels
- **Data types suited for:** Temporal data with many overlapping signals where separation aids comparison.
- **Interesting feature extraction/manipulation of data:** Wrap-around time alignment is the key derived transformation that creates the eye diagram; spreading layers is a display transformation of the same data.

---

### 2D Point Cloud / Scatter Display (empirical reference, p. 130)

- **What it shows:** High-dimensional data reduced to 2D via dimensionality reduction, shown as colored points.
- **When to use:** When task is search or cluster estimation on dimensionally-reduced data. Outperforms 2D and 3D landscapes in controlled experiments (p. 130).
- **When to avoid:** When precise density estimation is the task (use contour plot instead).
- **Interesting properties:** Empirically shown to outperform both 2D and 3D terrain/landscape idioms for search and point estimation tasks (Tory et al., p. 130).
- **Marks:** Points (colored)
- **Channels:** 2D planar position (two derived synthetic dimensions from dimensionality reduction), color hue (cluster or category)
- **Annotation options:** Cluster labels, axis labels (synthetic dimension names), color legend
- **Data types suited for:** High-dimensional data after PCA/t-SNE/UMAP dimensionality reduction
- **Interesting feature extraction/manipulation of data:** Dimensionality reduction itself is the key data manipulation. Derived attributes: cluster membership, density.

---

### Information Landscape / Terrain Plot (anti-pattern reference, p. 129–130)

- **What it shows:** Point density on a 2D plane encoded as a 3D surface height, similar to geographic terrain.
- **When to use:** Very rarely. Marginally better than 3D landscape: use colored 2D contour/heatmap version when showing density.
- **When to avoid:** 3D landscape version consistently underperforms 2D point displays for search and estimation tasks. The familiar "landscape" metaphor does not help with abstract data tasks.
- **Interesting properties:** Proponents argue familiarity and engagement, but empirical evidence contradicts these claims for task performance.
- **Marks:** 3D surface
- **Channels:** Height (density — derived), position on ground plane (2D reduced dimensions), color (optional)
- **Annotation options:** Contour lines, color scale
- **Data types suited for:** 2D point data with density estimation. Prefer 2D contour plot.
- **Interesting feature extraction/manipulation of data:** Key manipulation: kernel density estimation to derive a continuous surface from discrete points.

---

### Small Multiples (referenced, p. 133)

- **What it shows:** The same visualization type repeated across a small grid of panels, each showing a different subset, time point, or condition.
- **When to use:** When comparing across many frames/conditions is needed and the full detail of each panel must be preserved. Preferred over animation for detailed multi-frame comparison tasks.
- **When to avoid:** When the number of panels exceeds what can be legibly displayed at sufficient detail (typically dozens, not hundreds, at current display resolutions). Not suitable when each panel requires significant interaction.
- **Interesting properties:** Exploits the "eyes beat memory" principle — all panels are simultaneously visible, so comparison uses perceptual system rather than memory. Outperforms animation for exploratory analysis tasks (Robertson et al., p. 133).
- **Marks:** Whatever the repeated idiom uses
- **Channels:** Same as repeated idiom + panel position encodes the faceting variable
- **Annotation options:** Panel labels (faceting variable value), shared or per-panel axes, connecting lines across panels
- **Data types suited for:** Any data faceted by a categorical or ordinal attribute. Time series faceted by time period. Spatial data faceted by season/condition.
- **Interesting feature extraction/manipulation of data:** Key manipulation: faceting/slicing by a categorical or temporal attribute into small equal panels. Derived attribute: the faceting variable itself.

---

### Heatmap (referenced, p. 146)

- **What it shows:** Two categorical/ordinal keys form a matrix; a single value attribute is encoded with color for each cell.
- **When to use:** Two keys + one value. Excellent for revealing patterns across a full matrix (correlations, co-occurrence, presence/absence).
- **When to avoid:** When precise value reading is required (color luminance/saturation are low-accuracy channels). When one key has too many levels (cells become too small).
- **Interesting properties:** Uses color saturation or luminance for value encoding — lower accuracy than position but allows a dense 2D matrix. Row/column ordering is a crucial design choice (cluster by value, not alphabetically).
- **Marks:** Area (cells/rectangles)
- **Channels:** Horizontal position (categorical key 1), vertical position (categorical key 2), color luminance/saturation (quantitative value)
- **Annotation options:** Row and column labels, color scale bar, cell value labels (for small matrices), hierarchical dendrogram alongside rows/columns
- **Data types suited for:** 2-key tables with one quantitative or ordinal value. Species × site presence/absence matrices, correlation matrices.
- **Interesting feature extraction/manipulation of data:** Hierarchical clustering of rows and columns to reveal block structure. Derived attributes: row/column cluster membership, sorted order.
