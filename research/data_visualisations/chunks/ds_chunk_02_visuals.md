# [agent_07] Data Sketches — pages 51-100

## Visualization Catalogue

---

### Film Flowers (p.53–58)
- **What it shows:** Each movie as a flower-shaped glyph. Petals represent individual genres. The size of the whole flower encodes the IMDb rating (or runtime). Colors represent genre categories. Number of petals = number of genres.
- **When to use:** Showing a multi-attribute categorical item (movies with multiple genres) where identity matters more than precise comparison. Avoid when precise quantitative comparison is needed.
- **Interesting properties:** Custom SVG path shapes (petal shape drawn with cubic Bezier curves). Colors are blended using CSS blend modes (multiply) and feathered with SVG Gaussian blur filter, making multi-genre flowers visually richer. One leaf = seen the movie; two leaves = saw it in theatres (personal encoding hidden in the mark shape). Flowers are arranged together as a collection/garden, not on axes.
- **Marks:** Custom petal paths (one per genre); circle (one per flower for blended color overlay); text (movie title label).
- **Channels:** Size/radius of overall flower = IMDb rating (quantitative); number of petals = number of genres (quantitative, ordinal); color hue (per petal/per genre circle) = genre category (categorical); position = no data encoding, used for aesthetic arrangement; opacity + blend mode = genre overlap/blending effect.
- **Annotation options:** Title labels; legend mapping color to genre; personal annotations (leaf count for personal viewing history).
- **Data types suited for:** Quantitative (rating/size), categorical (genre/color), derived count (number of genres).
- **Interesting feature extraction/manipulation:** Movies aggregated by genre combination. Rating maps to flower size — a natural metaphor (bigger = better/more impressive). Multi-genre movies get overlapping colored circles showing genre mixing.

---

### Olympic Feathers (p.62–76)
- **What it shows:** Every Olympic gold medal from 1896 to 2016, across all sporting disciplines, organized as five concentric "feather" circles (matching the Olympic logo). Each sport is one "feather" within a circle; each medal is one arc segment within the feather. Time (Olympic edition/year) is encoded as radial distance from center. Continent of winning country is encoded in color.
- **When to use:** Showing temporal change across many parallel categories simultaneously, where the categories have a natural grouping (5 groupings here = 5 circles). Excellent for revealing which categories dominated which eras. Avoid for precise quantitative comparison — radial position is less accurate than linear.
- **Interesting properties:** Radial layout inspired by peacock tail feathers. Each medal occupies the same arc length regardless of how many medals a sport has — this creates white space in some feathers (sports only held in some editions) that itself encodes historical gaps. Inner symmetry: men's events on one side of each feather, women's on the other. Radial gradient background (bluish/reddish per half) distinguishes gender without color-encoding each medal. Hover reveals individual medal detail. Hover on year highlights all medals from that edition across all sports.
- **Marks:** Arc segments (one per gold medal); feather outline (custom SVG path); text annotations for sport names and historical anecdotes; white circle superimposed on medal = Olympic or world record.
- **Channels:** Radial distance from center = Olympic edition/year (temporal, quantitative); angular position within circle = sport (categorical); color hue of arc segment = continent of winning country (categorical, 5 levels matching Olympic ring colors); arc length (constant) = one medal; background gradient color = gender (binary categorical); white circle overlay = record status (binary).
- **Annotation options:** Sport name labels around the feather; textual annotations for unusual historical events; hover tooltips showing event, edition, winner, record status; highlighted edition on hover of year notations.
- **Data types suited for:** Temporal (year/edition), categorical (sport, country, continent, gender), binary (record status).
- **Interesting feature extraction/manipulation:** Each medal = equal arc regardless of sport size — a deliberate simplification that favors historical overview over proportionality. Country → continent mapping required as a data transformation. Sorted by continent winning most medals per edition (ranked order), adding an additional data layer.

---

### Dive Fractals (p.78–88)
- **What it shows:** Synchronized diving scores from the 2016 Olympics. Each team's performance across all rounds of an event is shown as a sweeping fractal line flow. The overall shape encodes score; the texture encodes execution variability.
- **When to use:** Showing multi-round sequential scores for multiple competing teams, where the aesthetic metaphor (silk/water) reinforces the subject matter. Avoid when precise numerical comparison is the goal — this is more data art than analytical chart.
- **Interesting properties:** Based on Dan Gries' "Sweeping Fractal Lines" algorithm. The "squiggly" line shape is generated by fractal subdivision of a straight line, with the midpoint y-position varied using execution scores. The fractal morphs from one round to the next, creating a flowing animation. Colors are the two primary colors of each team's national flag. The height between each starting and ending fractal line = the score for that round. The radius of each fractal circle = the difficulty score of that dive.
- **Marks:** Fractal line drawn to canvas (one per round transition per team); each set of fractal lines forms a "flow" (one per team).
- **Channels:** Height of each fractal zone = score for that round (quantitative); radius of circular fractal = difficulty score (quantitative); squiggliness/texture of line = execution score variation (quantitative, encoded into shape noise); color hue = team's national colors (categorical/identity); vertical position = round number (ordinal/sequential); animation speed = score height (the taller the zone, the longer the animation).
- **Annotation options:** Team name, country, score per round; hover reveals detailed score breakdown for a round; click filters all flows by that round.
- **Data types suited for:** Quantitative (scores, difficulty), ordinal (rounds), categorical (teams/countries).
- **Interesting feature extraction/manipulation:** Execution scores used to seed the fractal subdivision algorithm — the data controls the shape of the fractal noise, making texture a data channel. Difficulty score maps to radius (size), overall score maps to height (length/position). Three teams per event shown side by side (Silver, Gold, Bronze order).

---

### My Life in Vacations — Compressed Timeline (p.92–100)
- **What it shows:** Personal vacation history from birth to present, one row per year. Each vacation is a colored rectangle. The time axis is non-linear: months with no vacation are compressed/squeezed; vacation months have full space. This gives vacations visual prominence despite occupying <10% of actual time.
- **When to use:** Showing sparse events over a long time range where the events are the focus, not the gaps. Also for personal/biographical data visualizations. Avoid when precise temporal positioning matters or when the audience needs to compare exact dates across rows.
- **Interesting properties:** The compressed time axis is the key innovation — non-linear time scale that distorts empty periods to give prominence to the data of interest. The year is centered on August (typical vacation month). Each vacation rectangle contains internal texture encoding the trip type (nature = randomly drawn squiggly line; culture = regular line pattern; sun = sun icon; snow = snow icon). Icons on top of rectangles encode travel companions (heart = boyfriend; blue circle = father; pink circle = mother). Blur filter on rectangle edges encodes uncertainty: horizontal blur = uncertain exact dates; vertical blur = uncertain enjoyment; both = both unknown. Hover interaction highlights the same month across all years.
- **Marks:** Colored rectangles (one per vacation); internal texture patterns (lines, icons) within each rectangle; person icons above each rectangle; month-dividing curved lines connecting rows; text annotations for major life events.
- **Channels:** Horizontal position = time within year (compressed/non-linear temporal); vertical position = year/age (ordinal, one row per year); rectangle width = vacation duration (quantitative, but compressed); rectangle color = not specified as data-encoding (bright colors for visual appeal); internal texture/pattern = vacation type/purpose (categorical); icon overlay = travel companion (categorical); blur direction and intensity = uncertainty in dates (horizontal) and enjoyment (vertical); presence/absence of special icons = unusual events (Mickey Mouse for Disney, Olympic torch for Olympics attended, safari animal for safari trips).
- **Annotation options:** Life event annotations on the side; legend explaining all visual touches; hover tooltip highlighting same month across years.
- **Data types suited for:** Temporal (dates, duration), categorical (trip type, companions), binary/presence (uncertainty), personal/biographical narrative.
- **Interesting feature extraction/manipulation:** Months compressed based on vacation presence/absence — a non-standard time scale transformation. Purpose/type of vacation added as a manually coded variable. Enjoyment rating added as a subjective manually recorded variable. Uncertainty (forgotten details) itself encoded as a visual property rather than excluded or omitted.
