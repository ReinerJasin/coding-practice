#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    min_sum = 0
    max_sum = 0
    
    for index, score in enumerate(scores):
        if score < min_score:
            min_score = score
            min_sum += 1
            
        if score > max_score:
            max_score = score
            max_sum += 1
            
    return max_sum, min_sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
