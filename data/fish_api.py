import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bream_length1 = pd.read_csv("C:/fish/bream_length.csv")
bream_length = bream_length1.to_numpy()
#print(bream_length)

bream_weight1  = pd.read_csv("C:/fish/bream_weight.csv")
bream_weight = bream_weight1.to_numpy()

bream_data = np.column_stack((bream_length, bream_weight))
print(bream_data.shape)

smelt_length1  = pd.read_csv("C:/fish/smelt_length.csv")
smelt_length = smelt_length1.to_numpy()

smelt_weight1  = pd.read_csv("C:/fish/smelt_weight.csv")
smelt_weight = smelt_weight1.to_numpy()

smelt_data = np.column_stack((smelt_length, smelt_weight))
print(smelt_data.shape)

plt.scatter(bream_data[:,0], bream_data[:,1])
plt.scatter(smelt_data[:,0], smelt_data[:,1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()


