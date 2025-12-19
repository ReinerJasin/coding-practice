#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(set(ranked))
    ranked = sorted(ranked, reverse=True)
    
    result = []
    
    for score in player:
        # print(f'checking score: {score}')
        # print(f'ranked: {ranked}')
        
        # Remove irrelevant scores
        while len(ranked) > 0 and score > ranked[-1]:
            # print('irrelevant number exist in the list')
            # print(f'removing last number {ranked[-1]} from ranked')
                
            ranked.pop()
            # print(f'new ranked --> {ranked}')
            
        # check if equal
        if len(ranked) == 0:
            result.append(1)
            
        elif score == ranked[-1]:
            # print(f'adding {len(ranked)} to result\n')
            result.append(len(ranked))
           
        # Check if smaller
        elif score < ranked[-1]:
            # print(f'adding {len(ranked) + 1} to result\n')
            result.append(len(ranked) + 1)
    
    # print(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()