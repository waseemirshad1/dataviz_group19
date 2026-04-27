# [agent_23] Visualization Analysis and Design — pages 351-400

## CV Visualization Ideas

Target context: Psychology + sales + software development background → data science career transition. Applying for ML6 internship in Belgium. Goal: make the CV visually distinctive, readable, and demonstrate data visualization competence without sacrificing ATS scannability.

---

### CV Idea: Skills Relevance Spiral (p. 347–350)

- **What it visualizes:** All skills and competencies arranged in a spiral from center outward, where radial position encodes relevance to a specific target role (e.g., ML6 data science internship). Skills closest to the center are most relevant.
- **How it works:** Each skill is a colored square or circle; color encodes category (psychology/behavioral skills = one hue, software/technical skills = another, sales/communication = a third). The spiral layout is inspired by VisDB's spiral ordering, which allows a large number of items to be read as a continuous gradient while also being visually memorable. Items at the center are immediately readable; peripheral items naturally recede.
- **Adaptation for our context:** The "query" is the job description. The relevance score for each skill is computed (manually or with a keyword match) from the job posting. The resulting spiral makes it immediately obvious that the candidate has positioned themselves around the exact skills the employer is seeking, with visually distinct categories showing the interdisciplinary background.
- **Page reference:** p. 347–350

---

### CV Idea: Career Timeline as Stretch-and-Squish Navigation (p. 356–358)

- **What it visualizes:** A career timeline where the most recent and most relevant experience is "stretched" (shown large and detailed) and older or less relevant experience is "squished" (shown compressed but still visible).
- **How it works:** Inspired by TreeJuxtaposer's rubber-sheet metaphor. The timeline runs horizontally; the current/target roles have full-width detail blocks (job title, key achievements, skills used). Earlier roles from psychology or sales compress to narrow blocks with only a title and one-line summary. Guaranteed visibility ensures that even the oldest experience never disappears — consistent with the principle that all items remain within the viewport.
- **Adaptation for our context:** The ML6 internship application benefits from emphasizing recent software development and data science work prominently, while still acknowledging the psychology and sales history (which provides differentiated soft skills). The visual compression signals intentionality: the candidate has curated, not hidden, their background.
- **Page reference:** p. 356–358

---

### CV Idea: Competency PivotGraph — Skills by Category × Proficiency (p. 355–358)

- **What it visualizes:** An aggregate node-link diagram where skills are grouped by two categorical attributes: (1) domain category (psychology/behavioral, technical/ML, sales/communication, domain knowledge) and (2) proficiency level (beginner, intermediate, advanced). Each aggregate node shows the count of skills in that group; link width shows how many skills bridge two categories (cross-domain skills).
- **How it works:** Each skill is a "node" in an underlying network. The PivotGraph roll-up creates a compact 4×3 grid of aggregate nodes. Cross-category links are especially interesting: a skill like "presenting data insights to non-technical stakeholders" spans both the psychology and the communication categories — shown as a wide link. Node size encodes skill count; an additional color encodes relevance to the target role (diverging: blue=less relevant, red=highly relevant).
- **Adaptation for our context:** A PivotGraph of skills is unusual and shows mastery of data visualization concepts directly in the CV. For ML6, which specifically values bridging technical and business communication, the cross-category links become a key visual argument: this candidate has skills that span the technical-human divide. The visual can fit in a single side panel (~1/4 page width).
- **Page reference:** p. 355–358

---

### CV Idea: Scagnostics-Inspired "Profile Fingerprint" — 9 Measures of Professional Shape (p. 342–345)

- **What it visualizes:** Nine radar/rose chart axes, each corresponding to one "scagnostics-like" professional measure: e.g., Technical Depth, Human Insight (psychology), Communication Breadth, Learning Velocity, Cross-Domain Span, Independence, Collaborative Style, Data Fluency, Business Acumen. The resulting shape is a fingerprint of the candidate's professional profile.
- **How it works:** Each axis is scored 0–10 based on the CV evidence. The resulting polygon is the "profile shape." A second light polygon shows the ideal ML6 intern profile (derived from the job description). The overlap and gaps between the two shapes immediately communicate fit and growth potential.
- **Adaptation for our context:** The psychology background scores high on Human Insight and Communication Breadth. Software development scores high on Technical Depth and Data Fluency. Sales scores high on Business Acumen. The composite shape is distinctive and multi-dimensional — not a standard "skills bar chart." The gap between the two polygons (candidate vs. ideal) can be framed as learning agenda items in the cover letter.
- **Page reference:** p. 342–345

---

### CV Idea: Three-Level Semantic Zoom Career Narrative (p. 363–366)

- **What it visualizes:** A CV that exists at three zoom levels: (1) one-page overview showing only roles + years + one headline metric per role; (2) intermediate level showing key projects and skills per role; (3) full detail level with specific achievements, technologies, and measurable impact.
- **How it works:** Inspired by Constellation's semantic zooming across three levels. At each level, space allocation shifts: the current/most relevant role always gets more space. At the overview level, the horizontal axis encodes career progression (left=start, right=now) and vertical space allocation reflects role relevance to the target position. At deeper zoom levels, space becomes more equal as all content deserves equal reading attention.
- **Adaptation for our context:** Practically, this could be implemented as a three-page CV where page 1 is the overview, page 2 expands the two most relevant roles, and page 3 (portfolio link or appendix) contains full project details. For an ML6 application, the data science/software work fills the expanded level, while psychology and sales compress gracefully to supporting evidence at the overview level. The visual metaphor itself signals systematic thinking — a valuable signal for a data science candidate.
- **Page reference:** p. 363–366
