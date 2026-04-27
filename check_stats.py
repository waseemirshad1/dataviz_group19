import pandas as pd
df = pd.read_excel("~/dataviz_group19/data/g0r72a_data_ines_2526-main/Environmental_and_management_variables.xlsx")
print(df['Coffee dominance'].describe())
print(df['Coffee dominance'].head())
