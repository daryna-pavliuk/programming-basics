# How many samples are there? Which organisms? 🔢
# What is the mean length of all samples? 📏
# Show only E. coli samples 🦠
# Show samples with GC > 42 and length > 1000
# Top 3 samples by GC content 🥇
# Add a column length_kb
# 💡 Bonus: what does df["organism"].value_counts() do?

import pandas as pd

df = pd.read_csv("data/samples.csv")
print("How many samples: ", df.shape[0])
print("Which organisms: ", df["organism"].unique())
print("Mean length: ", round(df["length"].mean(), 2))
print("\n=== E. coli only ===\n", df[df["organism"] == "Escherichia coli"])
print("\n=== Big GC and length only ===\n", df[(df["gc_content"] > 42) & (df["length"] > 1000)])
print("\n=== Biggest GC ===\n", df.sort_values("gc_content", ascending=False).head(3))
df["length_kb"] = df["length"] / 1000
df["organism"].value_counts()


gc_rich = df[df["gc_content"] > 45]
gc_rich.to_csv("results/gc_rich.csv", index=False) #without row numbers
gc_rich.to_csv("results/gc_rich_1.csv") #with row numbers

import matplotlib.pyplot as plt

fig, ax = plt.subplots()             # 1. an empty canvas
ax.hist(df["gc_content"], bins=6)    # 2. draw something
ax.set_xlabel("GC content (%)")      # 3. label it
ax.set_ylabel("Number of samples")
ax.set_title("GC content distribution")
plt.show()

fig.savefig("results/gc_per_organism.png", dpi=150, bbox_inches="tight")