#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # Method 1 - Do comprehension for each, must loop 3 times
    # print(len([x for x in arr if x>0]) / len(arr))
    # print(len([x for x in arr if x<0]) / len(arr))
    # print(len([x for x in arr if x==0]) / len(arr))
    
    # Method 2 - Loop once with counter
    high = 0
    low = 0
    zero = 0
    n = len(arr)
    
    for i in arr:
        if i > 0:
            high += 1
        elif i < 0:
            low += 1
        elif i == 0:
            zero += 1
    
    print(f"{high / n:.6f}")
    print(f"{low / n:.6f}")
    print(f"{zero / n:.6f}")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
