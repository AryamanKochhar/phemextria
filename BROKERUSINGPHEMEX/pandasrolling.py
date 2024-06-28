import pandas as pd
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'group': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A'],
    'value': [1, 3, 2, 5, 6, 7, 8, 6, 5, 2]
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

rolling_mean_grouped = df.groupby('group')['value'].rolling(window=3).mean().reset_index(level=0, drop=True)
print(rolling_mean_grouped)
