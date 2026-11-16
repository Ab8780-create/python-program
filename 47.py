import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Priya', 'Neha'],
    'Age': [21, None, 20, 23],
    'Marks': [85, 90, None, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove rows containing missing values
print("\nAfter dropna():")
print(df.dropna())

# Replace missing values
print("\nAfter fillna():")
print(df.fillna(0))
