# [agent_15] examples from class (dutch) — pages 1-3

## Overview

The document is a Dutch-language catalogue of visualization types applied to **energy consumption data**, combining dimensions such as building type, energy type, time, and location. It is organized into seven sections of visualization families, each with named subtypes.

---

## Section 1: Matrix and Heatmap Visualizations (p.1)

- **Matrix (building types × energy types):** Rows = building types, columns = energy types. Dark cells = high consumption; light cells = low consumption.
- Color intensity (saturation/luminance) is the primary channel for encoding magnitude in a 2D matrix.
- Hierarchical clustering can be applied to both rows and columns to reveal patterns — a key data manipulation technique that groups similar buildings or energy types together.
- **Heatmap of days × times:** Time on both axes (days of week vs. hours). Encodes when energy peaks occur (weekdays show higher consumption than weekends in office buildings).
- Rule of thumb: heatmaps are excellent for showing two categorical/ordinal dimensions against a quantitative value — the resulting pattern is immediately scannable.

---

## Section 2: Time and Clock Diagrams (p.1)

- **JA7 — Mirror chart (vertical time axis):** Time runs vertically over a year or day; the chart is mirrored horizontally around zero. Commercial and residential buildings shown on opposite sides. This is a diverging layout encoding comparison across a shared time axis.
  - Channel: position (horizontal distance from center = magnitude); direction (left/right = category).
- **JA6 — 24-hour clock diagram as bar chart:** Each hour gets its own bar radiating from a center. Total energy per building type per hour in a city. Polar bar chart (also called radial bar chart).
  - Advantage: makes cyclical patterns (daily rhythm) visually intuitive.
  - Risk: bar lengths near center are compressed — magnitude comparison less accurate than linear bar charts.
- **Heating vs Cooling per month (monthly clock):** 12-month radial diagram where one side = heating, other side = cooling. Seasonal differences become immediately visible.
  - Marks: bars; Channels: angle (month), length (magnitude), direction (heating vs. cooling = side).

---

## Section 3: Cumulative Consumption Lines (p.1)

- **Total gas consumption over time (cumulative line):** Lines that never decrease — only plateau or rise — because cumulative totals are always non-decreasing.
  - Seasonal spikes are visible as steep rises (e.g., high gas consumption in winter for heating).
  - Key property: the slope of the line encodes the rate of consumption; flat = no consumption, steep = high consumption.
  - Useful manipulation: converting raw time-series to cumulative form reveals total burden over time and highlights seasonal intensity.

---

## Section 4: Pictograms and Symbols (p.1–2)

- **Flames for gas consumption:** Large flames = high gas use; small flames = low gas use. Different applications (cooking vs. heating) shown with differently sized or styled pictograms.
  - Channel: size of symbol encodes magnitude.
  - Risk: size-based magnitude encoding is less accurate than length or position — use for approximate/intuitive communication, not precise comparison.
- **Lightning bolts for electricity:** Size of pictogram encodes electricity consumption level.
  - Same strengths and risks as flame pictograms.
- Rule of thumb: pictograms increase memorability and audience engagement but sacrifice precision. Best for communication to general public, not analysts.

---

## Section 5: Bar and Pie Charts (p.2)

- **Horizontal bar chart (JA1):** Total gas consumption across all building types, split by category. Horizontal layout is preferred when category labels are long.
  - Channel: length (most accurate magnitude channel after position).
- **Pie chart (taartdiagram):** Distribution of energy types and applications within one city.
  - Risk: humans judge angles and arc lengths poorly. Pie charts are appropriate only when showing rough part-to-whole relationships with few slices (2–4). Avoid for comparison across multiple pies.
- **Bubble chart:** Bubble size = total consumption per location; bubble color = building type (hospitals, schools, offices).
  - Channels: size (quantitative magnitude — area), color hue (categorical).
  - Risk: area judgment is less accurate than length. Works well for overview/geographic scatter but not precise comparison.

---

## Section 6: Innovative Visualizations (p.2)

- **"Flower" diagram (Bloemen-diagram):** Each petal = one electricity activity (heating, cooling, cooking, etc.). Petal size is proportional to energy use.
  - Marks: petals (custom shapes); Channel: size/area of petal = magnitude.
  - Semantically novel: the flower metaphor makes the visualization memorable and maps naturally to "components of a whole" without requiring a legend if petals are labeled.
  - Risk: area comparison across petals is imprecise; good for communication, not analysis.
- **Home vs. Office comparison (24-hour chart):** Dual-line or dual-area chart over 24 hours, showing energy peaks at morning (home) and daytime (office).
  - Useful design: overlaying two contexts on the same time axis enables direct comparison of behavioral patterns.
- **Climate stripes (Klimaatstrepen):** Color-coded deviation from average energy consumption. Dark red = high deviation above average; dark blue = low/below average.
  - Marks: rectangles (stripes); Channel: color hue + saturation encodes direction and magnitude of deviation.
  - Derived from the well-known "warming stripes" by Ed Hawkins — a case of a standard chart in a novel semantic role.
  - No axes needed — the color pattern communicates the trend directly.

---

## Section 7: New Conceptual Visualization (JA9) (p.2–3)

- **Matrix-as-network diagram:** Cities and building types as nodes connected by lines in a matrix structure.
  - Node size (circle area) encodes amount of energy consumption.
  - Line color and thickness encode energy type and quantity.
  - Can be extended with stacked bar segments within each node, showing energy type breakdown.
  - This is a hybrid: matrix layout + network/graph visual + proportional symbol + stacked bar — a combined visualization answering questions about multi-dimensional relationships that no single basic chart could.

---

## Cross-Cutting Design Principles (extracted from examples)

- **Dual encoding:** Several examples use both size and color (bubble chart, flower diagram) — effective for encoding two variables simultaneously but risks overload.
- **Cyclic data → radial layout:** When data is inherently cyclical (hours, months), radial/clock layouts align visual structure with data structure.
- **Cumulative transformation:** Converting time-series to cumulative form changes the question from "how much now?" to "how much total so far?" — a deliberate data manipulation choice.
- **Hierarchical clustering on matrices:** Reorganizing rows/columns by similarity reveals structure invisible in the raw order.
- **Semantic novelty:** Climate stripes and flower diagrams use standard encoding (color, size) in novel semantic contexts — increasing engagement without sacrificing accuracy.
- **Magnitude channels ranked (implicit in examples):** Position > Length (bar charts, mirror charts) > Size/Area (bubbles, petals, pictograms) > Color saturation (heatmaps, climate stripes) > Shape (flames vs. lightning).
