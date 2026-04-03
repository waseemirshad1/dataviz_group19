# [agent_21] Visualization Analysis and Design — pages 251-300

## Chapter 10 (cont.): Map Color and Other Channels (pp.251–266)

### Color Channels — Colormaps

**Categorical Colormaps** (p.251–254)
- Also called qualitative colormaps; designed to encode categories and groupings
- Best channel after spatial position for categorical data
- Use color as an integral identity channel — encode ONE attribute, not three separate channels (hue/saturation/luminance)
- Discriminable colors for small separated regions: **6–12 bins maximum** (include background and default colors in the count)
- Prefer easily nameable colors: red, blue, green, yellow (opponent color axes); then orange, brown, pink, magenta, purple, cyan
- Luminance contrast is a major issue: colors should be close in luminance to avoid salience differences; OR sufficiently different in luminance to be distinguishable in grayscale
- Colormaps for small regions (lines, points): high saturation; large regions (areas): low saturation — the mark type matters (p.252)
- Practical tool: **ColorBrewer** at colorbrewer2.org (p.252)
- Anti-pattern: using >12 categorical colors for small, non-contiguous regions — up to 21 can be distinguished in large contiguous areas, but only ~12 in small scattered regions (p.253–254)

**Two solutions to discriminability mismatch** (p.254):
1. Reduce number of bins via data transformation — exploit hierarchy, aggregate into meaningful groups, or filter to top categories + "other"
2. Use a different visual encoding that adds other channels (shape, size, complex glyphs) in addition to color

**Ordered Colormaps** (p.254–256)
- Sequential colormap: minimum to maximum value; if luminance only = grayscale ramp; one hue at full saturation at one end, pale/white at other; or dark/black at other end
- Diverging colormap: two hues at endpoints, neutral (white/gray/black/yellow) at midpoint
- Number of hues in continuous colormap determines what level of structure is emphasized:
  - Many hues (rainbow): emphasizes mid-level neighborhood structure (p.257)
  - Two hues: emphasizes large-scale structure (p.257)

**Problems with Rainbow Colormaps** (p.257–258) — key anti-pattern:
1. Hue encodes order but hue is an identity channel (expressiveness mismatch)
2. Not perceptually linear — same-size numeric ranges look different at different parts of the scale
3. Fine detail cannot be perceived via hue; luminance is much better for edge detection

**Solution: Monotonically increasing luminance colormaps** (p.258):
- Combine multiple hues ordered by luminance (lowest to highest)
- Varying hues allow mid-level categorical segmentation
- Luminance provides perceptual ordering (magnitude channel)
- Supports high-level distinctions AND low-level fine structure

**Segmented rainbow** (p.259): acceptable for categorical data with few categories; acceptable for ordered data where perceptual nonlinearity is solved by explicit discretization into bins — better to bin deliberately than to rely on the eye to create unequal bins

**Bivariate Colormaps** (p.259–260):
- Safest: univariate (one attribute per colormap)
- Safe bivariate case: one attribute is binary — use two color families varying in saturation
- Poor result: two categorical attributes with multiple levels each — avoid
- Middle ground: sequential–sequential, diverging–diverging etc. with 3 levels each — used but some people find interpretation difficult

**Colorblind-Safe Design** (p.260):
- Red-green color blindness: affects 8% of males, 0.5% of females
- Confused pairs: red/black, blue/purple, light green/white, brown/green
- Solution: vary luminance OR saturation in addition to hue; avoid red-green diverging ramps
- Practical tool: color blindness simulators (Adobe Illustrator, Photoshop, web tools)

---

### Other Channels (pp.261–265)

**Size Channels** (p.261):
- Size is a **magnitude channel** suitable for ordered data
- Length (1D): extremely accurate — comparable to unaligned planar position; only aligned planar position is more accurate
- Area (2D): significantly less accurate — Stevens power law exponent 0.7; mid-range in rankings
- Volume (3D): quite inaccurate — bottom of rankings, equivalence class with curvature; rarely the right choice
- Length and area cannot be simultaneously used to encode different dimensions (subsumed)
- Combination of width and height often perceived as areas, not two separate dimensions (integral, not separable)

**Angle Channel** (p.262):
- Magnitude channel for orientation of a mark
- Angle = orientation relative to another line; Tilt = orientation against global display frame
- Less accurate than length and position; more accurate than area
- Cyclic property: line mark cycles 4 times per full 360° rotation; arrow cycles once
- Sequential within 90° quadrant; diverging with 180° arrow glyph (like a diverging colormap)
- Best accuracy near exact horizontal, vertical, or diagonal positions (89° vs 90° distinguishable); poor accuracy in between (37° vs 38° not distinguishable)

**Curvature Channel** (p.263):
- Only usable with line marks (not points, not areas)
- ~2–3 distinguishable bins — bottom of magnitude rankings (equivalence class with volume)

**Shape Channel** (p.263):
- **Identity channel** — for categorical data
- Applicable to point marks (common) and line marks (stipple patterns)
- Cannot be applied to area marks
- Up to dozens/hundreds of bins if point size is large; far fewer when space is limited (e.g., ~12 in a 10×10 pixel area)
- Interference with other channels similar to size; filled shapes (disks) are good substrate for color hue

**Motion Channels** (p.264):
- Types: direction of motion, velocity, flicker frequency
- Extremely salient; strongly separable from all static channels (especially color and position)
- Cannot be selectively ignored — major strength and weakness
- Flicker/blinking: nearly impossible to ignore; use with great care
- Safe strategy: binary motion channel (moving vs not moving) — for highlighting only
- Best for transient highlighting (mouseover, click) not permanent encoding (p.264)

**Texture and Stippling** (p.264–265):
- Three perceptual dimensions: orientation, scale, contrast (maps to angle, size, luminance channels)
- Categorical use: 1–2 dozen distinguishable bins with careful design across all three dimensions
- Ordered use: 3–4 bins per dimension individually; ~12 bins when all three combined for one attribute
- Stippling: short strokes filling regions; dotted/dashed lines are line-mark case; area stippling less used now with color printing

---

## Chapter 11: Manipulate View (pp.267–287)

### The Big Picture — Change, Select, Navigate (p.268–269)

**Five major options for handling visual complexity** (p.269):
1. Derive new data
2. Change view over time (this chapter)
3. Facet data into multiple views (Chapter 12)
4. Reduce data shown in view (Chapter 13)
5. Embed focus+context in single view (Chapter 14)

**Why Change?** (p.269): Computer display's fundamental advantage over print — interactivity enables dynamic response to user input

### Changing Views Over Time (p.269–272)

**What can be changed** (p.269–271):
- Visual encoding (switch between idioms completely, e.g., node-link to matrix)
- Encoding parameters (e.g., mark size range)
- Arrangement/ordering (sorting by different attributes)
- Viewpoint (navigation)
- Filtered attributes
- Aggregation level

**Reordering / Sorting** (p.271):
- Powerful technique — exploits position as highest-ranked channel
- Works for any categorical attribute
- Does NOT apply to ordered attributes (already have a given order)
- Allows pattern-finding by the visual system in new spatial configurations

**Example: LineUp system** (p.271–273):
- Supports exploration of multi-attribute tables via reordering and realignment
- Sort by individual attributes OR weighted combinations of multiple attributes
- Designed for comparing multiple rankings
- Encoding: stacked bar charts + slope graphs (bump charts) between columns
- Scented widgets: histograms in column headers show distributions
- Collapsed heatmap view: grayscale encoding instead of bar length
- Four alignment options: classical stacked, diverging stacked, ordered stacked, separately aligned (small multiples)
- Uses animated transitions between alignment states

**Animated Transitions** (p.273–274):
- Alternative to jump cuts (abrupt change between states)
- Benefits: maintain user context; show how items move from old to new position
- Limitations: only effective when amount of change is limited; people cannot track many simultaneous changes
- Work well: small number of objects changing, OR groups moving together
- Empirical evidence: properly designed animated transitions improve graphical perception of change [Heer & Robertson 07]

### Selection Design Choices (p.274–278)

**What can be selected** (p.275):
- Data items (most common)
- Links (network data)
- Data attributes
- Levels within an attribute (all items sharing a value)
- Views themselves (in multi-view systems)

**Number of selection types** (p.275–276):
- Single type (binary: selected/not)
- Two types: e.g., click vs hover
- Multiple types with keyboard modifiers

**Selection set size** (p.276):
- Exactly one item (replaced when new item selected)
- Many items (requires add/remove/clear actions)
- Zero is valid (leave detail pane blank)
- Primary vs secondary selection (e.g., source vs target in path traversal)

**Highlighting** (p.276–278):
- Selection must trigger highlighting for immediate visual feedback
- Two independent design decisions: (1) how user selects, (2) how selected elements are highlighted
- Highlight methods:
  - Color change (very common; drawback: hides existing color coding temporarily)
  - Outline addition/change (preserves color coding; less salient for small marks)
  - Size change (increase item size or line width)
  - Shape change (e.g., solid line to dashed)
  - Motion coding (oscillation around location) — empirically outperforms color/outline/size [Ware & Bobrow 04]
  - Connection marks between selected objects (explicit links)
- Combinations increase salience (e.g., increased width + color change for links)
- Highlight color must create visual popout — sufficient hue, luminance, or saturation contrast

**Context-Preserving Visual Links** (p.278): link marks drawn as curves routed between existing elements; routing considers link length, occlusion of salient regions, color contrast with crossed elements, and bundling

**Selection outcomes** (p.279): selection often first step in chained sequence — output becomes input to next action (filter, aggregate, encode, reorder, navigate to)

---

### Navigate: Changing Viewpoint (p.279–286)

**Three components of navigation** (p.279):
- Zoom: camera moves closer/farther from plane
- Pan/Translate: camera moves parallel to image plane
- Rotate: camera spins (rare in 2D, important in 3D)

**Navigation outcomes**: filtering (zoom in/pan) or aggregation/overview (zoom out) (p.280)

**Geometric Zooming** (p.280): corresponds to real-world experience of moving closer/farther; object appearance is fixed, only size changes

**Semantic Zooming** (p.280–281):
- Representation of objects adapts to available pixels
- Appearance can change dramatically at different scales (not just size change)
- Example: LiveRAC — time-series grid with adaptive content: color only (tiny), sparklines (small), full axes and superimposed line charts (large)
- Stretch-and-squish interaction is a focus+context approach

**Constrained Navigation** (p.281–282):
- Limits camera motion to prevent getting lost; prevents interpenetration, empty frames
- Common constraints: limit zoom range; auto-calculate camera trajectory to frame selected item
- Particularly powerful when combined with linked navigation across multiple views
- Both constrained (shortcuts) and unconstrained (backup) can coexist

---

### Navigate: Reducing Attributes (p.282–286)

**Slice** (p.283–284):
- Extract only items matching a chosen value in one dimension
- Reduces dimensionality (e.g., 3D to 2D)
- Axis-aligned slices may correspond to familiar views (coronal, sagittal, horizontal)
- Generalizes to hyperplanes; can eliminate multiple dimensions at once

**Cut** (p.285):
- Divides viewing volume with a plane; hides everything on the camera-facing side
- Shows more than slice (surrounding 3D context is still visible behind cutting plane)
- Can be axis-aligned or arbitrarily oriented

**Project** (p.285–286):
- All items shown but values for excluded dimensions are dropped
- Orthographic: simply drops excluded dimension values — all depth information lost
- Perspective: retains partial depth info via foreshortening
- Map projections: transform curved Earth surface to flat — trade-offs between distorting angles vs areas

---

## Chapter 12: Facet into Multiple Views (pp.289–300)

### Big Picture — Faceting Strategies (p.290)

**Two main faceting approaches**:
1. Juxtapose views side by side (multiple coordinated views)
2. Superimpose views as layers within a single view

**Cost/benefit of juxtaposition**:
- Benefit: simultaneous visibility → easy eye movement comparison (Eyes Beat Memory)
- Cost: screen real estate — two views → each gets half the area

**Cost/benefit of superimposition**:
- Benefit: no extra screen space needed
- Cost: strong limits on layers before clutter: 2 is feasible, 3 possible with care, more is very difficult (p.291)

### Why Facet? (p.290–291)
- No single encoding optimal for all tasks → multiform views support more tasks
- Linked highlighting allows seeing whether spatial neighborhood in one view is contiguous in others
- Partitioning is powerful, especially hierarchical — order of attributes used to partition profoundly affects visual salience (p.291)
- Trade-off: display area (scarce external resource) vs working memory (scarce internal resource) (p.291)

### Juxtapose and Coordinate Views (p.267 = p.292 in book)

**Four major design choices for coordination** (p.292):
1. Share encoding (same or different visual encoding across views)
2. Share data (all, subset, or none)
3. Highlight linking
4. Share navigation (synchronized viewpoint)

**Share Encoding: Same/Different** (p.292–293):
- Shared encoding: identical encoding across views
- Multiform views: different encoding in some/all views (different spatial layouts, same color coding, etc.)
- Linked highlighting: items selected in one view immediately highlighted in all others — a shared color channel encoding
- Central benefit: seeing how a region contiguous in one view is distributed in another
- Multiform rationale: a single view has strong limits on simultaneous attributes; multiple views can show subsets and exploit different encoding strengths

**Example: EDV (Exploratory Data Visualizer)** (p.293–294):
- Baseball stats with linked bar charts, scatterplots, histograms
- Selecting high salaries in histogram reveals their distribution in other views
- Bottom cluster in scatterplot corresponds to specific field positions

**Share Data: All, Subset, None** (p.294–295):
- All data in each view: common with multiform (different encoding per view)
- Overview–detail: one view shows full dataset, another shows subset
- Small multiples: different partitions of dataset in each view

**Overview–Detail** (p.294–296):
- Large view for detail exploration + small "bird's-eye" view for context
- Minimum linkage: unidirectional (overview rectangle updates as detail view pans/zooms)
- Bidirectional: rectangle in overview can also move the detail view
- Detail-on-demand: popup or fixed panel showing extra info about selected item(s)

**Example: Bird's-Eye Maps** (p.295–296):
- Geographic maps with small overview window
- Same encoding + same dataset + different viewpoints/sizes
- Rectangle in overview shows currently visible region in detail view

**Example: Multiform Overview–Detail Microarrays** (p.296–298):
- Dataset: genes × time × microarray measurements
- Derived attributes: value change, percentage of max value, fold change (log-scale)
- Graph view (overview): globally superimposed line charts — all genes, time on x-axis
- Scatterplot (detail): user selects time window in graph view; scatterplot shows derived attributes for that window; color encodes functional gene groups; label on hover
- List view: all gene names in alphabetical order — textual overview, browsing, lookup
- Key insight: "a text list may seem trivial as a stand-alone view, but plays useful roles in multi-view systems" (p.298)

**Small Multiples** (p.298–299):
- Same encoding, different data partitions → common reference frame for comparison
- Aligned in list or matrix for comparison with highest precision
- Inverse of multiform views (encoding identical, data differs)
- Weakness: screen real estate — operational limit ~few dozen views × several hundred elements each
- Strength: simultaneous visibility → glance quickly without interaction or memory load
- Often alternative to animation (all frames visible simultaneously vs one by one)
- Animation imposes massive memory load when change between frames is complex and distributed

**Example: Cerebral** (p.299–300):
- Dataset: genes × experimental condition × gene activity (multidimensional table) + gene interaction network
- Main view: node-link network; nodes = genes; links = known interactions; vertical position = cell location; containment marks = coregulated groups
- Small-multiple views: partitioned by condition, colored with diverging red-green colormap per condition
- Large view color: diverging orange-blue encoding DIFFERENCE between two selected conditions (derived attribute)
- Also multiform: parallel coordinates view at bottom
- Linked navigation between views

**Share Navigation: Synchronize** (p.276 = p.301 in book):
- Moving viewpoint in one view synchronized to movement in others
- Common in map overview+detail

**Summary design matrix** (p.276 = p.301):
- Encoding same/different × Data all/subset/none → 6 possibilities:
  - Same encoding + all data = REDUNDANT (avoid)
  - Same encoding + subset = Overview–Detail
  - Same encoding + partition = Small Multiples
  - Different encoding + all data = Multiform
  - Different encoding + subset = Multiform Overview–Detail
  - Different encoding + different data = NO LINKAGE (avoid)

---

## Key Rules of Thumb and Anti-Patterns

- **6–12 color bins max** for non-contiguous small regions in categorical colormaps (p.251)
- **Avoid rainbow colormaps** as default; they have three serious perceptual problems (p.257)
- **Use monotonically increasing luminance** colormaps for ordered data with multiple hues (p.258)
- **Low saturation for large areas, high saturation for small regions** (p.252)
- **Volume encoding is almost never right** — too inaccurate (p.261)
- **Area encoding is less accurate** than length; consider whether users will accidentally make length judgments (p.261)
- **Motion is nearly impossible to ignore** — use only for transient highlighting (p.264)
- **Flicker/blink should be used with great care** (p.264)
- **Animation has high cognitive load** — use animated transitions only when change is limited in scope (p.273–274)
- **Eyes Beat Memory**: juxtaposed views allow eye movement comparison; changing views require working memory (p.291)
- **Two layers feasible, three with care, more very difficult** for superimposed views (p.291)
- **Reordering uses position channel** (highest ranked) to reveal patterns; powerful for exploration (p.271)
- **Constrained navigation** prevents getting lost; auto-frame-selected-item trajectory is good design (p.282)
- **Colorblind-safe**: avoid encoding information with hue alone; vary luminance/saturation; avoid red-green diverging ramps (p.260)
- **Text list views seem trivial but play useful supporting roles** in multi-view systems (p.298)
- **Small multiples often preferable to animation** for complex, spatially distributed changes (p.299)
