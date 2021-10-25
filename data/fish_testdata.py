import numpy as np
import pandas as pd

def getTest_Data():
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


    # 14개
    test_input = fish_data[index[35:]] # 훈련 데이터 (검증)

    test_weight = test_input[:, 1]
    test_length = test_input[:, 0]

    test_target = fish_target[index[35:]] # 타겟 데이터 (검증)

    tests = np.column_stack((test_length, test_weight, test_target))
    test_dataFrame = pd.DataFrame(tests, columns=["test_len", "test_wei", "test_target"])
    return test_dataFrame