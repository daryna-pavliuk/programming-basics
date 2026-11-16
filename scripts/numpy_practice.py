import numpy as np
import pandas as pd

df = pd.read_csv("data/samples.csv")
arr = np.array(df["length"])

print("Mean: ", arr.mean()) # mean is both method and function
print("Standard deviation: ", arr.std())
print("Median: ", np.median(arr)) # median is only a function

arr_kb = arr/1000
print(arr[arr>1000])