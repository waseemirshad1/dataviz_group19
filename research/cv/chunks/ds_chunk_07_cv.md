# [agent_12] Data Sketches — pages 301-350

## Infographic CV / Visual Resume Ideas

These pages are primarily process-narrative chapters (Culture, Breathing Earth, Community, Myths & Legends intro), not visualization design theory chapters. However, several specific techniques and concepts are directly transferable to an infographic CV context.

---

### CV Idea: "Beeswarm Skills Timeline" (p.338–340)

- **What it visualizes:** Each skill or competency is a dot. The x-axis represents time (years of experience with the skill). Dots for skills in a given domain (psychology, sales, software dev, data science) are grouped vertically by domain category. The above/below split from the "drip and rise" metaphor (p.339) could separate "currently active skills" (rising = being used/growing) from "retired skills" (dripping = used in the past, no longer primary focus). Dot fill vs. outline could indicate formal certification vs. self-taught.
- **How it works:** Use D3 force layout or a simple manual beeswarm to avoid dot overlap. Add a box-and-whisker overlay per domain group showing the median experience level. Color by domain (psychology = one hue, sales = another, data science = another). The reader can see at a glance which domain has the broadest and deepest skill set.
- **Adaptation for our context:** The pivot story is visually encoded: older dots (further right on the time axis) in psychology/sales, newer dots (more to the left) clustering densely in the data science zone. The "rise" above the center for data science skills vs. the "drip" for past roles that are less active makes the career direction narrative implicit and emotionally legible.
- **Page reference:** p.338–340

---

### CV Idea: "Stepper Introduction" — Animated CV Walkthrough (p.310)

- **What it visualizes:** A web-based CV where each section is introduced through a stepper animation — click (or auto-play) through: (1) Education, (2) Work Experience, (3) Skills, (4) Projects, (5) "Where I'm going." Each step adds one visual layer to a central layout, so the reader sees the full picture only after the complete reveal.
- **How it works:** Use the stepper technique (p.310): auto-play the sequence, but allow clicking any step indicator to replay from that point. This keeps all content in a single compact space rather than requiring scrolling. Transitions (Greensock-style) animate new elements in as each step is clicked.
- **Adaptation for our context:** Step 1 shows a timeline backbone (years). Step 2 adds education blocks. Step 3 adds work experience blocks on the same timeline. Step 4 animates skill icons or dots appearing, clustered by type. Step 5 highlights the pivot: a color shift or growing cluster of data science skills, making the direction of change visually obvious.
- **Page reference:** p.310

---

### CV Idea: "Arc Timeline" — Career Direction by Year (p.305–307)

- **What it visualizes:** A personal version of the arc timeline (p.305). Each year of the career is a circle on a horizontal axis. An arc above the axis = a year where data-science-oriented activity increased (new skills learned, more technical projects). An arc below = a year dominated by psychology/sales work (the past trajectory). The shape of the arc encodes magnitude of that year's growth in the target direction.
- **How it works:** The x-axis is chronological (years). Each year-circle is positioned by the cumulative "data science orientation score" (self-assessed or based on projects/courses completed that year). The arc direction (up = moving toward data science, down = moving away) tells the growth story at a glance.
- **Adaptation for our context:** This encodes the pivot narrative as a clear directional trend: early years show arcs pointing mostly downward (in the psychology/sales zone), with a clear inflection point where arcs start rising consistently. The reader sees not just "I pivoted" but "here's exactly when and how steeply." Annotate the inflection point with a label (e.g., "Started ML coursework," "First data project").
- **Page reference:** p.305–307

---

### CV Idea: "Visual Metaphor Growth Chart" — Skills That Rise and Fall (p.339)

- **What it visualizes:** Skills are represented as dots. Those that are growing/current "rise" above a central axis (like bubbles floating up). Skills that were part of a past career phase "sink" below the axis (like settling sediment). The central axis is labeled "pivot point" — the career transition moment.
- **How it works:** The vertical metaphor (p.339 — frustrations drip down, satisfaction rises up) is repurposed: past-career skills (clinical psychology methods, sales techniques) hang below; target-career skills (ML, Python, data visualization, SQL) float above. X-axis could encode proficiency level. Color encodes domain.
- **Adaptation for our context:** Makes the dual identity (psychology background + data science aspirant) visually legible without words. The recruiter immediately sees the bridge: some skills (statistics, research methods, understanding human behavior) are encoded as skills rising from the psychology zone into the data science zone — the transferable skills.
- **Page reference:** p.339

---

### CV Idea: "Seasonal Block" — Activity Density per Role (p.305–306)

- **What it visualizes:** Each job/role is a column. Within each column, blocks represent activities/responsibilities. Block height = time spent on that activity (estimated %). Color = type of activity (technical, communication, analytical, management). The overall height of each column = years in the role.
- **How it works:** The key insight from p.305 is that encoding height (not just presence) reveals patterns. Applied to a CV: the activity block chart shows not just "what I did" but "how much of my time each activity took." A recruiter can see at a glance that the data science internship role had tall "analytical" and "technical" blocks, while the sales role had tall "communication" blocks — and the applicant is deliberately building toward the former.
- **Adaptation for our context:** Group columns left to right chronologically. Use a consistent color legend for activity types. The shift in block color profile from left (sales/psych colors dominate) to right (technical/analytical colors dominate) tells the pivot story visually without a single word.
- **Page reference:** p.305–306
