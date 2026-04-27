# [agent_18] Visualization Analysis and Design — pages 101-150

## CV Visualization Ideas

Context: Psychology + sales + software development background → transitioning to data science. Target: ML6 internship, Belgium.

---

### CV Idea: Skill Channel Rankings Bar Chart (p. 101–102)

- **What it visualizes:** A personal "channel effectiveness ranking" — skills and competencies ordered by their effectiveness/relevance for the target data science role, directly mirroring Figure 5.6's ranked channel list.
- **How it works:** Horizontal bars (using aligned position — highest accuracy magnitude channel per p. 101) show self-assessed proficiency or relevance of each skill. Skills grouped into two categories analogous to the book's magnitude/identity split: "Technical skills" (quantitative — length/bar) and "Soft skills" (categorical — color hue grouping). The most relevant skills for ML6 appear at the top, following the effectiveness principle that important attributes should use the most salient channels (p. 101).
- **Adaptation for our context:** Order bars from top to bottom: Python/ML → Data Visualization → Statistics → Psychology Research → Sales Communication → Software Dev. Use two color hue categories: technical (one hue) vs. interpersonal (another hue). The visual design itself demonstrates knowledge of the channel rankings principle — a meta-message to an ML6 interviewer.
- **Page reference:** p. 101–102

---

### CV Idea: Career Trajectory Scatterplot — Experience × Relevance (p. 146–148)

- **What it visualizes:** Past experiences/roles plotted as points where x-axis = time (years in role) and y-axis = relevance to data science. Each point = one experience/role. Size = impact/responsibility level. Color hue = domain (psychology / sales / software / data projects).
- **How it works:** Uses the scatterplot idiom to show correlation between duration and relevance — demonstrating that the trajectory leads upward to data science. A regression-line-style arrow from bottom-left (early roles, lower relevance) to top-right (recent projects, high relevance) makes the intentionality of the career pivot explicit. Directly applies the principle that scatterplots are excellent for showing trends and correlation (p. 147).
- **Adaptation for our context:** X-axis: duration or year of each role. Y-axis: subjective "relevance to ML/data science" score (1–10). Points: Psychology internship, sales role, software dev projects, data science coursework, datathon projects. Color hue: domain category (4 categories — within discriminability limits p. 106). Size: team/project scope. The narrative of career pivot is encoded in the upward-right trend.
- **Page reference:** p. 146–148 (scatterplot design, regression overlay as narrative device)

---

### CV Idea: Popout-Highlighted Unique Competency Map (p. 109–111)

- **What it visualizes:** A competency overview where unique cross-domain skills (psychology + tech + sales) are made to pop out from a background of standard data science candidate skills, using single-channel size or color popout.
- **How it works:** A dot grid or bubble layout where most competencies are shown as small neutral-colored dots (standard data science skills), but the unique intersections (e.g., user research + ML, persuasive communication + data storytelling, behavioral psychology + model interpretability) are shown as large or distinctly colored dots — exploiting visual popout (p. 109). The popout draws the recruiter's eye immediately to what differentiates this candidate, without requiring serial reading of a skill list.
- **Adaptation for our context:** Group dots by category (technical, domain, communication). Make the 3–4 unique intersection skills pop out via size increase (large dot = uncommon combination). Use a single channel only (size) to ensure clean popout per the rule on p. 110. Label only the popped-out dots. Remaining dots serve as contrast background. Works in black and white (size survives grayscale — per Rule 7, p. 140).
- **Page reference:** p. 109–111 (single-channel popout design rule)

---

### CV Idea: Linked Overview + Detail Timeline (p. 135–137)

- **What it visualizes:** Career timeline as a two-level linked view: an overview bar (all roles across time, color-coded by domain) + a detail panel that expands the selected period with specific achievements, tools used, and skills developed.
- **How it works:** Directly applies Shneiderman's "Overview First, Zoom and Filter, Details on Demand" mantra (p. 135). The overview timeline gives the full career arc at a glance (the summary level). Clicking a period expands the detail panel below showing relevant projects, technologies, and data science connections. In a static CV this becomes a two-section layout: compact timeline strip at top + detailed sections below that are spatially linked by alignment.
- **Adaptation for our context:** Top strip: horizontal timeline bar from first role to present, color hue = domain (psychology/sales/dev/data science). Below: for each selected period, bullet points with key achievements. The top strip functions as an overview that immediately shows the breadth and intentionality of the career arc. The aligned layout (common horizontal time axis) uses the highest-accuracy position channel for time comparisons (p. 102).
- **Page reference:** p. 135–137 (Overview First, Zoom and Filter, Details on Demand)

---

### CV Idea: Separability-Tested Skill Heatmap (p. 106–108)

- **What it visualizes:** Skills vs. project/role matrix (heatmap), where cell color saturation shows depth of experience and the row/column ordering groups related skills and roles together.
- **How it works:** Uses the heatmap idiom (2 keys + 1 value, p. 146) where rows = skill categories (statistics, programming, visualization, behavioral research, communication) and columns = roles/projects. Cell color saturation encodes depth of use (light = basic exposure, dark = primary tool). Applies the separability principle (p. 107): position channels (row/column structure) carry categorical identity, while color saturation carries the ordered magnitude of experience depth — a separable pair.
- **Adaptation for our context:** Rows: Python, R, ML algorithms, data viz, user research, sales analytics, statistical analysis. Columns: psychology thesis, sales role, software projects, data visualization course, datathon. Color saturation: 4 levels (none / basic / proficient / expert). The heatmap shows at a glance which skills were used across multiple contexts (wide horizontal coverage = transferable skill) and which are deep specializations (dark color = mastery). ML6 can see immediately which data science skills are broad and which are deep.
- **Page reference:** p. 106–108 (discriminability — 4 saturation levels within bin limit; separability — position + saturation are separable channels)

---

### CV Idea: Function First, Form Next — Anti-decoration Principle as Design Statement (p. 140–141)

- **What it visualizes:** Not a specific chart type but a design philosophy demonstrated through the CV layout itself: clean, information-dense, no decorative chartjunk.
- **How it works:** Apply Rule 8 (Function First, Form Next, p. 140–141) as a deliberate visible constraint: every visual element on the CV encodes information (no decorative bars, no skill circle-meters, no decorative icons that add no data). The contrast with most visual CVs (which use decoration extensively but encode little) is itself a signal to a data science recruiter that the candidate understands the difference between informative and decorative visual elements. Works in black and white (Rule 7, p. 140).
- **Adaptation for our context:** Use bar charts (not progress circle arcs — circles violate accuracy because angle perception is less accurate than aligned position, p. 101) for skill levels. Use a clean timeline (horizontal position for time, the most accurate channel). Use color hue sparingly for categorical grouping only (not decoration). Add a small caption: "This CV is designed using the principles from Munzner's Visualization Analysis and Design — function before form" — a direct signal to ML6 that visualization knowledge is applied, not just claimed.
- **Page reference:** p. 140–141 (Function First, Form Next), p. 140 (Get It Right in Black and White)
