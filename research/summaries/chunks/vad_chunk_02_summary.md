# [agent_17] Visualization Analysis and Design — pages 51-100

## Overview of Pages Covered

Pages 51–100 span three full chapters:
- **Chapter 2 (continued): What — Data Abstraction** (pp. 51–65)
- **Chapter 3: Why — Task Abstraction** (pp. 67–90)
- **Chapter 4: Analysis — Four Levels for Validation** (pp. 91–100)

---

## Data Types (Chapter 2 continued)

### Networks and Trees (p.51–52)
- **Network (graph):** specifies relationships between items. Nodes = items, links = relations between two items.
  - Nodes may have attributes (like items in a table); links can also have attributes.
  - Examples: social networks, gene interaction networks, computer networks.
  - Spatial layout is separate from the abstract concept of the network.
- **Trees:** networks with hierarchical structure; no cycles. Each child node has exactly one parent.
  - Examples: org chart, biological tree of life.

### Fields (p.52–55)
- **Field:** attribute values associated with cells from a **continuous domain** — conceptually infinitely many measurement points.
  - Examples: temperature maps, pressure fields, medical scans, simulated fluid data.
  - Fields require careful treatment of **sampling** (how frequently to measure) and **interpolation** (how to show values between sampled points).
  - Contrast with discrete data (tables, networks) where interpolation is meaningless.
- **Spatial fields:** field cells based on sampling at spatial positions. Tasks typically involve understanding **shape** (e.g. locating tumors in medical scans, comparing flow patterns over airfoils).
- **Scientific visualization (scivis):** focused on spatial data (given spatial positions).
- **Information visualization (infovis):** focused on abstract/nonspatial data (designer chooses use of space).
- **Grid types:** uniform grid → rectilinear grid → structured (curvilinear) grid → unstructured grid (increasing flexibility, increasing storage requirements) (p.54).

### Geometry (p.54–55)
- Shape of items with explicit spatial positions: points, 1D lines/curves, 2D surfaces/regions, 3D volumes.
- Intrinsically spatial; often hierarchical.
- May lack attributes; purely geometric data is only vis-interesting when derived/transformed (e.g. contours from scalar fields).
- Geometry is often the spatial backdrop for overlaid additional information.

### Other Combinations (p.55–56)
- **Set:** unordered group of items.
- **List:** ordered group of items (also called array).
- **Cluster:** grouping based on attribute similarity.
- **Path (in network):** ordered set of segments formed by links connecting nodes.
- **Compound network:** network with an associated tree (all network nodes are leaves of the tree).
- Complex hybrid combinations (multiple basic types) are common in real-world applications.

### Dataset Availability (p.56)
- **Static (offline):** entire dataset available at once. Default assumption.
- **Dynamic (online, streaming):** dataset trickles in during the vis session; items/attributes may be added, deleted, or changed.
- Designing for streaming data adds significant complexity.

---

## Attribute Types (p.56–59)

Figure 2.7 (p.57) summarizes the type hierarchy:

```
Attributes
  ├── Categorical (nominal): no implicit ordering; hierarchical structure possible
  └── Ordered
        ├── Ordinal: well-defined ordering, but no full arithmetic (e.g. shirt sizes, rankings)
        └── Quantitative: supports full arithmetic (heights, weights, temperatures, prices)
              Ordering Direction:
                ├── Sequential: homogeneous range from min to max
                ├── Diverging: two sequences meeting at a zero point
                └── Cyclic: values wrap around (hours of day, days of week, months of year)
```

- **Categorical** (p.57): no implicit ordering; can only distinguish same/different. External orderings (e.g. alphabetical) can be imposed but are not intrinsic.
- **Ordinal** (p.57–58): well-defined ordering but arithmetic meaningless ("large minus medium" has no value). Examples: shirt sizes, rankings, survey scales.
- **Quantitative** (p.58): supports arithmetic. Examples: height, weight, temperature, stock price, integer counts. Includes both integers and real numbers.
- **Sequential vs. Diverging** (p.58): sequential = min to max (e.g. mountain heights above sea level); diverging = two sequences meeting at zero (e.g. full elevation including below sea level).
- **Cyclic** (p.59): values wrap around — hour of day, day of week, month of year.
- **Hierarchical attributes** (p.59): temporal or geographic data can be aggregated hierarchically (day → week → month → year; postal code → city → state → country).

---

## Data Semantics (p.59–64)

### Key vs. Value Semantics (p.59–62)
- **Key attribute (independent attribute / dimension):** acts as index to look up values.
- **Value attribute (dependent attribute / measure):** the dependent data looked up by a key.
- This distinction matters enormously for tables and fields.

#### Flat Tables (p.59–60)
- One key; may be implicit (row number) or explicit (unique identifier column).
- Keys must be unique; quantitative attributes are typically unsuitable as keys (duplicates likely).
- Keys may be categorical or ordinal.

#### Multidimensional Tables (p.61)
- Multiple keys required to look up an item; combination of all keys must be unique.
- Example: gene × time → activity level.
- Determining which attributes are keys vs. values may itself be the vis goal.

#### Fields (p.62)
- Spatial position acts as a **quantitative key**.
- Fields differ from tables because useful answers are returned for all locations in a range, not just exact sampled points.
- Multidimensional = multiple keys; multivariate = multiple values.
  - **Scalar field:** one value attribute per point (univariate).
  - **Vector field:** multiple attribute values per point (direction + magnitude; e.g. air velocity).
  - **Tensor field:** array of attributes per point (e.g. stress in 3D: 9 numbers).

### Temporal Semantics (p.63–65)
- Temporal attributes relate to time; complicated by rich hierarchical and periodic structure.
- **Time-varying data:** time is a key attribute. Example: sensor network tracking animal locations.
- **Temporal value:** date or duration as a dependent value, not a key.
- **Time-series dataset:** ordered sequence of time-value pairs; special case of tables where time is the key.
- Typical time-series tasks: finding trends, correlations, variations at multiple scales (hourly, daily, weekly, seasonal).
- "Dynamic" is ambiguous: sometimes means time-varying semantics, sometimes means streaming data — Munzner carefully distinguishes these.

---

## Task Abstraction Framework (Chapter 3, pp. 67–90)

### Why Analyze Tasks Abstractly? (p.68–69)
- Translating domain-specific task descriptions into abstract form reveals similarities that would otherwise be obscured by different vocabulary.
- Example: "contrast prognosis between patient groups" and "see if tissue sample results match" are both instances of "compare values between two groups."
- A small, carefully chosen vocabulary of verbs (actions) and nouns (targets) is used to describe user goals precisely.
- Same vis tool may support many goals; useful to consider one goal at a time.
- Task abstraction can and should guide data abstraction.

### Three-Level Action Hierarchy (p.70–71, Figure 3.2)

#### Level 1: Analyze (high-level)
- **Consume:** use existing information
  - **Discover (p.71–72):** find new knowledge not previously known; generate or verify hypotheses. Classic motivation for interactive idioms.
  - **Present (p.72–73):** communicate something specific and already understood to an audience; tell a story with data. Knowledge is known to presenter in advance.
  - **Enjoy (p.73):** casual encounter with vis, driven by curiosity rather than pressing need. Example: Name Voyager tool (p.73–74).
- **Produce:** generate new material
  - **Annotate (p.74):** add graphical or textual annotations to existing visualization elements (e.g. text-label a cluster).
  - **Record (p.74–75):** save/capture vis elements as persistent artifacts — screenshots, bookmarks, parameter settings, interaction logs, graphical history (e.g. Tableau's graphical history feature).
  - **Derive (p.75–78):** produce new data elements from existing ones. Key insight: **don't just draw what you're given; decide what to show, create it with transformations, and draw that** (p.76).

**On Derive (p.75–78):**
- Designers actively choose data abstraction; it is not simply given by the user's data.
- Derived attributes can change data type (quantitative → ordinal → categorical).
- Derived attributes can require external data (city name → latitude/longitude via lookup).
- Derived attributes can use arithmetic, logical, or statistical operations.
- Example of derived subtraction attribute: trade balance = exports − imports. Encoding the derived attribute directly is easier to perceive than judging difference between two raw curves (p.77–78).
- Datasets can be transformed into entirely different types (e.g. genomics table → similarity network: [Davidson et al. 01]).

#### Level 2: Search (mid-level) (p.78–80)
Broken down by whether the identity and location of the target are known:

| Search type | Target known | Location known |
|---|---|---|
| **Lookup** | Yes | Yes |
| **Locate** | Yes | No |
| **Browse** | No | Yes |
| **Explore** | No | No |

- **Lookup:** user knows both what and where (e.g. finding humans in a phylogenetic tree by knowing their classification).
- **Locate:** known target at unknown location (e.g. finding rabbits in a phylogenetic tree — they are lagomorphs, not rodents).
- **Browse:** unknown exact target at known location (e.g. examining share prices on a specific date across multiple lines).
- **Explore:** unknown target at unknown location, often starting from an overview. Examples: searching for outliers in a scatterplot, anomalous spikes in time-series data, spatially dependent patterns in a choropleth map.

#### Level 3: Query (low-level) (p.80)
Three scopes for querying the targets found:
- **Identify:** single target — return its characteristics.
- **Compare:** multiple targets — compare their characteristics. More demanding than identify.
- **Summarize (overview):** all possible targets — provide comprehensive view. Extremely common goal in vis.

### Targets (p.80–82, Figure 3.6)

**All data:**
- **Trends (patterns):** high-level characterization of patterns — increases, decreases, peaks, troughs, plateaus.
- **Outliers (anomalies, deviants, surprises):** data that doesn't fit the backdrop trend.
- **Features:** any particular structures of interest (task-dependent).

**Attributes:**
- Individual value
- Extremes (minimum or maximum)
- Distribution of all values
- **Multiple attributes:** dependencies, correlations, similarities

**Network data:**
- Topology (overall structure of interconnections)
- Paths (specific routes between nodes)

**Spatial data:**
- Shape

### How: A Preview (p.82–83, Figure 3.7)
Four major families of how-choices:
1. **Encode:** arrange data spatially (express, separate, order, align, use given spatial data); map with nonspatial channels (color: hue/saturation/luminance; size; angle; curvature; shape; motion: direction/rate/frequency).
2. **Manipulate:** change view, select elements, navigate viewpoint.
3. **Facet:** juxtapose and coordinate multiple views; partition data between views; superimpose layers.
4. **Reduce:** filter data; aggregate data; embed focus and context together.

### Examples of What-Why-How Analysis (pp. 84–89)

**Example 1: SpaceTree vs. TreeJuxtaposer (p.84–86)**
- Same what (large tree) and why (present a path between two nodes).
- Different how: SpaceTree uses aggregation/filtering on unselected items; TreeJuxtaposer uses arrange to ensure visibility.

**Example 2: Deriving Strahler Numbers (p.86–87)**
- Derive a quantitative importance attribute (Strahler number) for each node → filter to show only top 5000 nodes → summarize tree topology.
- Strahler number = centrality metric; global computation (not just local neighborhood).
- Result: recognizable skeleton of a tree with >500,000 nodes.

**Example 3: Computational Fluid Dynamics Derived Spaces (p.87–89)**
- Original: time-varying spatial field (velocity on curvilinear mesh around airfoil).
- Derive: many new quantitative attributes (vorticity, entropy, enthalpy, pressure, temperature).
- Encode each pair of derived variables into a scatterplot view.
- Facet: multiple juxtaposed views coordinated with shared color highlighting.
- Result: features invisible in physical space become clearly distinguishable in derived spaces.

---

## Four Levels for Validation (Chapter 4, pp. 91–100)

### Four Nested Levels of Vis Design (p.92–94, Figure 4.2)
1. **Domain situation:** specific application domain, target users, their questions, their data.
2. **Data/task abstraction:** map domain-specific problems and data into generic, domain-independent forms.
3. **Visual encoding / interaction idiom:** specific way to create and manipulate the visual representation.
4. **Algorithm:** efficient computational procedures to implement the idiom.

Each level feeds into the next. Wrong choices at upstream levels cascade to all downstream levels.

### Domain Situation Level (p.94–96)
- Outcome: identification of detailed questions and data characteristics of target users.
- Methods: interviews, observations, user research.
- Common pitfall: making assumptions rather than engaging with actual users.
- What users say they do ≠ what they actually do (introspection is insufficient).
- Requirements must be specific enough to be useful (e.g. "What is the density of coverage and where are the gaps across a chromosome?" — useful; "What is the genetic basis of disease?" — too general).

### Task and Data Abstraction Level (p.96)
- Task blocks are *identified* (browsing, comparing, summarizing).
- Abstract data blocks are *designed* — a creative, active choice to possibly transform original data.
- Goal: determine which data type supports a visual encoding that addresses user's problem.
- Pitfall: doing abstraction implicitly and without justification (example: early web vis papers implicitly assumed users needed a visual map of the web's hyperlink graph — users just needed to find pages, not understand topology).

### Visual Encoding and Interaction Idiom Level (p.96–98)
- Two concerns: (a) encoding idiom — what users see; (b) interaction idiom — how users change what they see.
- Design space is enormous; task/data abstraction from previous level is used to rule out unsuitable options.
- Some vis tools support a single idiom; others provide many.
- Example: Word Tree (Wattenberg & Viegas 08) — horizontal hierarchical tree of keywords + navigation by keyword selection.

### Algorithm Level (p.98)
- Design efficient algorithms to instantiate the chosen idiom.
- Multiple algorithms may implement the same idiom (e.g. ray casting, splatting, texture mapping all instantiate direct volume rendering).
- Concerns: computation speed, memory, accuracy.
- Algorithm and idiom concerns must remain separated: algorithm design = computational concerns; idiom design = human perceptual concerns.

### Threats to Validity (p.99–100, Figure 4.4)
| Level | Threat |
|---|---|
| Domain situation | You misunderstood their needs (wrong problem) |
| Data/task abstraction | You're showing them the wrong thing (wrong abstraction) |
| Visual encoding / interaction idiom | The way you show it doesn't work (wrong idiom) |
| Algorithm | Your code is too slow (wrong algorithm) |

### Validation Approaches (p.100)
Different threats require different validation methods. Validation approaches differ per level (details continue on next pages beyond chunk scope).

### Angles of Attack (p.98–100)
- **Problem-driven (top-down):** start at domain situation, work down through abstraction → idiom → algorithm. Often called a "design study." Much challenge lies at abstraction level. Process is iterative, not linear.
- **Technique-driven (bottom-up):** start with new idiom or algorithm; articulate assumptions at the level above.

---

## Design Process Guidance (Cross-chapter)

- **What-Why-How framework** is the central analysis/design tool of the book. Every vis instance can be described along three dimensions: what data, why the vis is used, how the idiom is constructed.
- **Nested model (four levels)** separates domain situation, abstraction, idiom, and algorithm for cleaner analysis and validation.
- **Principle of design as redesign** [Green 89]: vis design is iterative refinement, not linear (p.93).
- **Don't just draw what you're given** (p.76): actively decide on the right representation, derive new data if needed.
- Task abstraction should guide data abstraction (p.69, p.96).
- The hardest stage to get right is often the abstraction stage; designers frequently skip it.

---

## Common Mistakes and Anti-patterns

- Skipping the domain situation level entirely (p.98–99).
- Short-circuiting abstraction: assuming the first abstraction that comes to mind is correct, then jumping straight to idiom design.
- Making assumptions about user needs rather than observing users (p.94–95).
- Doing abstraction implicitly and without justification (example: early web vis tools encoding hyperlink topology when users just needed to find pages).
- Asking users to introspect about their needs instead of observing them in action (p.95).

---

## Practical Rules of Thumb

- Translate domain-specific task/data descriptions into the most generic terms possible (p.68).
- Consider a chained sequence of tasks (output of one feeds into next) for complex activities (p.69).
- For comparison tasks, encoding the *derived difference* attribute directly is preferable to requiring the user to judge the height difference between two raw curves (p.77).
- Ask whether to use data as-is or to derive/transform it before encoding (p.75).
- Describe actions at all three levels (analyze, search, query) to fully characterize a task (p.81).
- When a search returns a target, use identify/compare/summarize to describe the scope of subsequent querying (p.80).
- In problem-driven work: always go back and validate the domain situation even while working at lower levels (p.99).
