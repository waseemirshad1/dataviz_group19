from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool
import math
import numpy as np
q = np.array([0, 0, 1, 1, 2, 2])
r = np.array([0, 1, 0, 1, 0, 1])

source = ColumnDataSource(dict(q=q, r=r, hatch=['/', '\\', '/', '\\', '/', '\\']))
p = figure(width=400, height=400, tools="hover,pan,wheel_zoom")
p.hex_tile(q="q", r="r", size=1, fill_color="blue", hatch_pattern="hatch", source=source)
output_file("test_bokeh.html")
save(p)
