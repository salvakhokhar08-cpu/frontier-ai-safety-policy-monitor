import pandas as pd

# Load the dataset
df = pd.read_excel("data/raw/oecd_ai_incidents.xlsx.xlsx")

# Basic info
print("Shape (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isnull().sum())