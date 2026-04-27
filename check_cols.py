import pandas as pd
df = pd.read_excel("~/dataviz_group19/data/g0r72a_data_ines_2526-main/Environmental_and_management_variables.xlsx")
print([c for c in df.columns if 'dominance' in c.lower() or 'coffee' in c.lower()])
