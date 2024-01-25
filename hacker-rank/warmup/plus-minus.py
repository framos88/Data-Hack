#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    num = len(arr)
    p = 0
    n = 0
    z = 0
    
    frm = "{:.6f}"
    
    for i in arr:
        if i > 0:
            p = p+1
        elif i < 0:
            n = n+1
        else:
            z = z+1
    print(frm.format(p/num))
    print(frm.format(n/num))
    print(frm.format(z/num))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

