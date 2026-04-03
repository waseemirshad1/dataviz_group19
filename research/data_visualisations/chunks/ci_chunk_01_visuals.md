# [agent_01] Cool Infographics — pages 1-50

---

### Multi-Line Area Chart with Volume Sub-Chart (p.19–20)
- **What it shows:** Long-term price trends for S&P 500, NASDAQ, and Dow Jones Industrial Average from 1935–2010; a secondary volume bar chart below shows trading volume over time
- **When to use:** Comparing multiple time series over long periods; showing both trend and supporting context (volume) simultaneously; avoid when fewer than 2 series or short time span
- **Interesting properties:** Displays ~80,000 data points on one page; reader sees overall pattern, comparison between indices, and significant events (spikes/dips) in seconds; dual-chart layout (price + volume stacked vertically) adds explanatory power
- **Marks:** Lines (price trends), areas under lines (can be filled or not), bars (volume)
- **Channels:** Position (x = time, y = price/volume), color hue (one color per index), area fill for volume
- **Annotation options:** Callout labels at line ends; event annotations on timeline; legend at top
- **Data types suited for:** Quantitative (price, volume), temporal
- **Interesting feature extraction/manipulation:** Normalizing all three indices to a common baseline (0%) to show relative growth rather than absolute price enables fair comparison

---

### Treemap / Heatmap Grid (StockTouch iPad App) (p.21)
- **What it shows:** Top 100 US stocks organized by market sector (9 sectors); each stock is a colored rectangle; color encodes price performance over a selectable time period (green = increase, red = decrease); size encodes market capitalization
- **When to use:** When you need to show both membership in categories and a quantitative performance metric for many items simultaneously; avoid when precise value reading is needed
- **Interesting properties:** Spiral arrangement within each sector from largest (center) to smallest; sectors are tiled as sub-regions; time period adjustable via slider — makes it interactive; sectors labeled with aggregate performance
- **Marks:** Rectangles (areas)
- **Channels:** Area/size (market cap), color hue (green/red for direction), color saturation (magnitude of change), position within sector (relative market cap rank), spatial grouping (sector membership)
- **Annotation options:** Sector labels with aggregate % change; stock ticker labels on each cell
- **Data types suited for:** Quantitative (market cap, % change), categorical (sector)
- **Interesting feature extraction/manipulation:** Aggregating to sector level (sector label shows sector-total % change) while preserving individual stock detail

---

### Multiple Small Line Charts in Grid (p.22)
- **What it shows:** Ten separate Yes/No binary outcome questions plotted as individual line charts, each with age (0–100) on X and Yes/No on Y; titled "Could You Be a Failure? (and other charts by age)"
- **When to use:** When the same X variable (age) must be related to many different Y outcomes simultaneously; small multiples allow comparison across panels; avoid if too many panels or if the patterns are indistinguishable
- **Interesting properties:** Humorously framed — outcomes are subjective traits (Failure, Awesome, High, Loser, Important, Entrepreneur, Depressed, Misunderstood, Liar, All the Answers); the hand-drawn on graph-paper aesthetic reinforces casual tone; layout is vertical strip
- **Marks:** Lines (each panel is a simple area/line chart)
- **Channels:** Position (x = age, y = Yes/No magnitude implied by line height), layout/facet (each panel = one question)
- **Annotation options:** Panel titles as questions; Y-axis labels (Yes/No); X-axis label (Age)
- **Data types suited for:** Quantitative (age), ordinal/binary (Yes/No outcome), categorical (question type)
- **Interesting feature extraction/manipulation:** This is sketch/concept data — the power is in applying line chart form to subjective, non-numeric questions, making viewers project their own experience

---

### Area Chart — Single Series with Strong Fill (p.24)
- **What it shows:** Growth of Google search volume for the term "infographic" from 2004 to 2013; explosive exponential growth visible
- **When to use:** Single time series where the area below the line conveys magnitude over time; especially effective for showing exponential growth
- **Interesting properties:** Large typographic annotation embedded in white space to left of the chart ("Explosive growth… more than 20 times in 3 years") — text and chart are unified; gradient fill from light at the base to dark at the peaks
- **Marks:** Area, line
- **Channels:** Position (x = time, y = search volume), area fill (magnitude)
- **Annotation options:** Key statistic as large text integrated into chart canvas
- **Data types suited for:** Quantitative, temporal

---

### Isotype / Unit Chart — Newspaper Grid (p.25)
- **What it shows:** Information overload comparison — 174 newspapers (2007) vs. 40 newspapers (1986) shown as a grid of newspaper icons; 40 newspapers highlighted with a red box at the bottom
- **When to use:** Showing a count or quantity using repeated unit icons; especially effective for "how many of X" comparisons where the unit icon is meaningful; avoid when the number is too large to count visually
- **Interesting properties:** The 40 highlighted in red at the bottom makes the comparison between 40 and 174 immediately visceral; the grid format naturally communicates quantity through count
- **Marks:** Icons (newspaper pictograms arranged in a grid)
- **Channels:** Position (row/column = count), color highlight (red border box = old quantity for comparison)
- **Annotation options:** Title text; quantity labels below each group; color highlight on the comparison group
- **Data types suited for:** Quantitative (counts), categorical (time period)
- **Interesting feature extraction/manipulation:** Converting raw data (information capacity in gigabytes) into a relatable human-scale unit (newspapers per day)

---

### Nested Area Size Comparison — Squares (p.26)
- **What it shows:** Relative sizes of gigabyte, terabyte, and petabyte — a tiny yellow square (gigabyte), a small blue square (terabyte), and a large purple square (petabyte) nested or positioned together
- **When to use:** When the ratio between values is so extreme that a standard bar chart would be unreadable; size-area comparison makes the ratio visceral; avoid when precise reading is needed
- **Interesting properties:** Each square is 1,024x the previous — the visual makes this multiplicative relationship immediately comprehensible; color differentiates the units
- **Marks:** Rectangles/squares (areas)
- **Channels:** Area/size (relative data magnitude), color hue (unit identity), position (lower-left anchored so they share a corner, making comparison natural)
- **Annotation options:** Unit labels, text callouts with arrows
- **Data types suited for:** Quantitative (large ratio comparisons)

---

### Proportional Circle Comparison (p.30)
- **What it shows:** Global internet users (2.27B) vs. US total population (311M) as two circles of proportional area; the larger circle represents internet users, the smaller embedded circle represents the US
- **When to use:** Comparing two magnitudes where one contains or relates to the other; when a second reference value is needed to give the primary value context
- **Interesting properties:** The US flag fills the smaller circle, making national identity immediately recognizable; the size ratio (7:1) is viscerally apparent without reading numbers
- **Marks:** Circles/areas
- **Channels:** Area (quantity), color/fill (identity — flag imagery)
- **Annotation options:** Large numerals as data labels; source and date
- **Data types suited for:** Quantitative (two magnitudes for comparison)

---

### Globe Pie Chart / Proportional Globe Segment (p.31)
- **What it shows:** Internet users (2.27B) as a proportion of total world population (7B) — shown as a partial globe, with approximately one-third colored (internet access) and two-thirds grey (no access)
- **When to use:** When one value is a subset of a total and geographic/global framing adds meaning; the globe metaphor reinforces the "worldwide" scope
- **Interesting properties:** Using a 3D globe instead of a flat pie chart adds geographic metaphor weight; the grey-vs-color contrast is stark
- **Marks:** Globe area (3D sphere segment)
- **Channels:** Color hue (blue = connected, grey = not connected), area proportion (fraction of sphere)
- **Annotation options:** Large numerals; labels for each segment
- **Data types suited for:** Quantitative ratio (part-to-whole), spatial (global)

---

### Waffle Chart / Grid Unit Chart — Picture Superiority Effect (p.32)
- **What it shows:** Memory retention after 3 days: text only = 10% (1 row of blue squares out of a 10x10 grid), text + picture = 65% (6.5 rows of blue squares)
- **When to use:** Showing percentages as fractions of a whole when you want the visual to be proportional and countable; more honest than pie charts for comparing two percentages
- **Interesting properties:** Two side-by-side waffle charts allow direct comparison; the grey squares represent "forgotten" content; large % labels below reinforce the visual
- **Marks:** Small squares in a 10x10 grid
- **Channels:** Color (blue = remembered, grey = forgotten), position (each cell = 1%)
- **Annotation options:** % labels, category labels (Text or Audio Only / Text + Picture)
- **Data types suited for:** Quantitative percentage, part-to-whole

---

### "Underskin" — Subway Map Applied to Human Body (p.34)
- **What it shows:** Eight systems of the human body (Arterial, CNS, Digestive, Lymphatic, Musculoskeletal, Respiratory, Urinary, Venous) mapped as colored "subway lines" running through a human body silhouette; major anatomical junctions shown as station nodes
- **When to use:** When you want to show how multiple parallel systems share connection points along a common structure; the subway metaphor works wherever there are parallel routes with shared nodes
- **Interesting properties:** This is a semantic re-application — subway map visual style applied to anatomy. The result went viral because the design style was known but the subject was novel. The body silhouette serves as the spatial anchor; each system is a colored line; organs are stations
- **Marks:** Lines (body systems as routes), circles (nodes/junctions/organs), silhouette (spatial frame)
- **Channels:** Color hue (one color per body system), position (anatomical location on body), node size (implicitly — major organs = larger circles)
- **Annotation options:** Station labels (organ names), line labels (system names), color-coded legend
- **Data types suited for:** Relational (which systems share connection points), categorical (system type), spatial (body position)
- **Interesting feature extraction/manipulation:** Abstracting the messy anatomy into clean geometric lines and nodes — the schematic simplification is what makes the information readable

---

### "Tower of Beer" — Vertical Scale Comparison Infographic (p.37–38)
- **What it shows:** The height of stacked beer cases a person could afford if saving $1/day from age 25 to 70 in a Roth IRA; compared in height to the Statue of Liberty and Burj Khalifa tower; the tower of beer cases is drawn to scale alongside these known references
- **When to use:** When a large quantitative result needs to be made viscerally tangible by translating it into a familiar physical object at a human scale
- **Interesting properties:** The financial concept (compound savings) is translated into a ridiculous but relatable physical unit (beer cases); the height comparison to famous buildings provides immediate scale; the vertical orientation of the infographic reinforces the metaphor
- **Marks:** Stacked rectangular blocks (beer cases), building silhouettes
- **Channels:** Height/length (quantity), color and texture (beer case branding vs. building silhouette), position (shared ground line for fair height comparison)
- **Annotation options:** Height labels, dollar amounts, age markers in the text, building names and heights at the base
- **Data types suited for:** Quantitative (savings amount), temporal (age progression)
- **Interesting feature extraction/manipulation:** Converting financial data (dollar savings + compound interest) into a physical height measurement using the size of a beer case as the unit

---

### Radial Category Wheel with Icons (VinTank Wine Apps) (p.47)
- **What it shows:** Top 26 most promising wine apps, grouped into 8 categories (Restaurants, Travel, Utility, Winery, Combo, Journaling, Social, Reference, Retail), arranged as a color-coded wheel with app icons placed in their category segment
- **When to use:** Showing membership of many items in mutually exclusive categories arranged radially; when icons/images of items are meaningful to show; avoid when precise ordering within categories matters
- **Interesting properties:** Each app icon is an HTML clickable link — the visualization doubles as a navigation interface; each category is a distinct color segment; icon size and placement within the segment is informal but the color ensures clear grouping
- **Marks:** Icons (app images), circular sectors (category regions)
- **Channels:** Color hue (category), angular position (category), radial distance from center (informal — not data-encoded), icon identity (brand/visual recognition)
- **Annotation options:** Category labels on outer rim; center label (VinTank branding + title)
- **Data types suited for:** Categorical (app type), nominal (app identity)
- **Interesting feature extraction/manipulation:** Grouping apps by functional category rather than listing alphabetically — the category is the key insight, not the individual rank

---

### Beer Brand Ownership Bubble Cluster Network (p.45)
- **What it shows:** Ownership relationships between parent beer companies and their brand portfolios; each parent company is a large labeled circle; each brand variety is a small circle; brands cluster around their parent company
- **When to use:** Showing hierarchical ownership or membership where the number of items under each parent varies greatly; when showing the portfolio breadth of each entity
- **Interesting properties:** The whole visualization is circular in a beer-colored background; dashed lines connect parent companies that share partial ownership; the cluster layout encodes hierarchical containment through spatial proximity rather than lines
- **Marks:** Circles (large = parent company, small = brand variant)
- **Channels:** Size (parent company importance), position (clusters by parent), color (uniform gold on brown — aesthetic, not data-encoded), dashed lines (partial ownership links)
- **Annotation options:** Company and brand name labels on each circle
- **Data types suited for:** Relational (ownership hierarchy), categorical (parent company), quantitative (portfolio size implied by cluster size)
- **Interesting feature extraction/manipulation:** The total count of small circles around each parent visually encodes portfolio breadth without needing a bar chart

---

### Circular Timeline with Pop-Up Hover Detail ("A Raw Chocolate History") (p.47–49)
- **What it shows:** The history of chocolate from ancient times to present, arranged as a circular/spiral timeline with illustrated icons at each historical milestone; hovering over any milestone reveals a pop-up text block with detailed information about that time period
- **When to use:** When a timeline has many events that would clutter a single view if all detail was shown; circular format works for cyclical or long-span histories; pop-up detail manages information density
- **Interesting properties:** The primary design is visually clean — only icons and dates on the circular path; all textual detail is hidden in hover states; the decorative cocoa leaf border integrates the data and the aesthetic; a bar chart of "Chocolate Purity (Cocoa Solids %)" is embedded in the lower-left of the circular design
- **Marks:** Circular/spiral path (timeline), icons/illustrations (events), pop-up rectangles (hover detail)
- **Channels:** Position along the arc (temporal), icon identity (event type), color of icons (different types of events), size (prominence)
- **Annotation options:** Date labels along the path, event titles at icon positions, full detail text in hover pop-ups
- **Data types suited for:** Temporal (historical progression), categorical (event type), narrative
- **Interesting feature extraction/manipulation:** Separating primary vs. secondary information into two layers (visible vs. hover) is a key complexity management technique

---

### Subway Map Style Applied to Information Network ("My Visual Mapping Blogroll") (p.50)
- **What it shows:** A network of information visualization and knowledge mapping blogs, arranged as a subway map with each blog as a station; lines represent thematic categories (Creativity, Visualization, Pedagogy, etc.); stations where blogs appear on multiple lines represent blogs that span multiple themes
- **When to use:** When a large relational network of items needs to be organized by multiple overlapping categories; subway map style communicates "routes" (themes) and "junctions" (multi-category members) intuitively
- **Interesting properties:** Semantic novelty — subway map applied to a blogroll, not a city. The same visual grammar (colored lines = themes, circles = nodes, labels = names) is repurposed for information categorization. Each station (blog) is a clickable PDF link.
- **Marks:** Lines (thematic categories), circles/nodes (individual blogs), intersection nodes (multi-category blogs)
- **Channels:** Color hue (thematic category/line), position (spatial layout by conceptual proximity), line overlap (multi-category membership)
- **Annotation options:** Station name labels, line/category name labels at terminals, numbered terminal circles
- **Data types suited for:** Relational (blog network), categorical (theme), nominal (blog identity)
