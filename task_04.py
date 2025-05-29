import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (load only required columns to save memory)
cols = ['Accident_Index', 'longitude', 'latitude', 'Accident_Severity',
        'Number_of_Vehicles', 'Number_of_Casualties', 'Day_of_Week',
        'Time', 'Local_Authority_(District)']

df = pd.read_csv("AccidentsBig.csv", usecols=cols)

# Quick data check
print(df.head())

# Handle missing values
df.dropna(subset=['Time', 'longitude', 'latitude'], inplace=True)

# Convert Time to Hour
df['Hour'] = df['Time'].str[:2].astype(int)

# --- ACCIDENT SEVERITY COUNT ---
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Accident_Severity', palette='coolwarm')
plt.title("Accident Severity Count")
plt.xlabel("Severity Level")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# --- ACCIDENTS BY DAY OF WEEK ---
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='Day_of_Week', palette='viridis')
plt.title("Accidents by Day of Week")
plt.xlabel("Day of Week (1=Sunday, 7=Saturday)")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

# --- ACCIDENTS BY HOUR ---
plt.figure(figsize=(10, 4))
sns.histplot(df['Hour'], bins=24, kde=True, color='orange')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Accident Count")
plt.tight_layout()
plt.show()

# --- ACCIDENTS BY DISTRICT ---
top_districts = df['Local_Authority_(District)'].value_counts().head(10)
plt.figure(figsize=(10, 4))
sns.barplot(x=top_districts.index, y=top_districts.values, palette='mako')
plt.title("Top 10 Districts with Highest Accidents")
plt.xlabel("District")
plt.ylabel("Accident Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- ACCIDENT HOTSPOTS MAP (LAT-LONG) ---
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df.sample(5000), x='longitude', y='latitude', hue='Accident_Severity', palette='Set1', alpha=0.5)
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Severity", loc="upper right")
plt.tight_layout()
plt.show()
