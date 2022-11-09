#!/usr/bin/env python
# coding: utf-8
# %%
import numpy as np
    
def rmse(target, output):
    target, output = np.array(target), np.array(output)
    return np.sqrt(((output - target) ** 2).mean())

def recall_n(target, output):
    comb = list(zip(output, target))
    comb.sort(key=lambda x:x[0])
    flag = False
    for i, (out, gt) in enumerate(comb):
        if gt == 1:
            if flag:
                break
            flag = True
    return (sum(target)-1) / (len(target)-i)

# %%
if __name__ == "__main__":
    # example 1
    y_true = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    y_pred = [0.9, 0.9, 0.2, 0.2, 0.2, 0.9, 0.9, 0.4, 0.2]
    
    result = recall_n(y_true, y_pred)
    print('recall_n:', round(result, 4))
    
    result = rmse(y_true, y_pred)
    print('rmse:', round(result, 4))
    
    
