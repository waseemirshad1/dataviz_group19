# [agent_25] Example Student Reports — pages 1-15 + 1-14

---

### Idea: Bubble Grid — Two Quantitative Variables on a Categorical Matrix (from report_1 p.4, p.8–9, p.13)
- **Basic visuals combined:** Scatter plot / position grid + proportional circle (bubble) + colour saturation encoding
- **What the combination adds:** A standard bubble chart encodes one quantitative variable (size) per mark. This design encodes TWO quantitative variables per mark (size = revenue, saturation = average price) placed at grid positions defined by two categorical axes (area × product type). This is impossible with a bar chart or simple scatter plot alone. It surfaces "anomalous" cells — e.g., high price but low revenue (Jewellery) — that would require multiple separate charts to find otherwise.
- **Data manipulation applied:** Revenue aggregated by (area × product type); average order price computed as mean CartPrice per (area × product type) group. Key insight: granularity had to be reduced from individual products to product types to make saturation encoding readable.
- **Marks:** Circles (one per cell in the grid)
- **Channels:** Size (circle area) → total revenue; Saturation of blue → average order value; Vertical position → area (5 regions); Horizontal position → product type (8 types)
- **User task supported:** Compare performance across two categorical dimensions simultaneously; identify outliers in both revenue and pricing; filter to subsets of interest
- **What it shows:** Which product types perform best in which regions; whether high-revenue product types also command high average prices; which combinations are underperforming
- **Persona it could serve (in our dataset):** Sofia (researcher comparing performance across sites and species groups) or Elena (site manager wanting to know which plant groups correlate with yield)
- **Interaction if present:** Hover tooltip (exact values); checkboxes to filter by region and product type; filtered circles group together for cleaner comparison
- **Page reference:** report_1 p.4, p.8–9, p.13

---

### Idea: Circular Tile Map — Proportional Tiles in Geographic Sectors with Overlaid Dot Channel (from report_1 p.6–7, p.10–11)
- **Basic visuals combined:** Treemap (proportional area tiles) + pie chart sectors (geographic area identity) + dot overlay (high-value order concentration) + luminance encoding (delivery performance)
- **What the combination adds:** A standard treemap shows hierarchy and proportion but loses geographic orientation. This design restores geographic meaning by arranging tiles in compass-oriented sectors (North/South/East/West/Underdark-center). Adding brightness as a third channel (delivery efficiency) and dot size as a fourth channel (high-value orders) allows three analytical questions to be answered from a single static view, with interaction adding precision.
- **Data manipulation applied:** Revenue aggregated by nation (57 units); delivery metric reformulated from mean days to proportion of orders >20 days (threshold selected from distribution analysis — bimodal shape with sharp drop after 20 days); high-value order threshold set at 25,000 Copper Pieces (empirically from distribution); tile areas computed proportional to revenue.
- **Marks:** Irregular polygon tiles (nations); green dots overlaid on tiles (high-value order hubs)
- **Channels:** Tile area → revenue; Colour hue → area identity (5 colours for 5 areas); Luminance/brightness → delivery performance (lighter = fewer late deliveries = better); Dot size → concentration of high-value orders; Spatial sector position → area geographic identity
- **User task supported:** Identify which nations generate most revenue; identify delivery problem areas; find high-value order hubs; explore whether revenue and delivery performance correlate
- **What it shows:** Revenue distribution across 57 nations; delivery inefficiency hotspots; concentration of high-value orders; whether high-revenue nations also have efficient delivery
- **Persona it could serve (in our dataset):** Elena (site-level performance monitoring across many sites — coffee sites could be nations, regions could be areas); Sofia (identifying which site clusters drive the most yield/performance while also flagging problem sites)
- **Interaction if present:** Hover reveals exact revenue, late-delivery proportion, high-value order count; previously viewed tiles blur to aid tracking
- **Page reference:** report_1 p.6–7, p.10–11

---

### Idea: Semantically-Shaped Distribution Mark — Battery-as-Vessel Metaphor (from report_2 p.3–4, p.6–7, p.11)
- **Basic visuals combined:** Stacked bar chart (proportional fill) + metaphorical domain object (battery cylinder) + pre-attentive alarm indicator (coloured dot)
- **What the combination adds:** A standard stacked bar shows proportional composition but has no intrinsic domain meaning. Using the battery cylinder as the mark creates immediate semantic resonance for a battery company — the fill level is analogous to charge level. The alarm dot (green/orange/red traffic-light coding) adds a pre-attentive overview layer so users can scan 5 distribution centers instantly before reading detailed values. This is a standard chart type (proportional bar) used in a semantically novel role.
- **Data manipulation applied:** Raw inventory/forecast quantities normalized as percentage of a user-selected threshold; alarm logic derived by joining Forecast and Inventory datasets and comparing both product types to threshold simultaneously.
- **Marks:** Vertical cylinders (battery shapes), divided into coloured fill sections; small circle (alarm dot) at top of each cylinder
- **Channels:** Fill height → percentage of forecast quantity; Colour (yellow vs teal) within cylinder → product type; Alarm dot colour (green/orange/red) → inventory status (both above / one below / both below threshold); Horizontal position → distribution center identity
- **User task supported:** Monitor inventory levels across multiple distribution centers at a glance; identify which DCs are below threshold; drill down for exact quantities; track changes over time via year filter
- **What it shows:** Relative forecast quantities per product type per DC; which DCs are at risk of stockout; how inventory changes year by year
- **Persona it could serve (in our dataset):** Hana (farm manager monitoring site-level inputs/outputs — the battery could become a "site performance vessel" showing yield vs. expected target per site); Elena (multi-site operational monitor)
- **Interaction if present:** Hover tooltip (material type and quantity); year dropdown (historical + forecast data); threshold dropdown (custom alert levels); sections below threshold flash to draw attention
- **Page reference:** report_2 p.3–4, p.6–7, p.11

---

### Idea: Gauge (Speedometer) as Multi-Metric KPI Dashboard per Entity (from report_2 p.3, p.7, p.11)
- **Basic visuals combined:** Semi-circular gauge dial + multiple needle encoding (4 metrics per gauge) + nested dual gauges (outer = one product type, inner = another)
- **What the combination adds:** A single gauge conveys one value; nesting two gauges per DC and placing 4 colour-coded needles on each gauge allows 8 metrics to be read per DC without requiring a table or multiple charts. The angular position of needles is rapidly scannable for anomalies. The paired display with the battery visualization (above) allows cross-validation of forecast vs. inventory vs. actual sales in one dashboard view.
- **Data manipulation applied:** Joins across Inventory, Forecast, and Sales datasets; computes comparable quantities for Gross, On-Shelf, In-Transit, and Order metrics from different source tables.
- **Marks:** Arcs (gauge backgrounds); needles (metric values); colour fills
- **Channels:** Needle angle → metric value; Colour of needle → metric identity (4 distinct colours); Gauge radius (outer vs inner arc) → product type; Position (left-to-right) → distribution center
- **User task supported:** Compare multiple inventory metrics across distribution centers; identify discrepancies between expected and actual; monitor KPI performance year-over-year
- **What it shows:** Whether Gross, On-Shelf, In-Transit, and Order quantities are balanced; whether inventory can meet forecasted sales demand; which DCs show discrepancies
- **Persona it could serve (in our dataset):** Hana (monitoring multiple site-level metrics simultaneously — yield, biodiversity index, density could each be a needle); Sofia (comparing ecological performance metrics across sites)
- **Interaction if present:** Year dropdown updates all gauges; legend decodes needle colours; paired with battery visualization for cross-validation
- **Page reference:** report_2 p.3, p.7, p.11

---

### Idea: Drilldown Map Transition — World Map to Regional Detail Map with Overlay Charts (from report_2 p.8–9, p.12)
- **Basic visuals combined:** Geographic network map (world scale) + geographic map (EU regional scale) + overlay bar chart boxes per location + blur transition between scales
- **What the combination adds:** A single map cannot show both global context (vendor locations worldwide) and local detail (DC-level shipping performance in Europe) without severe overplotting. The drilldown transition — click a production plant on the world map, EU map appears with the world map blurred behind — allows users to navigate between two levels of geographic detail without losing spatial context. The 5 overlay boxes with bar charts at each DC position combine geographic encoding with quantitative comparison.
- **Data manipulation applied:** Total Inbound Lead Time computed as production time + transportation + goods receipt processing; late shipment rate = proportion of records where Shipping Date > Receipt Date; data discrepancy rate computed per DC.
- **Marks:** Circles (external vendors); rectangles (plants/DCs); splines (vendor-plant relationships); bar segments within overlay boxes (shipping metrics)
- **Channels:** Mark colour (red = external vendor, green = plant, yellow = DC); Spline presence → relationship exists; Bar length → percentage on-time or late; Geographic position → real location; Overlay box position → DC location on EU map
- **User task supported:** Identify which external vendors cause longest lead times; navigate from global supply chain view to European DC performance view; compare shipping reliability across DCs
- **What it shows:** Global vendor-to-plant material flow and lead times; European plant-to-DC shipping performance; data quality issues per DC
- **Persona it could serve (in our dataset):** Sofia (navigating from a global overview of site characteristics to regional detail — e.g., from world coffee-belt map to individual site performance); Elena (comparing performance metrics across sites in a geographic context)
- **Interaction if present:** Hover on vendor/plant circles (name, location, resize); material dropdown filter (highlights relevant splines); click plant → blur transition to EU map; hover on DC overlay boxes; Return button back to world map
- **Page reference:** report_2 p.8–9, p.12

---

### Idea: Converge 2 — Multi-Level Supply Chain Overview Combining Battery Marks + Histograms + Time-Series Lines (from report_2 p.5)
- **Basic visuals combined:** Metaphorical domain marks (battery shapes for production plants) + linked arrows (plant-to-DC relationships) + histograms (sales order distribution over time) + translucent circle plots (individual sales orders by size) + line charts (inventory and forecast trends)
- **What the combination adds:** No single chart type can simultaneously show the organizational hierarchy (plants → DCs), the time-series behaviour of inventory and sales, and the distribution of individual order sizes. This converge sketch stacks all three within a spatial layout that preserves the plant → DC hierarchy as the primary organizing structure, with detail plots appearing below each DC.
- **Data manipulation applied:** Sales aggregated by month per DC per product type; inventory levels aggregated over time; sales orders sized by quantity for circle marks.
- **Marks:** Battery cylinders (production plants, top); downward arrows (plant-to-DC links); histogram bars (sales distribution); translucent circles (individual orders); lines (inventory and forecast trends)
- **Channels:** Battery fill → total purchase order quantity per product; Arrow direction → production-to-distribution flow; Histogram colour (solid maroon vs coral) → product type (EV Battery vs Home Battery); Circle size → sales order quantity; Line colour (blue = gross inventory, neon green = forecasted sales) → metric type; Time on x-axis → temporal ordering
- **User task supported:** Identify seasonal patterns; compare DC performance; understand stock levels relative to demand; see which production plants serve which DCs
- **What it shows:** End-to-end supply chain view from production to distribution; seasonal demand patterns; inventory vs forecast alignment; geographic impact on sales
- **Persona it could serve (in our dataset):** Hana (overall farm system view combining site structure, production output, and seasonal patterns — coffee yield by season across sites with species context below)
- **Interaction if present:** Year filter; hover for detail; DC-level plots linked to production plant above
- **Page reference:** report_2 p.5
