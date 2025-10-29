#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    min_sec = s[3:8]
    status = s[-2:]

    if status == "AM" and hour == "12":
        hour = "00"
    elif status == "PM" and hour != "12":
        hour = str(int(hour) + 12)
        
    return f"{hour}:{min_sec}"    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
