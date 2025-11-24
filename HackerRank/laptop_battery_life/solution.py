#!/bin/python3

import math
import os
import random
import re
import sys

import pandas as pd

from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    # Make sure to install scikit-learn first `!pip install scikit-learn`
    
    timeCharged = float(input().strip())

    charge_duration = []
    usage_duration = []
    
    threshold = 4.0

    data = pd.read_csv("trainingdata.txt", header=None)
    
    data_threshold = data[data[0] < threshold]
    
    lr = LinearRegression()
    
    x = data_threshold[[0]]
    y = data_threshold[1]
    
    lr.fit(x,y)
    
    if timeCharged < 4:
        prediction = lr.predict([[timeCharged]])[0]
    else:
        prediction = lr.predict([[threshold]])[0]
    
    print(prediction)