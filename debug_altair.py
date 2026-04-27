import altair as alt
import pandas as pd
import numpy as np

# Mocking the df to exactly replicate the situation
df = pd.DataFrame({
    'Total_Spps_richness': np.linspace(30, 100, 60),
    'Mean_CC_Yield': np.linspace(100, 2000, 60),
    'Dominance Normalized': np.linspace(0, 1, 60),
    'Yield Quantile': ['Low']*20 + ['Medium']*20 + ['High']*20
})

points = alt.Chart(df).mark_circle(opacity=0.8, stroke='white', strokeWidth=1).encode(
    x=alt.X('Total_Spps_richness:Q', title='Total Species Richness (Biodiversity)'),
    y=alt.Y('Mean_CC_Yield:Q', title='Mean Clean Coffee Yield (kg)'),
    color=alt.Color('Yield Quantile:N', scale=alt.Scale(scheme='viridis')),
    size=alt.Size('Dominance Normalized:Q', scale=alt.Scale(range=[20, 800]), title='Coffee Dominance Index')
)

chart = points.properties(width=700, height=500)
chart.save('debug_chart.html')
print("Chart generated. Checking outputs...")
