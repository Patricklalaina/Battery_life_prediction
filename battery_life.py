#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# battery_life = a * time_charging + b

def model_process(x_train, y_train, x_test):
    mean_x = sum(i for i in x_train) / len(x_train)
    mean_y = sum(i for i in y_train) / len(y_train)
    var_xn = sum((i - mean_x) ** 2 for i in x_train)
    cov_xy = sum((y - mean_y) * (x - mean_x) for y, x in zip(y_train, x_train))
    a = cov_xy / var_xn
    b = mean_y - a * mean_x
    y_preds = a * x_test + b
    return min(y_preds, 8.0)
    
    
def get_file_content(link):
    data = {
        'x': [],
        'y': []
    }
    with open(link, 'r') as file:
        for line in file:
            splited = line.strip().split(',')
            x = float(splited[0])
            y = float(splited[1])
            if y >= 0 and y < 8.0:
                data['x'].append(x)
                data['y'].append(y)
    return data
            
        
if __name__ == '__main__':
    timeCharged = float(input().strip())
    data = get_file_content('trainingdata.txt')
    x_train, y_train = data['x'], data['y']
    x_test = timeCharged
    y_predicted = model_process(x_train, y_train, x_test)
    print(y_predicted)    
