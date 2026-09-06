import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_excel("data/raw/oecd_ai_incidents.xlsx.xlsx")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Create output folder for reports if it doesn't exist
os.makedirs("reports", exist_ok=True)

# --- Analysis 1: Incidents per country ---
country_counts = df['country'].value_counts()
print("Incidents per country:")
print(country_counts)

plt.figure(figsize=(8, 5))
country_counts.plot(kind='bar', color='steelblue')
plt.title("AI Safety Incidents by Country")
plt.xlabel("Country")
plt.ylabel("Number of Incidents")
plt.tight_layout()
plt.savefig("reports/incidents_by_country.png")
plt.close()

# --- Analysis 2: Incidents over time ---
incidents_by_date = df.groupby(df['date'].dt.date).size()
print("\nIncidents by date:")
print(incidents_by_date)

plt.figure(figsize=(8, 5))
incidents_by_date.plot(kind='line', marker='o', color='darkred')
plt.title("AI Safety Incidents Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Incidents")
plt.tight_layout()
plt.savefig("reports/incidents_over_time.png")
plt.close()

# --- Save a simple summary report ---
with open("reports/summary_report.txt", "w", encoding="utf-8") as f:
    f.write("Frontier AI Safety Policy Monitor - Summary Report\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Total incidents recorded: {len(df)}\n\n")
    f.write("Incidents by country:\n")
    f.write(country_counts.to_string())
    f.write("\n\nIncident titles:\n")
    for title in df['title']:
        f.write(f"- {title}\n")

print("\nAnalysis complete! Charts and report saved in the 'reports' folder.")