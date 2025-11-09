#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    factors = []
    
    for i in range(a[-1], b[0]+1):
        # Rule 1
        valid_1 = True
        
        for a_item in a:
            if i % a_item != 0:
                valid_1 = False
               
        # Rule 2 
        valid_2 = True
        
        for b_item in b:
            if b_item % i != 0:
                valid_2 = False
                
        # Check both for appending
        if (valid_1 and valid_2):
            factors.append(i)
    
    # print(f'Factors: {factors}')
    return(len(factors))        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
