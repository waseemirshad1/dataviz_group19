import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import os

base_path = "data/g0r72a_data_ines_2526-main/"
df_yield = pd.read_excel(base_path + "Coffee_yield.xlsx")
# calc trend
def calc_trend(row):
    y = [row['CC_Yield_2017'], row['CC_Yield_2018'], row['CC_Yield_2019']]
    x = [0, 1, 2]
    # slope
    m, b = np.polyfit(x, y, 1)
    return "Declining" if m < 0 else "Safe"

df_yield['Trend'] = df_yield.apply(calc_trend, axis=1)

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')

# layout 60 sites in a hex grid
cols = 10
for i, row in df_yield.iterrows():
    col = i % cols
    r = i // cols
    
    # hex grid math
    x = col * np.sqrt(3) + (np.sqrt(3)/2 if r % 2 == 1 else 0)
    y = r * 1.5
    
    trend = row['Trend']
    color = 'red' if trend == 'Declining' else 'green'
    hatch = '//' if trend == 'Declining' else '\\\\'
    
    size_radius = 0.5 + (row['Mean_CC_Yield'] / df_yield['Mean_CC_Yield'].max()) * 0.5
    
    hex_patch = RegularPolygon((x, y), numVertices=6, radius=size_radius, 
                               orientation=np.radians(30),
                               facecolor=color, edgecolor='black', hatch=hatch, alpha=0.7)
    ax.add_patch(hex_patch)
    ax.text(x, y, row['Site ID'], ha='center', va='center', fontsize=6)

ax.autoscale()
plt.axis('off')
plt.savefig('hex_test.png')
print("Done")
