import pandas as pd
import matplotlib.pyplot as plt

# --- Load your cleaned data ---
# Replace this with your actual cleaned CSV path
clean_data = pd.read_csv("cleaned_data.csv")

# --- Figure with 3 subplots ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Scatter plot: Experience vs Salary
axes[0].scatter(clean_data["Exp"], clean_data["Salary"], alpha=0.6, color="steelblue")
axes[0].set_title("Experience vs Salary")
axes[0].set_xlabel("Experience (years)")
axes[0].set_ylabel("Salary")
axes[0].grid(True, linestyle="--", alpha=0.5)

# 2. Histogram of Salary distribution
axes[1].hist(clean_data["Salary"], bins=20, color="seagreen", edgecolor="black")
axes[1].set_title("Salary Distribution")
axes[1].set_xlabel("Salary")
axes[1].set_ylabel("Count")

# 3. Histogram of Experience distribution
axes[2].hist(clean_data["Exp"], bins=15, color="darkorange", edgecolor="black")
axes[2].set_title("Experience Distribution")
axes[2].set_xlabel("Experience (years)")
axes[2].set_ylabel("Count")

plt.tight_layout()
plt.savefig("salary_exp_plots.png", dpi=150)
plt.show()

print("Saved plot as salary_exp_plots.png")
