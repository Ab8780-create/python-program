import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Priya', 'Neha'],
    'Age': [21, 22, 20, 23],
    'Marks': [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nFirst 2 Records:")
print(df.head(2))

print("\nData Information:")
print(df.info())

print("\nStatistical Analysis:")
print(df.describe())

print("\nAverage Marks:")
print(df['Marks'].mean())

print("\nMaximum Marks:")
print(df['Marks'].max())
