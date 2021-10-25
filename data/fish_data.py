import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bream_length1 = pd.read_csv("C:/fish/bream_length.csv")
bream_length = bream_length1.to_numpy().flatten()
print(bream_length)

bream_weight1  = pd.read_csv("C:/fish/bream_weight.csv")
bream_weight = bream_weight1.to_numpy().flatten()

#bream_data = np.column_stack((bream_length, bream_weight))
#print(bream_data.shape)

smelt_length1  = pd.read_csv("C:/fish/smelt_length.csv")
smelt_length = smelt_length1.to_numpy().flatten()
print(smelt_length)

smelt_weight1  = pd.read_csv("C:/fish/smelt_weight.csv")
smelt_weight = smelt_weight1.to_numpy().flatten()

#smelt_data = np.column_stack((smelt_length, smelt_weight))


fish_length = np.concatenate((bream_length,smelt_length))
fish_weight =  np.concatenate((bream_weight,smelt_weight))

fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data)
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)