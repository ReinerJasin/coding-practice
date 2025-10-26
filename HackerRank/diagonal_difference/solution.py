#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # print(f'arr = {arr}')
    # print(f'arr[0] len = {len(arr[0])}')
    diag = 0
    
    for i in range(0, len(arr[0])):
        # print(f'diag 1 = {arr[i][i]}')
        # print(f'diag 2 = {arr[i][-i-1]}')
        diag += arr[i][i]-arr[i][-i-1]
        
    return abs(diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
