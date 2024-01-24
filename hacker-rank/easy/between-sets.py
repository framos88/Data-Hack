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
    
    arr2 = []
    
    for i in range(1, 101):
        arr1 = []
        for n1 in a:
            if i % n1 == 0:
                arr1.append(i)
                
        for n2 in b:
            if n2 % i == 0:
                arr1.append(i)
        
        if len(arr1) == len(a) + len(b):
            arr2.append(i)
    
    return len(arr2)
        
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

