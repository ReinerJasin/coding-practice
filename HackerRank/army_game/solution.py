#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def gameWithCells(n, m):
    # Write your code here
    odd_n = n % 2 != 0
    odd_m = m % 2 != 0
    
    supply_4 = (n // 2) * (m // 2)
    
    supply_row_2 = m // 2 if odd_n else 0
    supply_col_2 = n // 2 if odd_m else 0
    
    supply_row_col = 1 if (odd_n and odd_m) else 0
    
    return (supply_4 + supply_row_2 + supply_col_2 + supply_row_col)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
