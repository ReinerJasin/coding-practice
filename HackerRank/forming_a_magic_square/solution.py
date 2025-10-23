#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    # STEP 1: Count how many times each number appears in the magic square
    number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for row_idx, row in enumerate(s):
        for col_idx, element in enumerate(row):
            # print(f"Element at ({row_idx}, {col_idx}): {element}")
            number_count[element-1] += 1
            
    print(f'number count: {number_count}')
    
    # STEP 2: Identify the step in modifying the element to make s magic square valid
    modification = []
    for i_idx, duplicates in enumerate(number_count):
        # If found duplicates
        if number_count[i_idx] > 1:
            for loop in range(number_count[i_idx]-1):
                # Loop through the data and change it to the first empty number
                for j_idx, zeros in enumerate(number_count):

                    if number_count[j_idx] == 0:
                        # Save the number to be modified with a format of (from, to)
                        # print(f'============================')
                        # print(f'i_idx: {i_idx}, found number {number_count[i_idx]}')
                        # print(f'j_idx: {j_idx}, found number {number_count[j_idx]}')
                        modification.append((i_idx+1, j_idx+1))
                        number_count[i_idx] -= 1
                        number_count[j_idx] += 1
                        # print(f'number count: {number_count}')
                        break
                
    print(f'number count: {number_count}')
    print(f'modification: {modification}')
        
    # STEP 3: Change duplicate number into the one that doesn't exist
    cost = 0
    
    for before, after in modification:
        
        # for row_idx, row in enumerate(s):
        #     for col_idx, element in enumerate(row):
        #         # Found the first occurence of duplicates, must be changes to missing number
        #         if element == before:
        #             s[row_idx][col_idx] = after
        cost += abs(before-after)
                    
    # print(f'Square condition: {s}')
    # print(f'My calculated minimal cost is {cost}')

    # Next step: calculate the cost for switching two numbers instead of fixing numbers

    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
