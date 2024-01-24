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
    
    arr = [-1]
    p = -1
    n = -1
    
    for i in scores:
        max_score = max(arr)
        if i > max_score:
            arr.append(i)
            p += 1
    
    positive_infinity = float('inf')
    arr = [positive_infinity]
    
    for i in scores:
        min_score = min(arr)
        if i < min_score:
            arr.append(i)
            n += 1
    
    response = [p, n]
    
    return response

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

