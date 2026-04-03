# [agent_05] Cool Infographics — pages 201-249

## Overview of pages 201–249

Pages 201–220 cover Chapter 6: best practices for infographic design (accuracy, data honesty, minimalism, topic selection, key message focus). Pages 221–249 cover Chapter 7: design resources — desktop software, online visualization tools, data sources, and a reading list. The chapter is primarily practical and process-oriented rather than theoretical.

---

## Visualizing Area: The Core Accuracy Rule

- We visually compare objects by **area**, not by height or diameter alone. (p.201–204)
- Numerical values are one-dimensional; objects on a page are two-dimensional — designers must account for this. (p.201)
- **Bar charts** are safe: width stays constant, only height changes, so area scales in direct proportion to value. Formula: Width × Height = Area. (p.203)
- **Circles are dangerous**: changing the diameter to match data values is WRONG. If you triple the diameter, the area becomes ~8.95× larger (not 3×), because Area = π × radius². (p.204)
- Correct circle sizing workflow:
  1. Choose a "Master circle" as baseline.
  2. Calculate each other circle's area as a ratio of the master's area.
  3. Derive diameter from the correct area: Radius = √(Area / π), Diameter = 2 × Radius.
  4. Enter only the diameter into the design software — never stretch both dimensions simultaneously. (p.205)
- Same problem applies to squares, icons, logos: do not change both width and height. Keep aspect ratio constant and scale by area calculation. (p.204)

**Rule of thumb:** When sizing any non-rectangular shape to represent data, always calculate area proportions using mathematics before touching the design software. (p.205)

---

## Topic Selection

### Pick a Good Topic (p.206)
- A good infographic topic must be **interesting to the target audience** — readers don't waste time on boring topics.
- Ideal: previously unknown information on a subject the audience cares about.
- Best topics are **counterintuitive or surprising** — readers want to share new information.
- **Trending topics** attract traffic automatically but are short-lived; relevance fades quickly. (p.206)
- **Controversial topics** drive emotional engagement and sharing but risk alienating part of the audience. (p.207)

### Search for Prior Art (p.207)
- Before designing, search for existing infographics on your topic.
- Goals: avoid duplicating existing work; avoid reusing color palettes or illustration styles; find additional data sources; identify sites to include in outreach.
- Mainstream media may refuse to publish an infographic if an identical design already exists. (p.207)

---

## Focus on the Key Message

### Define the Key Message First (p.208)
- The key message is the primary thing you want readers to understand and remember after viewing.
- **Include only data and visuals that support the key message — eliminate everything else.** (p.208)
- Adding multiple unrelated data points increases complexity without adding credibility.
- If a design has no clear story, readers give up and move on. (p.208)

### The 5-Second Rule (p.208)
- Most readers skim for only 5–10 seconds.
- A good infographic must communicate its key message within 5 seconds to succeed with skimming readers — even those who never read further. (p.208)
- The design must communicate the main point visually, not via text.

---

## Visualize When Possible

- Visualizing data helps by: grabbing attention, reducing time to comprehension, providing comparison context, making the key message memorable (Picture Superiority Effect), and making information accessible across languages. (p.211)
- **Big fonts are NOT data visualizations.** Displaying a number in large type gives no context or frame of reference — each reader interprets it differently from their own perspective. The designer loses control of interpretation. (p.211)
- **Visuals pull attention away from text**: any data shown as text alone is perceived as less important or secondary. Readers focus on visuals, skip text. (p.212)
- Rule: If data is important enough to include, it is important enough to visualize. (p.212)

---

## Minimize Text

- Less text = more readers. At first glance, text-heavy designs are judged "not worthy" of time investment. (p.212)
- The infographic should communicate the key message — not be a comprehensive guide to the company or product.
- Example: Marc Morera's Star Wars Episode IV infographic uses minimal text and visual paths for character interactions — less text encourages longer engagement as readers trace paths. (p.213)

---

## Eliminate Chart Legends

- Chart legends are a design anti-pattern: they force readers to repeatedly look back and forth between the chart and the key, increasing eye movement and cognitive load. (p.214)
- **Solution:** Build the guide directly into the chart — use inline labels, icons embedded into bar bases, or descriptions placed directly at the data. (p.214–215)
- Icons embedded into a chart make color-coding faster to understand because all relevant information is within the reader's field of view simultaneously.
- Eliminating legends also opens space for the chart to be enlarged or for additional information.

---

## Be Data Transparent

- A large portion of audiences are initially skeptical — infographics must pass a data credibility test quickly. (p.215)
- Readers ask: Where does data come from? How old is it? Why should I believe it? Is this credible? (p.215)

### Common Anti-Patterns in Data Transparency (p.216)
- **No data sources listed**: audience quickly becomes unbelievers; all conversation shifts to questioning the numbers rather than engaging with the message.
- **Vague data sources**: listing just a site name (e.g., "Data.gov") without a specific report or URL makes data impossible to verify.
- **Questionable sources**: Wikipedia and personal blogs are automatic skepticism triggers for many readers.

### Best Practices (p.216)
- Track down and cite the original source, not just a news article that quoted data.
- List data sources inline with data or in the footer.
- Link to the specific page or dataset, not just the host site.
- Include the date or year the data was published.
- Best practice: Make source data available as a public Google Docs spreadsheet with URL included in the infographic.

---

## The Fine Print (p.217–218)

Every infographic should include in its footer, at minimum:
- **Company logo** (so the publisher is known when re-shared)
- **Landing page URL** (so the original full-size version can be found)
- **Source links** (specific citations)
- **Creative Commons or copyright license** (so reuse terms are clear)
- **Designer credit** (builds human credibility; readers more likely to share work attributed to a person than a faceless company)

---

## Design Resources — Key Practical Notes

### Periodic Table of Visualization Methods (p.232)
- A reference tool from Visual-Literacy.org that groups visualization types by data type: Data Visualization, Information Visualization, Concept Visualization, Strategy Visualization, Metaphor Visualization, Compound Visualization.
- Hovering (online) shows an example of each method.
- Useful to break out of defaults (bar, pie, line) and find the right method for the data type.

### Word Clouds (p.233)
- Useful when data is more qualitative than quantitative.
- Font size encodes word frequency; no hard values.
- Advanced: can analyze phrases to distinguish sentiment ("love" vs. "don't love"). (p.233)

### Gauge / Dial Charts (p.234)
- Circular dial with needle showing a single value on a scale.
- Good for showing current status against a range (memory, CPU, network — example from Chartle.net).

### Choropleth Maps (p.234–235)
- Color encodes quantitative values over geographic regions.
- Example: Global Peace Index 2012, showing country-level rankings with a 5-level color scale (very high to very low). ChartsBin used for world map visualization.

### Network Diagrams (p.236)
- Gephi: handles large imported datasets (50,000+ nodes), described as "Photoshop for data."
- Nodes and edges show relationships; useful for showing complex interconnected data.

### Online Infographic Design Sites — Advantages and Disadvantages (p.241–242)
**Advantages:** Speed (under 1 hour), hosting, SEO optimization, fresh design styles.
**Disadvantages:** Generic-looking templates (loss of uniqueness), may force wrong chart type for data, dependency risk, traffic/backlinks go to design site not your site, potential confidentiality issues with company data.

---

## Practical Rules of Thumb (Summary)

- Size circles by area, not diameter. (p.203–205)
- One clear key message per infographic — eliminate everything else. (p.208)
- Communicate the key message in under 5 seconds. (p.208)
- Never use big fonts as a substitute for data visualization. (p.211)
- If it's important enough to include, it's important enough to visualize. (p.212)
- Eliminate chart legends — embed labels directly. (p.214)
- Always cite specific data sources with URLs and dates. (p.216)
- Always include company logo, URL, sources, license, and designer credit in every infographic footer. (p.218)
