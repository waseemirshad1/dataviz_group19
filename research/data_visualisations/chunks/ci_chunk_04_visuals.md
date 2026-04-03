# [agent_04] Cool Infographics — pages 151-200

---

### Radial Proportional Circle Budget Diagram (p.181–182)
- **What it shows:** Hierarchical budget breakdown — one large central circle for total, medium circles for departments, small satellite circles for sub-departments; connecting arrows show direction of year-over-year change
- **When to use:** Showing budget allocations with multiple hierarchy levels and change over time; avoid when more than ~15 leaf nodes (becomes cluttered)
- **Interesting properties:** Arrow color (red/yellow/green) encodes budget change direction as a third variable without adding a separate chart; viewers can scan both magnitude and trend simultaneously
- **Marks:** Circles (areas), directed arrows
- **Channels:** Circle area = dollar amount; arrow color hue = change direction (red=decrease, yellow=unchanged, green=increase); arrow direction = hierarchical relationship; label text = dollar value and percentage
- **Annotation options:** Dollar value and percentage change inside or adjacent to each circle; parent category name as label
- **Data types suited for:** Quantitative (budget amounts), categorical (departments), ordinal (change direction)
- **Interesting feature extraction/manipulation:** Computing year-over-year percentage change and encoding it as a discrete three-category (red/yellow/green) rather than a continuous scale — simplifies reading considerably

---

### Treemap Budget Visualization (p.182–183, Fig. 5-3 BBC-o-Gram)
- **What it shows:** Proportional area allocation of budget across departments and sub-items; BBC budget 2008/09 showing TV, Radio, Online, Running Costs, Income, Wages as colour categories
- **When to use:** When you need to show part-of-whole for many items simultaneously; works well when there are 2 levels of hierarchy (category → item); avoid when items are very similar in size (small area differences are hard to read)
- **Interesting properties:** Sub-rectangles fill parent rectangles, so hierarchy is physically embedded in the layout; color coding separates categories without need for a separate legend panel
- **Marks:** Rectangles (nested)
- **Channels:** Area = budget amount; color hue = budget category (TV vs Radio etc.); position within parent = sub-category membership; label text = item name and value
- **Annotation options:** Item names and values as text inside rectangles when rectangles are large enough; color legend strip
- **Data types suited for:** Quantitative (budget), categorical (department/category), hierarchical
- **Interesting feature extraction/manipulation:** Showing only select highlights rather than complete budget — editorial filtering reduces cognitive load while preserving the proportional story

---

### Back-to-Back Opposing Bar Chart — Sales vs. Profit (p.183–184, Fig. 5-4)
- **What it shows:** Two related but distinct quantities for each item (product), displayed as bars extending in opposite directions from a central product name axis; annual sales (blue, left) vs. annual profit (green, right) for top 10 products
- **When to use:** When you need to compare two quantities per item and reveal that the ranking on one quantity does not match the other; avoid for more than ~15 items (becomes long); not natively available in Excel — must be built manually
- **Interesting properties:** The opposing layout makes it visually obvious when the sales-rank order differs from the profit-rank order (e.g., Product A has highest sales but Product D has highest profit margin)
- **Marks:** Horizontal bars
- **Channels:** Length = monetary amount; color hue = metric type (blue=sales, green=profit); position on vertical axis = product identity; label inside bar = exact value and percentage
- **Annotation options:** Values labelled inside bars; percentage profit margin shown next to profit bar
- **Data types suited for:** Quantitative (two metrics), categorical (products)
- **Interesting feature extraction/manipulation:** Pre-computing profit margin percentage and displaying it alongside absolute profit dollar value — reveals the rate dimension that pure absolute comparison misses

---

### Proportionally Sized Logo Circles — Sales by Channel (p.184–185, Fig. 5-5)
- **What it shows:** Sales volume per retail channel, where each channel is represented by its actual logo placed inside a circle sized proportionally to its sales contribution
- **When to use:** When the categorical identity is universally recognised through a logo/brand (companies, sports teams, countries); when showing data to an internal audience familiar with those brands; avoid when logos are not universally known
- **Interesting properties:** The logo itself is the identity channel — no labels, no legend needed. This allows showing relative magnitude while hiding exact values (useful for internal presentations where confidentiality is needed)
- **Marks:** Circles containing logo images
- **Channels:** Circle area = sales magnitude; logo image = category identity; spatial arrangement = grouping (loose bubble layout)
- **Annotation options:** Can omit values entirely for confidentiality; can add text labels below circles if needed
- **Data types suited for:** Quantitative (sales), categorical (brands/channels)
- **Interesting feature extraction/manipulation:** Choosing to omit exact values deliberately — shows relative rank without revealing competitive information to visitors

---

### 10×10 Icon/Square Grid (Waffle Chart) — Survey Research Data (p.190–192, Fig. 5-11)
- **What it shows:** Percentage values for multiple brands across multiple attributes, shown as a grid of 100 colored/greyed squares where filled squares = percentage; 3 brands × 7 attributes = 21 grids arranged as a small multiples matrix
- **When to use:** Comparing percentages across many categories; when audience may not be comfortable with bar charts; when you want to show both the value and the "out of 100" context; always use rows of 10
- **Interesting properties:** Immediately readable because humans are Base-10 intuitive. Small colored dots beneath each grid encode which other brands scored significantly lower (statistical significance as a secondary encoding). All 21 data points fit on one page.
- **Marks:** Squares (100 per grid); small colored dots below grids
- **Channels:** Color fill of squares = percentage value; square count = the percentage literally; dot color below grid = which competitor scored significantly lower; brand color = identity across all grids; position in matrix = brand × attribute combination
- **Annotation options:** Percentage value printed below each grid; brand name and logo at row start; attribute name at column head
- **Data types suited for:** Quantitative (percentages), categorical (brands, attributes)
- **Interesting feature extraction/manipulation:** Encoding statistical significance as secondary small-dot markers — adds inferential information without disrupting the primary percentage reading

---

### Person Icon Array / Isotype Chart (p.193–194, Fig. 5-13)
- **What it shows:** Literal count of survey respondents, where each person-shaped icon represents one individual; filled (green) = responded positively, grey = responded negatively; shown as a row of 6 icons
- **When to use:** Visualising qualitative/small-sample data where showing exact individual count is important; prevents audience from drawing false statistical conclusions; avoid for large samples (n>50 becomes unwieldy)
- **Interesting properties:** The small sample size is visually self-evident — no false impression of statistical power. Each icon stands for a specific person, reinforcing the qualitative nature of the data.
- **Marks:** Person-shaped icons (glyphs)
- **Channels:** Color fill = response category (positive/negative); count of colored icons = literal frequency; icon shape = human individual
- **Annotation options:** Text label below stating "4 out of 6 people interviewed would buy the product"
- **Data types suited for:** Categorical (response), small-count quantitative
- **Interesting feature extraction/manipulation:** Deliberately NOT computing a percentage — the literal count is the point; only compute percentages when n is large enough for statistical validity

---

### Word Cloud — Sentiment Analysis (p.194–195, Figs. 5-14 and 5-15)
- **What it shows:** Most frequent words from 15,000 Amazon product review comments; shown as two separate clouds — one green (positive reviews) and one red (negative reviews)
- **When to use:** Showing qualitative text data to reveal common themes and sentiment; useful for large volumes of verbatim comments; avoid when you need precise frequencies or when the audience might mistake it for quantitative data
- **Interesting properties:** Color separation of clouds by sentiment makes the contrast immediately visible without reading individual words. The viewer can compare which themes dominate positive vs. negative experiences.
- **Marks:** Text words at varying sizes
- **Channels:** Font size = word frequency; color hue = sentiment category (green/positive, red/negative); spatial arrangement = no data meaning (decorative layout)
- **Annotation options:** Title identifying sentiment category; source note
- **Data types suited for:** Textual/qualitative, frequency
- **Interesting feature extraction/manipulation:** Splitting a single text corpus into two separate sentiment clouds by first filtering positive vs. negative reviews — the comparison between the two clouds is the insight

---

### Enriched Process Timeline with Sized Circles (p.186, Fig. 5-7 "A Website Designed")
- **What it shows:** Website design process across 8 weeks with two swim lanes (Designer, Client); phases shown as colour-coded circles of varying size along a horizontal timeline; milestones shown as small dots; label font size encodes importance
- **When to use:** When a process has multiple parallel tracks, variable involvement levels, and key milestones to highlight; richer alternative to a standard Gantt chart
- **Interesting properties:** Three separate channels encode three different dimensions of information simultaneously on the same marks (size = involvement, color = phase, font size = importance), avoiding the need for multiple charts
- **Marks:** Circles (phases), dots (milestones), lines (timeline)
- **Channels:** Circle diameter = estimated involvement level; color hue = project phase (research/wireframes/coding/etc.); font size of label = importance level; horizontal position = time (week); vertical position = actor (designer/client)
- **Annotation options:** Phase names at top of circles; milestone labels with connecting lines; legend panel for involvement scale, colour-phase mapping
- **Data types suited for:** Temporal, quantitative (involvement), categorical (phase, actor)
- **Interesting feature extraction/manipulation:** Converting estimated involvement (qualitative judgment) into a continuous circle size — requires the designer to make an explicit magnitude estimate for each phase

---

### Illustrated Character Process Path (p.187, Fig. 5-8 "How Affiliate Marketing Works")
- **What it shows:** A 10-step affiliate marketing process shown as an isometric path with human character figures performing each action; each step is a tile on the path with a character acting out the activity
- **When to use:** Internal process communication where employee identification with characters is important; when you want the audience to see themselves in the process; avoid for highly technical processes where precision matters more than relatability
- **Interesting properties:** Characters replace abstract process boxes — the viewer can immediately understand what activity is happening by seeing a human do it; no need to decode symbols
- **Marks:** Human figure glyphs, isometric path tiles, speech/action callouts
- **Channels:** Character appearance (colour) = actor identity (Affiliate=blue, Merchant=orange, Customer=yellow); path position = sequence; callout text = step description
- **Annotation options:** Step description text as callouts above each character; character name labels
- **Data types suited for:** Sequential/ordinal (process steps), categorical (actor roles)
- **Interesting feature extraction/manipulation:** Reducing a complex multi-party process to three actor roles with colour-coded characters — the simplification makes who-does-what immediately readable

---

### Standard Flowchart (p.185–186, Fig. 5-6)
- **What it shows:** Business decision process with standard shape conventions: rounded rectangles = start/end, rectangles = process steps, rectangles with torn bottom = documents, diamonds = decision points
- **When to use:** Formal process documentation; when precision and standardisation matter; avoid when you want engagement — standard flowcharts become generic and unmemorable at scale
- **Interesting properties:** Universal symbol vocabulary means any employee can read it; disadvantage is that identical styling across hundreds of flowcharts makes none stand out
- **Marks:** Rectangles, diamonds, rounded rectangles, directed arrows
- **Channels:** Shape = step type; arrow direction = flow; color hue = step category (orange/red/green/blue in the example)
- **Annotation options:** Step name inside shape; Yes/No labels on decision arrows
- **Data types suited for:** Categorical (step type), sequential (order)

---

### Infographic Resume — Combined Timeline + Skill Bars (p.152, Fig. 4-16 Anibal Maiz Caceres)
- **What it shows:** Employment and education history on a horizontal timeline (2003–2012) with two swim lanes (Employment top, Education bottom); software proficiency shown as a grouped bar chart; language proficiency shown as a pie chart
- **When to use:** When a person has parallel career/education streams that overlap in time; when software skills are a primary differentiator
- **Interesting properties:** Country flags are embedded as identity markers for each employer/school; QR code links to online portfolio. The timeline makes overlapping roles and education simultaneously visible.
- **Marks:** Timeline with event markers (circles), bars (software proficiency), pie segments (language)
- **Channels:** Horizontal position = time; vertical position = track (employment/education); bar height = proficiency percentage; pie segment angle = language proficiency; flag image = country identity
- **Annotation options:** Institution/role name and description at each event; percentage values on bar chart y-axis
- **Data types suited for:** Temporal, quantitative (proficiency), categorical (employer, language)

---

### Infographic Resume — DNA Strand Timeline (p.154, Fig. 4-17 Mino Parisi)
- **What it shows:** Education and work history plotted along a horizontal timeline shaped like a stylised DNA double helix; events are connected to the strand at the appropriate year; skill areas shown as overlapping bubble clusters; skill domain shown as four donut charts (one per work domain)
- **When to use:** When the designer wants a distinctive metaphor that is consistent with a creative/design professional identity; when multiple skill dimensions need to be shown simultaneously
- **Interesting properties:** The DNA metaphor visually implies that professional history is "encoded" in the person — a semantically resonant choice for a designer. Overlapping skill bubbles use area and overlap to suggest interconnectedness without precise values.
- **Marks:** Curved path (DNA strand), circles/bubbles (skills), donut segments (proficiency by domain)
- **Channels:** Position along strand = time; bubble size = skill importance; bubble overlap = skill relatedness; donut segment arc = proficiency allocation across tools within each domain; color hue = tool identity
- **Annotation options:** Year labels along timeline; event labels with connecting lines; skill name inside bubbles; domain name above each donut
- **Data types suited for:** Temporal, categorical (skills, employers), quantitative (proficiency allocation)

---

### Infographic Resume — Multi-Chart Combined Design (p.155, Fig. 4-17 Mino Parisi — full page)
- **What it shows:** Full infographic resume with: 4 donut charts (proficiency per design domain), overlapping skill bubbles, DNA timeline, and icon-based additional information section
- **When to use:** Standalone infographic supplement to a traditional text resume; works best for creative professionals where design quality itself is evidence of skill
- **Interesting properties:** Uses icons for hobbies/interests (gamepad, music notes, camera, tools) — removes the need for text entirely in the additional information section; each icon is universally readable
- **Marks:** Donut arcs, circles, icons, timeline path
- **Channels:** Donut arc = proportion of proficiency per tool within domain; bubble size = skill weight; icon shape = hobby/interest identity
- **Annotation options:** Tool name next to each icon in legend; domain name above each donut; dates below timeline events

---

### Infographic Resume — Integrated Text + Visual Timeline (p.157–158, Fig. 4-19 Vanessa Wilson)
- **What it shows:** Work experience timeline running down the left side of the page as three parallel curved lines (colour = work experience/education/volunteer), with full text descriptions of each role to the right; skill bars shown on the right panel
- **When to use:** Combined infographic+text format where job application systems need the text AND the reader gets the visual at the same time; single-document solution
- **Interesting properties:** The three parallel curved lines show temporal overlap between education, work, and volunteer activities — impossible to show this in a standard text resume. The eye can instantly see which time periods had multiple concurrent commitments.
- **Marks:** Curved lines (three), text blocks, horizontal bars (skills)
- **Channels:** Line color = track type (work/education/volunteer); horizontal position = time; vertical position = chronological period; bar length = skill level
- **Annotation options:** Year labels on left; role name and description to the right of timeline
- **Data types suited for:** Temporal, categorical (role type), quantitative (skill level)

---

### Infographic Resume — Elevator Pitch / iPad Format (p.163, Fig. 4-23 Dave Rodgerson)
- **What it shows:** Condensed visual resume for tablet display using employer logos, client logos, and university logos inside labelled circular clusters (Prior Employers, Major Clients, Universities & Associations); LinkedIn network map shown at bottom; word cloud from social media shown at top right
- **When to use:** When the resume is shown in-person on a tablet; when logo recognition is high; when you want to show professional network depth as a qualitative signal
- **Interesting properties:** Text is almost entirely eliminated — icons and logos carry all the meaning. The LinkedIn network map is a genuine data visualisation of the person's professional connections, colour-clustered by industry.
- **Marks:** Circles containing logos, network nodes (dots), network edges (lines), word cloud text
- **Channels:** Logo image = identity; circle cluster = category (employer/client/university); node color = industry cluster; edge = connection; font size in word cloud = interest frequency
- **Annotation options:** Cluster label (Prior Employers, etc.); shopping cart icon as thematic metaphor (retail focus); tappable links in PDF version

---

### cvgram.me — Dual-Ring Skill Glyph (p.173, Fig. 4-28)
- **What it shows:** Per-skill proficiency vs. frequency of use, shown as two concentric rings per skill — outer ring = expertise level, inner ring = frequency of use; a star icon indicates "top skill"
- **When to use:** When both mastery level and actual usage frequency are important dimensions (they can diverge — expert but rarely used vs. beginner but used daily)
- **Interesting properties:** The two-ring glyph is a compact multi-variable encoding — it answers two questions simultaneously per skill. The star adds a third binary dimension (top skill yes/no) without adding visual complexity.
- **Marks:** Concentric donut rings, star icon
- **Channels:** Outer ring arc = expertise level; inner ring arc = frequency of use; star presence = top skill flag; label = skill name; layout position = arbitrary (grid)
- **Annotation options:** Expertise level label (Always/Pro, Advance/Usually, Intermediate/Regular, Beginner/Sometimes) below each glyph
- **Data types suited for:** Quantitative (two proficiency dimensions), categorical (skill name, top skill flag)

---

### ResumUP.com — Integrated Identity Wheel (p.172, Fig. 4-27)
- **What it shows:** A "personality/identity" radar-style dial showing traits on a circular scale (Outgoing/Reserved, Flexible/Directed, Steady/Sensitive, Efficient/Carefree, Curious/Consistent); combined on the same page with work timeline, skill bars, and hobby icons
- **When to use:** When the candidate wants to communicate personality fit alongside hard skills; when applying to companies that value culture fit
- **Interesting properties:** The identity dial encodes personality traits as positions on a linear scale between two poles — semantically similar to a slider; more honest than a radar chart because it doesn't imply the traits are independent dimensions
- **Marks:** Dial/slider markers, bars, icons, timeline
- **Channels:** Marker position between two poles = personality trait value; bar length = skill level; icon = hobby identity; timeline position = work period
- **Annotation options:** Pole labels at each end; trait name beside each slider

---

### Proportional Circles with Change Arrows — Police Budget Detail (p.181–182, Fig. 5-2)
- **What it shows:** Close-up of a single department (Police, $10.9M) with all its sub-departments shown as satellite circles; arrows in red/yellow/green point from sub-circle to parent circle encoding year-over-year change
- **When to use:** When you need to drill down into a single node of the radial budget diagram to show sub-level detail
- **Interesting properties:** The "NEW" label on one satellite circle (Red Light Camera) highlights a new budget item — a fourth state beyond the three change colors
- **Marks:** Circles, directed arrows
- **Channels:** Circle area = dollar amount; arrow color = change direction; "NEW" text label = new item flag; percentage label = change magnitude
- **Data types suited for:** Quantitative (amounts), ordinal (change direction), categorical (departments)
