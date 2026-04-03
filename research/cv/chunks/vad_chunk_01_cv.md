# [agent_16] Visualization Analysis and Design — pages 1-50

## CV Visualization Ideas
### Target: Psychology + sales + software dev → data science (internship at ML6 Belgium)
### Goal: Visualize degrees, skills, experience, growth over time, traits

---

## Theoretical basis from pages 1-50

Relevant principles for designing a visual CV:

- **External representation principle (p.6)**: A visual CV offloads the cognitive work of pattern recognition from the reader to the perceptual system. A recruiter scanning dozens of CVs benefits from visual encoding that supports rapid recognition of structure (skills, growth, trajectory).
- **Anscombe's Quartet principle (p.7–8)**: A standard plain-text CV is like a statistical summary — it hides the shape of the story. A visual CV reveals structure that a list of bullet points obscures: the shape of a career transition, the acceleration of skill acquisition, the density of experience in a domain.
- **Task design principle (p.9, p.44–46)**: A recruiter's task is compare (screening: is this person better than others for this role?) and identify (what specific qualifications does this person have?). The visual design must support both tasks rapidly.
- **Present goal (p.46–47)**: A CV is a presentation artifact — the designer (applicant) communicates already-known information to an audience (recruiter/hiring manager). This means the design can be highly intentional and guided; it does not need to support open-ended exploration.
- **Derive principle (p.50–53)**: Don't just list what happened — derive attributes that make the argument. Derive: years of experience per domain, skill coverage overlap (psychology × data science × sales), growth rate in technical skills, progression from student to practitioner.
- **Information density (p.15–16)**: A CV has severe space constraints (one page typical). High information density with spatial organization is a design goal. Figure 1.6 example: compact layout that still encodes depth via position.

---

### CV Idea 1: Career Transition Timeline as a River Diagram (p.7–8, p.46–47)

- **What it visualizes:** The full career arc from psychology → sales → software development → data science; time on the x-axis; domains as stacked or flowing bands; ML6 internship as the current destination
- **How it works:** Horizontal time axis (left = start of studies, right = now); each major domain or role is a colored band whose width encodes time invested; bands narrow and merge as the career converges toward data science; the ML6 internship appears at the rightmost tip as the current focus
- **Adaptation for our context:** Colors encode domain: psychology (warm), sales (gold), software (blue), data science (deep blue/purple); skill acquisition events are marked as dots on the timeline; educational milestones (degrees) are shown as labeled vertical markers; the visual narrative is: "All streams feed into data science"
- **Page reference:** p.46–47 (present goal — guided narrative of a known story), p.7–8 (Anscombe — show structure that a bullet list hides)

---

### CV Idea 2: Skills Radar Chart / Profile (p.52, p.57)

- **What it visualizes:** A multidimensional skills profile showing competence across 6–8 domains (psychology, statistics, machine learning, software engineering, sales/communication, domain knowledge, visualization)
- **How it works:** Spider/radar chart with one axis per skill domain; the filled area shows current competence level; a second lighter overlay shows typical entry-level data scientist baseline for comparison; the gap between the two profiles highlights unique strengths
- **Adaptation for our context:** Psychology and communication axes will be visually larger than typical data science candidates — this asymmetry is the argument: "I bring skills ML6 candidates rarely have." The radar chart encodes this claim directly in position and area. Label psychology and sales axes with specific examples (e.g., "behavioral research methods", "B2B client relationships").
- **Page reference:** p.52 (directly encode the derived comparison — not "I have psychology skills" but "my skill profile compared to a baseline shows these specific advantages"), p.57 (the How framework — map channels to attribute types)

---

### CV Idea 3: Experience Density Heatmap (p.15–16, p.50)

- **What it visualizes:** A compact matrix showing time periods (columns = months or semesters) × activity types (rows = education, technical projects, sales experience, research, extracurricular); color intensity = degree of engagement/relevance
- **How it works:** Each cell is colored by intensity of activity: dark = heavy involvement, light = peripheral. The matrix is ordered chronologically (left = past, right = present). A cluster of high-intensity cells in the right columns (recent technical/data science activities) shows accelerating focus shift.
- **Adaptation for our context:** Rows could be: Coursework, Programming projects, Sales/client work, Research/psychology, Visualization/ML. Color palette: single hue (blue) with saturation for quantitative intensity — easy to scan. This works as a compact "at a glance" summary at the top of a CV, followed by conventional text detail below.
- **Page reference:** p.15–16 (information density — maximize information per pixel within space constraints), p.50 (derive principle — intensity is a derived attribute computed from raw activity data)

---

### CV Idea 4: The Growth Trajectory Scatterplot — Skills Over Time (p.8, p.52)

- **What it visualizes:** Each skill or technology is a point; x-axis = when first acquired (timeline); y-axis = current proficiency level; size = depth of use (projects, months); color = domain (psychology/stats/code/sales)
- **How it works:** The scatterplot layout reveals the shape of skill acquisition: many psychology skills on the left (early, high proficiency), sales skills in the middle, a wave of technical/data science skills on the right (recent, increasing proficiency). This shows both breadth (many points) and trajectory (recent cluster of technical skills with growing proficiency).
- **Adaptation for our context:** Annotate specific skills relevant to ML6 (Python, machine learning frameworks, data wrangling, statistics) with labels. The fact that psychology and statistics skills appear at high proficiency on the left while technical skills are growing rapidly on the right tells a story: "I'm not starting from zero — I'm completing a deliberate transition."
- **Page reference:** p.8 (Anscombe — showing detail reveals structure; a list of skills on a CV is like summary statistics — it hides the shape of acquisition), p.52 (derive and encode the story directly)

---

### CV Idea 5: The "What I Bring" Glyph — A Single Infographic Summary (p.6, p.46–47)

- **What it visualizes:** A single compact visual combining: a small timeline (career path), a skills profile (bar or radar), one or two achievement highlights (quantified outcomes), and a "fit for ML6" callout
- **How it works:** Inspired by the external representation principle (p.6): one image that spatially organizes all the key facts so a recruiter can form an impression in seconds. Layout: left third = timeline/career arc; center = skills profile; right third = key achievements + ML6 alignment. Each section uses its own visual encoding but they share a color scheme for coherence.
- **Adaptation for our context:** The visual is designed to be placed at the top of a one-page CV as a header; the conventional text below provides detail. The visual's job is the present task: communicate the core argument immediately. The argument: "Unusual background (psychology + sales + code) = unusual value for ML6's applied ML work."
- **Page reference:** p.6 (external representations speed recognition and search by spatial organization), p.46–47 (present goal — the designer knows the message; the design delivers it efficiently)

