# [agent_14] Data Sketches — pages 401-428

## Overview of Pages 401–428

Pages 401–428 cover two major projects — "An Ode to Cardcaptor Sakura" (pp. 401–404) and "One Amongst Many" (pp. 406–421) — followed by a lessons index (pp. 423–424), a closing interview with Tamara Munzner (pp. 425–426), and acknowledgments (pp. 427–428). The data visualization knowledge is concentrated in the two projects and the curated lessons index.

---

## Interaction Design

### Hover-Reveal as a Primary Interaction Pattern (pp. 402–404)
- The Cardcaptor Sakura visualization uses hover to progressively reveal information. Hovering over a character reveals only the chapters they appeared in — reducing clutter while maintaining full data availability (p. 402)
- Hovering over a chapter "pill" in the outer ring shows all characters in that chapter — bidirectional filtering from either dimension (p. 402)
- Hovering over "relationship lines" in the inner structure triggers a small annotation with additional detail (p. 403)
- Key principle: **hover-reveal reduces visual noise at rest while supporting exploration on demand** — the default state is clean, the detailed state is accessible

### Dual-Direction Interaction (pp. 402–403)
- Users can explore from either dimension (character → chapters, or chapter → characters)
- This bidirectional approach lets different users follow different mental models — "who was in this chapter?" vs "which chapters did this character appear in?"
- Rule of thumb: when data has two categorical dimensions, support interaction from both sides

### Annotation as On-Demand Detail (pp. 403–404)
- Relationship lines in the inner circle carry annotation popups with contextual text (p. 403)
- The outer ring's CMYK dotted circles encode color palette of cover art; hovering reveals character presence on that cover (p. 404)
- **Anti-pattern avoided:** not showing all annotations at once — that would overwhelm; instead annotations appear only on hover

---

## Visual Metaphor and Data Mapping

### Metaphor-Driven Design (pp. 408–410)
- In "One Amongst Many," the physical orbs start dimmed and brighten as visitors interact with them — a metaphor for the invisibility of women in computing whose contributions become "illuminated" through attention (p. 410)
- The y-axis encodes "renown" (number of Wikipedia backlinks): more renowned women hang higher — metaphorically "out of reach" — while lesser-known women are lower and more accessible for readers (p. 408)
- The z-axis (depth of installation) encodes time — year of accomplishment — so visitors physically walk through history (p. 408)
- **Rule of thumb:** when physical or spatial dimensions are available, mapping data to them creates embodied understanding that pure screen visualization cannot

### Choosing Metaphor Before Channel (p. 408)
- The team began with the desired *feeling* ("highlighting invisibility") and worked backward to technical solutions — not the other way around
- The dimmed-to-bright lighting metaphor arose from the conceptual goal, not from a list of possible visual channels

---

## Color as Channel

### Difficulty of Color Discrimination (p. 410)
- When the team wanted to map data to color of lights, they found it nearly impossible to distinguish colors from each other unless they were very different (e.g., red, blue, green)
- They retained RGB Neopixels for control convenience but dropped the color-encoding idea
- **Rule of thumb confirming theory:** color hue is useful for categorical distinction only when hues are strongly separated; subtle hue variation fails as an encoding channel in practice

---

## Design Process Guidance

### Sketch Early with Cheap Materials (pp. 408–413)
- The team physically prototyped orbs using fillable Christmas ornaments, spray paint, cellophane, and vellum before committing to final materials (pp. 411–413)
- Rapid cheap prototyping revealed that: (1) reflective spray paint doesn't work on plastic, (2) peepholes were too small for comfortable reading, (3) cellophane with backlight created a beautiful frosted effect (p. 413)
- **Rule of thumb:** always prototype with cheap stand-ins before committing to expensive or irreversible materials or code — the lesson applies equally to digital mockups before coding

### Incremental Complexity in Code (pp. 414–415)
- When coding the Arduino system, the author first used a simple button and LED (familiar tools) to validate the interaction logic, then swapped in the actual tilt sensor and Neopixel (p. 414)
- **Design principle:** prototype the logic with familiar tools before introducing the real components — isolate variables in development

### Constraints as Creativity Enablers (p. 426)
- Tamara Munzner's interview reveals the advice: "placing constraints on how you approach your work ... sometimes constraints can actually make you more creative" (p. 426)
- Example constraint suggested: "whatever we made after 20 hours, we'd use"

---

## Storytelling and End-User Focus

### Shift from Technical to User-Centered Design (p. 425)
- Shirley Wu explicitly describes growth from "focus on fun" to "the end user is extremely important" (p. 425)
- Key realization: the end user's ability to read and understand the visualization is critical; don't do something "just for the technical fun of it" (p. 425)
- **Rule of thumb:** always ask "what does the reader/visitor need to understand?" before choosing a technique

### Narrative Arc in Multi-Visual Projects (p. 425)
- Nadieh Bremer learned that making an entire dataviz-driven story is "more than just the visuals and the layout; you must be able to design for multiple visuals and make them flow together" (p. 425)

---

## Physical / Spatial Encoding (unique to this chunk)

### Three Spatial Axes as Channels (p. 408)
- z-axis = time (year of accomplishment) — visitors physically walk through history
- y-axis = renown (backlink count) — higher = more famous, literally further from reach
- Object identity = individual woman — each orb is one data point
- **Interesting property:** physical installation allows embodied interaction impossible in screen-based visualization — picking up an orb is a genuinely different affordance from clicking

### Grouped Interaction with Staggered Delay (pp. 415–416)
- Women were grouped into four categories; interacting with one orb caused the others in its group to light up with a staggered delay (p. 415)
- The delay communicates group membership without labels — a temporal/spatial encoding of categorical relationship
- **Rule of thumb:** staggered animation can communicate grouping and relationships without adding marks or labels

---

## Annotations Are of Vital Importance (p. 424 — Lessons Index)

The lessons index (pp. 423–424) confirms "Annotations Are of Vital Importance" as a named lesson, attributed to Myths & Legends (Nadieh, p. 362). This reinforces the use of in-context annotation as a key dataviz principle throughout the book.

---

## Common Mistakes and Anti-Patterns

- **Color-encoding with subtle hues:** color hue as channel only works with strongly separated categories — rejected in practice (p. 410)
- **Peephole interaction:** requiring users to peer through a small hole to read content is too demanding — rejected after prototype testing (p. 412)
- **Over-engineering sensors:** complex mechanical solutions (pulley systems, motors) are fragile with real users; simpler solutions (tilt sensor + light) are more robust (p. 410)
- **Explaining process instead of reasoning:** bookification challenge — just showing screenshots without explaining *why* decisions were made is insufficient for teaching (p. 425)

---

## Lessons Index Summary (pp. 423–424)

The book concludes with a curated index of named lessons across all chapters. Relevant categories include:

- **Data:** Check accuracy/completeness; explore by asking questions; manually add new variables
- **Sketch:** Add context using remaining visual channels; design to maximize delight; sketch to discover and remove thinking errors; use visual metaphors
- **Code:** Annotations are vital; combine tools; precalculate visual variables; use trigonometry; custom animations; marks and channels
- **Design:** Design with code; remix what's out there; scales in D3.js

The "Marks and Channels" lesson is explicitly indexed, attributed to Movies (Shirley, p. 47) — confirming it as a named, teachable principle within the book.
