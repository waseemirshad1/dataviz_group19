# [agent_18] Visualization Analysis and Design — pages 101-150

## Coverage Overview

Pages 101–150 cover:
- Chapter 5 (continued): Marks and Channels — channel effectiveness in depth
- Chapter 6: Rules of Thumb — eight practical design guidelines
- Chapter 7 (start): Arrange Tables — spatial encoding of tabular data

---

## Marks and Channels (Chapter 5, pp. 101–115)

### Expressiveness and Effectiveness Principles (p. 101)

- **Expressiveness principle**: encode only what is in the data; match channel type to attribute type
  - Magnitude channels → ordered (quantitative/ordinal) attributes
  - Identity channels → categorical attributes
- **Effectiveness principle**: more important attributes should use more effective (salient, accurate) channels

### Full Channel Rankings (p. 101–102, Figure 5.6)

**Magnitude Channels (for Ordered Attributes) — ranked most to least effective:**
1. Position on common (aligned) scale
2. Position on unaligned scale
3. Length (1D size)
4. Tilt / angle
5. Area (2D size)
6. Depth (3D position)
7. Color luminance
8. Color saturation
9. Curvature
10. Volume (3D size)

**Identity Channels (for Categorical Attributes) — ranked most to least effective:**
1. Spatial region
2. Color hue
3. Motion
4. Shape

**Key insight**: Spatial position channels appear at the top of BOTH lists. They are the only channels effective for both ordered and categorical data. (p. 101–102)

**Critical note**: Using a magnitude channel for categorical data (or identity channel for ordered data) violates the expressiveness principle and produces poor encodings. (p. 101)

**The attribute encoded with position dominates the user's mental model** more than any other channel. (p. 102)

### 5.5 Channel Effectiveness — Five Criteria (pp. 103–114)

#### 5.5.1 Accuracy (pp. 103–105)

- **Stevens' Power Law**: `S = I^n` where S = perceived sensation, I = physical intensity
  - n < 1: sensation compressed (brightness n ≈ 0.5, area n ≈ 0.7)
  - n = 1: perfectly linear perception (**length** has n = 1.0 — perfectly accurate)
  - n > 1: sensation magnified (red-gray saturation magnified; electric current n = 3.5)
- **Cleveland & McGill accuracy experiments** confirmed order: aligned position > unaligned position > length > angle >> area; volume, curvature, luminance worst
- **Heer & Bostock crowdsourced replication** largely confirmed this; found length ≈ angle in accuracy
- **Design implication**: length is very accurately perceived; area is significantly less so; never use volume/curvature for precise comparisons

#### 5.5.2 Discriminability (pp. 106)

- Each channel has a limited number of **bins** — distinguishable steps
- Example: line width works for 3–4 values but fails for dozens (mark perceived as area beyond a limit)
- **Rule**: number of attribute values must not exceed number of available bins for the chosen channel
- If mismatched: either aggregate the attribute or choose a different channel (p. 106)

#### 5.5.3 Separability (pp. 106–109)

- Channels range from **separable** (independent) to **integral** (fused into combined perception)
- **Fully separable**: position + color hue — can attend to each independently (p. 107)
- **Some interference**: size + color hue — color harder to discriminate for small objects (p. 107)
- **Integral pair**: horizontal size + vertical size → perceived as area (three groups: small/flat/large), not two independent variables (p. 108)
- **Most inseparable**: RGB red + green channels → perceived as fused hue, not two separate attributes (p. 108)
- **Design rule**: use separable channels when encoding two different attributes; use integral channels only when you want a single combined perception (p. 108–109)
- Integrality ≠ bad; it's about matching channel characteristics to design goals (p. 108)

#### 5.5.4 Popout / Preattentive Processing (pp. 109–111)

- **Visual popout**: a distinct item stands out from many others **immediately** (parallel processing, time independent of set size) (p. 109)
- Channels supporting popout: color hue, shape, size, tilt, proximity, shadow direction, motion (flicker, direction, velocity) (p. 111)
- **Popout is NOT additive**: combining two channels (e.g., color + shape) usually eliminates popout and requires serial search (p. 110)
- **Exceptions**: space + color, and motion + shape support combined popout (p. 110)
- **Rule**: only rely on popout for a single channel at a time (p. 110)
- Some channels do NOT support popout: e.g., parallelism requires serial search (p. 111)
- Popout is not binary — depends on both channel type AND magnitude of difference (p. 109)

#### 5.5.5 Grouping (pp. 111–112)

- **Containment marks** → strongest perceptual grouping cue
- **Connection marks** → second strongest
- **Proximity** (spatial region) → third strongest → explains why spatial region is top identity channel
- **Color hue / motion / shape** → weakest grouping, but add less visual clutter
- Shape needs careful selection: forward 'C' vs. backward 'C' do NOT form preattentive groups; circle vs. star DO (p. 112)
- Motion with multiple levels can overwhelm selective attention (p. 112)

### 5.6 Relative versus Absolute Judgements (pp. 112–114)

- **Weber's Law**: perception is based on **relative** differences, not absolute ones; detectable difference is a fixed percentage of the reference magnitude (p. 112)
- Explains why aligned position (common scale) is more accurate than unaligned position:
  - Aligned bars allow comparison of unfilled frame sections (a large relative difference) vs. the bars alone (small relative difference) (p. 112–113)
- **Color/luminance perception is entirely contextual**: same gray square appears different depending on surroundings (checkerboard illusion, p. 113–114)
- Color constancy: our visual system compensates for illumination conditions, meaning color channels are unreliable for precise quantitative encoding (p. 114)

---

## Chapter 6: Rules of Thumb (pp. 117–142)

Eight rules of thumb (p. 116–117):

### Rule 1: No Unjustified 3D (pp. 117–130)

**When 3D is justified**: only when the task requires understanding inherently 3D spatial structure (fluid flow, medical imaging, molecular structure) (p. 117–118, 124–125)

**Costs of 3D**:
- **The Power of the Plane**: spatial position rankings only apply to 2D planar position, not 3D depth (p. 118)
  - Vertical > horizontal due to gravity but display aspect ratios often override this (p. 118)
- **Disparity of Depth** (p. 118–119): depth perception follows a power law with n = 0.67 — worse than area (n = 0.7). We effectively "see in 2.05D" (Ware) (p. 119)
- **Line-of-sight ambiguity**: only one point visible per depth ray vs. millions of points per lateral ray (p. 119–120)
- **Occlusion** hides information; navigation to reveal hidden info takes time and imposes cognitive load (p. 120–121)
- **Perspective distortion**: distant objects appear smaller and shift position, destroying planar channels and size channel; 3D bar charts are harder to read than 2D (pp. 121–122)
- **Lighting/shadows**: create visual clutter, can be mistaken for data marks, interfere with color channels (p. 123)
- **Stereoscopic depth** helps but is weak for distant objects and cannot solve perspective distortion (p. 123)
- **Tilted text is not legible**: fonts designed for 2D pixel grids; tilted text is blocky/jaggy (p. 124)

**Case study: 3D vs. 2D time-series** (van Wijk & van Selow, pp. 126–127):
- 3D view of one year of power consumption data showed only large-scale seasonal patterns
- 2D linked views with hierarchical clustering and calendar layout revealed fine-grained weekday, seasonal, and holiday patterns invisible in 3D

**Case study: Justified 3D** (oscilloscope eye diagram, Lopez-Hernandez, p. 128):
- Layers always face viewer (orthographic), constrained navigation → acceptable 3D use

**Empirical evidence** (p. 129–130):
- People state preference for 3D but perform worse on tasks with 3D
- 3D better for shape understanding; 2D better for relative position tasks
- 3D cone trees vs. 2D tree browser: significant time cost for 3D
- Points outperformed 2D and 3D landscapes for search and estimation tasks

### Rule 2: No Unjustified 2D (p. 131)

- Laying out data in 2D vs. 1D list also needs justification
- **Lists**: maximum information density (text labels), excellent for ordered lookup tasks
- **2D layouts** (node-link): require more space, worse for lookup; justified when task requires understanding topological network structure

### Rule 3: Eyes Beat Memory (pp. 131–134)

- Comparing simultaneously visible views has much lower cognitive load than comparing current view to memory
- **Working memory is very limited**; long-term memory is unlimited but slow to access (p. 132)
- **Vigilance degrades quickly** with time; performance much worse after hours vs. first minutes (p. 132)

**Animation types** (p. 132–133):
1. Narrative storytelling (movies)
2. Transitions between two states — powerful for tracking change, helps context maintenance
3. Video-style multiframe playback

- Animation for transitions: effective when few objects change; fails when many objects change simultaneously (p. 132–133)
- **Blink comparator**: user-controlled jump between two frames — effective for detecting localized differences (p. 133)
- Multiframe animations require memory for inter-frame comparison → high cognitive load (p. 133)
- **Small multiples often better than animation** for detailed comparison across frames (p. 133)

**Change blindness** (p. 133–134): we fail to notice dramatic changes when attention is directed elsewhere — major challenge for animation-based vis

### Rule 4: Resolution over Immersion (pp. 134–135)

- Pixels are precious: resolution >> immersion in most cases
- Immersive displays (VR/head-mounted) have lower pixel density per area than desktop displays
- Immersion also breaks workflow integration (no standard keyboard/mouse input)
- Only justified for: phobia desensitization, presence tasks, 3D spatial data with careful justification

### Rule 5: Overview First, Zoom and Filter, Details on Demand (pp. 135–137)

- **Shneiderman's mantra** [Shneiderman 96] (p. 135)
- Overview: show all items simultaneously to reveal regions worth drilling into
- Overviews created via: geometric zooming out, aggregation, semantic zooming
- Three idiom families: (1) multiple views, (2) single view with zooming/filtering, (3) focus+context in one view (p. 137)
- **Alternative for huge datasets**: "Search, Show Context, Expand on Demand" [van Ham & Perer 09] (p. 137)
- Overview ≠ strictly one phase; users interleave overview and detail constantly (p. 136)

### Rule 6: Responsiveness Is Required (pp. 137–140)

**Three latency thresholds** (Table 6.1, p. 137):
| Time constant | Value | Relevant for |
|---|---|---|
| Perceptual processing | 0.1 s | Screen updates |
| Immediate response | 1 s | Selection feedback, animated transitions |
| Brief tasks | 10 s | Task granularity chunks |

- System must provide feedback within the relevant time class for each interaction type
- **Visual feedback**: highlight selected items; show progress indicators when crossing latency classes
- **Latency interaction design**: mouseover > click for speed; popup at cursor > side pane for fast visual feedback
- **Interactivity has cost**: human time + attention; if exhaustive checking required, vis degenerates into manual search (p. 140)
- Detect features automatically where possible; always keep human in the loop for pattern detection (p. 140)

### Rule 7: Get It Right in Black and White (p. 140)

- **Maureen Stone's guideline**: ensure most critical aspects are legible in grayscale
- Encode the most important attribute with **luminance** channel to guarantee contrast
- Use hue and saturation as secondary channels only
- Literally print in black and white to check (p. 140)

### Rule 8: Function First, Form Next (pp. 140–141)

- Effective but ugly design can be refined; beautiful but ineffective design must be discarded
- Progressive refinement from function to form is possible; the reverse is not
- "Form never" is also wrong: beauty enhances effectiveness; users prefer beautiful designs when equal effectiveness

---

## Chapter 7 (start): Arrange Tables (pp. 144–150)

### Why Arrange? (pp. 145–146)

- Spatial arrangement is the **most crucial** encoding choice — dominates user's mental model
- Top 3 effectiveness channels for ordered attributes are all spatial; top channel for categorical is also spatial (region)
- No non-spatial channel is highly effective for all attribute types (p. 145)

### Keys and Values (pp. 145–146)

- **Key**: independent attribute used as unique index (categorical or ordinal)
- **Value**: dependent attribute (categorical, ordinal, or quantitative)
- **Levels**: unique values of a categorical/ordered attribute
- Core design choices map to key count:
  - 0 keys, 2 values → **scatterplot**
  - 1 key, 1 value → **bar chart**
  - 2 keys, 1 value → **heatmap**
  - Many keys, many values → **recursive subdivision** (scatterplot matrix)

### Express: Quantitative Values — Scatterplots (pp. 146–148)

- Each item = point mark at (x, y) position encoding two quantitative value attributes
- Excellent for: overview, distribution, outliers, correlation (diagonal line pattern), clusters
- Additional channels: color for categorical attribute, size for another quantitative attribute (bubble plot)
- **Scalability**: suitable for dozens to hundreds of items; limited by point overlap/discriminability
- **Derived data enhancement**: log-transform axes to reveal correlations obscured in raw scale (p. 147–148)
- Superimpose regression line when correlation detection is the primary task (p. 148)

**What-Why-How summary** (p. 148):
| | |
|---|---|
| What: Data | Table: two quantitative value attributes |
| How: Encode | Express values with horizontal/vertical position + point marks |
| Why: Task | Find trends, outliers, distribution, correlation; locate clusters |
| Scale | Items: hundreds |

### Separate, Order, and Align: Categorical Regions (pp. 149–150)

- Categorical attributes cannot be expressed with spatial position (violates expressiveness)
- Categorical attributes match spatial regions: contiguous areas distinct from each other
- Three operations: **separate** (by categorical attribute), **align** (optional, by ordered attribute), **order** (required, by ordered attribute) (p. 149)
- Separation uses categorical attribute; ordering must use an ordered (non-categorical) attribute (p. 149)

### Bar Charts (p. 150)

- **1 categorical key** → one region per item in 1D list alignment
- Line mark, value attribute encoded with aligned spatial position (highest accuracy)
- Categorical key attribute encoded as spatial region along horizontal axis
- **Ordering matters**: alphabetical is default but hides trends; order by value attribute for pattern visibility
- **Scalability**: several to dozens of bars comfortably; theoretical limit ~hundreds at pixel scale

---

## Anti-Patterns and Common Mistakes

- Using 3D when task does not require understanding 3D geometry (p. 117–118)
- Perspective distortion in bar charts — 3D bar charts harder to read (p. 122)
- Encoding categorical data with magnitude channels (violates expressiveness) (p. 101)
- Encoding ordered data with identity channels (violates expressiveness) (p. 101)
- Using more visual channels than discriminable bins (p. 106)
- Using integral channels to encode two separate attributes (p. 108)
- Relying on popout for two or more channels simultaneously (p. 110)
- Animation with simultaneous widespread changes (change blindness, memory overload) (p. 133)
- Immersive displays for abstract data tasks (resolution loss not worth it) (p. 134)
- Using 2D layout when a 1D list suffices (e.g., no topological structure to show) (p. 131)
- Ordering bar chart alphabetically by default when task is trend comparison (p. 150)
- Using RGB channels as separate data encodings (completely integral — perceived as fused hue) (p. 108)

---

## Practical Rules of Thumb — Consolidated

1. Match channel type to attribute type: magnitude for ordered, identity for categorical (p. 101)
2. Match attribute importance to channel salience (p. 101)
3. Encode most important attribute with position (p. 102)
4. Use length for accurate 1D comparisons; avoid area/volume for precise comparisons (p. 104)
5. Keep number of attribute values within discriminable bins per channel (p. 106)
6. Use separable channel pairs when encoding two separate attributes (p. 108)
7. Only rely on popout for one channel at a time (p. 110)
8. Use containment/connection for strongest grouping; proximity/hue for lightweight grouping (p. 111)
9. Always align bars to a common baseline for maximum accuracy (p. 112–113)
10. Check designs in black and white (p. 140)
11. Function first, refine form after (p. 141)
12. Prefer resolution over immersion (p. 134)
13. Show simultaneous views rather than relying on memory; use small multiples over animation for comparison (p. 133)
14. Respond within 0.1s (screen), 1s (feedback), 10s (task completion) (p. 137)
15. Justify 3D only for inherently spatial 3D tasks (p. 117)
16. Justify 2D layout over 1D list when topological structure matters (p. 131)
17. Order categorical regions by value attribute, not alphabetically, for trend detection (p. 150)
