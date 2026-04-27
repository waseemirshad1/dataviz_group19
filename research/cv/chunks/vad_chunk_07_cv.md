# [agent_22] Visualization Analysis and Design — pages 301-350

## CV Visualization Ideas
### Target: Psychology + Sales + Software Dev → Data Science | ML6 Internship Belgium

---

### CV Idea: Trellis Career Matrix (p.307-309)

- **What it visualizes:** Skills and experiences partitioned into a 2D matrix — rows = skill domain (Psychology / Sales / Software Dev / Data Science), columns = time period (e.g., education, early career, current) — with a dot or bar within each cell indicating depth/proficiency
- **How it works:** Uses Trellis-style main-effects ordering: domains are ordered top-to-bottom by relevance to ML6 data science role (most relevant = top), and time periods left-to-right. Main-effects ordering makes the growth trajectory visible — skills that grow over time are immediately apparent as upward-trending positions across columns. Outlier skills (e.g., a psychology project that became a data analysis project) are visible as mismatches in the general trend, just as Morris was in the barley data
- **Adaptation for our context:** Each cell shows a small dot/bar for depth; highlight cells that are "data science adjacent" (e.g., experimental design from psychology = statistical rigor; sales = stakeholder communication; software dev = ML pipelines). The matrix immediately communicates: "this person has a structured multi-domain background all pointing toward data science"
- **Page reference:** p.307-309

---

### CV Idea: Coordinated Multiple View Skills Profile (p.301-303)

- **What it visualizes:** Two or three juxtaposed views of the same career data: (1) a timeline view of experiences, (2) a radar/star chart of current skill levels across data science competencies, (3) a brief project list with linked highlighting
- **How it works:** Uses the Improvise-style coordinated multiple view principle (p.302-303): all views share a common color encoding (domain color: psychology=purple, sales=blue, dev=green, ML=orange). When the reader's eye moves to any view, the shared color encoding links the information across views. The timeline shows chronology; the radar shows current state; the project list shows evidence. Together they answer three different hiring questions simultaneously: "What did they do? What can they do now? What have they built?"
- **Adaptation for our context:** Keep it static (print CV) but use color consistently across all three visual elements. The radar chart goes on the right sidebar; timeline goes in the main column; 2-3 highlighted projects with matching color dots appear below. The visual linkage reduces cognitive load for the ML6 recruiter scanning quickly
- **Page reference:** p.301-303

---

### CV Idea: Superimposed Layers Skills Timeline (p.313-317)

- **What it visualizes:** A horizontal timeline with multiple superimposed layers — one per skill domain (psychology/sales/software/data science) — where activity intensity in each domain is shown as a filled area, and the layers are visually distinguishable by hue and luminance
- **How it works:** Uses the static superimposition principle (p.314-315): background layer (soft gray, low saturation) shows education/time base; middle layers show domain activity (psychology: purple, sales: blue, dev: green — all medium saturation); foreground layer (fully saturated, high luminance) shows data science milestones and ML-relevant projects. Luminance contrast ensures each layer is distinguishable even in grayscale (the "Get It Right in Black and White" principle, p.314). The pattern shows a clear convergence trajectory: multiple domains feeding into the foreground data science layer
- **Adaptation for our context:** Keep to 3-4 layers maximum (area marks limit); use filled area marks (wide, low opacity) for each domain activity; use a thin high-saturation line for the data science trajectory overlay as the foreground. Add ML6-relevant milestones as point marks on the top layer
- **Page reference:** p.313-317

---

### CV Idea: Dynamic Query Self-Presentation (FilmFinder Pattern) (p.326-328)

- **What it visualizes:** An interactive digital CV where the reader can filter experiences by skill category (data analysis / ML / client-facing / psychology research) using slider-style controls, seeing only the relevant projects/experiences highlighted in a visual scatterplot (projects plotted by complexity vs. relevance to ML)
- **How it works:** Applies FilmFinder's (p.326-328) dynamic query principle: all experiences shown in overview first; filtering by skill type immediately highlights/enlarges relevant ones; clicking an experience brings up a popup detail card. For an internship application, this format immediately demonstrates interaction design skills and data visualization competency by being the artifact itself. Mark auto-labeling (when only a few experiences remain after filtering) mirrors FilmFinder's behavior
- **Adaptation for our context:** Build as a simple interactive HTML/JavaScript page or Tableau/Observable notebook — appropriate for a data science portfolio link included in the CV header. Scatterplot axes: x = "ML relevance" (self-assessed 1-5), y = "complexity/scope". Filter widgets: checkboxes for domain, dual slider for year range, text filter for technology keywords (Python, R, SQL). Each project = one dot, colored by domain
- **Page reference:** p.326-328

---

### CV Idea: Focus+Context Career Narrative (p.348-350)

- **What it visualizes:** A single-page CV layout where the current role/goal (ML6 data science internship) is the permanent focus in a visually prominent central panel, and all prior experiences are embedded as context using a DOI-style prioritization: closest to the focus goal = larger/more detailed; further away = smaller/summarized
- **How it works:** Applies focus+context embedding (p.348-350): the DOI function is adapted conceptually — interest I(x) = relevance to data science/ML; distance D(x, y) = how far from ML the experience is semantically. High-DOI items (ML projects, data analysis work, statistical research) get full detail (title, description, bullet points, tech stack). Lower-DOI items (pure sales administration, generic software work) are elided to one-line summaries. This focuses recruiter attention without hiding the breadth of background — the contextual elided items still prove the full career arc
- **Adaptation for our context:** Psychology research → show DOI score as "high" (experimental design = statistical methods); sales role → medium DOI (client communication, stakeholder framing of insights); software dev → high DOI (technical foundation). Layout: ML/data science projects in the main column with full detail; psychology/sales/software in a compressed sidebar showing titles only, with brief role descriptors. The visual hierarchy itself communicates "I know what ML6 needs and I've organized this CV to answer that question"
- **Page reference:** p.348-350

---

### CV Idea: Scented Skill Bars (p.328)

- **What it visualizes:** Skill proficiency bars (standard CV component) augmented with data-distribution encoding inside the bar — showing not just "my level" but also the distribution of typical candidates at this level, positioned within the bar background
- **How it works:** Scented widgets (p.328) embed concise statistical graphics inside standard interface controls. Here: each skill bar has a thin background histogram (or gradient) showing where this skill level sits in a reference population (e.g., "advanced Python" sits at the 80th percentile of data science candidates, visualized as a filled region within the bar). This transforms a static "I rate myself 4/5" claim into a contextualized, data-informed signal — exactly the kind of quantitative thinking that ML6 would value
- **Adaptation for our context:** Can be implemented as a simple static graphic: skill bar in foreground (filled to self-assessed level, saturated color), reference distribution as light gray background gradient (wider = more candidates at that level). Add a small label: "Top 20% data science candidates" derived from public survey data (e.g., Stack Overflow Developer Survey). This demonstrates both visualization skill and data literacy simultaneously
- **Page reference:** p.328
