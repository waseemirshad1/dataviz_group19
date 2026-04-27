# Project Synthesis and Plan: Yield vs Biodiversity Trade-off
**Dataset:** Coffee/Biodiversity Dataset
**Persona:** Mixed/Overall (Hana Abebe & Sofia Almeida combined tension) - Agronomist/Ecologist evaluating trade-offs.

## Guiding Questions:
1. Are there sites that achieve both high yield and high biodiversity, or is the trade-off unavoidable?
2. How do management variables (like coffee density and structure) influence this trade-off?
3. Which species groups are most sensitive to management intensity?

## Strategy to achieve "Good (+2)" in all categories

### 1. Design Space Exploration (Novel/Semantically Unusual Designs)
Instead of standard scatter plots to show Yield vs Biodiversity, we will create composite and semantically unusual charts:
- **Concept 1: Similarity Network Map (Sites as Nodes).** A network graph where nodes represent Coffee Sites. Edges connect sites that have similar management profiles (density/structure). Node size = Yield, Node Color = Biodiversity. This uses a network layout for multidimensional similarity rather than physical/literal connections.
- **Concept 2: The Trade-off Comet Chart (Tadpole Chart).** Instead of a point, each site is a 'comet'. The head position represents (Yield, Biodiversity). The tail vector represents the management intensity (direction = dominant management practice, length = intensity level or structure index).
- **Concept 3: Radial Stacked Bar with Central Bubble.** A single visual combining a radial stacked bar (showing species composition: woody, bryophytes, herbaceous) with a central bubble representing the total yield.

### 2. Well-Annotated Designs
Every interactive chart in Marimo will feature comprehensive tooltips, legends, and most importantly, markdown blocks alongside them that explicitly spell out:
- **Marks used:** (e.g., Nodes, Lines, Tails)
- **Channels used:** (e.g., Position, Color Hue, Size, Length)
- **Rationale:** Why this encoding is effective for the data type.

### 3. Meaningful Reworking
The notebook will demonstrate an evolution:
- **Diverge:** Start with the guiding question.
- **Emerge:** Show the thought process of combining a scatter plot of yield/biodiversity with a vector representation of management (SCAMPER - Combine & Modify).
- **Converge:** The final implemented interactive visualization (e.g., Comet Chart or Similarity Network) with an explicit critique.

### 4. Explanation of Design Decisions (Theory Grounded)
Decisions will be explicitly mapped to visualization theory:
- *Expressiveness and Effectiveness:* We use position (the strongest channel) for the most critical variables (Yield and Total Richness). 
- *Pre-attentive processing:* Color hue is used for categorical groupings or highlighting top performers so they pop out.
- *Gestalt Principles:* Connection (in the network graph) leverages Gestalt principle of connectedness to imply similarity in management practices. 

This document serves as the structural guide for the `design_code_1/code.py` Marimo notebook.
