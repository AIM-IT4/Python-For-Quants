
import pandas as pd

# Series and DataFrames
s = pd.Series([1, 2, 3, 4, 5], name="Example Series")
print(s)

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
print(df)

# Data cleaning and preparation
df['D'] = df['A'] + df['B']
print("After adding a new column D:", df)
