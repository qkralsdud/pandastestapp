import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bream_length1 = pd.read_csv("C:/fish/bream_length.csv")
bream_length = bream_length1.to_numpy().flatten()
#print(bream_length)

bream_weight1  = pd.read_csv("C:/fish/bream_weight.csv")
bream_weight = bream_weight1.to_numpy().flatten()

#bream_data = np.column_stack((bream_length, bream_weight))
#print(bream_data.shape)

smelt_length1  = pd.read_csv("C:/fish/smelt_length.csv")
smelt_length = smelt_length1.to_numpy().flatten()
#print(smelt_length)

smelt_weight1  = pd.read_csv("C:/fish/smelt_weight.csv")
smelt_weight = smelt_weight1.to_numpy().flatten()

#smelt_data = np.column_stack((smelt_length, smelt_weight))


fish_length = np.concatenate((bream_length,smelt_length))
fish_weight =  np.concatenate((bream_weight,smelt_weight))

fish_data = np.column_stack((fish_length, fish_weight))
#print(fish_data)
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
#print(fish_target)

index = np.arange(47) 
np.random.shuffle(index)

# 35
train_input = fish_data[index[:35]] # 훈련 데이터 (모델)
target_target = fish_target[index[:35]] # 타겟 데이터 (모델)
# print(train_input)
# print(target_target)

# 14개
test_input = fish_data[index[35:]] # 훈련 데이터 (검증)
test_target = fish_target[index[35:]] # 타겟 데이터 (검증)

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()