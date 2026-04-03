# [agent_03] Cool Infographics — pages 101-150

## Visualization Catalogue

---

### Mountain Metaphor Chart — Google PageRank Explained (p.105)
- **What it shows:** A logarithmic scale (0–10) of website authority/PageRank, with real websites (Google.com=10, eBay=9, ESPN=8, GE.com=7, GeneralMills=6, Swingline=5) labeled at their position. A diagonal red line sweeps from lower-left to upper-right representing "level of effort" required to reach each rank.
- **When to use:** Explaining a complex abstract score (logarithmic, non-linear) in intuitive spatial terms. Use when you want the audience to grasp relative difficulty of levels, not just their numeric value. Avoid for precise quantitative comparison.
- **Interesting properties:** The mountain illustration is placed in the background behind the diagonal axis — the mountain peak aligns with ranks 8–10. The chart is technically a custom annotated number-line, but the mountain metaphor makes it memorable. Websites are shown as colored flag markers (elite = red, above average = blue, average = purple, below average = black) so the categorical legend is embedded in the mark itself.
- **Marks:** Diagonal axis line (the "slope"), colored flag/pin icons at specific rank positions, illustrated mountain in background
- **Channels:** Position on diagonal axis = PageRank score; color of marker = performance tier; text labels = website name; background illustration = metaphoric context
- **Annotation options:** Tier legend (Elite 8–10, Above Average 5–7, Average 3–5, Below Average 0–2); website names as callout labels; "LEVEL OF EFFORT" label on the right vertical edge
- **Data types suited for:** Ordinal/quantitative (ranked score), categorical (performance tier)
- **Interesting feature extraction/manipulation:** The logarithmic scale is linearized visually — the spatial position does not reflect the true exponential gap between ranks 9 and 10 vs. 3 and 4. This is an intentional simplification that makes the concept approachable.

---

### Viral Sharing Tree / Radial Network Diagram (p.109)
- **What it shows:** How one piece of content (one source person-icon at center) propagates exponentially through social sharing — each recipient shares to ~2 more people, creating a radial tree of person-icons expanding outward.
- **When to use:** Showing exponential diffusion or network propagation. Use when the message is about reach, not about which specific nodes are connected. Avoid when you need to show real network topology.
- **Interesting properties:** All nodes are identical person-icons (no differentiation by color or size), so the visual emphasis is entirely on the structural growth pattern, not on individuals. The radial layout makes the exponential explosion visually immediate.
- **Marks:** Person-icon glyphs (nodes), thin lines (edges/connections)
- **Channels:** Position (radial distance from center = generation number); structure (number of connections = branching factor)
- **Annotation options:** Generation labels; count of nodes per ring; percentage reach estimates
- **Data types suited for:** Network/relational, temporal (generation sequence)
- **Interesting feature extraction/manipulation:** Abstracting real social network data into a uniform tree model removes real-world complexity but makes the core exponential principle immediately legible.

---

### Annotated Narrative Timeline Infographic — "Bringing Down Bin Laden" (p.120)
- **What it shows:** A complex multi-section infographic combining: a pre-operation timeline (text + event marks), a 3D isometric illustration of the compound, a Twitter feed column showing real-time tweets, and a bottom strip of photographic thumbnails with time-stamped captions.
- **When to use:** Breaking news events where sequence, geography, and social reaction must all be shown simultaneously. Avoid for data requiring precision — this is story-driven, not analytically driven.
- **Interesting properties:** The isometric compound illustration serves as a geographic anchor that grounds the timeline in physical space. The Twitter feed column beside it adds a real-time emotional/social layer — fusing data types (timestamps, quote text, social metadata) with the visual narrative.
- **Marks:** Event dots on timeline, isometric building illustration, photo thumbnails, text blocks
- **Channels:** Position (horizontal = time); spatial layout (left panel = pre-operation narrative, center = spatial/geographic, right = social reaction); color (dark background with green highlights = military/night-ops aesthetic)
- **Annotation options:** Time stamps, location labels, Twitter handles, photo captions
- **Data types suited for:** Temporal, spatial, qualitative/narrative
- **Interesting feature extraction/manipulation:** Collapsing multi-day pre-operation timeline and 38-minute operation into a single continuous visual requires a time-scale break, handled by separating sections visually.

---

### "Death & Taxes" Radial Budget Map (p.121)
- **What it shows:** The US Federal Budget 2014 — a large circular/radial layout where department seals (circular logos) are arranged around a central ring. Lines or arcs connect departments to budget amounts. A bar chart in the corner shows total budget comparison.
- **When to use:** Showing the proportional allocation of a large budget across many departments simultaneously, with visual identity markers (logos) adding instant recognition. Avoid when precise comparison between departments is needed — the radial layout makes magnitude comparison difficult.
- **Interesting properties:** Using official government/department seals as node marks gives the visualization instant institutional legibility. The circular layout evokes a government "ecosystem" or organism metaphor.
- **Marks:** Circular logo seals (department nodes), connecting lines, bar chart (corner)
- **Channels:** Angular position = department identity; size of connecting elements = budget proportion; color = department category
- **Annotation options:** Dollar amounts, department names, percentage labels
- **Data types suited for:** Quantitative (budget amounts), categorical (department), relational (connections between departments and totals)
- **Interesting feature extraction/manipulation:** Annual data — visualization becomes obsolete each budget cycle. The lifespan is ~1 year.

---

### Multi-Track Horizontal Timeline — "The Visual History of Halloween" (p.121)
- **What it shows:** A long horizontal timeline spanning from ancient times (~2000 BC) to present, with three parallel horizontal tracks: Festivals, Monsters, and a central event spine. Each track has annotated image + text blocks at specific dates.
- **When to use:** Historical topics with multiple parallel narrative threads that evolve over the same time period. Use when both the sequence and the thematic grouping of events matter. Long-lifespan topics are ideal.
- **Interesting properties:** Three simultaneous tracks allow the viewer to follow one strand (e.g., just the evolution of monsters) or read across all tracks at a given time period to understand context. The track metaphor is borrowed from music notation — each "instrument" plays its own melody along the same time axis.
- **Marks:** Image thumbnails (photo/illustration), text annotation blocks, horizontal track lines, date markers
- **Channels:** Horizontal position = time; vertical position = thematic track (Festivals vs. Monsters vs. general); color coding per track
- **Annotation options:** Date labels, event names, descriptive paragraphs, source citations
- **Data types suited for:** Temporal, categorical (track/theme), qualitative/narrative
- **Interesting feature extraction/manipulation:** Selecting which events are significant enough to include requires editorial curation — the visualization summarizes/abstracts a large body of historical knowledge.

---

### Connection Matrix / Flow Diagram — "Pairing Wine & Food" (p.122)
- **What it shows:** A grid of connections between food categories (top row, shown as illustrated food icons) and wine types (bottom row, shown as illustrated wine bottle icons). Colored lines connect each food to its compatible wines.
- **When to use:** Showing many-to-many relationships between two categorical sets where the number of connections is moderate. Avoid when connections are too dense (all items connect to all) — the lines become unreadable.
- **Interesting properties:** Using illustrated icons (realistic food and bottle drawings) instead of abstract marks makes the connections immediately semantically legible without reading labels. The colored lines group by wine type. A separate row at the bottom lists "foods that are hard to match with wine."
- **Marks:** Illustrated icon glyphs (foods and wine bottles), curved colored lines (connections)
- **Channels:** Horizontal position = food/wine identity; color of line = wine category; line presence/absence = compatibility relationship
- **Annotation options:** Wine style descriptions (inside bottle icons), food category labels, "hard to match" footer section
- **Data types suited for:** Categorical (food types, wine types), relational (compatibility links)
- **Interesting feature extraction/manipulation:** Binary simplification — either a pairing is compatible or it is not. Degree of compatibility or flavor profile similarity is abstracted away.

---

### Multi-Layer Area Chart Career Timeline — Michael Anderson Resume (p.132)
- **What it shows:** A horizontal timeline (1995–2008) showing work history above the date line and academic history below. Multiple overlapping colored area bands represent different concurrent jobs. A small 3D area chart ("Daily Intake & Output") shows daily activities from 8am–2am. A donut chart shows primary skill sets with two dimensions: slice angle = time spent developing skill (personal); slice height = professional deployment.
- **When to use:** Career histories where concurrent activities, overlapping roles, and the transition from education to employment all need to be shown simultaneously. Powerful for candidates with varied or non-linear histories.
- **Interesting properties:** The Y-axis is labeled "Area represents relative energy expenditure over time" — a subjective, self-defined metric, not measured data. This makes the chart honest about its qualitative nature while still using quantitative visual form. The dual-dimension donut (angle + height) encodes two variables on a single chart type.
- **Marks:** Overlapping area fills (timeline bands), 3D extruded area (daily activities), donut slices (skills)
- **Channels:** Horizontal position = time; vertical position + area fill = energy expenditure (subjective); color hue = activity/job type; donut angle = personal time investment; donut height = professional deployment level
- **Annotation options:** Job names with dates, skill labels on donut slices (a–f), color legend for daily activities
- **Data types suited for:** Temporal, quantitative (subjective), categorical (job types, skills)
- **Interesting feature extraction/manipulation:** Values are entirely subjective and self-assigned — no real numeric data underlies the charts. Actual values were created to generate the design but are deliberately not shown, reducing perceived precision and keeping the focus on relative patterns.

---

### Faz Besharatian Resume — Dual-Axis Vertical Timeline with Embedded Donut (p.134)
- **What it shows:** A vertical timeline (1989–2013) with Education on the left column and Professional Experience on the right. Each year is a row; colored horizontal bars extend left or right to show the duration and intensity of each activity. A donut chart at the bottom shows "Professional Investment" across five skill domains. Skill Areas are annotated along the right edge.
- **When to use:** Long career histories (20+ years) where both education and employment need to be shown simultaneously. The vertical layout allows more vertical space than horizontal. Use when the career is the dominant narrative.
- **Interesting properties:** The colored horizontal bars vary in width/length — encoding duration AND relative engagement in a single mark. The "Peak Engagement" annotation calls out the busiest career period visually. Using a central spine (the year column) creates a mirrored butterfly layout — instantly communicating that both sides are parallel narratives of the same time period.
- **Marks:** Horizontal colored bars (extending left = education, right = employment), circular donut (skill investment), text labels
- **Channels:** Vertical position = year/time; horizontal length = duration/intensity; color hue = activity domain; left/right side = education vs. employment
- **Annotation options:** Company names with roles, year labels, "Peak Engagement" callout, skill domain labels on donut
- **Data types suited for:** Temporal, categorical (education/employment domains), quantitative (duration)
- **Interesting feature extraction/manipulation:** Bar widths represent both duration and engagement intensity simultaneously — a dual encoding that is interpretable but requires a legend for clarity.

---

### Randall Knapp Resume — Overlapping Area Chart Timeline + Horizontal Bar Skill Chart (p.138)
- **What it shows:** Upper section: area chart timeline (2003–2009) with overlapping color areas for Code, Projects, Math/Physics, Level Design — both academic and professional activities on same axis. Lower section: horizontal bar chart showing skills (y-axis) vs. proficiency/experience in years (x-axis), labeled "Strengths" as text blocks.
- **When to use:** Technical candidates who want to show skills developing over time AND their current relative proficiency. The combination answers: "when did you learn X?" and "how good are you at X?" simultaneously.
- **Interesting properties:** Milestones (white dots with labels) are overlaid on the timeline to mark project completions — adding a discrete event layer on top of the continuous area. The lower bar chart deliberately labels bars at different lengths without giving numeric values, encoding relative proficiency without false precision.
- **Marks:** Overlapping area fills, white milestone dots, horizontal bars (lower section)
- **Channels:** Horizontal position = time (upper) or proficiency (lower); vertical stacking = activity type; color hue = skill domain; bar length = relative proficiency
- **Annotation options:** Project labels at milestones, skill names on y-axis, experience-in-years labels
- **Data types suited for:** Temporal, quantitative (relative), categorical (skill domains)
- **Interesting feature extraction/manipulation:** Selecting which skills to show requires editorial curation. The "experience in years" axis for the bar chart is straightforward but the bar endpoint positions are subjective estimates.

---

### Mike Wirth Resume — Full-Page Stacked Area Timeline with Geographic Columns (p.140)
- **What it shows:** A full-page horizontal stacked area chart (1996–2009) where each colored layer = a skill/discipline. The x-axis is years; the y-axis is total experience volume (stacked). Geographic location columns are shown as gray vertical bands behind the colored areas, marking where the person lived at each period.
- **When to use:** Highly multidisciplinary candidates where the growth and evolution of a broad skill portfolio over time is the primary message. Geographic career path as secondary layer.
- **Interesting properties:** The gray location columns function as a background "context grid" — they do not disrupt the skill area chart but add a geographic narrative without requiring a separate section. The total height of the stacked area growing over time visualizes overall experience accumulation — a powerful "career growth" narrative.
- **Marks:** Stacked color area fills (skills), gray vertical background bands (locations)
- **Channels:** Horizontal position = time; vertical height = accumulated experience volume; color hue = skill/discipline; gray band width = time spent in a location
- **Annotation options:** Location names above gray columns, skill labels within color bands, year labels on x-axis
- **Data types suited for:** Temporal, quantitative (accumulated), categorical (skill domains, locations)
- **Interesting feature extraction/manipulation:** Stacking all skill areas means the viewer sees total growth, but cannot easily isolate growth of any single skill — a deliberate design choice that emphasizes breadth over depth.

---

### Duncan McKean Resume — Central Spine Butterfly Timeline (p.141)
- **What it shows:** A vertical timeline from birth (1974) to present, with a central spine of year circles. Education extends as colored horizontal bars to the LEFT; Employment extends as colored horizontal bars to the RIGHT. Personal life milestones appear as small text callouts on the far left.
- **When to use:** Showing education and employment as two parallel narratives on the same time axis. Unusually personal — includes life events alongside career events, creating a holistic life narrative.
- **Interesting properties:** The inclusion of personal milestones ("Got Married," "Moved to Bristol," "Shouldn't have read 'It' by Stephen King") is semantically novel for a resume. It communicates personality and life context, not just professional history. The bars have no numeric labels — bar length = relative duration, encoded by position.
- **Marks:** Horizontal bars (left = education, right = employment), central spine circles (years), text callouts
- **Channels:** Vertical position = year; horizontal length = duration; color hue = activity type; left/right side = education vs. employment
- **Annotation options:** Company/institution names, role titles, personal life event callouts, year circles
- **Data types suited for:** Temporal, categorical (education/employment), qualitative (life events)
- **Interesting feature extraction/manipulation:** Including personal life events transforms a resume into a life narrative — a semantic novelty that reframes the purpose of the document.

---

### Hana Tesar Resume — Multi-Section Relative Bar Chart + Wavy Line Chart (p.141)
- **What it shows:** A dark-background resume where skills are shown as vertical red bars of varying heights (no numeric labels) grouped by domain (Illustration, Freelance, Software, Graphic Design). A wavy line chart (sine-wave style) shows "daily intake & output" behavioral patterns. Language proficiency shown as separate horizontal bars with level labels.
- **When to use:** Creative roles where visual boldness is itself a signal of ability. The dark background and stark red bars create a strong aesthetic identity that functions as portfolio evidence.
- **Interesting properties:** The wavy line chart for "daily intake & output" echoes Michael Anderson's daily chart — using a non-standard chart form to show rhythmic behavioral data. The combination of relative skill bars + behavioral pattern + language bars encodes three completely different data types in a single visual.
- **Marks:** Vertical bars (skills), wavy lines (daily pattern), horizontal bars (languages)
- **Channels:** Bar height = relative skill level; color (red vs. dark) = skill vs. background; line shape = behavioral rhythm; horizontal bar length = language proficiency level
- **Annotation options:** Skill name labels (rotated on bars), domain group labels below, language level text (mother tongue / fluent / advanced / beginner)
- **Data types suited for:** Quantitative (relative), categorical (skill domains, languages), temporal/cyclical (daily pattern)
- **Interesting feature extraction/manipulation:** All skill levels are self-assessed and unlabeled — the visual conveys relative ranking, not absolute measurement.

---

### Navdeep Raj Resume — Vertical Timeline + Categorical Skill Bar Chart (p.141)
- **What it shows:** Left panel: a vertical timeline of career events. Center/right panel (expanded detail): two grouped bar charts — "Practice Areas" and "Technologies" — each showing relative proficiency as horizontal bars of varying length, with a secondary text column of additional skills labeled "More."
- **When to use:** Technology roles where skill comparison across a long list of tools is central. The two-section split (primary skills as bars, secondary skills as text) manages the long-tail of minor skills without cluttering the main chart.
- **Interesting properties:** The "More" column beside the bar chart is an elegant solution to the long-tail problem — skills that exist but are not strong enough to warrant a bar are acknowledged without visual noise. This is a partial-chart approach — the chart deliberately omits some data points and substitutes text.
- **Marks:** Horizontal bars (primary skills), text list (secondary skills), icon glyphs (skill category markers on left edge)
- **Channels:** Bar length = relative proficiency; vertical position = skill rank within category; icon glyph = skill domain identity; color hue = bar category (Practice Areas vs. Technologies)
- **Annotation options:** Skill names as y-axis labels, category headers, "More" secondary text column
- **Data types suited for:** Categorical (skill domains), quantitative (relative proficiency)
- **Interesting feature extraction/manipulation:** Separating skills into "chart-worthy" and "list-worthy" tiers is a data simplification decision that prevents clutter while maintaining completeness.

---

### Geographic Map Resume — Ana Foureaux Frazao (p.142)
- **What it shows:** 2-page resume. Page 1: metaphor-driven — a heart illustration (passions), a brain/mind illustration (analytical traits), and a face/person image — each with callout labels for personality traits, languages (as bar charts), and interests. Page 2: a world map with color-coded location pins marking international work experience. Pie chart for primary skill sets. Company logos and work history text.
- **When to use:** Candidates with strong international experience, where geographic breadth is a key differentiator. Also useful for creatives who want to show personality as a data layer.
- **Interesting properties:** Using anatomical metaphors (heart = passions, brain = analytical traits) is a strong semantic novelty — the shape of the mark itself carries the meaning. The map uses color-coded pins where pin color = type of work (Presentation Design, International PR, Law) so the map encodes two variables simultaneously.
- **Marks:** Illustrated anatomical shapes (heart, brain) as glyph containers, map with colored pins, pie chart slices, horizontal language bars
- **Channels:** Pin color = work type; pin position = geographic location; pie slice size = skill domain proportion; bar length = language proficiency; illustrated shape = personal domain (heart=passion, brain=intellect)
- **Annotation options:** Callout labels from heart/brain, language level labels, work type legend for map, skill labels on pie
- **Data types suited for:** Spatial (geographic), categorical (skill domains, work types, personality traits), quantitative (relative proficiency)
- **Interesting feature extraction/manipulation:** Country borders removed from the map — simplified to landmasses only, reducing visual noise and keeping focus on pin locations.

---

### Chris Robertson Resume — Timeline + Map + Custom Glyph Skill Chart (p.143)
- **What it shows:** Top section: a horizontal timeline (1999–present) showing employment locations (US states + international) with career title progression. Map shows only the relevant US states and countries. Middle section: a custom skill chart where mustache/wave glyphs in three rows represent proficiency tiers (Awesome / Average / Noob) — a playful, non-standard ordinal encoding. Bottom section: trophy icons for awards (quantity shown by number of trophy marks), a pie chart for code skill breakdown.
- **When to use:** Creative/design roles where demonstrating personality and creative thinking through the resume format itself is part of the message. Avoid for conservative industries.
- **Interesting properties:** The mustache glyph for skills is a spectacular example of a domain-specific, metaphor-driven mark — the mustache is associated with creative/hipster culture. The glyph SIZE within each tier (larger mustache = more awesome) adds a second channel. This is semantically novel: a glyph whose shape itself signals the domain (creative culture) rather than the data.
- **Marks:** Location pins on map (timeline integration), mustache glyphs (skills), trophy icon counts (awards), pie slices (code breakdown)
- **Channels:** Horizontal position = time (timeline); map position = geographic location; mustache row = proficiency tier (ordinal); icon count = award quantity; pie slice = code domain proportion
- **Annotation options:** Software names below each mustache column, company names and dates on timeline, award competition names in bar section
- **Data types suited for:** Temporal, spatial, ordinal (skill tiers), quantitative (award counts)
- **Interesting feature extraction/manipulation:** Collapsing the world map to show only relevant regions (specific US states + Dubai/Egypt/Lebanon) saves space and focuses attention on the meaningful geographic narrative.

---

### Logo-Only Resume — Adrian Saker (p.144)
- **What it shows:** A resume where company name text is replaced entirely by company brand logos, grouped into rows by employer (left side) with corresponding client logos beside them. Additional logo groups for Skills, Education, Memberships, Interests, and Software tools.
- **When to use:** Candidates with experience at well-known, instantly recognizable brands where the logo alone communicates more than the company name. Also effective when the client portfolio is impressive.
- **Interesting properties:** Logos function as **marks that carry both identity and brand reputation** in a single glyph. The reader processes "IBM," "Coca-Cola," "American Express" visually within milliseconds. No text needed — the brain decodes brand logos faster than it reads text. Semantically novel: logos are usually decorative; here they ARE the primary data encoding.
- **Marks:** Brand logo images (company/client/skill icons)
- **Channels:** Logo identity = company/client name; row grouping = employer relationship; section grouping = CV category (employment/education/interests/software)
- **Annotation options:** Employer name labels on left (row headers), section labels
- **Data types suited for:** Categorical (companies, skills, interests), relational (client-employer groupings)
- **Interesting feature extraction/manipulation:** This design only works if the audience recognizes the logos — it fails completely for unknown brands. It requires careful curation of which logos to include.

---

### Sascha Kuntze Resume — Growth Area Chart + Social Metrics + Logo Grid (p.145)
- **What it shows:** Top section: area chart timeline (2001–2010) with overlapping color bands for education, work, and "other experience." Milestone labels for each role annotated along the chart. Bottom section: client logo grid, social media follower counts (YouTube, Twitter, Google), awards list in large typographic display, recent "pitches" as Pac-Man game icon.
- **When to use:** Marketing/creative candidates where quantitative social proof (followers, awards) is a key differentiator. The combination of career timeline + social metrics is unusual and effective for digital/social roles.
- **Interesting properties:** Social media metrics displayed as large typographic numbers create immediate visual weight — 274,876 YouTube views, 3,012 Twitter followers. The Pac-Man icon for "recent pitches" is a semantic playfulness that signals creative awareness. The "I AM THE SUM OF WHAT I'VE DONE" photo of the candidate pointing at the timeline creates a literal human-data connection.
- **Marks:** Overlapping area fills, logo icons (client grid), large typographic numbers, photo of candidate
- **Channels:** Area height = career activity volume; horizontal position = time; number size = social metric magnitude; logo identity = brand recognition
- **Annotation options:** Role labels on timeline, social platform names, award counts
- **Data types suited for:** Temporal, quantitative (social metrics, awards), categorical (skill domains, clients)
- **Interesting feature extraction/manipulation:** Social metrics are absolute numbers as of a specific date — they communicate scale but not growth trend.

---

### David P. Ingram Resume — Testimonial + Achievement Metrics + Honeycomb Chart (p.146)
- **What it shows:** A multi-section resume combining: company logo timeline (top right), large pull-quote testimonials from named executives, key achievement metrics as large typographic numbers ($1.6M raised, 300% contract value increase, 88% revenue growth), a honeycomb/hexagon chart for "I Like / I Dislike" categories, and a horizontal timeline at the bottom with narrative milestones.
- **When to use:** Business/product management roles where quantified achievements are the primary signal. The testimonial section converts qualitative endorsements into a visual element.
- **Interesting properties:** The honeycomb chart for personality traits ("I Like / I Dislike") is semantically novel for a resume — it uses a spatial cluster of hexagons where positive traits radiate outward from the candidate's name and negative traits (what the candidate dislikes in workplaces) point inward. This converts subjective personality data into a spatial proximity encoding.
- **Marks:** Hexagon tiles (personality traits), large typographic numbers (achievements), pull-quote text blocks, company logos (timeline)
- **Channels:** Hexagon position = positive vs. negative trait valence; large number magnitude = achievement scale; logo identity = employer brand
- **Annotation options:** Trait labels in hexagons, dollar amounts, percentage labels, executive names on testimonials
- **Data types suited for:** Quantitative (financial achievements), categorical (personality traits, employers), qualitative (testimonial text)
- **Interesting feature extraction/manipulation:** Converting qualitative testimonials to a visual element by selecting the most impactful quotes and attributing them to named, titled sources creates visual social proof without fabricating data.
