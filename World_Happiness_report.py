import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# To display plots inline (only in Jupyter)
%matplotlib inline

print("Pandas version:", pd.__version__)
print("Numpy version:", np.__version__)

# ---------------------------
# Load dataset
# ---------------------------
df = pd.read_csv("world-happiness-report-2021.csv")

# Display first 5 rows
df.head()

# ---------------------------
# 1. Overall Happiness Score
# ---------------------------
mean_score = round(df["Ladder score"].mean(), 2)
median_score = round(df["Ladder score"].median(), 2)
print(f"Mean Happiness Score: {mean_score}")
print(f"Median Happiness Score: {median_score}")

# ---------------------------
# 2. Top and Bottom Countries
# ---------------------------
sorted_df = df.sort_values(by="Ladder score", ascending=False)
top5 = sorted_df.head(5)[["Country name", "Ladder score"]]
bottom5 = sorted_df.tail(5)[["Country name", "Ladder score"]]

print("\nTop 5 Happiest Countries:\n", top5.to_string(index=False))
print("\nBottom 5 Least Happy Countries:\n", bottom5.to_string(index=False))

# ---------------------------
# 3. Percent Difference
# ---------------------------
highest = top5["Ladder score"].max()
lowest = bottom5["Ladder score"].min()
percent_diff = round(((highest - lowest) / lowest) * 100, 1)
print(f"\nPercent Difference between highest and lowest scoring countries: {percent_diff}%")

# ---------------------------
# 4. Average Happiness by Region
# ---------------------------
region_avg = df.groupby("Regional indicator")["Ladder score"].mean().sort_values()

# Bar chart
plt.figure(figsize=(10,6))
sns.barplot(x=region_avg.values, y=region_avg.index, palette="viridis")
plt.title("Average Happiness Score by Region", fontsize=14)
plt.xlabel("Average Ladder Score")
plt.ylabel("Region")
plt.show()

# Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(x="Ladder score", y="Regional indicator", data=df, palette="coolwarm")
plt.title("Happiness Score Distribution by Region", fontsize=14)
plt.xlabel("Ladder Score")
plt.ylabel("Region")
plt.show()

# ---------------------------
# 5. Correlation Analysis
# ---------------------------
corr_gdp = round(df["Logged GDP per capita"].corr(df["Ladder score"]), 3)
corr_social = round(df["Social support"].corr(df["Ladder score"]), 3)

print(f"\nCorrelation with GDP per capita: {corr_gdp}")
print(f"Correlation with Social support: {corr_social}")

# Heatmap of correlations
plt.figure(figsize=(8,6))
sns.heatmap(df[["Ladder score","Logged GDP per capita","Social support",
                "Healthy life expectancy","Freedom to make life choices"]].corr(),
            annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=14)
plt.show()

# Scatter plots
plt.figure(figsize=(7,5))
sns.regplot(x="Logged GDP per capita", y="Ladder score", data=df, scatter_kws={"alpha":0.6})
plt.title("GDP per Capita vs Happiness Score", fontsize=14)
plt.show()

plt.figure(figsize=(7,5))
sns.regplot(x="Social support", y="Ladder score", data=df, scatter_kws={"alpha":0.6}, color="green")
plt.title("Social Support vs Happiness Score", fontsize=14)
plt.show()

# Distribution of happiness scores
plt.figure(figsize=(8,5))
sns.histplot(df["Ladder score"], bins=15, kde=True, color="skyblue")
plt.title("Distribution of Happiness Scores", fontsize=14)
plt.xlabel("Happiness Score")
plt.ylabel("Frequency")
plt.show()

# ---------------------------
# 6. Insights Table (as Figure)
# ---------------------------
summary_data = {
    "Metric": ["Mean Score", "Median Score", "Top Country", "Bottom Country", "Strongest Correlation"],
    "Value": [
        mean_score,
        median_score,
        f"{top5.iloc[0]['Country name']} ({top5.iloc[0]['Ladder score']})",
        f"{bottom5.iloc[-1]['Country name']} ({bottom5.iloc[-1]['Ladder score']})",
        "GDP per capita" if corr_gdp > corr_social else "Social support"
    ]
}

summary_df = pd.DataFrame(summary_data)

fig, ax = plt.subplots(figsize=(7,2))
ax.axis("off")
table = ax.table(cellText=summary_df.values, colLabels=summary_df.columns, loc="center")
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.2)
plt.title("Key Insights from World Happiness Report 2021", fontsize=12, pad=10)
plt.show()

# ---------------------------
# 7. Summary / Insights
# ---------------------------
print("\n📊 Summary of World Happiness Report 2021 Analysis\n")
print(f"1. Overall global happiness lies around {mean_score} (mean) and {median_score} (median).")
print("2. Finland and other Nordic countries consistently top the rankings.")
print(f"3. The gap between happiest and least happy countries is {percent_diff}%.")
print("4. Regional differences are visible: Western Europe & North America score higher than Sub-Saharan Africa & South Asia.")
print(f"5. Correlations: GDP ({corr_gdp}) and Social Support ({corr_social}) are the strongest drivers of happiness.")
print("6. Insight: While wealth contributes strongly to happiness, social support is nearly equally important.")
