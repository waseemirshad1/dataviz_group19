# [agent_21] Visualization Analysis and Design — pages 251-300

---

### CV Idea: Diverging Skill Bar Chart — Comfort vs Aspiration (p.255–256)

- **What it visualizes:** Technical and soft skills, encoded as a diverging bar chart centered on a neutral midpoint. Left direction = current proficiency; right direction = aspiration/growth direction. The diverging center (neutral) makes skills "in progress" visually distinct from both mastered skills and unexplored ones.
- **How it works:** Each skill is a row. Left bars extend toward "current proficiency" (blue hue with increasing luminance toward mastery); right bars extend toward "target proficiency" (orange/warm hue with increasing luminance toward high aspiration). The gap between left and right bar length encodes the growth potential visually. A monotonically increasing luminance design (p.258) ensures fine discrimination between proficiency levels without the rainbow problem.
- **Adaptation for our context:** Skills: Python, R, SQL, Machine Learning, Statistics, Data Visualization, Excel/Business Tools, Communication, Client-facing Sales, Software Development. The psychology background appears as a unique skill cluster (soft skills, behavioral understanding, survey design) positioned distinctly from technical skills — making the interdisciplinary bridge to data science visible. Aspiration bars point toward ML6 internship requirements.
- **Page reference:** p.255–258 (diverging + monotonic luminance colormaps)

---

### CV Idea: Timeline as Slope Graph — Career Trajectory Showing Shift from Sales/Psychology to Data Science (p.272)

- **What it visualizes:** Career stages as ranked positions along multiple attribute axes (role type, technical depth, people-focus, analytical depth) shown across time. The slope graph shows how each attribute's rank shifted between key career periods.
- **How it works:** Columns = career stages (Psychology degree → Sales role → Software development → Current/ML6 target). Rows/lines = attributes (technical depth, human insight, analytical rigor, client interaction). Lines connecting same attribute across stages reveal where the trajectory bends: technical depth rises sharply; sales/client interaction stays high; human insight (psychology background) remains a differentiator.
- **Adaptation for our context:** Steep upward slopes in technical depth and data science skills make the growth narrative visible at a glance. Flat lines for communication and people skills show persistent strengths. The combined trajectory tells the story: "I bring the human side that pure data scientists lack." The crossing lines where technical depth overtakes the previous dominance of client-facing work make the career pivot the visual focal point — the exact structure that makes slope graphs compelling (p.272).
- **Page reference:** p.272 (slope graphs / bump charts, LineUp example)

---

### CV Idea: Small Multiples of Experience Facets — Same Role Seen Through 3 Lenses (p.298–299)

- **What it visualizes:** Each job/project is shown three times in small multiples — once for technical skills applied, once for soft skills/impact, once for data science relevance. The shared position axis (same job order across all three panels) enables immediate comparison.
- **How it works:** Three aligned panels (columns). Each row = one role or project. Panel 1: technical skills bar (what tools/methods were used). Panel 2: impact bar (client reach, revenue, team size, user impact). Panel 3: data science relevance bar (how directly this feeds into the ML6/data science target). Same ordering across all three panels = Eyes Beat Memory benefit (p.291) — the viewer glances left-right rather than memorizing.
- **Adaptation for our context:** The third panel (data science relevance) reframes seemingly unrelated experiences (sales, psychology) as valuable: customer behavior pattern analysis in sales = feature engineering mindset; experimental psychology = hypothesis-driven methodology; software development = production code awareness. The small multiples format prevents the "so what?" reaction by making the relevance column immediately adjacent to the experience description.
- **Page reference:** p.298–299 (small multiples), p.291 (Eyes Beat Memory — simultaneous vs sequential)

---

### CV Idea: Linked Highlighting CV — Hover Skill, See Experiences Light Up (p.292–294)

- **What it visualizes:** A static CV layout with an interactive layer: hovering over any skill in the skills section highlights all experiences/projects where that skill was applied. Hovering an experience highlights all skills it involved.
- **How it works:** Implemented as a web-based CV. Skill tags and experience entries share a categorical color channel (skill category: ML, visualization, statistics, communication, domain knowledge). Linked highlighting across sections shows the skill–experience mapping without requiring a separate matrix view — the existing layout becomes a multi-view system (p.293).
- **Adaptation for our context:** The psychology degree and sales background become visually connected to "human factors," "behavioral analytics," and "client communication" skill tags. The software development experience connects to "production code" and "deployment" tags. The ML6 internship section lists required skills; highlighting shows exactly which existing experiences cover each requirement — making the match argument visual and interactive.
- **Page reference:** p.292–294 (linked highlighting / multiform views, EDV example)

---

### CV Idea: Overview–Detail Career Narrative — Bird's-Eye Timeline + Drill-Down per Role (p.295–296)

- **What it visualizes:** A compact timeline overview of the full career arc (bird's-eye view) paired with a detail panel that expands on click to show the full context of any selected role/project.
- **How it works:** Overview: small horizontal timeline with colored markers for each role, clustered visually by domain (psychology, sales, software, data). Detail: clicking any marker opens a fixed panel showing full role description, skills, achievements, relevance to data science. The overview rectangle metaphor (p.295) is applied as a "currently selected" highlight on the timeline.
- **Adaptation for our context:** The timeline overview gives the recruiter an immediate sense of trajectory and recency without overwhelming detail. The detail-on-demand design means the full narrative of the psychology degree and its relevance to ML6 is available but not forced on the viewer. Bidirectional linking: the detail panel also contains tags that, when clicked, highlight all roles involving the same skill on the timeline overview.
- **Page reference:** p.295–296 (Bird's-Eye Maps / overview-detail)

---

### CV Idea: Animated Transition Between CV "Modes" — Technical vs Business Persona (p.273–274)

- **What it visualizes:** A single-page CV that smoothly transitions between a "data scientist" framing and a "business/sales" framing of the same experiences — same layout, different emphasis. An animated transition shows how the same skills and experiences are re-framed for different audiences.
- **How it works:** Two states share the same layout structure (items stay in place). Toggling a "mode" button triggers an animated transition: bar charts resize (technical depth vs business impact); color coding shifts; some text labels change emphasis. Because the items stay in position and only their visual encoding changes, the transition is legible and maintains context (p.273–274 — animated transitions work best when groups of objects move together or a small number of properties change).
- **Adaptation for our context:** ML6 target: toggle to "data scientist" mode — ML, Python, statistics bars grow; sales bars shrink. Other recruiters: toggle to "hybrid analyst" mode — communication, domain knowledge, sales analytics bars come to the front. The animation itself demonstrates data visualization competence, which is directly relevant for a data science role at ML6.
- **Page reference:** p.273–274 (animated transitions — when and how to use them effectively)
