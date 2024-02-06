#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    target = arr[n-1]
    ordered = arr[:]
    ordered.sort()
    
    for index in range(n-1, 0, -1):
        arr[index] = target
        if arr != ordered:
            arr[index] = arr[index-1]
            print(*arr)
        else:
            print(*arr)
            break
    
    if arr != ordered:
        print(*ordered)
                  
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

