# [agent_21] Visualization Analysis and Design — pages 251-300

---

### Categorical Colormap (p.251–254)
- **What it shows:** Categorical/nominal attributes encoded through color groupings
- **When to use:** When encoding 6–12 distinct categories for visual grouping; best non-positional channel for categorical data
- **When to avoid:** More than 12 levels in non-contiguous small regions; never encode two multi-level categorical attributes simultaneously in bivariate colormap
- **Interesting properties:** Must include background and default object colors in the bin count; easily nameable colors improve memorability and discussion; highly saturated for small marks, lower saturation for large area marks
- **Marks:** Point, line, or area marks (saturation level must match mark size)
- **Channels:** Color hue (identity channel) as primary; luminance/saturation should be consistent across categories to avoid salience differences
- **Annotation options:** Color legend with named swatches; tooltip with category name
- **Data types suited for:** Categorical/nominal attributes with up to 12 levels
- **Interesting feature extraction/manipulation of data:** Aggregate excess categories into an "other" bin to stay within discriminable limit; exploit hierarchical structure to use one color per group

---

### Sequential Colormap (p.254–256)
- **What it shows:** Ordered/quantitative attributes encoded through a ramp from minimum to maximum
- **When to use:** Quantitative or ordinal attributes with a natural minimum and maximum and no meaningful midpoint
- **When to avoid:** Categorical data; attributes with a meaningful midpoint (use diverging instead)
- **Interesting properties:** Luminance-only = grayscale ramp; one end is a specific hue at full saturation, other end is pale/white or dark/black
- **Marks:** Any mark type
- **Channels:** Color luminance (magnitude channel) as primary; optionally hue for semantic segmentation within the ramp
- **Annotation options:** Colorbar legend with tick marks and value labels
- **Data types suited for:** Quantitative and ordinal attributes
- **Interesting feature extraction/manipulation of data:** Use segmentation (binning) to convert quantitative to ordinal, allowing explicit meaningful bin boundaries rather than relying on eye-based segmentation

---

### Diverging Colormap (p.255–256)
- **What it shows:** Ordered/quantitative attributes with a meaningful midpoint (zero, mean, threshold)
- **When to use:** When the attribute has a natural neutral midpoint and both directions from that midpoint are meaningful (e.g., positive/negative, above/below mean)
- **When to avoid:** Data without a meaningful midpoint
- **Interesting properties:** Two contrasting hues at endpoints, neutral color (white, gray, black, or high-luminance yellow) at midpoint; the zero/midpoint is semantically anchored
- **Marks:** Any mark type; commonly used for area marks (choropleth maps, heatmaps)
- **Channels:** Color hue (two hues) + luminance (monotonically increasing from midpoint outward)
- **Annotation options:** Colorbar with labeled midpoint; annotation of the midpoint value's meaning
- **Data types suited for:** Quantitative attributes with a meaningful midpoint
- **Interesting feature extraction/manipulation of data:** Derive a "difference" or "deviation from mean" attribute to create the diverging dimension; e.g., Cerebral (p.299–300) derives difference between two experimental conditions

---

### Bivariate Colormap (p.259–260)
- **What it shows:** Two attributes simultaneously encoded in color
- **When to use:** Safe only when one attribute is binary (two levels) — use two families varying in saturation; also usable for single categorical attribute with hierarchical structure
- **When to avoid:** Both attributes categorical with multiple levels (results will be poor); use with caution even for sequential–sequential or diverging–sequential combinations
- **Interesting properties:** The binary+categorical combination uses a base set of hues and varies saturation; multi-level bivariate colormaps appear frequently despite known interpretability issues
- **Marks:** Primarily area marks
- **Channels:** Hue (for one attribute) + saturation (for the other, especially binary)
- **Annotation options:** 2D color legend (matrix showing both attribute axes)
- **Data types suited for:** Two attributes where at least one is binary
- **Interesting feature extraction/manipulation of data:** Deliberately limit one attribute to binary classification if full encoding is not discriminable

---

### Tiltmap / Angle Encoding (p.262)
- **What it shows:** Ordered attributes encoded through the angle/orientation of a mark
- **When to use:** Sequential ordered data (within one 90° quadrant); diverging data (using arrow glyph across 180°); cyclic data (full 360° rotation)
- **When to avoid:** Fine-grained discrimination between values not near horizontal/vertical/diagonal; when length or position is available (more accurate channels)
- **Interesting properties:** Cyclic property: line marks cycle 4 times per full rotation; arrows cycle once; best accuracy near 0°, 45°, 90° positions
- **Marks:** Line marks or arrow glyphs
- **Channels:** Angle/tilt (magnitude channel); more accurate than area, less accurate than length
- **Annotation options:** Reference angle guide; labeled arrows
- **Data types suited for:** Sequential, diverging, or cyclic ordered data
- **Interesting feature extraction/manipulation of data:** Wind direction, flow direction, gradient direction in spatial fields

---

### LineUp: Multi-Attribute Ranking Table (p.271–273)
- **What it shows:** Multiple rankings of the same items by different weighted combinations of attributes; comparison of rankings across time/methods
- **When to use:** Comparing items along many quantitative attributes; exploring how ranking changes when weights or attributes change
- **When to avoid:** When users do not need to compare multiple rankings; purely nominal data
- **Interesting properties:** User derives data on the fly by choosing attribute weights; four alignment options provide different analytical tasks; between-column slope graphs show rank changes; scented widgets (histograms in column headers) show distributions; collapsed heatmap columns for compact overview
- **Marks:** Horizontal bar marks (stacked); slope graph line marks connecting items between columns; grayscale rectangle marks for collapsed heatmap columns
- **Channels:** Length (bar length encodes attribute contribution); position (spatial order encodes rank); slope/angle of connecting lines (encodes rank change); luminance (collapsed heatmap encodes value)
- **Annotation options:** Column headers with attribute names; histograms as scented widget decorations; rank number labels
- **Data types suited for:** Multi-attribute quantitative tables; ranked lists
- **Interesting feature extraction/manipulation of data:** Derive weighted combination attribute on the fly; use log-scale or normalized values within bars for comparability across attributes with different ranges

---

### Animated Transitions (p.273–274)
- **What it shows:** The process of change between two visualization states
- **When to use:** When change is limited in scope (small number of items change, or groups move together); bridging between reordering, filtering, or navigation states
- **When to avoid:** When many items change in different ways simultaneously (cognitive overload); when state difference is immediately obvious without animation
- **Interesting properties:** Empirically validated to improve graphical perception of change [Heer & Robertson 07]; can be decomposed into stages for complex transitions; alternative to jump cuts
- **Marks:** Same as the underlying visualization
- **Channels:** Motion channels (position change over time); temporal channel
- **Annotation options:** Progress indicator; "before" ghost marks
- **Data types suited for:** Any data type that can be visualized statically
- **Interesting feature extraction/manipulation of data:** Use staged transitions (e.g., first reorder, then resize, then recolor) to clarify the nature of the change

---

### Context-Preserving Visual Links (p.278)
- **What it shows:** Relationships between items in different views, drawn explicitly as curved link marks
- **When to use:** When implicit linked highlighting is not clear enough; when showing semantic relationships between items in different views
- **When to avoid:** When many links would create visual clutter
- **Interesting properties:** Routing algorithm considers four criteria: minimize link length, minimize occlusion of salient regions, maximize color contrast with crossed elements, maximize bundling of parallel links
- **Marks:** Curved line (connection) marks
- **Channels:** Position (routing), color (contrast with background), curvature/bundling
- **Annotation options:** Arrow direction; color coding by link type
- **Data types suited for:** Any data with relational or correspondence structure across multiple views
- **Interesting feature extraction/manipulation of data:** Can encode link importance with width or color

---

### LiveRAC: Semantic Zoom Grid of Time-Series (p.280–281)
- **What it shows:** Large collections of time-series data with adaptive detail level based on available space
- **When to use:** Large number of time series (e.g., system administration metrics) where user needs both overview and detail
- **When to avoid:** Single or few time series; when all series need full detail simultaneously
- **Interesting properties:** Semantic (not geometric) zooming — representation changes qualitatively: color only → sparklines with min/max dots → full axes → multiple superimposed lines; stretch-and-squish navigation for rows and columns
- **Marks:** Color fills (tiny); sparkline line marks with dot marks; full line chart marks
- **Channels:** Color (categorical, tiny); position (sparkline); length + position (full line charts)
- **Annotation options:** Axes appear at larger sizes; min/max dots appear at intermediate sizes
- **Data types suited for:** Many time series with one or more quantitative attributes
- **Interesting feature extraction/manipulation of data:** Min/max extraction per time window as derived attributes shown at intermediate zoom

---

### HyperSlice: Multi-Dimensional Slice Matrix (p.284–285)
- **What it shows:** All pairwise 2D slices of a high-dimensional scalar function
- **When to use:** Understanding structure of high-dimensional abstract data (e.g., optimization functions, parameter spaces)
- **When to avoid:** When data is not a scalar function of many variables; when fewer than 3 dimensions are involved
- **Interesting properties:** Views arranged in a symmetric matrix; each view is both display and navigation control (dragging changes the slice point); linked navigation across all views simultaneously
- **Marks:** Area marks in a 2D grid, with luminance encoding the function value
- **Channels:** Position (two dimensions per view); luminance (function value)
- **Annotation options:** Axis labels per view; shared slice position indicator
- **Data types suited for:** Multidimensional scalar fields; abstract high-dimensional quantitative data
- **Interesting feature extraction/manipulation of data:** Fixing slice coordinates reduces dimensionality; can reveal independence between variables if slices show similar structure

---

### Bird's-Eye Map (Overview–Detail, Geographic) (p.295–296)
- **What it shows:** Geographic data at two scales simultaneously — full extent (overview) + detailed region (detail view)
- **When to use:** Geographic navigation tasks where context and detail are both needed; any spatial data with multi-scale structure
- **When to avoid:** Non-spatial data; when full dataset fits comfortably at single zoom level
- **Interesting properties:** Both views use same encoding and same dataset; differ only in viewpoint and size; rectangle in overview marks the detail view region; bidirectional linkage allows controlling detail view from overview
- **Marks:** Spatial marks (points, lines, areas) in both views; rectangle mark in overview
- **Channels:** Position (spatial, given geography); size difference between views provides context
- **Annotation options:** Rectangle border in overview; labels visible in detail but not overview
- **Data types suited for:** Geographic/spatial data; any spatially embedded data
- **Interesting feature extraction/manipulation of data:** Region selection from overview as input to further analysis

---

### Multiform Overview–Detail System (Microarrays) (p.296–298)
- **What it shows:** Time-series gene expression data at multiple levels: overview of all genes across time; detail of derived metrics for a selected time window; list of gene names
- **When to use:** When no single view suffices for a domain task; when task requires both discovery of patterns and lookup of specific items
- **When to avoid:** Simple data where one view is sufficient
- **Interesting properties:** Three different view types serving distinct tasks (pattern discovery in graph view; comparison of derived attributes in scatterplot; browsing/lookup in list view); list view seems trivial but provides essential textual overview and direct item selection
- **Marks:** Line marks (graph view); point marks (scatterplot); text marks (list)
- **Channels:** Position x/y (time + value in graph; derived attributes in scatterplot); color hue (functional gene group); label text (gene names); time slider (interactive window selection)
- **Annotation options:** Functional group color legend; axis labels; gene label on hover in scatterplot
- **Data types suited for:** Multidimensional tables with time series; derived quantitative attributes
- **Interesting feature extraction/manipulation of data:** Three derived attributes: value change, percentage of max value, fold change (log-scale) — all computed within the interactively selected time window

---

### Cerebral: Small Multiple Network Views (p.299–300)
- **What it shows:** Same gene interaction network colored by expression level under different experimental conditions; main view shows derived difference attribute between two selected conditions
- **When to use:** Comparing the same network structure across multiple categorical conditions; when both the network topology and attribute differences are of interest
- **When to avoid:** When conditions are too numerous (visual clutter in small multiples); when network is too large for small-multiple rendering
- **Interesting properties:** Small multiples use diverging red-green colormap per condition (domain convention); main view derives a difference attribute (orange-blue) between two selected conditions; parallel coordinates view provides an additional encoding at the bottom; aligned matrix of small multiples is reorderable
- **Marks:** Node marks (circles); link marks (edges); containment marks (coregulated groups); parallel coordinate axis marks
- **Channels:** Vertical position (cell location of interaction); color diverging (gene activity per condition or difference); containment (group membership)
- **Annotation options:** Condition labels on small-multiple titlebars; highlighted titlebars for selected conditions; node labels
- **Data types suited for:** Network + multidimensional table with shared key (gene); categorical condition attribute
- **Interesting feature extraction/manipulation of data:** Derived difference attribute between two selected conditions — enables direct comparison of two conditions in the main view

---

### Slope Graph / Bump Chart (p.272)
- **What it shows:** Change in ranking or value between two or more time points or conditions
- **When to use:** Showing rank changes between categories across a small number of time points; used between columns in LineUp to show ranking changes
- **When to avoid:** Many intermediate points (line chart is better); when absolute values rather than rank changes are the focus
- **Interesting properties:** Also known as bump charts; straight lines = no rank change; crossing lines = significant rank change; angle of slope encodes magnitude of change
- **Marks:** Line marks connecting same item across columns
- **Channels:** Slope/angle (rank change magnitude); color (item identity); position (rank)
- **Annotation options:** Labels at endpoints; color coding by category
- **Data types suited for:** Ranked/ordered attributes at multiple time points; categorical items with quantitative rankings
- **Interesting feature extraction/manipulation of data:** Rank transformation of quantitative values before plotting; weighted-combination ranking as derived attribute

---

### Small Multiples (General Idiom) (p.298–299)
- **What it shows:** Same visual encoding applied to different partitions of a dataset; allows simultaneous comparison across categories, conditions, or time periods
- **When to use:** Comparing patterns across many categories/conditions; as an alternative to animation when all frames need to be visible; when the number of views is manageable (~few dozen)
- **When to avoid:** When partitions are too numerous for the available screen space; when users need to see the full dataset rather than partitions
- **Interesting properties:** Shared encoding = common reference frame for comparison by position; aligned in list or matrix maximizes positional comparison precision; simultaneous visibility eliminates memory load; each view shows ~several hundred elements maximum
- **Marks:** Same as underlying encoding (any)
- **Channels:** Position (primary comparison channel between views); any channels used in individual views
- **Annotation options:** Partition label per view (category name, condition, time period); shared axis labels or scale
- **Data types suited for:** Any data type with a categorical or ordinal partitioning attribute; temporal data with discrete time steps
- **Interesting feature extraction/manipulation of data:** Hierarchical partitioning — order of attributes used for partitioning profoundly affects what patterns become visible
