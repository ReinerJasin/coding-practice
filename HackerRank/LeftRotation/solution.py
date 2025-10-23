#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here

    # Solution 1  -  loop through and append
    d = d % len(arr)
    result = []
    i = d
    
    for j in range(len(arr)):
        result.append(arr[i])
        i+=1
        
        if i==len(arr):
            i=0

    # Solution 2  -  python array slicing
    # d = d % len(arr)
    # result = arr[d:] + arr[:d]

    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
