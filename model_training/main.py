import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("raw_data.csv", sep=",")

# print(df.shape)    # (9279, 2)
# print(df.head())

# remove NA values
df = df[df["DCOILBRENTEU"] != "."]

# print(df.shape)

# df_ind = df.set_index("DATE")

# Visualising the Data
# df_ind = df_ind.astype(float)
# df_ind.plot()
# plt.savefig("img/data.png")
# plt.show()

batch_size = 64
timesteps = 30
test_percent = 0.1
timesteps = 30

# getting the training size
def get_train_size(data, batch_size, test_percent):
    val = []
    n = len(data)
    n *= (1 - test_percent)
    if int(n) % batch_size == 0:
        val.append(int(n))
    for i in range(int(n) - batch_size * 2, int(n)):
        if i % batch_size == 0:
            val.append(i)
    return max(val)

# getting the test size
def get_test_size(data, batch_size):
    val = []
    n = len(data)
    for i in range(n - batch_size * 2, n - timesteps * 2):
        if (i - train_size) % batch_size == 0:
            val.append(i)
    return max(val)

print(len(df) * (1 - test_percent))                         # 8126.1
print(get_train_size(df, batch_size, test_percent))         # 8064

train_size = get_train_size(df, batch_size, test_percent) + 2 * timesteps
df_train = df[0: train_size]  # 7892, 2
training_set = df_train.iloc[:, 1:2].values
print(training_set.shape)                                   # (8124, 1)

print(len(df) * (test_percent))                             # 902.9
print(get_test_size(df, batch_size))                        # 8956

test_size = get_test_size(df, batch_size) + 2 * timesteps
df_test = df[train_size: test_size]                         
test_set = df_test.iloc[:, 1:2].values
print(test_set.shape)                                       # (892, 1)