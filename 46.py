import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

print("CSV File Data:")
print(df)

# Read Excel file
df2 = pd.read_excel("students.xlsx")

print("\nExcel File Data:")
print(df2)
