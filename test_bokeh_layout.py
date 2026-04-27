import numpy as np
from bokeh.plotting import figure, save, output_file
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
import random

# simulate random data
np.random.seed(42)
random.seed(42)

df_hex = pd.DataFrame({
    'Site ID': [f"Ge{i}" for i in range(60)],
    'Coffee density in 30 x 30m plot': np.random.uniform(500, 2000, 60),
    'Mean_CC_Yield': np.random.uniform(50, 1500, 60),
    'Trend': random.choices(['Declining', 'Safe'], k=60)
})

# generating contiguous layout
directions = [(1,0), (1,-1), (0,-1), (-1,0), (-1,1), (0,1)]
coords = [(0,0)]
visited = set(coords)

while len(coords) < 60:
    curr = random.choice(coords)
    d = random.choice(directions)
    cand = (curr[0]+d[0], curr[1]+d[1])
    if cand not in visited:
        visited.add(cand)
        coords.append(cand)

max_dens = df_hex['Coffee density in 30 x 30m plot'].max()

xs_list = []
ys_list = []
colors = []
hatches = []

for idx, (row, (q, r)) in enumerate(zip(df_hex.iterrows(), coords)):
    row = row[1]
    
    # center
    cx = np.sqrt(3) * (q + r/2)
    cy = 1.5 * r
    
    scale = 0.4 + (row['Coffee density in 30 x 30m plot'] / max_dens) * 0.5
    
    angles = [np.radians(60 * i + 30) for i in range(6)]
    xs = [cx + scale * np.cos(a) for a in angles]
    ys = [cy + scale * np.sin(a) for a in angles]
    
    xs_list.append(xs)
    ys_list.append(ys)
    
    colors.append('#ff6b6b' if row['Trend'] == 'Declining' else '#51cf66')
    hatches.append('/' if row['Trend'] == 'Declining' else '\\')

df_hex['xs'] = xs_list
df_hex['ys'] = ys_list
df_hex['color'] = colors
df_hex['hatch'] = hatches

source = ColumnDataSource(df_hex)

p = figure(title="Interactive Contiguous Hexagon Map", tools="pan,wheel_zoom,reset,save", match_aspect=True)
p.patches('xs', 'ys', source=source, fill_color='color', hatch_pattern='hatch', line_color="black", line_width=1, fill_alpha=0.85)

hover = HoverTool(tooltips=[
    ("Site ID", "@{Site ID}"),
    ("Trend", "@Trend"),
    ("Density", "@{Coffee density in 30 x 30m plot}{0.0}"),
    ("Yield", "@Mean_CC_Yield{0.0}")
])
p.add_tools(hover)
p.axis.visible = False
p.grid.visible = False

output_file("test_bokeh_layout.html")
save(p)
