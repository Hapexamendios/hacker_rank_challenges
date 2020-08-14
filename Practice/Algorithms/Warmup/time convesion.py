#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #s="12:45:54PM"
    print(s)
    # 00:00:00PM
    #print(s[8])
    hr=int(s[0]+s[1])
    #print(hr)
    if s[8]=="A" and hr==12:
        time24="00:"+s[3]+s[4]+":"+s[6]+s[7]
    elif s[8]=="P" and hr!=12:
        hr=hr+12
        time24=str(hr)+":"+s[3]+s[4]+":"+s[6]+s[7]
    elif s[8]=="P" and hr==12:
        time24=str(hr)+":"+s[3]+s[4]+":"+s[6]+s[7]
    else:
        time24="0"+str(hr)+":"+s[3]+s[4]+":"+s[6]+s[7]
    print(time24)
    return time24

        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
