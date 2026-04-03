# [agent_08] Data Sketches — pages 101-150

## Overview of Pages Covered

Pages 101–150 span three projects:
- **"Four Years of Vacations in 20,000 Colors"** by Shirley Wu (pp. 102–113): Personal travel photos reduced to color data and visualized radially.
- **"Royal Constellations"** by Nadieh Bremer (pp. 117–132): European royal family genealogy as a network/constellation diagram.
- **"Putting Emojis on the President's Face"** by Shirley Wu (pp. 133–148): Obama late-night TV appearances, video captions, and facial emotion detection visualized as scrollytelling.

---

## Goal and Function of Visuals

- A visualization can serve **personal discovery** — Shirley found that her red/orange photo colors mapped to food photography, not travel scenery, only once she explored the data visually. (p. 109)
- Visualizations can function as **commemorative artifacts** — the travel piece was valued as a personal memory record, not just an analytic tool. (p. 111)
- Visualizations can be **multi-section scrollytelling narratives** — breaking a rich, multi-dimensional dataset into sequential reveals, where the reader only needs to scroll. (p. 137, p. 142)
- **Audience response matters but should not be the only measure of success** — the Obamas project received less external praise than its effort warranted, teaching the lesson that the process of learning counts independently of reception. (p. 144)

---

## Marks and Channels

### Color as the Primary Mark (pp. 103–111)
- When data IS color (e.g., extracted image colors), color is both the mark and the data. The design challenge shifts to arranging those colors meaningfully.
- **Hue** was mapped to radius in the radial layout; **time of day** mapped to angle. This created a sunburst-style distribution.
- Swapping the encoding (hue → angle, time → radius) was tried but rejected: the first day of a trip would be a tiny arc, the last day a large arc — **inaccurate spatial representation of equal time units**. Lesson: radial circumference grows with radius, so time mapped to radius creates perceptual distortion. (p. 109)

### Node-Link (Network) Marks (pp. 119–128)
- **Nodes** = people (circles); **links** = family connections (lines)
- Node size: large circles for current royal hereditary leaders; small for others
- Node color: birth year mapped to color gradient (dark blue = oldest → yellow = youngest)
- Node opacity: distance from a current monarch — close relatives are fully visible, distant relatives fade to near-transparent. This creates a **focus + context** effect without filtering data out. (p. 125)
- Link style: solid line = blood relation; dotted line = marriage. **Visual encoding of relationship type via line texture/dash pattern.** (p. 127)

### Icon/Headshot as Marks (pp. 139–141)
- Each Obama late-night appearance was represented by a **photographic headshot** of the person who appeared — treating a photograph as a categorical mark.
- The same marks transition between layouts (grid by show host → timeline by date) via scroll-driven animation, showing that **the same mark can serve multiple spatial encodings across sections**.

### Circles with Dual Radii (p. 141)
- Inner filled circle radius = number of views (quantitative)
- Outer ring radius = duration of video (quantitative)
- Small dots on the ring = moments of detected joy/laughter (categorical/temporal)
- This stacks three variables onto a single circular mark — a composed glyph.

---

## Task-Encoding Fit

| Task | Channel Used | Example from pages |
|---|---|---|
| Identify time structure | Angle in radial layout | Time of day → angle in travel visualization (p. 107) |
| Identify color type | Hue → radius (sorted HSV) | Detecting food photos vs. nature photos (p. 109) |
| Compare relatedness | Opacity gradient | Closeness to royal family leaders (p. 125) |
| Find shortest path | Highlighted path + fade-out of others | Royal Constellations shortest path interaction (p. 127) |
| Explore chronological structure | Horizontal position forced by birth year | Network pulled apart chronologically (p. 123–124) |
| Distinguish relationship type | Line style (solid vs. dotted) | Blood vs. marriage in Royal Constellations (p. 127) |
| Navigate dense timeline | Fisheye distortion on hover | Obama video timeline (p. 143) |

---

## Data Manipulation

- **Extracting primary colors from images**: Images were resized to thumbnails (13KB), then a color-extraction library (`get-image-colors`) returned the top 5 colors per photo. Crucial lesson: **always pass the smallest version of the data to computation** — processing full-size images was 30x slower for no gain. (p. 104)
- **HSV sorting**: Colors were sorted by hue-saturation-value to create a visually coherent radial gradient, not just random dot placement. (p. 107)
- **Estimating missing birth years**: For the genealogy dataset, ~40% had no birth date. R script inferred birth year from death date (subtract 60 years) or from relatives' dates. This enabled the chronological force layout axis. (p. 120, 124)
- **Calculating network distance**: For each of 3,000 people, the shortest hop count to each of 10 current monarchs was pre-calculated and stored, then used both for opacity and for gravitational pull in layout. (p. 125)
- **Face detection timestamps**: Video screenshots were taken at every caption timestamp, uploaded to Google Cloud Vision API, and returned face bounds + emotion scores, then joined with caption data. (p. 135)

---

## Design Process Guidance

- **Always explore the data before sketching** — Shirley's "Man Peeing into Puddle" failure (Fig. 3.6, p. 106) resulted from sketching an idea without first checking if the data would support it. Key rule: explore first, design second.
- **Data exploration workflow** (Shirley's personal process, p. 106):
  1. Identify the "lowest" unit of data (one photo, one color, one person)
  2. List all attributes and tag each as quantitative / categorical / ordinal / temporal / spatial
  3. Highlight interesting attributes
  4. Formulate hypotheses and test with a charting library
- **Design with code when the dataset is large** (Nadieh, p. 126): Pixel-perfect design from dummy data breaks when real data has unexpected scale or distribution. Better to sketch rough shapes on paper, then design in code with actual data.
- **Iterate on layout before aesthetics**: Nadieh spent hours on network structure before switching to dark background and glow effects. Structure first, style second. (pp. 122–124)
- **Try the reverse encoding** — swapping hue↔time was done in two lines and quickly revealed it was worse. Rapid encoding reversals are cheap experiments with high diagnostic value. (p. 109)
- **80% of the work is in annotations** — explicitly stated as a lesson from the travel project. (p. 109)
- **Scrollytelling design principle**: Leave a portion of each section static (no animation during that scroll range) so the reader can read the text before the visualization changes. Moving text and visualization simultaneously is overwhelming. (p. 139)

---

## Interaction Design

- **Hover over a day (not individual dots)** — when elements are too small/thin, hovering individual marks causes unbearable flicker. Expanding the hover target to a larger unit (a whole day's arc) solves the problem while still providing detail on demand. (p. 111)
- **Six degrees of separation hover** — in Royal Constellations, hovering a node highlights all nodes reachable within 6 steps, fading out the rest. Shows spreading influence/relatedness across a network. (p. 125)
- **Shortest path on click** — clicking two nodes shows the shortest genealogical path between them with animated transitions (fade out unrelated nodes, highlight path). (p. 127)
- **Fisheye timeline** — horizontal fisheye distortion on hover expands the hovered segment of a dense timeline so the user can see more detail in that region without losing context of the whole. (p. 143)
- **Scroll-linked animation** — animations tied to scroll position (not auto-play): scroll progress mapped to interpolation progress (0.0→1.0), enabling fine user control over the pace of reveal. (p. 139–142)
- **Hover on link in dense network** — for tangled link sets, hovering a host highlights only the corresponding guest appearances, dramatically reducing visual noise. (p. 141)

---

## Common Mistakes and Anti-Patterns

- **Sketching before data exploration** — leads to designs that fail when actual data is plugged in (the "Man Peeing into Puddle" incident). (p. 106)
- **Hairball networks** — when force layout is not given enough space or the parameters are wrong, the network collapses into an unreadable circular clump. Solution: massively increase canvas size first, then tune. (p. 121)
- **Encoding time along a radial radius** — makes early-trip days smaller in circumference than late-trip days, misrepresenting equal time units. (p. 109)
- **Hovering on tiny marks** — triggers flicker when the user accidentally unhovers. Expand the hover target to a logical group. (p. 111)
- **Too many simultaneous animations** — if text and visualization both move during a scroll transition, users don't know where to look and may feel nauseous. (p. 139)
- **"Reciting facts" in text** — the Obama project text received poor reception because it stated data facts rather than telling a story or conveying personal meaning. Contrast with the Hamilton project which made readers feel something. (p. 144)
- **Composing too many variables on one mark** — the filled circle + outer ring + dots-on-ring encoding in the video section was self-described as "overwhelming and confusing." (p. 141)

---

## Practical Rules of Thumb

- When using radial layouts, **map time to angle** (not radius) to keep equal time units at equal arc lengths. (p. 109)
- **Use force simulation** to de-overlap marks that have calculated x/y positions — `d3.forceX()`, `d3.forceY()`, `d3.forceCollide()` — without losing the positional meaning of the axes. (p. 107)
- **Trigonometry for radial layouts**: `x = r * cos(angle)`, `y = r * sin(angle)`. Use `Math.atan2(y, x)` to go the other way. (p. 110)
- For networks: **pre-calculate derived variables** (shortest path, hop count to key nodes) before rendering, then use them as layout forces and visual channels simultaneously. (p. 125)
- **Use opacity as a focus+context channel in dense networks**: visible = important/close, faded = distant/contextual, without removing data. (p. 125)
- **Test the performance of interactions early** — Nadieh expected shortest-path calculation across 3,000 nodes to be slow but it returned instantly. Don't optimize prematurely; test first. (p. 127)
- **Mobile design**: Detect device type and pass different width parameters; use the D3.js drag module instead of native touchmove for smooth scrubbing. (p. 143)
