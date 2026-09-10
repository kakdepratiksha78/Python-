"""
Seaborn Example Script
=======================
Demonstrates a few common seaborn plot types using the built-in
'tips' dataset. Run this script to generate and save several
example visualizations.

Requirements:
    pip install seaborn matplotlib pandas
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Set a nice default theme
sns.set_theme(style="whitegrid")

# Load a built-in sample dataset
tips = sns.load_dataset("tips")

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Seaborn Plot Examples (tips dataset)", fontsize=16)

# 1. Scatter plot with regression line
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=axes[0, 0])
axes[0, 0].set_title("Total Bill vs Tip")

# 2. Box plot
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker", ax=axes[0, 1])
axes[0, 1].set_title("Total Bill by Day and Smoker Status")

# 3. Histogram / distribution plot
sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Distribution of Total Bill")

# 4. Bar plot with error bars
sns.barplot(data=tips, x="day", y="tip", hue="sex", ax=axes[1, 1])
axes[1, 1].set_title("Average Tip by Day and Sex")

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure
output_path = "seaborn_examples.png"
plt.savefig(output_path, dpi=150)
print(f"Saved plot to {output_path}")

# Uncomment to display interactively
# plt.show()
