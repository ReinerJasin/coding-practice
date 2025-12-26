#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beautiful_day_count = 0
    
    for num in range(i,j+1):
        # Count the difference |i - reverse(i)|
        reverse = int(str(num)[::-1])
        
        # Calculate absolute of difference
        diff_abs = abs(num - reverse)
        
        # Check if day is beautiful or not
        if diff_abs % k == 0:
            beautiful_day_count += 1
            
    return beautiful_day_count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
