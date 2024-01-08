#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arrsum = []
    arrinit = arr[:]
    for i in arrinit:
        arr = arrinit[:]
        arr.remove(i)
        soma = sum(arr)
        arrsum.append(soma)
    
    maxsum = max(arrsum)
    minsum = min(arrsum)
    
    return print(minsum, maxsum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

