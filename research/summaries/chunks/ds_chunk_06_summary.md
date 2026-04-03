# [agent_11] Data Sketches — pages 251-300

## Overview of Content
Pages 251–300 cover three projects: "Marble Butterflies" (Nadieh, generative art with butterfly data), "Send Me Love" (Shirley, SFMOMA text messages), and "Beautiful in English" (Nadieh, Google Translate word frequency data). The culture section introduces a fourth project ("Explore/Adventure" by Shirley, Google Trends travel data) starting at p.298. The pages are rich in design process guidance, interaction design, coding reflections, and practical rules of thumb.

---

## Design Process Guidance

### Sketch to Discover and Remove Thinking Errors (p.284)
- Sketching before coding reveals logical/mathematical flaws early — if you can't make the design work on paper, it definitely won't work in code with actual data.
- Iterative sketching allows rapid exploration of alternatives: the author pivoted from a "natural swirl" concept to "beads on a string" after realising the swirl was not mathematically realisable in a responsive layout.
- Keep a mood board (e.g., Pinterest) to collect visual inspiration before starting — even a "secret" personal one is valuable (p.283).
- Sketch not just the visual concept but also the math: place arrows, paths, and angles on paper to work out trigonometric formulas before coding (p.283–284).

### Designing with Code (p.257)
- When a sketch cannot capture the intended delicateness or nuance of a visual, go straight to code to explore — especially for generative/animated work.
- Iterate by keeping parts that look good and discarding what doesn't; treat the code as a design medium itself.
- Looking at other people's work (generative artists, demos) is a legitimate design step; inspiration from external examples often unlocks the solution (p.253–255).

### "Start at the Top and Provide More Detail" Hierarchy (p.282–283)
- Layer complexity progressively: overview first (the single most translated word), then per-language summary (tree ring), then cross-language similarity (network), then time dimension (bump chart).
- Each new visual answers a deeper question than the previous.

### Managing Visual Busyness (p.289–290, p.286)
- Replacing connecting lines with words in a network caused chaos — words overlapped and the visual became unreadable (p.290).
- Solution: revert to lines, keep only the central English translation word on each link — maximum signal, minimum noise.
- Alberto Cairo's advice: "make it even more minimal and only keep the central dark word on the line to really get the focus" (p.290).
- When animation is too busy or staggered, try a different approach: rotating text out/in rather than physically moving circles produced a better result and was actually preferred (p.286).

---

## Interaction Design

### Hover as Reward Mechanism (p.288, p.274)
- Hover interactions can be designed as a reward for users who actively explore — they reveal additional depth not visible in the static view.
- Example: hovering over a language circle in the word string revealed an elaborate tooltip with a line chart (Google Trends 5-year trend) and a word cloud of related queries (p.288).
- Example: hovering a flower/leaf in "Send Me Love" drew arrows showing the sequence of texts sent before and after, plus keyword, timestamp, and artwork received (p.274).

### Sequential Narrative via Interaction (p.274)
- Hover-triggered arrows that chain one text message to the next enabled the viewer to follow an individual's emotional "journey" — the interaction itself told the story.
- This is a strong pattern: use interaction to reveal temporal or causal sequence that would be too cluttered if shown statically.

### Responsive / Adaptive Layout (p.291)
- Responsive design for data viz is not just "scale down" or "stack vertically": the best approach is to change the layout and move data to make the most of available space.
- Example: circular network on desktop → rectangular grid on mobile, keeping nodes the same size but rearranging their positions (p.291).
- Example: "word snake" recalculates whether 2, 3, or 4 beads fit per row; 80% of the math for one layout option transfers to the others (p.291).

### Carousel / Expand-Collapse Layout (p.273–274)
- When multiple items compete for screen space, a carousel with one item "expanded" and the rest "minimized" lets all items be visible simultaneously while giving full detail to the selected one.
- CSS Grid was used to make this perfectly responsive (p.274).

---

## Data Manipulation

### Combining Rankings Across Groups (p.282)
- To derive an overall "most translated word" across 10 languages, a point system was used: top word in a language gets N points, second gets N-1, etc. — the word with the most cumulative points wins.
- This avoids raw frequency comparisons when absolute counts differ greatly between language groups.

### Synonym and Variant Collapsing (p.281–282)
- Multiple source words translating to the same English word (e.g., "hermosa," "hermoso," "bonito" → "beautiful") were manually merged per language before ranking.
- Critical for fair cross-language comparisons: without this step, rankings would be fragmented.

### Filtering by Word Class (p.281)
- Filtering to only nouns and adjectives (using NLP tagging in R) removed common phrases and exposed more culturally revealing differences.
- Rule of thumb: removing the most common/obvious entries often reveals the more interesting signal underneath.

### Sentiment Scoring (p.264)
- Used "sentiment" (Node.js package) to score each keyword as positive or negative — enabling categorisation of text messages without manual labelling.

### Shannon Entropy as Data Variable (p.264)
- Used as a proxy for how "chaotic" or visually complex an artwork is — a novel quantitative variable derived from image data, enriching a non-visual dataset.

### Manually Categorising Taxonomy-like Data (p.299–300)
- Google Knowledge Graph returned 252 "types" for travel topics. Eight summary categories were defined, and a mapping script handled most; remaining 45 edge cases were manually assigned.
- Rule of thumb: automated categorisation covers ~80–90%; always budget time for manual review of edge cases.

---

## Marks and Channels

### Opacity and Thickness for Data Encoding (p.254)
- Butterfly path opacity and line thickness were mapped to wingspan (small / medium / large) — heavier butterflies leave thicker, more opaque traces.
- Path type (solid line / dotted line / circles) was varied by species category (regular species vs. Skippers), adding a shape/texture channel.

### Color Hue for Category, Slight Randomisation for Variety (p.254)
- Main butterfly color defined path hue; slight randomisation across 5 very similar colors added diversity without losing category identity.
- Rule: pure categorical color can look monotonous; small random variation within a hue range adds visual richness while preserving the encoding.

### Text as Mark (p.283–286, p.290)
- Using the actual words as the visual marks (instead of bars or circles) makes the content self-labelling — no separate legend needed.
- Works well for linguistic/textual data; risks chaos when many labels overlap (p.290). Mitigate by limiting labels to the most prominent element (the center of a link, not both endpoints).

### Radial / Circular Layouts (p.286–287)
- "Tree ring" structure: languages arranged in concentric arcs; each arc level is a rank in the top 10.
- Network with languages as circles on a ring: visual topology conveys similarity (closer languages appear more connected).

---

## Common Mistakes and Anti-Patterns

### Random Paths Without Natural Smoothing Look Terrible (p.252–253)
- First attempt with random straight-line paths was "absolutely dreadful." Lesson: making random things look beautiful is genuinely difficult and requires iterative refinement.
- Fix: use spline smoothing (curved spline through control points) + gentle jitter + very low opacity.

### Too Many Flowers = Computational Overload and Aesthetic Mess (p.267)
- Drawing a flower for every single text message caused performance problems and visual clutter.
- Fix: only draw flowers for positive messages; use simpler marks (leaves, circles) for neutral/negative ones. Simplification of representation matches the data's semantic importance.

### Overlapping Network Labels = Chaos (p.289–290)
- Replacing link lines with word labels in a network made everything unreadable.
- Fix: revert to lines with only one key word label per link. Less is more when the visual already has a complex topology.

### Staggered Animation Obscures the Story (p.286)
- Moving circles to switch places in an animation was so choppy it hid the logical transition.
- Fix: rotate text out of view then back in. Simpler, faster animation communicates the change more clearly.

---

## Practical Rules of Thumb

- If you can't sketch a design that works logically on paper, it won't work in code. Sketch to validate the concept first (p.284).
- Learn basic trigonometry (sin, cos, polar/Euclidean conversion) — it becomes essential the moment you deviate from standard chart layouts (p.288).
- Use web workers when computation (not rendering) is the bottleneck — they don't make code faster but prevent the UI from freezing (p.268).
- Custom animations need: an interpolator, a duration, and (optionally) an easing function — because nothing in nature moves at a perfectly linear rate (p.270).
- For multi-language or multi-group comparisons, always check for synonyms and variants that map to the same target concept; merge them before ranking (p.281–282).
- On hover, reward engaged users with richer data — a tooltip that tells a small story (trend line + word cloud) is far more valuable than a tooltip that just repeats the data point's value (p.288).
- Minimalism is not the starting point; it is the destination after iteration. Start with more, then strip away anything that does not add focus (p.290, Alberto Cairo's advice).
