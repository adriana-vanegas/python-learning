import pandas as pd

pd.set_option('display.max.rows',234)
# pd.set_option('display.max.columns',18)

df = pd.read_csv(r'week_9_10/learning_pandas/world_population.csv')
print(df.head())


# Filter
max_10 = df[df['Country'] == 'Brazil']
print(max_10)