import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Generate synthetic customer spending data ---
np.random.seed(42)
segments = ["Budget", "Regular", "Premium", "VIP"]

data = []
for segment in segments:
    if segment == "Budget":
        spends = np.random.normal(50, 10, 150)
    elif segment == "Regular":
        spends = np.random.normal(120, 20, 150)
    elif segment == "Premium":
        spends = np.random.normal(250, 40, 150)
    else:  # VIP
        spends = np.random.normal(500, 80, 150)
    for amount in spends:
        data.append([segment, amount])

df = pd.DataFrame(data, columns=["Segment", "PurchaseAmount"])

# --- Visualization ---
sns.set_style("whitegrid")
sns.set_context("talk")

# Figure size: 8x8 inches, dpi=64 → exactly 512x512 pixels
plt.figure(figsize=(8, 8), dpi=64)
ax = sns.boxplot(x="Segment", y="PurchaseAmount", data=df, palette="Set2")

ax.set_title("Purchase Amount Distribution by Customer Segment", fontsize=16, weight="bold")
ax.set_xlabel("Customer Segment", fontsize=14)
ax.set_ylabel("Purchase Amount ($)", fontsize=14)

# Save chart at exactly 512x512 pixels
plt.savefig("chart.png", dpi=64)  # no bbox_inches
