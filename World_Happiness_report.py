

import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Load Dataset ---
DATA_PATH = "world-happiness-report-2021.csv"  # update path if needed
df = pd.read_csv(DATA_PATH)

# --- 2. Overall Happiness Scores ---
mean_score = df["Ladder score"].mean()
median_score = df["Ladder score"].median()

print("### 1. Overall Happiness Scores ###")
print(f"Mean Happiness Score: {mean_score:.2f}")
print(f"Median Happiness Score: {median_score:.2f}\n")

# --- 3. Country Rankings ---
df_sorted = df.sort_values(by="Ladder score", ascending=False)

top5 = df_sorted.head(5)[["Country name", "Ladder score"]]
bottom5 = df_sorted.tail(5)[["Country name", "Ladder score"]]

print("### 2. Country Rankings ###")
print("\nTop 5 Happiest Countries:")
print(top5.to_string(index=False))

print("\nBottom 5 Happiest Countries:")
print(bottom5.to_string(index=False))

# --- 4. Score Disparity ---
highest = df_sorted.iloc[0]["Ladder score"]
lowest = df_sorted.iloc[-1]["Ladder score"]

percent_diff = ((highest - lowest) / lowest) * 100

print("\n### 3. Score Disparity ###")
print(f"Relative Percent Difference: {percent_diff:.2f}%")
print(
    f"Interpretation: The top-ranked country ({df_sorted.iloc[0]['Country name']}) "
    f"has a happiness score over {percent_diff:.0f}% higher than the lowest-ranked country "
    f"({df_sorted.iloc[-1]['Country name']}), showing vast inequality in well-being globally."
)

# --- 5. Average Happiness Score by Continent ---
# Some datasets have 'Regional indicator', which we’ll treat as continent/region
region_means = df.groupby("Regional indicator")["Ladder score"].mean().sort_values(ascending=False)

print("\n### 4. Average Happiness Score by Continent/Region ###")
print(region_means)

# --- 6. Visualization ---
FIG_OUT = "average_by_continent.png"

plt.figure(figsize=(10, 6))
region_means.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Happiness Score by Continent/Region (2021)", fontsize=14, weight="bold")
plt.ylabel("Average Ladder Score")
plt.xlabel("Region")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save and Show
plt.savefig(FIG_OUT, dpi=300, bbox_inches="tight")
plt.show()   # shows inline
plt.close()

print(f"\nBar chart saved to: {FIG_OUT}")
