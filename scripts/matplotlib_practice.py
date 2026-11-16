import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/samples.csv")

fig, ax = plt.subplots()             # 1. an empty canvas
mean_gc = df.groupby("organism")["gc_content"].mean()
ax.bar(mean_gc.index, mean_gc.values)  # 2. draw something
ax.set_xlabel("GC content (%)")      # 3. label it
ax.set_ylabel("Number of samples")
ax.set_title("GC content distribution")

fig.savefig("results/gc_per_organism.png", dpi=150, bbox_inches="tight")

plt.show()