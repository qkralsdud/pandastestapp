import numpy as np
import pandas as pd

def getTrain_Data():
    bream_length1 = pd.read_csv("C:/fish/bream_length.csv")
    bream_length = bream_length1.to_numpy().flatten()

    bream_weight1  = pd.read_csv("C:/fish/bream_weight.csv")
    bream_weight = bream_weight1.to_numpy().flatten()


    smelt_length1  = pd.read_csv("C:/fish/smelt_length.csv")
    smelt_length = smelt_length1.to_numpy().flatten()

    smelt_weight1  = pd.read_csv("C:/fish/smelt_weight.csv")
    smelt_weight = smelt_weight1.to_numpy().flatten()


    fish_length = np.concatenate((bream_length,smelt_length))
    fish_weight =  np.concatenate((bream_weight,smelt_weight))

    fish_data = np.column_stack((fish_length, fish_weight))

    fish_target = np.concatenate((np.ones(35), np.zeros(14)))


    index = np.arange(47) 
    np.random.shuffle(index)

    # 35
    train_input = fish_data[index[:35]] # 훈련 데이터 (모델)
    train_weight = train_input[:, 1]
    train_length = train_input[:, 0]

    target_target = fish_target[index[:35]] # 타겟 데이터 (모델)

    trains = np.column_stack((train_length, train_weight, target_target))
    train_dataFrame = pd.DataFrame(trains, columns=["train_len", "train_wei", "train_target"])
    return train_dataFrame
