# [agent_05] Cool Infographics — pages 201-249

## Overview

Pages 201–249 are primarily about design principles and design tools rather than a gallery of visualization types. However, a number of specific chart types are shown or described in examples. Extracted below.

---

### Stacked Bar Chart (p.201)
- **What it shows:** Part-to-whole proportions for multiple categories simultaneously; here used to show survey percentage responses (Apples 70%, Oranges 63%, Grapes 60%).
- **When to use:** Comparing part-to-whole across multiple categories. Avoid when there are too many stacked segments (hard to compare middle segments).
- **Interesting properties:** Color-coded categories with percentage labels embedded in the colored portion. The "remaining" portion shown in grey, giving immediate visual sense of how much of 100% is filled.
- **Marks:** Rectangles (bars), vertically stacked.
- **Channels:** Height (proportional to percentage value), color hue (category identity — red/orange/purple matched to category label), position (vertical, on shared baseline).
- **Annotation options:** Percentage values embedded inside colored bars; category names below each bar in matching color.
- **Data types suited for:** Quantitative (ratios/proportions), categorical.
- **Interesting manipulation:** Using grey remainder to show "how much headroom remains" is a clean way to contextualize percentages without showing a full 100% stacked bar.

---

### Sized Circle / Bubble Chart (p.203–205)
- **What it shows:** Quantitative magnitudes compared through circle area (e.g., Marketing budget $1M vs. Sales budget $3M).
- **When to use:** Comparing magnitudes where bar chart would be too wide or where spatial layout matters. Avoid when exact comparison is critical (area is less precise than length).
- **Interesting properties:** The book demonstrates correct vs. incorrect sizing extensively. The critical distinction: circles must be sized by **area** (π × r²), not diameter. Incorrect diameter-based sizing makes a 3× difference appear as ~9× visually.
- **Marks:** Filled circles.
- **Channels:** Area (quantitative magnitude — must be computed correctly); color hue (categorical distinction — blue for Marketing, red for Sales); text label inside circle (direct annotation).
- **Annotation options:** Value labels inside circle, area calculation shown below, diameter measurement arrow above.
- **Data types suited for:** Quantitative magnitudes, categorical groupings.
- **Interesting feature extraction/manipulation:** Requires pre-calculation of radius from area before entering into design software. Spreadsheet template approach: enter value → compute area ratio → compute radius → compute diameter → enter diameter only in software.

---

### Annotated Vertical Scale / Graduated Scale Chart ("The Caffeine Poster") (p.210)
- **What it shows:** Ranking of items (drinks) along a continuous quantitative scale (milligrams of caffeine), with item icons placed at their value position on both sides of the scale.
- **When to use:** When you want to show where many items fall on a single dimension, especially with strong visual icons for each item. Good for comparing items to thresholds. Avoid when items cluster too tightly to be legible.
- **Interesting properties:** Central vertical scale bar with color gradient (red at top = danger/high, green at bottom = low/safe). Items (coffee cups with logos, energy drink cans with product photos) placed at their exact scale position on left and right. Threshold annotation ("Caffeine Intoxication occurs at 300mg") placed at the relevant scale level. Only one variable shown — all other potential data (brand ownership, geographic location, annual sales, drink sizes variation) deliberately excluded to maintain focus.
- **Marks:** Vertical graduated bar (the scale), product icon images at scale positions, horizontal arrows pointing from icon to scale.
- **Channels:** Position along vertical axis (caffeine content in mg), color saturation of scale bar (danger level), side of axis (coffee left / energy drinks right as categorical grouping), icon identity (brand recognition).
- **Annotation options:** Threshold labels at specific scale values, fact boxes at key positions ("September 29 is National Coffee Day"), chemical structure in corner.
- **Data types suited for:** Quantitative (single continuous dimension), categorical (drink type / brand).
- **Interesting manipulation:** Data reduced to single dimension only — a deliberate simplification that makes the one key comparison (which drink has most caffeine) immediately clear. The split left/right by drink type adds one categorical dimension without adding visual complexity.

---

### Ranked Pie / Fan Chart with Extended Legend Lines ("Where's Google Making Its Money?") (p.208–209)
- **What it shows:** Ranking and proportion of the top 20 most expensive Google AdWords keyword categories, with percentage of keywords in the top 10,000 per category.
- **When to use:** When both rank and proportion matter and there are many categories. Avoid for simple part-to-whole comparisons (a standard pie chart would be clearer).
- **Interesting properties:** Pie chart where slices are numbered (#1 through #20) and ordered by rank; top slices are large with label embedded directly; smaller slices are too thin for labels so extended leader lines connect them to a ranked list below the chart. The pie acts as a visual anchor while the full detail appears in the list. The key message (97% of Google's revenue = advertising) is shown as a large number in the corner, separate from the pie.
- **Marks:** Pie slices (wedges), extended leader lines, ranked list below, large number callout.
- **Channels:** Arc angle (percentage of keywords in category), color hue (category identity), rank number embedded in large slices, line extensions from small slices to text list.
- **Annotation options:** Rank numbers inside large slices; price-per-click annotations on large slices; leader lines to ranked list for small slices.
- **Data types suited for:** Categorical (keyword category), quantitative (percentage share, cost-per-click), ordinal (ranking).
- **Interesting manipulation:** The combination of pie + ranked list solves the small-slices legibility problem. The large "97%" callout is the key message, deliberately separated from the pie's detail data.

---

### Character Relationship / Flow Diagram (Star Wars Infographic) (p.213)
- **What it shows:** Character interactions and narrative flow through a movie, with color-coded paths for each character's journey and circular "scene hubs" grouping characters who share a scene.
- **When to use:** Showing narrative or process flow with multiple agents. When minimizing text is a goal. Avoid for data requiring precise quantitative comparison.
- **Interesting properties:** Each character has a color-coded path line. Scene locations are shown as large circles with the character icons inside. Lines connect characters through scenes in temporal sequence. No data values — purely relational and sequential. Very low text density encourages readers to trace paths themselves and engage longer.
- **Marks:** Path lines (one per character), circles (scene locations), human-shaped icons (characters), labeled event boxes (key plot points like "RESCUE", "BATTLE OF YAVIN").
- **Channels:** Color hue (character identity), path curvature and routing (narrative sequence), circle size (scene importance/number of characters), icon shape (character identity), position (rough temporal sequence left-to-right, location top-to-bottom).
- **Annotation options:** Scene name labels on circles, event labels on path intersections, character names below icons.
- **Data types suited for:** Relational (who interacts with whom), sequential/temporal (narrative order), categorical (characters, locations).
- **Interesting manipulation:** All quantitative and descriptive data eliminated; only the relational/sequential structure is preserved. This forces visual engagement rather than reading.

---

### Bar Chart with Inline Icons (Replacing Legend) (p.215)
- **What it shows:** U.S. population by generational cohort (Gen Z, Gen Y/Millennials, Gen X, Baby Boomers, Silent Generation) in thousands.
- **When to use:** Any grouped bar chart where you want to eliminate the legend entirely. Particularly effective when the categories have strong visual metaphors.
- **Interesting properties:** The chart legend is replaced entirely by: (1) category names as x-axis labels, and (2) generation-representative icon clusters placed at the base of each bar inside the bar area. The icons (baby with stroller, parent with child, working adult, older adult, elderly couple) immediately convey the generational meaning without any separate key.
- **Marks:** Vertical bars, human figure icons at bar base.
- **Channels:** Bar height (population count), color hue (generational category), icon shape (generational archetype), position on common baseline (comparison across categories).
- **Annotation options:** Icons directly embedded in bars, x-axis category names, y-axis scale.
- **Data types suited for:** Quantitative (population count), categorical (generational group).
- **Interesting manipulation:** Embedding icons into bars completely removes the legend-to-chart eye movement. All relevant information is in the reader's field of view simultaneously.

---

### Doughnut Chart / Gauge Combination (p.212)
- **What it shows:** A percentage (48% of parents use phone to monitor child's location) shown as a doughnut chart arc, placed next to a text-only version of a companion statistic (64%) — demonstrating the contrast between visualized and unvisualized data.
- **When to use:** When a single percentage needs to be shown in context of the whole 100%, with a clear "filled vs. remaining" distinction.
- **Marks:** Arc (doughnut/ring), center icon.
- **Channels:** Arc length (percentage value), color hue (filled vs. unfilled portion), center icon (conceptual anchor for what the percentage refers to — phone/location icon).
- **Annotation options:** Percentage value as large text alongside arc, descriptive text below.
- **Data types suited for:** Quantitative (single proportion/percentage).

---

### Gauge / Dial Chart (p.234)
- **What it shows:** A single quantitative value shown as a needle position on a circular dial (e.g., Memory: 80.5, CPU: 55.6, Network: 68 — from Chartle.net example).
- **When to use:** Status monitoring; showing current value against a known min-max range. Avoid for precise value comparison between multiple items (hard to read exact values).
- **Marks:** Circular dial face, needle/pointer.
- **Channels:** Needle angle (quantitative value on scale), color zones on dial face (green/yellow/red for good/warning/danger ranges).
- **Annotation options:** Numeric value below dial, label above dial (e.g., "Memory"), min/max values at dial ends.
- **Data types suited for:** Quantitative (single value against a range).

---

### Choropleth World Map (p.235)
- **What it shows:** Global Peace Index 2012 — country-level quantitative ranking encoded as color fill of country shapes.
- **When to use:** When geographic distribution of a quantitative or ordinal variable matters. Avoid when country size biases the visual (large countries dominate visually regardless of value).
- **Marks:** Country polygon fills.
- **Channels:** Color saturation/hue (ordered peace index level: very high = dark green through very low = dark red), geographic position (country location is implicit meaning).
- **Annotation options:** Color legend with five levels, source citation, note about year-to-year changes.
- **Data types suited for:** Quantitative or ordinal (country-level scores), spatial (geographic distribution).
- **Interesting manipulation:** Grouping the continuous index into 5 discrete bands (very high, high, medium, low, very low) simplifies interpretation at the cost of within-band precision.

---

### Word Cloud (p.233)
- **What it shows:** Frequency distribution of words in a text corpus (e.g., Facebook Privacy Policy — showing that "information", "Facebook", "public", "friends" are most frequent).
- **When to use:** Qualitative text data where overall themes and relative frequencies matter more than exact counts. Avoid when precise frequency comparison is needed.
- **Marks:** Word text strings at varying sizes and positions.
- **Channels:** Font size (word frequency), color hue (optional categorical grouping or aesthetic), position (no meaning — determined by layout algorithm).
- **Annotation options:** None standard (the words are self-annotating).
- **Data types suited for:** Categorical (word types), quantitative (frequency).
- **Interesting manipulation:** Phrase-level analysis (rather than individual words) can separate positive from negative sentiment — "love" vs. "don't love" are counted separately when phrases are used.

---

### Periodic Table of Visualization Methods (p.232)
- **What it shows:** A taxonomy of ~100 visualization method types organized into a periodic-table layout, grouped by category: Data Visualization, Information Visualization, Concept Visualization, Strategy Visualization, Metaphor Visualization, Compound Visualization.
- **When to use:** As a reference/ideation tool, not for showing data. Useful for designers choosing among visualization types.
- **Interesting properties:** Each "element" has an abbreviation code and full name. Hovering (online version) shows a visual example. The periodic table metaphor itself organizes types spatially by category groupings.
- **Marks:** Rectangular "element" tiles in a periodic-table grid layout.
- **Channels:** Color hue (visualization category type), position in grid (grouping by category), text label (visualization name and abbreviation).
- **Data types suited for:** Categorical (visualization method types), used as a navigation/reference tool.
