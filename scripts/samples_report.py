import pandas as pd

df = pd.read_csv("data/samples.csv")
print("Number of samples per organism: ", df["organism"].value_counts())
print("\n=== Mean GC ===\n", df.groupby("organism")["gc_content"].mean())
print("\n=== Max length ===\n", df.groupby("organism")["length"].max())
df_new = df[df["length"] > 1000]