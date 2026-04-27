# [agent_19] Visualization Analysis and Design — pages 151-200

## CV Ideas from Chapter 6 (Rules of Thumb) and Chapter 7 (Arrange Tables)

Target profile: Psychology + sales + software development background → data science / ML6 internship Belgium

---

### CV Idea: Function-First Career Narrative Bar Chart (p.140–141, p.150–151)
- **What it visualizes:** The progression of core competencies across three career domains (Psychology, Sales, Software Dev) encoded as bar charts — each domain is a categorical key, each competency level is a quantitative value
- **How it works:** Inspired by Munzner's "Function First, Form Next" principle (p.140) and bar chart design (p.150). Three grouped bars per competency cluster (e.g., "Data Analysis", "Communication", "Technical"). Each group shows the relative contribution from each domain background. Bars ordered by relevance to data science role (derived ordering) rather than alphabetically — following the principle that data-driven ordering reveals patterns (p.150)
- **Adaptation for our context:** Present competency clusters relevant to ML6 internship (Python/R proficiency, Statistical reasoning, Client communication, Behavioral data analysis) as aligned bars. The Psychology background fills "Behavioral analysis" and "Research methodology" bars fully; Sales fills "Stakeholder communication"; Software Dev fills "Technical implementation". This makes the combined profile immediately legible — you are not changing career, you are ADDING a layer. The "Get it right in black and white" rule (p.140) suggests the most important attribute (data science competency level) should drive the luminance, ensuring the chart reads clearly even in printed black-and-white CVs.
- **Page reference:** p.140–141, p.150–151

---

### CV Idea: Skills Cluster Heatmap — Domain × Competency Matrix (p.158–161)
- **What it visualizes:** A compact heatmap where rows = career domains/experiences (Psychology degree, Sales role, Software dev projects, Data visualization course) and columns = competency dimensions relevant to a data science role (Statistics, Visualization, Communication, Research, ML/Modeling, Tools)
- **How it works:** Inspired by the cluster heatmap (p.158–161). Each cell is colored by proficiency level (3–5 bins — matching the perceptual limit of 3–11 distinguishable bins in small non-contiguous areas, p.160). Matrix reordering by similarity of profiles: experiences with overlapping competencies cluster together, visually proving that the background is internally coherent, not scattered. Dendrograms on the periphery (optional, for design-savvy audiences) show which experiences are most complementary.
- **Adaptation for our context:** 4 rows (experiences) × 6 competency columns. Color: white = no exposure, light blue = awareness, mid blue = proficiency, dark blue = strength. The heatmap immediately shows that no cell is empty — every experience contributed something to the data science profile. This counters the "career change" narrative by showing additive depth. For a CV targeting ML6, the "Statistics" and "Data Visualization" columns should be the darkest (= highest proficiency) — most critical for the role. The heatmap format is compact, fitting in the sidebar of a one-page CV.
- **Page reference:** p.158–161

---

### CV Idea: Parallel Coordinates Skills Profile (p.163–166)
- **What it visualizes:** Multiple competency dimensions simultaneously as parallel vertical axes, with one "polyline" per past role/experience showing that role's contribution across all dimensions
- **How it works:** Inspired by parallel coordinates (p.163–166). Each axis = one competency dimension (Statistics, Programming, Research Design, Communication, Data Visualization, Domain Knowledge). Each polyline = one past experience. Key insight from the book: parallel coordinates are best used to show that multiple items share a similar profile across many attributes (positive correlation = parallel lines). For a CV, parallel polylines across the critical axes (Programming, Data Viz, Statistics) visually demonstrate that recent experiences consistently build in the same direction.
- **Adaptation for our context:** Draw 4–5 polylines (Psychology studies, Sales experience, Software dev project, Data Viz course project). Axis ordering: place "Data Science Core" axes (Statistics, Programming) adjacent to maximize the pattern of converging lines. Color each polyline by recency: oldest experiences in light gray, most recent (data science courses, visualization project) in strong color — visually telling the "trajectory toward ML" story. The book's warning about training time (p.165) applies: this works best for design/data-science-savvy audiences (like ML6 recruiters). For non-technical HR, prefer the bar chart version.
- **Page reference:** p.163–166

---

### CV Idea: Streamgraph of Time × Skill Focus (p.153–155)
- **What it visualizes:** How the focus of skill development has shifted over time, encoded as a streamgraph where the horizontal axis is time (years) and each colored stream is a competency domain (Psychology, Sales/Communication, Software Dev, Data Science/ML)
- **How it works:** Inspired by the streamgraph idiom (p.153–155) which shows time series with categorical breakdown as flowing layers. Each stream's height at a given time point represents the fraction of active learning/experience in that domain. Layer ordering follows the "onset time" principle (Figure 7.7b): earliest domain (Psychology) at the bottom, most recent (Data Science) at the top — exactly matching the career trajectory. The result is a visual narrative of deliberate skill evolution rather than a scattered career
- **Adaptation for our context:** X-axis spans ~6 years of study/work. Streams: Psychology (wide at start, narrows), Sales (mid-period peak, then narrows), Software Dev (grows and stabilizes), Data Science (grows rapidly at the right end). This is the most visually striking CV element but requires the most interpretation — best as a header/hero graphic on a portfolio page or in the cover letter, not on a traditional CV. Semantic novelty note: streamgraphs are typically used for media consumption or financial data — using them for personal career narrative is a genuinely novel semantic role (+2 for creative application)
- **Page reference:** p.153–155

---

### CV Idea: "Banking to 45° Career Trend" Line Chart (p.157–158)
- **What it visualizes:** A single line chart showing a "data science readiness score" over time, with aspect ratio deliberately chosen using the banking-to-45° principle to make the upward trajectory appear at the most perceptually compelling angle
- **How it works:** Inspired by the banking-to-45° principle (p.157–158) — the aspect ratio of a line chart should be chosen to maximize the number of line segments falling near the 45° diagonal. A line showing skill growth presented with a nearly-flat aspect ratio looks like slow progress; the same data shown with a steep aspect ratio looks like an explosion. Banking to 45° is the principled middle ground that makes the trend maximally legible. This is a subtle but sophisticated design signal to a data-science-savvy recruiter.
- **Adaptation for our context:** Create a simple line chart of a "composite readiness score" (e.g., average of self-assessed Python, Statistics, Visualization proficiency) over the last 3 years of study/work. Apply the banking-to-45° principle to determine aspect ratio. Add a locally weighted regression line (LOESS, as referenced p.158) as a smooth trend overlay. This demonstrates explicit knowledge of a real visualization research concept while also presenting compelling career data. Label key milestones (started data viz course, completed first ML project) as annotations on the line.
- **Page reference:** p.157–158

---

### CV Idea: Overview First — Portfolio as Shneiderman Mantra (p.135–137)
- **What it visualizes:** The overall portfolio page / CV structure itself designed following the "Overview First, Zoom and Filter, Details on Demand" mantra (p.135)
- **How it works:** Applied to CV/portfolio design: the top of the page or portfolio site is a compact overview showing ALL key dimensions at once (a dense summary visualization like a heatmap or compact bar chart grid). Below, each section is a "zoom" into a specific domain. A click or scroll reveals "details on demand" for each project, experience, or skill. This is a meta-application of the vis design principle to the CV artifact itself — the CV IS the visualization.
- **Adaptation for our context:** First screen / top third of page: a 4×6 skills heatmap (as above) + a 3-sentence narrative. Second section: project cards for each data science project, each with a small visualization thumbnail. Clicking a card (on digital CV/portfolio) reveals full project details. This structure signals deep understanding of information architecture principles — exactly what an ML6 internship hiring team would look for. Also follows "Get it right in black and white" (p.140): the overview heatmap must be legible when printed in gray.
- **Page reference:** p.135–137, p.140
