# [agent_25] Example Student Reports — pages 1-15 + 1-14

---

## Overview of Both Reports

Both are KU Leuven Data Visualisation course project reports produced by student groups. Report 1 (D.E.A.D dataset — a fictional sales/distribution company) is 15 pages including an appendix of sketches. Report 2 (SunCharge dataset — eco-friendly car/home battery supply chain) is 14 pages including an appendix Miro board overview. Both follow the same template structure: Metadata → Project Description → Visual Design (diverge/emerge/converge) → Implementation → Findings → Individual Contributions → Appendix.

---

## Report Structure — What Sections Appear and How Long They Are

### Report 1 (D.E.A.D)
- **Part 1. Metadata** — 0.5 page: version date, student names (redacted), dataset name
- **Part 2. Project description** — 1.5 pages: dataset description (4 bullet-listed files with row counts and field descriptions), initial data observations, 4 guiding research questions
- **Part 3. Visual design** — 6 pages: diverge (A), emerge (B), converge (C) with 3 clusters; each cluster has photos of hand-drawn sketches embedded inline with descriptive text; final converge sketches shown full-size
- **Part 4. Implementation** — 4 pages: two implementations (A and B), each with subsections "Intended design", "Actual design", "Visual encoding", "Interactions", "Intended vs actual design", code link
- **Part 5. Findings** — 3 pages: initial patterns and anomalies; findings per visualization with inline screenshots of the final implemented visuals
- **Part 6. Individual contributions** — 0.5 page: prose description of who did what
- **Appendix A** — 1 page: single overview image of all sketches clustered by theme

### Report 2 (SunCharge)
- **Part 1. Metadata** — 1 page (sparse, mostly redacted)
- **Part 2. Project description** — 1.5 pages: 3-sentence project overview; bullet-listed feature descriptions (Material, Quantity-related, Date-related, OrderType, Keys); 3 numbered guiding questions
- **Part 3. Visual design** — 3 pages: prose description of diverge/emerge/converge process with named techniques (SCAMPER, Miro, video calls); 7 numbered sketches each with bullet-list encoding description and a paragraph explaining insights; 1 section "Which 2-3 reworked sketches would you want implemented?" with 2 converge designs described
- **Part 4. Implementation** — 5 pages: introduction; tools used; Implementation 1 (Distribution Centers Performance Monitoring Tool) with subsections: Description, Intended Design (sketch references), Actual Design (visual encoding + interactions per sub-component), Data Used, Process, Challenges, Specific Features, Differences, Code Link; Implementation 2 (Plant Shipment Performance) with same structure
- **Part 5. Findings** — 2 pages: findings per implementation with inline screenshots
- **Part 6. Reflections** — 1 page: "most proud of" and "least proud of" paragraphs — UNIQUE TO REPORT 2, not in Report 1
- **Part 7. Individual contributions** — 1 page: bulleted lists per person
- **Appendix** — 1 page: Miro board overview image with colour-coded zones (Converge, Emerge, Diverge-JA, Diverge-SH)

### Key structural observations
- Both use the same top-level part numbering from the assignment template
- Report 2 uses numbered sub-questions within Part 3 (matching an apparent template prompt), while Report 1 uses free-form prose headers (A. Diverge, B. Emerge, C. Converge)
- Figures are embedded inline (not in a figure appendix) throughout both reports; Report 1 shows sketch photos mid-paragraph, Report 2 shows sketches alongside bullet-point descriptions
- Both include a code link for each implementation
- Report 2 adds a reflections section not present in Report 1

---

## How Students Justify Design Choices

### Report 1
- Uses informal but functional encoding language: "size of each circle corresponds to amount of revenue", "saturation of blue color within each circle represents the average order value", "darker shade would signify higher product prices", "lightness of each tile represents the average delivery time" (report_1 p.8–10)
- Uses the words "marks" and "channels" explicitly: "Each circle, serving as marks, represents the revenue and average order price... On the vertical axis, serving as position channel..." (report_1 p.8)
- Justifies design decisions by connecting them to the research questions: e.g., they chose the bubble plot grid because it "allowed us to analyze types of products across different areas... trends in location and product ranges in one plot" (report_1 p.4)
- Explicitly discusses why a design was rejected: "this visualization method became impractical, losing its informativeness" when saturation was applied to 2101 individual products instead of product types (report_1 p.8)
- Discusses the trade-off between complexity and digestibility: "the most informative and visually digestible graphs lay somewhere in the middle, with enough information portrayed so that unique insights could be extracted, but not so much that it resulted in information overload" (report_1 p.3)
- Iterates on metric choice: switched from average delivery time to proportion of deliveries exceeding 20 days after finding "minimal differences observed between nations" in the average metric (report_1 p.10–11)

### Report 2
- Uses formal encoding vocabulary consistently: "Nodes: Rectangles with labels denote raw materials and finished products", "Links: Flowing lines indicate material flow from raw components to finished products, with thickness reflecting material quantity" (report_2 p.3)
- Uses "Visual Encoding" as a section header explicitly, listing encoding choices as numbered bullet points (report_2 p.6–7, 9)
- Justifies colour choices operationally: "green indicates both inventory and forecasted quantities are above the threshold... Orange indicates that one of the forecasted quantities falls below the target... Red alerts that both inventory and forecasted quantities are below the threshold" (report_2 p.7)
- Justifies 3D-to-2D revision: "Note that 3D visualizations may be revised to a 2D format for clarity" (report_2 p.4)
- References specific prior sketches by ID when justifying converge designs: "Converge 2 integrates elements from sketches JA_4, JA_5, SH_6, SH_9, and SH_10" (report_2 p.5)
- Justifies spatial encoding semantically: positions areas (North, South, East, West, Underdark) to mimic a real map orientation — "mimicking the orientation of a traditional map" (report_1 p.10)

---

## How Students Handle Theory

### Report 1
- Does NOT cite Munzner or any named theory/textbook
- Uses theory-adjacent vocabulary ("marks", "channels", "visual encoding", "saturation") without attribution
- Implicitly applies task-encoding alignment: each design choice is justified by the analytical question it answers, not by abstract theory
- References "good design principles" in one sentence without elaboration: "while adhering to good design principles" (report_1 p.3)

### Report 2
- Does NOT cite Munzner or any named theory/textbook either
- Uses the term "visual encoding" as a section header (report_2 p.6, 9)
- Mentions SCAMPER as a named design technique: "we applied techniques such as reworking existing visuals, combining dissimilar ideas, and organizing our exploration using matrix-based approaches... we applied the SCAMPER technique to further develop and enhance our design ideas" (report_2 p.2)
- No explicit Munzner citations in either report — theory is applied implicitly through encoding vocabulary

---

## How Students Structure the Design Process (Diverge → Emerge → Converge)

### Report 1
- Named explicitly: Part 3 sections are labelled "A. Diverge", "B. Emerge", "C. Converge" (report_1 p.2–7)
- Diverge: Each team member created individual sketches independently, then shared them at a group meeting. Wide variety of types and complexity (report_1 p.2)
- Emerge: Used Miro to cluster sketches in two ways — by information content and by format. Three clusters emerged: (1) Revenue by type/subtype, (2) Circular visualizations, (3) Maps (report_1 p.3)
- Converge: Compared visualizations within and across clusters; selected one per cluster; described the full evolution from sketch to final design for each cluster (report_1 p.3–7)
- Sketches are photographed and embedded in the report with IDs (VVB11, SMM2, SMM4, C11, C12, SMM3, VVB4, VVB6, etc.)
- Explicitly states three converge candidates and then explains which two were selected for implementation and why (report_1 p.8)

### Report 2
- Uses diverge/emerge/converge language but describes it more briefly in prose (report_2 p.2)
- Diverge: Independent hand-drawn sketches; mentions Miro, Google Drive, GitHub for sharing
- Emerge: SCAMPER technique applied; video calls for real-time feedback; "matrix-based approaches" used
- Converge: Section 3 question 3 asks "Which 2-3 reworked sketches would you want implemented?" — answered with two named converge designs (report_2 p.5)
- Sketches named with author-based IDs (JA_3, SH_8, JA_1, JA_6, SH_9, JA_4) and shown with both an image and bullet-point encoding description side by side

---

## How Students Present Visualizations

### Both reports use the same structure for each implemented visualization:
1. Intended design (sketch shown + description of what it was meant to do)
2. Actual design (visual encoding described with marks/channels vocabulary; interactions listed)
3. Comparison of intended vs actual (what changed and why)
4. Screenshot of the implemented visualization

### Report 1 — Visualization A (Bubble Grid)
- States the user task first: "We can easily observe which product types are performing exceptionally and which product types are performing poorly in all areas" (report_1 p.8)
- Names marks explicitly: "Each circle, serving as marks"
- Names channels explicitly: "vertical axis, serving as position channel"
- Lists interactive features: hover dropdown, checkboxes for filtering by area and product type (report_1 p.9)

### Report 2 — Each Implementation Section
- Uses numbered bullet points for visual encoding: "1. Battery Shapes: Each distribution center is represented by a vertical cylinder (battery)...", "2. Y-Axis: Indicates the quantity of materials as a percentage", "3. Dynamic Data: Visualization updates based on the selected year..." (report_2 p.6)
- Interactions listed separately as numbered sub-bullets (report_2 p.7)
- Sections on "Data Used for the Visualization", "Process Followed to Create the Visualization", "Challenges Faced and Overcome", "Specific Features or Techniques Used" are unique to Report 2 and add significant depth

---

## Persona / User Framing

### Report 1
- No formal persona or user profile defined; the client (D.E.A.D company) serves as an implicit user
- Phrases like "the company should consider reallocating resources", "our most valuable orders", "can give an idea of money streams in the company" frame the user as a business analyst/manager
- User tasks are described in terms of business questions: "which product categories are excelling and which could be omitted?" (report_1 p.2)

### Report 2
- No formal persona defined either; uses "SunCharge" as the implicit user organization
- Frames tasks in supply chain operational terms: "quickly identify bottlenecks", "enhance inventory management practices", "optimize logistics operations" (report_2 p.8, 10)
- The alert system (green/orange/red) implies a monitoring user who needs to act on anomalies at a glance

---

## Quality Signals — What Distinguishes Strong Sections

- **Strong**: Report 1's cluster descriptions give full evolutionary narrative (sketch → intermediate → final), show rejected options with reasons, embed photos of intermediate sketches. This demonstrates genuine iteration, not post-hoc description.
- **Strong**: Report 2's visual encoding sections are highly structured (numbered lists, separate interaction sub-sections, challenges sub-section). This makes encoding decisions auditable.
- **Strong**: Both reports explicitly connect visualizations to their originating research questions, creating coherent question → design → finding loops.
- **Strong**: Report 1 describes metric reformulation as an iteration step (switching from average delivery time to proportion >20 days) — shows analytical thinking, not just visual thinking.
- **Strong**: Report 2 names specific sketch IDs in the converge section, making the lineage of each design decision traceable.

---

## Common Pitfalls Visible in These Reports

- **No theory citations**: Neither report cites Munzner or any visualization textbook, even when using encoding vocabulary. This is a weakness — using "marks and channels" without attribution is less convincing than tying it to the theoretical framework.
- **Loose findings sections**: Report 1's findings read somewhat like a bullet-point data summary rather than visualization-derived insight. The link back to specific visual features is sometimes absent.
- **Report 2 findings section is thin** (2 pages for 2 implementations): findings are descriptive of what the tool shows, not always analytical insights discovered through the tool.
- **Report 2's reflections section** mentions advanced features not implemented (moving splines, animated transitions) — acknowledging gaps is good, but the gap between intended and actual is large.
- **Neither report includes a formal limitations or future work section** beyond the "intended vs actual" comparison.
- **"Intended vs actual design" comparisons in Report 1 are sometimes too positive**: "This implementation serves as a comprehensive realization of the initial idea" (report_1 p.9) — no critical reflection.
- **No accessibility consideration** mentioned in either report (colour-blindness, contrast ratios, etc.).
- **Report 1 does not define personas**, which means design choices have no explicit user grounding beyond the client's business questions.

---

## What the Combined / Final Visualizations Actually Look Like

### Report 1 — Visualization A: "Revenue and average order value by types and areas" (Bubble Grid)
- A 2D grid with areas (North, South, East, West, Underdark) on the vertical axis and 8 product types (Adventuring equipment, Arms & Armour, Animals and transportation, Jewelry, Musical instruments, Potions & Scrolls, Summoning device, Tools & Kits) on the horizontal axis
- Each cell contains a circle (the mark); circle size encodes total revenue for that area × product type combination; saturation of blue encodes average order value (darker = more expensive)
- Interactive: hovering a circle shows a tooltip with exact revenue and average order value; checkboxes on the right let users filter by area and product type, grouping the remaining circles for cleaner comparison
- Implemented in Svelte; two screenshots shown — one with all data, one filtered (report_1 p.9, p.13)
- Key finding visible in the viz: North and South yield highest revenue; Adventuring Equipment and Arms & Armour are dominant product types; some low-revenue types like Tools & Kits show low values across all areas

### Report 1 — Visualization B: "D.E.A.D's Revenue Across The World" (Treemap-circle hybrid / Tile Map)
- A circular layout divided into 5 coloured sectors representing the 5 areas (North, South, East, West, Underdark in center), mimicking compass directions
- Within each sector, tiles (irregular polygons) represent nations; there are 57 nation-tiles total
- Tile size encodes revenue (proportional); tile colour encodes area identity (matching the sector colour); brightness of tile encodes proportion of late deliveries (>20 days) — lighter = fewer late deliveries (better performance); darker = more late deliveries
- Green dots overlaid on tiles encode number of high-value orders (>25,000 Copper Pieces) — larger dot = more such orders
- Interactive: hovering a tile shows name, total revenue, proportion of late orders, number of high-value orders; previously examined tiles blur/dim to aid tracking
- Implemented in 3D (not specified which framework beyond "3D"); Underdark positioned at center, cardinal areas surrounding
- Key design adjustment: average delivery time replaced by proportion of orders >20 days after the average showed insufficient variation (report_1 p.10–11)

### Report 2 — Implementation 1: "Distribution Centers Performance Monitoring Tool"
- Two-component visualization shown side by side for each of 5 Distribution Centers (Antwerp, Wroclaw, Lyon, Birmingham, Goteborg)
- **Top component (Battery Distribution Visualization)**: Each DC is a vertical cylinder drawn as a battery; cylinder is divided into coloured sections — yellow for EV Car Battery forecast quantity, teal for Home Battery forecast quantity; height of each section encodes the percentage of forecast quantity; an alarm dot at the top of each battery is green (both above threshold), orange (one below), or red (both below threshold)
- **Bottom component (Gauge Visualization)**: Below each battery is a semi-circular gauge dial for each material type, with multiple colour-coded needles and arcs representing Gross Inventory Quantity, On-Shelf Inventory Quantity, In-Transit Quantity, and Order Quantity; outer gauge = EV Car Battery, inner gauge = Home Battery
- Both components update dynamically based on a year dropdown and a threshold dropdown at the bottom
- Legend on the right decodes all colours and metrics
- Implemented in Svelte + D3.js (report_2 p.6–7, p.11)

### Report 2 — Implementation 2: "Plant Shipment Performance to Distribution Centers"
- Two-map visualization with a transition between them
- **World Map**: Shows external vendors as red circles and production plants as green rectangles plotted on a world map; splines connect vendors to plants, encoding Total Inbound Lead Time; hovering a red circle resizes it and shows vendor name/location; hovering a green rectangle shows plant name/location; a material dropdown filters which splines are highlighted; clicking a plant transitions to the EU map
- **EU Map**: Shows plants/internal vendors as green rectangles and 5 distribution centers as yellow rectangles; 5 overlay boxes appear on the map, one per DC, containing bar charts with shipping time metrics (Vendor Shipment, Yard Arrival, Receipt Date, Data Discrepancy percentages, on-time vs late breakdown); a Return button goes back to the world map
- Implemented in Svelte + D3.js; transition uses blur/darkening effect on the world map (report_2 p.8–9, p.12)
