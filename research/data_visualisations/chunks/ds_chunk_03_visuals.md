# [agent_08] Data Sketches — pages 101-150

---

### Radial Color Scatter (Sunburst-style) (p. 107–111)
- **What it shows:** Distribution of photo colors (extracted from vacation photos) across time-of-day and sorted by hue, organized into per-trip radial clusters.
- **When to use:** When the data *is* color (image datasets), and you want to show both temporal structure (time of day) and chromatic structure (hue spectrum) simultaneously. Avoid when data does not have meaningful hue values.
- **Interesting properties:** Each trip is its own radial cluster; colors are positioned using force simulation to de-overlap while nudging toward trigonometrically-calculated x/y. The "gooey effect" (SVG blur + high contrast) was considered for blending. The hue → radius encoding creates a natural rainbow gradient from center outward.
- **Marks:** Colored circles/dots (each = one color extracted from one photo)
- **Channels:**
  - Angle = time of day the photo was taken (temporal)
  - Radius = hue (HSV value, quantitative)
  - Color fill = the actual extracted color (nominal/literal)
  - Spatial cluster grouping = which trip (categorical)
- **Annotation options:** Per-day hover arcs (d3.arc pie-slice shape); annotations show where/with whom/enjoyment rating per day.
- **Data types suited for:** Quantitative (color values), temporal (time of day, day of trip), categorical (trip identity)
- **Interesting feature extraction/manipulation:** Colors extracted via `get-image-colors` from resized thumbnail images (not full-size); top 5 colors per photo; sorted by HSV hue value rather than raw RGB order. ~4,000 colors total from ~800 images (every 5th photo across 4 years of travel).

---

### Network / Force-Layout Genealogy Graph ("Royal Constellations") (p. 119–131)
- **What it shows:** Genealogical relationships among ~3,000 European royals, structured so that birth year determines horizontal position and family proximity to current monarchs determines vertical clustering and opacity.
- **When to use:** Relational data with both hierarchy and lateral connections (family trees, org charts, citation networks). Especially powerful when a temporal axis can be embedded. Avoid if the network is too dense without a meaningful axis to "pull apart" the hairball.
- **Interesting properties:** The "constellation" metaphor — dark background, glowing star-like nodes, star temperature color scale on hover — transforms a genealogy chart into an aesthetic night-sky visualization. The gravitational pull technique: nodes are not placed by pure force, but pulled toward a calculated x/y position derived from birth year (x) and closest royal family (y). Opacity encodes distance from power rather than filtering it out.
- **Marks:** Circles (nodes = people); lines (edges = family connections)
- **Channels:**
  - Horizontal position = birth year (temporal, quantitative — estimated for ~40% of records)
  - Vertical position = which of the 10 current royal families the person is closest to (categorical ordinal)
  - Node size = large for current hereditary leaders, small for all others (categorical binary)
  - Node color = birth year gradient (dark blue → yellow, temporal quantitative)
  - Node opacity = hop distance to nearest current monarch (quantitative — close = opaque, distant = transparent)
  - Line style = solid (blood relation) vs. dotted (marriage) — categorical
- **Annotation options:** Named labels for historically famous royals (Henry VIII, Marie Antoinette, etc.); introduction/legend at top; hover state shows name and generation count; click interaction shows shortest path.
- **Data types suited for:** Relational (network edges), temporal (birth/death dates), categorical (royal family membership), quantitative (hop distance)
- **Interesting feature extraction/manipulation:** Birth dates estimated for 40% of missing records using R script (death date minus 60 years, or inferred from spouse/children dates); hop distance to each of 10 monarchs pre-calculated and stored; non-linear squish of date scale for older centuries to focus on the most recent 200 years.

---

### Scroll-Animated Headshot Grid → Timeline Transition (p. 139–141)
- **What it shows:** Obama late-night TV appearances, first grouped by show host (grid), then rearranged by date (timeline), with scroll driving the animated transition between layouts.
- **When to use:** When you have the same items that need to be viewed through multiple organizational lenses (by category, then by time). Scrollytelling is best when there is a narrative progression and a general audience. Avoid for analytical audiences who need free exploration.
- **Interesting properties:** The same marks (photo headshots) serve as both categorical identifiers (which show) and temporal markers (when it occurred), with the transition itself being the insight — watching items reorganize from one frame to another reveals the structure change. Links between Obama headshots and host headshots appear during the timeline view and are revealed/highlighted on hover.
- **Marks:** Photographic headshots (each = one TV appearance)
- **Channels:**
  - Grid position (section 1) = show host grouping (categorical)
  - x-position (section 2) = date of appearance (temporal)
  - y-position / y-grouping (section 2) = Obama vs. host (categorical)
  - Links between marks = which host corresponded to which appearance (relational)
- **Annotation options:** Hover on host headshot highlights all corresponding guest appearances; text annotations per section describe what the layout reveals.
- **Data types suited for:** Categorical (show, person identity), temporal (date of appearance), relational (guest-host pairing)
- **Interesting feature extraction/manipulation:** IMDb credits cross-referenced with Wikipedia list of late-night shows; YouTube API used to find video clips; only 58 of 244 videos were relevant after manual filtering — data cleaning as design constraint (missing data is shown transparently rather than hidden).

---

### Bubble with Dual Radii + Dot Ring ("Video Emotion Glyph") (p. 141)
- **What it shows:** For each Obama YouTube video: view count, duration, and moments of detected joy/laughter — all encoded on a single circle glyph.
- **When to use:** When 3 variables need to be shown simultaneously for many items, and those variables naturally correspond to a center quantity, an outer boundary, and discrete events on the boundary. Avoid when all three channels are difficult to decode simultaneously — the author themselves noted this is "overwhelming and confusing."
- **Interesting properties:** A composed glyph that stacks three encodings: filled circle (one quantitative), outer ring (second quantitative), small dots on ring (discrete events). The temporal placement on the x-axis (shared with previous section) maintains continuity across scrollytelling sections.
- **Marks:** Filled circles (inner); ring/arc (outer); small dots on ring (event markers)
- **Channels:**
  - Filled circle radius = number of views (quantitative)
  - Outer ring radius = video duration (quantitative)
  - Dot position on ring = timestamp of detected joy expression (temporal within video)
  - x-position = date of appearance (temporal)
- **Annotation options:** Caption describing laughter count for POTUS vs. FLOTUS.
- **Data types suited for:** Quantitative (views, duration), temporal (date, moment within video), categorical (video identity)
- **Interesting feature extraction/manipulation:** Emotion detection via Google Cloud Vision API on screenshots taken at every caption timestamp; joy moments extracted from frame-level facial emotion scores.

---

### Fisheye Timeline (p. 143)
- **What it shows:** A dense horizontal timeline of video captions and detected emotions, with fisheye distortion that magnifies the hovered region while keeping context visible.
- **When to use:** When a timeline has too many items to read individually at normal scale, but you don't want to lose the overview. Particularly useful for long-duration time series with discrete events. Avoid when the distortion would mislead quantitative comparisons.
- **Interesting properties:** The fisheye creates a lens effect — the region under the mouse expands, adjacent regions compress, and the full timeline remains visible. Hovering shows the actual video screenshot (with emoji-overlaid faces) for that caption moment. The timeline serves as both a navigation tool and a data display.
- **Marks:** Segments/slices (each = one caption/moment in video); image thumbnail (on hover)
- **Channels:**
  - x-position = time within video (temporal)
  - Color or marking on segment = emotion detected (categorical: joy/neutral)
  - Fisheye distortion magnitude = proximity to cursor (spatial interaction)
- **Annotation options:** Caption text shown on hover; full screenshot with emoji faces overlaid.
- **Data types suited for:** Temporal (moment within video), categorical (emotion type), qualitative (caption text)
- **Interesting feature extraction/manipulation:** Caption timestamps from YouTube `vtt` files converted to JSON; screenshots taken with ffmpeg at those timestamps; faces detected and emotions scored by Google Cloud Vision API; all joined by timestamp.
