import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("raw_data.csv", sep=",")
print(df.shape)    # (9009, 2)
print(df.head())

# remove NA values
df = df[df["DCOILBRENTEU"] != "."]
print(df.shape)

df_ind = df.set_index("DATE")

# Visualising the Data
df_ind = df_ind.astype(float)
df_ind.plot()
plt.savefig("img/data.png")
plt.show()