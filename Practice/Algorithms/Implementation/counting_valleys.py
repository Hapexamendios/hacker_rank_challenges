#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    pastEle=0
    currentEle=0
    valleys=0
    for i in s:
        pastEle=currentEle
        if i=="D":
            currentEle-=1
        elif i=="U":
            currentEle+=1
        if pastEle==0 and currentEle==-1:
            valleys+=1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
