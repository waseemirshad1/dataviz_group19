import altair as alt
import pandas as pd
df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 2, 3], "z": [0.91, 0.95, 0.99], "yield": ["Low", "Medium", "High"]})
chart1 = alt.Chart(df).mark_circle().encode(
    x='x:Q', y='y:Q', size=alt.Size('z:Q', scale=alt.Scale(range=[50, 500]))
)
chart2 = alt.Chart(df).mark_circle().encode(
    x='x:Q', y='y:Q', size=alt.Size('z:Q', scale=alt.Scale(range=[50, 500], zero=False))
)
print("Chart 1 zero param:", chart1.encoding.size.scale.to_dict())
print("Chart 2 zero param:", chart2.encoding.size.scale.to_dict())
