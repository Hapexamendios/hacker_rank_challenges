#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    '''
    Complete the function kangaroo in the editor below. It should return YES if they reach the same position at the same time, or NO if they don't.

kangaroo has the following parameter(s):

x1, v1: integers, starting position and jump distance for kangaroo 1
x2, v2: integers, starting position and jump distance for kangaroo 2
    '''

    k1Loc=x1
    l2Loc=x2
    if x2<x1:
        counter=0
        while x2<x1:
            x1=x1+v1
            x2=x2+v2
            if x1==x2:
                print("YES")
                return("YES")
            counter+=1
            if counter>=50000:
                print("NO")
                return("NO")
    elif x1<x2:
        counter=0
        while x1<x2:
            x1=x1+v1
            x2=x2+v2
            if x1==x2:
                print("YES")
                return("YES")
            counter+=1
            if counter>=50000:
                print("NO")
                return("NO")
    print("NO")
    return("NO")



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
