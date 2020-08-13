#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max=0
    min=0
    arr=sorted(arr)
    for i in range(1,5):
        max=max+arr[i]
    for i in range(4):
        min=min+arr[i]
    print(min, end=" ")
    print(max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)