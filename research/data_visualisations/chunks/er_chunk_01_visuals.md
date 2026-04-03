# [agent_25] Example Student Reports — pages 1-15 + 1-14

All entries below are drawn from real student implementations and sketches. Each is tagged `[from student report]`.

---

### Bubble Grid / Proportional Circle Matrix [from student report] (report_1 p.8–9, p.13)
- **What it shows:** Total revenue AND average order price simultaneously, across a two-dimensional categorical space (area × product type). Each cell in the grid contains one mark. Two variables encoded per mark (size + saturation).
- **When to use:** When you have two quantitative variables to compare across two categorical dimensions simultaneously, and the number of cells is moderate (here 5 × 8 = 40 cells). Avoid when cell count is very high (over ~100) or when values are very similar in magnitude (size differences become imperceptible).
- **Interesting properties:** Can simultaneously reveal which categories dominate on one dimension (revenue) while also flagging anomalies on a second dimension (average price). The combination can surface cases like Jewellery — low revenue but high price per order — that bar charts would not reveal at a glance.
- **Marks:** Points (circles), sized and coloured.
- **Channels:** Size (area of circle) → total revenue; Saturation of blue → average order value (darker = higher price); Position on vertical axis → area/region; Position on horizontal axis → product type.
- **Annotation options:** Tooltip on hover (shows exact revenue and average order value); checkboxes for filtering areas and product types (groups remaining circles for comparison).
- **Data types suited for:** Two quantitative variables (revenue, average price) × two categorical variables (area, product type). Quantitative variables must be ratio-scale for size encoding to be meaningful.
- **Interesting feature extraction/manipulation of data:** Average order value is a computed field (not raw data); revenue is aggregated by area + product type group. Students noted that saturation encoding across 2101 individual products was unworkable — grouping to 8 product types was the key data manipulation that made the encoding viable.

---

### Circular Tile Map / Radial Treemap [from student report] (report_1 p.6–7, p.10–11)
- **What it shows:** Revenue, delivery performance, and concentration of high-value orders across 57 nations grouped into 5 areas, using a circular geographic metaphor (compass directions).
- **When to use:** When geographic hierarchy (area → nation) is important and you want to encode 3 variables per unit simultaneously. Useful when the number of leaf nodes (here 57) is too large for a standard map but too structured for a plain treemap.
- **Interesting properties:** The compass-orientation of sectors gives spatial meaning to the area groupings. Tile size, brightness, and dot size all encode different variables without overplotting because they operate on different visual channels. The design semantically maps "lighter = faster delivery = better" which is intuitive.
- **Marks:** Irregular polygon tiles (nations); dots overlaid on tiles (high-value orders).
- **Channels:** Tile size → total revenue (proportional); Colour hue → area identity (5 areas = 5 hues); Brightness/luminance of tile → proportion of deliveries >20 days (lighter = fewer late = better); Size of green dot → number of high-value orders (>25,000 Copper Pieces); Spatial position within circle → area identity (North/South/East/West/Underdark-center).
- **Annotation options:** Tooltip on hover (revenue, late-delivery proportion, high-value order count); previously examined tiles blur out for tracking; compass labels (North/South/East/West) on outer edge; legend for area colours and dot meaning.
- **Data types suited for:** Hierarchical categorical (area → nation); multiple quantitative overlays. Requires preprocessing to define tile sizes proportional to a quantity.
- **Interesting feature extraction/manipulation of data:** The delivery metric was reformulated during implementation — switched from mean delivery days (insufficient variance across nations) to proportion of orders exceeding 20 days (a threshold selected by analysing the distribution shape, which showed a sharp drop after 20 days). High-value order threshold (25,000 CP) was also determined empirically from the distribution.

---

### Sankey Diagram — Material Flow [from student report] (report_2 p.3, p.5)
- **What it shows:** Flow of raw materials through manufacturing into finished products (EV Car Battery, Home Battery). Thickness of links encodes material quantity. Nodes identify individual materials and finished products.
- **When to use:** When showing flows or transformations between two sets of categories (source → destination). Particularly useful for supply chain, resource allocation, or process flow analysis. Avoid when there are many crossing flows that create visual clutter.
- **Interesting properties:** When 9 materials are shared between two product types, the Sankey makes shared dependencies immediately visible. Icons on the finished-product nodes (car icon for EV battery, house icon for Home Battery) add semantic clarity without extra text.
- **Marks:** Rectangles (nodes for materials and products); flowing bands/links (material flows).
- **Channels:** Width/thickness of links → material quantity; Position (left = raw materials, right = finished products); Colour of nodes → material identity or type.
- **Annotation options:** Node labels with material names; icon overlay on finished-product nodes; thickness legend.
- **Data types suited for:** Flow data between two categorical sets. Best when flows can be quantified (here: material quantity). Works for 10–50 source nodes; degrades with more.
- **Interesting feature extraction/manipulation of data:** Identifying which of 33 materials are shared between the two product types (9 shared) required joining bills of materials across product lines. The Sankey makes shared dependencies a primary visual signal.

---

### Vendor-to-Production Network / Relationship Map [from student report] (report_2 p.3, p.5, p.8–9)
- **What it shows:** Geographic relationships between external vendors and production plants, with link thickness or annotations showing Total Inbound Lead Time.
- **When to use:** When the relationship between two sets of entities (vendors and plants) matters, and geographic position is meaningful. Useful for supply chain logistics analysis. Avoid when the graph is too dense (many vendors × many plants) creating crossing link clutter.
- **Interesting properties:** The spatial distribution of the map itself is a data encoding — vendors far from plants visually suggest longer lead times even before reading annotations. The distinction between external vendors (red circles) and internal plants (green rectangles) using both colour and shape simultaneously provides redundant encoding for accessibility.
- **Marks:** Circles (external vendors); Rectangles (production plants); Splines/curved lines (material flows / lead time relationships).
- **Channels:** Colour hue → entity type (red = external vendor, green = plant); Shape → entity type (circle vs rectangle) — redundant encoding; Spline presence → relationship exists; Lead time annotation on spline → total inbound lead time value; Position → geographic location.
- **Annotation options:** Tooltip on hover (vendor/plant name, location); Material dropdown filter (highlights splines for materials supplied by that vendor); animated spline movement (intended but not implemented due to coding complexity).
- **Data types suited for:** Bipartite network data with geographic coordinates; quantitative edge attributes (lead time).
- **Interesting feature extraction/manipulation of data:** Total Inbound Lead Time = production time + inbound transportation + goods receipt processing — a computed composite metric joining multiple date fields across datasets.

---

### Battery-Shape Distribution Visualization [from student report] (report_2 p.6–7, p.11)
- **What it shows:** Forecast quantities of two product types (EV Car Battery, Home Battery) per distribution center, as a proportion of a user-selected threshold. A semantic/metaphorical mark (battery cylinder) represents distribution centers, with fill level as the key channel.
- **When to use:** When you want an immediately legible "fill level" metaphor for inventory or capacity data and your audience is familiar with the domain (batteries/energy). Particularly effective in dashboards where quick anomaly detection matters. Avoid for precise comparison — the cylindrical 3D perspective distorts proportional judgements.
- **Interesting properties:** The mark is semantically novel — a battery shape is used not to represent a battery as an object, but as a metaphorical vessel whose fill level encodes a percentage of forecast. This creates immediate domain resonance for a supply chain company making batteries. The alarm dot (green/orange/red) at the battery top adds a pre-attentive alert layer above the quantitative encoding.
- **Marks:** Vertical cylinders (batteries), coloured sections within; coloured dot at top (alarm indicator).
- **Channels:** Fill height within cylinder → percentage of forecast quantity; Colour (yellow vs teal) → product type (EV Car Battery vs Home Battery); Position (left to right) → distribution center identity; Alarm dot colour (green/orange/red) → inventory status relative to threshold.
- **Annotation options:** Hover tooltip (material type and quantity); y-axis percentage scale; responsive legend updating based on selected year; year dropdown; threshold dropdown.
- **Data types suited for:** Proportional/percentage quantities across a small number of categories (here: 5 DCs × 2 product types). Works best when the proportional metaphor is semantically meaningful to the audience.
- **Interesting feature extraction/manipulation of data:** Quantities normalized as percentage of forecast quantity for cross-DC comparability. Alarm logic joins forecast data with inventory data across two separate datasets (Forecast and Inventory).

---

### Gauge / Speedometer Visualization for Inventory Performance [from student report] (report_2 p.3, p.7, p.11)
- **What it shows:** Multiple inventory metrics (Gross Inventory Quantity, On-Shelf Inventory Quantity, In-Transit Quantity, Order Quantity) for each DC and product type, displayed as needles on a semi-circular gauge dial.
- **When to use:** When monitoring performance against a benchmark or threshold in a dashboard context. Particularly useful for operational monitoring where users need to scan multiple metrics quickly. Avoid for analytical exploration — gauges convey single values, not distributions or trends.
- **Interesting properties:** Nesting two gauges (outer = EV Car Battery, inner = Home Battery) allows product-type comparison within one visual frame without side-by-side placement. Multiple colour-coded needles on one dial can show 4+ metrics simultaneously, though this risks clutter if needles overlap.
- **Marks:** Arcs (gauge background); Needles (metric values); Colour fills on arcs.
- **Channels:** Needle angle → metric value; Colour of needle/arc → metric identity (different colours for Gross, On-Shelf, In-Transit, Order quantities); Gauge radius (inner vs outer) → product type.
- **Annotation options:** Legend decoding needle/arc colours; dynamic update by year; paired with battery visualization above for context.
- **Data types suited for:** Single quantitative values per metric per unit; particularly suited for operational KPI monitoring. Does not suit distributional or trend data well.
- **Interesting feature extraction/manipulation of data:** Joins Inventory, Forecast, and Sales datasets across distribution centers; compares expected (forecast) vs actual (sales) quantities as the primary analytical question.

---

### EU Map with Overlay Bar Chart Boxes [from student report] (report_2 p.8–9, p.12)
- **What it shows:** Plant-to-distribution-center shipping performance across the European Union, using a geographic map as the base layer with 5 overlay boxes positioned near each DC containing bar charts of shipping metrics.
- **When to use:** When geographic position is meaningful and you want to provide detail-on-demand for specific locations. The layered approach (map + overlay boxes) avoids cluttering the map itself. Avoid when overlay boxes obstruct each other or important geographic features.
- **Interesting properties:** The overlay boxes act as a "small multiples in geographic space" approach — each DC gets its own mini-chart, positioned geographically. The blend of two visual idioms (map + bar chart) is uncommon but effective for this use case. The "blur transition" from world map to EU map on clicking a plant is a novel navigation mechanism.
- **Marks:** Rectangles (plants = green, DCs = yellow); Bars within overlay boxes (shipping time metrics); Splines connecting vendors to plants.
- **Channels:** Colour hue → entity type (green = plant/internal vendor, yellow = DC); Geographic position → real-world location; Bar length → percentage of shipments on time/late; Colour within bars → on-time vs late breakdown.
- **Annotation options:** Hover on rectangles → name and location; Return button → transition back to world map; Bar charts in overlay boxes show percentages (e.g. "36.4% on time/vendor", "16.6%" late rates for specific metrics).
- **Data types suited for:** Geographic point data with associated quantitative metrics; bipartite relationships between two sets of entities (plants and DCs).
- **Interesting feature extraction/manipulation of data:** Late shipment rate computed as proportion of records where Shipping Date > Receipt Date (~15% overall); DC GOT2 identified as having substantially lower data validity (higher data discrepancy %).

---

### Spider / Radar Chart for Regional Comparison [from student report] (report_1 p.5, sketch cluster 2)
- **What it shows:** Multiple metrics (revenue, number of orders, delivery time, customer type proportions) across 4–5 regions simultaneously, using radial axes.
- **When to use:** When comparing multiple quantitative variables across a small number of categories (typically 3–8) where no single variable is primary. Avoid with more than ~6 variables (axes become unreadable) or when precise comparison between non-adjacent axes is needed.
- **Interesting properties:** The sketch (described as merging SMM3 + VVB2 + VVB4 + VVB6 + VVB14/15) aimed to encode revenue, orders, delivery time, private/professional buyer proportion, and customer counts all on one radial chart per region. The students noted this became too complex and needed simplification.
- **Marks:** Lines/polygons connecting axis points; points on each axis.
- **Channels:** Radial distance on each axis → metric value; Axis direction → metric identity; Colour of polygon → region identity; Area of polygon → overall "performance" shape.
- **Annotation options:** Axis labels; legend for regions; note that delivery time axis was inverted (higher axis value = faster delivery = better performance).
- **Data types suited for:** Multiple quantitative metrics (4–8) across a small number of categories. All metrics should be normalized to a common scale.
- **Interesting feature extraction/manipulation of data:** Delivery time was inverted (transformed to 1/delivery_time or similar) so that higher values on the axis always mean better performance — this is a semantically important transformation that the students noted explicitly.

---

### Proportional Circle Map / Cartogram (sketch) [from student report] (report_1 p.6, sketch cluster 3 / SMM1)
- **What it shows:** Revenue and order value by nation, using a pie-like circular layout divided into 5 area sectors, each sector further divided into nation tiles sized by revenue.
- **When to use:** When hierarchical geographic data (area → nation) needs to be shown simultaneously, and you want revenue to drive the visual weight of each unit (not geographic area).
- **Interesting properties:** The SMM1 sketch added a green dot per tile representing number of high-value orders — this "dot on tile" overlay pattern became the final design approach. The tile-within-sector layout is a non-standard hybrid between a treemap and a pie chart.
- **Marks:** Sector slices (areas); tiles within sectors (nations); dots on tiles (high-value orders).
- **Channels:** Tile area → revenue; Colour → area identity; Dot size → count of high-value orders.
- **Annotation options:** Area labels; nation name labels on tiles; dot size legend.
- **Data types suited for:** Hierarchical quantitative data (revenue by area and nation). Requires pre-computation of tile areas.
- **Interesting feature extraction/manipulation of data:** Revenue aggregated by nation; high-value orders filtered by threshold (>50k Copper Pieces in sketch, adjusted to >25,000 CP in final implementation after analysing distribution).
