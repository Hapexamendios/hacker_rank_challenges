toTup = []
n = int(input()) #not used
userInput=input()
toTup=userInput.split()
for i in range(0,len(toTup)):
    toTup[i] = int(toTup[i])
tup = tuple(toTup)
print(hash(tup))