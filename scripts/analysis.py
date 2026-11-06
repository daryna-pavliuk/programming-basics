from my_stats import minimum, average
from statistics import mean
import pandas as pd

with open("data/samples.csv", "r") as file:
    lines = file.readlines()
    gc_list = []
    for line in lines[1:]:
        line = line.strip().split(",")
        gc_list.append(float(line[1]))
    print(average(gc_list))

df = pd.read_csv("data/samples.csv")
print(df["gc_content"].mean())
print(df.describe())