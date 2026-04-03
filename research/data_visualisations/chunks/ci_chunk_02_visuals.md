# [agent_02] Cool Infographics — pages 51-100

---

### Animated Infographic — Cheetah (p.51)
- **What it shows:** Physical anatomy and performance statistics of the cheetah (speed, stride, paw structure, organs) integrated into a running-motion animation
- **When to use / avoid:** Use when the subject matter involves motion or temporal sequence that benefits from showing rather than describing. Avoid if the animation distracts from reading the data.
- **Interesting properties:** Entire animation is contained in a GIF file, so it functions when embedded on any site or blog without code — key sharing advantage. Static sections of the infographic contain data (bar charts for speed comparisons, annotated body diagram) while the animation shows the cheetah running.
- **Marks:** Annotated illustration (the cheetah body as glyph), horizontal bars (speed comparison), line with tick marks (stride measurements)
- **Channels:** Position along horizontal bar (speed/mph), labeled callouts (anatomy labels), color (differentiated sections: speed, tail, stride, paws, organs)
- **Annotation options:** Inline labels with arrows pointing to anatomical features; numeric values alongside bars
- **Data types suited for:** Quantitative (speed, dimensions), categorical (body parts), comparative (cheetah vs. Porsche vs. greyhound vs. race horse)
- **Interesting feature extraction/manipulation:** Speed comparison is normalized against a common reference (0–80 mph scale) for direct comparison between cheetah, car, and other animals

---

### Scale Scrolling Infographic — "How Far is it to Mars?" (p.52–53)
- **What it shows:** True proportional scale distance between Earth and Mars, using Earth = 100 pixels as the unit
- **When to use / avoid:** Use when the core insight IS the scale itself — when numbers alone fail to convey magnitude. Requires web/interactive medium; does not work in print.
- **Interesting properties:** Clicking a down-arrow begins the animation; user scrolls through vast empty star field before Mars appears. The visual effort of scrolling IS the data — the distance becomes experiential, not just numerical.
- **Marks:** Circles (planets), dotted orbit rings, star field background
- **Channels:** Position on scroll axis (distance), size of circle (planet diameter), color (planet identity)
- **Annotation options:** Orbit labels (Low Earth Orbit, GPS Satellite Orbit) positioned at their correct relative distances
- **Data types suited for:** Quantitative (distance, scale), spatial
- **Interesting feature extraction/manipulation:** Normalization of Earth diameter to 100 pixels as a human-readable reference unit; all other distances then derived from this anchor

---

### Pictogram Bar Chart — Royksopp "Remind Me" video (p.54–55)
- **What it shows:** Commuter transport mode share (Train 35%, Bus 30%, Car 26%, By foot 7%) where each bar is composed of repeated icons of the transport mode
- **When to use / avoid:** Use when you want the mark to carry semantic meaning (the image IS the category). Avoid for fine-grained quantitative comparison — icon counting is imprecise.
- **Interesting properties:** Each bar consists of repeated images of the vehicle type (train icons stacked to form the train bar, bus icons for bus bar). Width/length encodes the percentage. Visually intuitive for a general audience.
- **Marks:** Repeated icon glyphs (train, bus, car, person) arranged as bars
- **Channels:** Bar length (quantity/percentage), icon identity (category)
- **Annotation options:** Percentage labels at end of bars; category name at left
- **Data types suited for:** Categorical (transport modes), quantitative (percentages)
- **Interesting feature extraction/manipulation:** None — simple proportional display

---

### Isometric Crowd Segmentation — Royksopp "Remind Me" video (p.54–55)
- **What it shows:** Pedestrian crowds color-coded by employment status (Employee type 1 = red, Worker = blue, Unemployed = yellow) flowing through a street scene
- **When to use / avoid:** Use when showing composition of a crowd or population in a spatially intuitive way. Works best for 3 categories or fewer.
- **Interesting properties:** People icons are placed in an isometric 3D street scene, not a flat chart; color distinguishes the three groups. The "chart" reads as a scene — semantically richer than a pie chart.
- **Marks:** Human figure glyphs (isometric), colored by group
- **Channels:** Color hue (employment category), spatial position (implicitly showing proportion by density)
- **Annotation options:** Color legend in top-left corner
- **Data types suited for:** Categorical (employment type), compositional
- **Interesting feature extraction/manipulation:** Embedding categorical breakdown into a narrative scene rather than an abstract chart

---

### Interactive Choropleth Map — NYT 2012 Election (p.58)
- **What it shows:** U.S. presidential election results by county, colored red/blue by winning candidate; updated in real time
- **When to use / avoid:** Use for spatial data where geographic distribution is itself the insight. Avoid when precise value comparison is needed (color saturation is imprecise).
- **Interesting properties:** Updated live as results came in. Filter controls (States / Counties / Size of lead / Shift from 2008) changed the view. Zoom was supported. Summary tallies shown at top.
- **Marks:** Filled polygons (counties/states)
- **Channels:** Color hue (party: red/blue), color saturation (margin of victory), position (geographic)
- **Annotation options:** State borders, numeric vote totals at top, filter labels on left sidebar
- **Data types suited for:** Spatial (geographic), categorical (party), quantitative (vote share, margin)
- **Interesting feature extraction/manipulation:** "Shift from 2008" view — showing change rather than absolute values; reveals where opinion moved

---

### Interactive Multi-Series Line Chart with Data Table — "Tale of 100 Entrepreneurs" / Tableau (p.59)
- **What it shows:** Revenue growth curves over time for 100 software companies, grouped into 3 growth archetypes (Rocket Ship / Hot Company / Slow Burner)
- **When to use / avoid:** Use when individual trajectories AND overall patterns both matter. The linked table below enables drill-down. Avoid when the number of lines causes too much overplotting to read individual items.
- **Interesting properties:** Each company is a single colored line; color encodes growth archetype. Checkboxes filter by industry segment — updating both the chart and the linked data table simultaneously. Hover reveals individual company name.
- **Marks:** Lines (one per company)
- **Channels:** Color hue (growth archetype: red/orange/blue), position x (years since founding), position y (revenue $), opacity (individual lines are semi-transparent to reduce overplot)
- **Annotation options:** Threshold line at $50M; archetype legend; industry checkbox filter
- **Data types suited for:** Temporal (years), quantitative (revenue), categorical (archetype, industry)
- **Interesting feature extraction/manipulation:** Grouping 100 companies into 3 archetypes — a clustering/segmentation abstraction that makes the pattern readable; years-since-founding normalization so all companies align at year 0

---

### Interactive Multi-Chart Dashboard — "Inside Super PACs" (p.60–61)
- **What it shows:** Political spending by Super PACs — who spent what, in support of or opposition to which candidates, over time
- **When to use / avoid:** Use when multiple related questions need to be answered about the same dataset. Avoid if the audience needs a single clear message — complexity may overwhelm.
- **Interesting properties:** Combines three chart types in one scrollable design: (1) sized pie charts per candidate (circle size = total spending, pie split = support vs. opposition), (2) stacked area chart over time showing total spending, (3) horizontal bar chart of spending per PAC filtered by a month slider. All charts are interactive.
- **Marks:** Circles (pie charts — size encodes total), filled areas (time series), horizontal bars (per PAC spending)
- **Channels:** Circle size (total PAC spending per candidate), pie angle (proportion support vs. opposition), position x (time), bar length (spending per PAC), color (support = teal, opposition = dark grey)
- **Annotation options:** Candidate names above circles; $ axis labels; month slider
- **Data types suited for:** Quantitative (spending amounts), temporal (months), categorical (candidates, PACs), compositional (support/opposition split)
- **Interesting feature extraction/manipulation:** Splitting spending into support vs. opposition is a derived ratio; month filter aggregates individual transactions into monthly totals

---

### Tall Format Multi-Section Infographic — "Mobile Youth: Teens & Cell Phones" (p.67)
- **What it shows:** Teen cell phone usage — communication methods (petal/wheel chart), gender divide, parental controls (donut charts), extra features (horizontal bars), texting and driving
- **When to use / avoid:** Use for a comprehensive overview of a topic with multiple sub-questions. Tall vertical format designed for online scrolling.
- **Interesting properties:** Top section uses a flower/petal chart (wedge slices arranged in a circle, each a different communication mode with its percentage). This is semantically a pie variant but visually distinctive — each petal carries an icon.
- **Marks:** Wedge/petal areas (communication wheel), filled human icons (gender), donut segments (parental controls), horizontal bars (features)
- **Channels:** Petal size/angle (percentage of teens), color hue (communication mode), icon color (gender — blue/pink), bar length (feature adoption rate)
- **Annotation options:** Percentage labels on each petal, category name on each petal
- **Data types suited for:** Compositional/percentage, categorical, comparative (boys vs. girls)
- **Interesting feature extraction/manipulation:** Nothing unusual — straightforward percentages displayed

---

### Horizontal Bar Chart with Icon Marks — "Lifespan of Storage Media" (p.78–79)
- **What it shows:** Lifespan (in years of use) of ~25 storage media types from 1940s to present, grouped by media category (magnetic tape, optical, video, photo)
- **When to use / avoid:** Use when ranking and comparing a large number of items along a single quantitative axis. Icon beside each bar makes identification immediate without reading labels.
- **Interesting properties:** Each row has: year introduced (left label), photo/icon of the device, green bar extending to lifespan value, occasional callout annotation explaining failure mode. Categories separated by colored section headers. The cloud (as the reference bar extending to 100+) is the hero item.
- **Marks:** Horizontal bars (length = lifespan), icon images (left of each bar), colored section backgrounds (category)
- **Channels:** Bar length (years of useful life), position y (media type identity), color of section header (media category), icon (visual identity of device)
- **Annotation options:** Failure-mode callout bubbles (e.g., "Click of Death", "Head Crash"); year introduced label; numeric value at bar end
- **Data types suited for:** Quantitative (years), categorical (media type, category), ordinal (by introduction date)
- **Interesting feature extraction/manipulation:** "Additional Ways Media Can Fail" section at bottom — extracted failure mode taxonomy shown as icons, decoupled from the bar chart

---

### Circular Chord Diagram + Radial Bar Chart — "Hockey: History of the Stanley Cup" (p.98–99)
- **What it shows:** All Stanley Cup Finals matchups between NHL teams, showing which teams met in finals, wins/losses per team, and number of Finals appearances
- **When to use / avoid:** Use when relationships between pairs of entities are the primary story AND the number of entities is large enough that a matrix would be hard to scan. Avoid when the audience is unfamiliar with chord diagrams.
- **Interesting properties:** Teams arranged in a circle (Western Conference on left, Eastern Conference on right). Lines connecting them represent each Finals matchup — line thickness encodes number of times that pair met. Bars radiating outward from each team encode their Finals appearances (two tones: wins vs. losses). Trophy at top, scorecard-style header showing overall record.
- **Marks:** Arc segments (teams), curved lines (matchups), radiating bars (appearance count)
- **Channels:** Line thickness (number of head-to-head Finals meetings), bar height (appearances), color (win = solid / loss = lighter tone), position on circle (conference identity)
- **Annotation options:** Team abbreviations on circle; wins/losses count as symbols; legend for line thickness and bar height
- **Data types suited for:** Relational (team matchups), quantitative (wins, losses, appearances), categorical (team, conference)
- **Interesting feature extraction/manipulation:** Aggregating all Finals matchups into pair-counts collapses ~100 years of data into a readable network; separating appearances into wins/losses adds a second data dimension to the bars

---

### Side-by-Side Comparison Infographic — "Making an Organic Choice" / SoNice (p.93–94)
- **What it shows:** Six dimensions of comparison between conventional farming (97.5% of food) and organic farming (2.5%): carbon footprint, market growth, food quality, pesticide usage, soil & fertilizer impact
- **When to use / avoid:** Use when the primary message IS the comparison between two categories across multiple dimensions. The two-column layout is immediately scannable. Avoid if the dimensions are too different to share a common visual language.
- **Interesting properties:** Central column has labeled category buttons (CARBON FOOTPRINT, MARKET GROWTH, etc.) as dividers. Left column (conventional) uses red/dark color tones; right column (organic) uses green/light tones. Each row uses a different visualization type per dimension: bar chart, number callout, bar chart with icons, icon array. Pie chart at top-right shows reasons Canadians chose organic.
- **Marks:** Bars, number callouts, icon arrays, pie wedges
- **Channels:** Color hue (conventional = dark/industrial, organic = green/natural), position in column (left = conventional, right = organic), bar length (quantities), icon count (e.g., 500 insect pests)
- **Annotation options:** Category label buttons in center column; numeric values; percentage callouts
- **Data types suited for:** Categorical (farming type), quantitative (CO2, growth %, nutrient increases), comparative
- **Interesting feature extraction/manipulation:** Selecting six standardized dimensions from disparate data types (weight, %, count) and presenting them on a common template forces comparability

---

### Multi-Row Timeline with Glyph Columns — Honda Accord 30 Years (p.95–96)
- **What it shows:** 9 generations of the Honda Accord (1982–2012), with each row showing: car photo, curb weight, engine size, price, horsepower, highlights (icon glyphs), and exterior color swatches
- **When to use / avoid:** Use when tracking evolution of a product or entity across multiple attributes over time. Each row is one generation/item; each column is one attribute.
- **Interesting properties:** Exterior color column is a pixel-mosaic of all available colors for that generation — a compact way to show a multi-value categorical attribute. Highlight features shown as icon glyphs rather than text. Weight and HP shown as a pig/cow-weight icon and running animal glyph.
- **Marks:** Car photo (image glyph), icon glyphs (features), color pixel mosaic (color options), bar/size comparison (dimensions)
- **Channels:** Row position (generation/year), icon identity (feature type), color mosaic (available colors), numeric label (price, HP, weight)
- **Annotation options:** Column headers; generation labels on left axis; callout for "new features in 9th generation"
- **Data types suited for:** Temporal (generation sequence), quantitative (price, HP, weight), categorical (features, colors)
- **Interesting feature extraction/manipulation:** The color mosaic is a creative encoding of a set-valued attribute (multiple colors per generation) into a small space; icon glyphs abstract feature lists into scannable symbols

---

### Radial Category Map — "The Conversation Prism" (p.100)
- **What it shows:** Landscape of social media companies and platforms, organized into radial sectors by category (Social Networks, Blogs/Microblogs, Social Commerce, Music, Video, etc.)
- **When to use / avoid:** Use for showing a large taxonomy of entities grouped into categories, where the relationship between items is membership in a category. Avoid when precise quantitative comparison is needed.
- **Interesting properties:** Hundreds of company logos arranged in concentric rings; innermost ring contains the brand's own identity ("YOU" at center with core values). Color hue of each sector identifies the category. The circular layout creates a sense of a complete ecosystem.
- **Marks:** Logo images (company identity), sector wedges (category boundary)
- **Channels:** Angular position (category membership), radial distance (implicitly: smaller companies further out, but not strictly quantitative), color hue (category)
- **Annotation options:** Category labels at outer edge of each sector; company names below logos
- **Data types suited for:** Categorical (company, sector), relational (membership), qualitative
- **Interesting feature extraction/manipulation:** Taxonomy of hundreds of entities compressed into a scannable circular layout; fair use of trademarked logos as data marks

---

### Genealogy Stream Map — "Genealogy of Pop/Rock Music" (p.98)
- **What it shows:** Evolution and influence relationships among music genres over time, displayed as flowing streams with branches and merges
- **When to use / avoid:** Use when evolution, divergence, and merging of categories over time is the story. Avoid when precise timing or magnitude is critical — stream widths are suggestive, not quantitatively exact.
- **Interesting properties:** Flows branch from common ancestors and merge into derivative genres; the shape of each stream suggests relative importance. Dense annotations throughout.
- **Marks:** Filled flowing streams (genres), branch/merge nodes
- **Channels:** Stream width (relative prominence), position x (time), position y (genre family grouping), color (genre identity)
- **Annotation options:** Genre names inline on streams; artist/band names as text along streams
- **Data types suited for:** Temporal, relational (influence), categorical (genre)
- **Interesting feature extraction/manipulation:** Curating influence relationships from qualitative music history knowledge; representing merging/splitting as a stream topology

---

### Multi-Attribute Product Timeline Table — "The Insanely Great History of Apple" (p.99)
- **What it shows:** Every Apple product from the company's founding to ~2012, organized into color-coded vertical columns by product category (Software, Input/Output, Desktop, Laptop, etc.) with time as the y-axis
- **When to use / avoid:** Use for a comprehensive historical taxonomy of a single company's product line. Width scales with number of categories, height with years — works best as a large poster.
- **Interesting properties:** Each product category is a color-coded vertical column; items within each column are placed at their release year on the y-axis with tiny product images. Lines connect successor products within a column. The result reads as both a timeline and a product family tree.
- **Marks:** Product image thumbnails, connecting lines (succession), colored column backgrounds (category)
- **Channels:** Position y (release year), column position x (product category), color of column (category hue), connecting line (product succession)
- **Annotation options:** Product names; year labels on y-axis; category headers
- **Data types suited for:** Temporal (release year), categorical (product type), relational (succession)
- **Interesting feature extraction/manipulation:** Separating one company's history into parallel product lineages makes simultaneous evolution visible

---

### Process Flow Diagram — "How Our Laws Are Made" (p.87)
- **What it shows:** The legislative process from bill introduction to enacted law in the U.S. Congress
- **When to use / avoid:** Use for explaining sequential or branching processes without numerical data. When the goal is comprehension of steps, not comparison of quantities.
- **Interesting properties:** Uses colored pathway with branching nodes (House path vs. Senate path), illustrated icons for each actor (Representative, Senator, Committee, President), and text callouts. No bar charts or data visualizations — purely explanatory.
- **Marks:** Pathway line (process flow), circle/icon nodes (actors/steps), color-coded zones (House = orange, Senate = blue/green)
- **Channels:** Path position (sequence in process), color hue (institutional identity), icon shape (actor type)
- **Annotation options:** Step labels, constitutional quote in upper right, legend at lower right
- **Data types suited for:** Process/procedural, categorical (actors), sequential
- **Interesting feature extraction/manipulation:** N/A — process rather than data

---

### Dish + Ingredient Icon Grid — P.F. Chang's Menu (p.90–92)
- **What it shows:** Four dishes paired with 3 key flavor/ingredient icons each; a separate section pairs wine types with flavor profiles
- **When to use / avoid:** Use for showing composition or pairing relationships where the visual identity of items (photo of dish) is part of the message. Effective for food/lifestyle content.
- **Interesting properties:** Each dish shown as a food photograph, then 3 circular icon glyphs showing its key ingredients (Cilantro, Mint, Thai Basil, etc.) in stylized botanical illustration style. Icon circles use color to suggest flavor character (green = herbal, red = spicy). The wine section uses glass silhouettes of different types as category marks.
- **Marks:** Food photograph (dish identity), circular icon glyphs (ingredients)
- **Channels:** Color of icon (flavor character — green/herbal, red/spicy, orange/fruity), shape of icon (ingredient identity), position in grid row (association with dish)
- **Annotation options:** Ingredient name below each icon; colored label at side of dish name showing spice level
- **Data types suited for:** Categorical (dish, ingredient, flavor), relational (pairing)
- **Interesting feature extraction/manipulation:** Reducing ingredient list to 3 "hero" ingredients per dish — editorial abstraction that simplifies without losing character

---

### Node-Link Hierarchical Diagram — "The Common Cook's How-Many Guide" (p.76–77)
- **What it shows:** Kitchen measurement conversions between units (Gallon → Quart → Pint → Cup → Tablespoon → Teaspoon → fractional cups)
- **When to use / avoid:** Use when the relationships between units (ratios/conversions) matter as much as the values themselves. Node-link format makes the hierarchy navigable.
- **Interesting properties:** Each unit is represented as a donut circle (ring) with the unit name in the center. Lines connecting circles are labeled with the conversion ratio. Larger units are higher in the layout; smaller units fan out below. The donut ring itself is divided into segments showing sub-unit divisions.
- **Marks:** Donut rings (units), connecting lines (conversion relationships)
- **Channels:** Size of ring (unit size — larger rings for larger units), position y (hierarchy level), line label (conversion ratio)
- **Annotation options:** Unit name in ring center; ratio numbers on connecting lines
- **Data types suited for:** Hierarchical, quantitative (ratios), relational (conversion)
- **Interesting feature extraction/manipulation:** The ring segmentation shows how many of the next smaller unit fit into each ring — ratio encoded visually as well as numerically

---

### Visual History Poster — "A Visual History of the American Presidency" / Timeplots (p.100)
- **What it shows:** All U.S. presidents from Washington to Obama with parallel columns: presidential transitions (snake timeline), name (typography sized by fame/significance), political indicators (dot matrix for Senate/House/Cabinet composition), economic/war data (area charts), and text summaries
- **When to use / avoid:** Use for rich historical comparison where many parallel attributes need to be shown simultaneously per time period. Works as a poster; too dense for casual reading.
- **Interesting properties:** Presidential name typography is sized by historical significance — Obama's name is largest, Adams's smallest, visually encoding perceived importance. Snake/zigzag timeline on left encodes party (red = Republican, blue = Democrat) with portrait photos at election points.
- **Marks:** Typography (name as mark), dots (congressional composition), area (economy/war), snake path (temporal sequence)
- **Channels:** Text size (historical significance), position y (time), text color/path color (party), dot density (composition), area height (economic indicator)
- **Annotation options:** War period shading; annotations for major events; text summary column at right
- **Data types suited for:** Temporal, categorical (party), quantitative (economy), ordinal (significance)
- **Interesting feature extraction/manipulation:** Typography as a quantitative channel (size encodes significance) — unusual and semantically interesting
