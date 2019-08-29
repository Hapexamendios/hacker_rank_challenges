if __name__ == '__main__':
    n = int(input())

print(*range(1,n+1),sep="")
#The * operator prior to range unpacks or "splats" the individual elements of the iterable object. Best explation I found: https://codeyarns.com/2012/04/26/unpack-operator-in-python/