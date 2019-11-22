alnum = 0
alpha = 0
digit = 0
lower = 0
upper = 0
userInput = input()
inputList=list(userInput)
for i in inputList:
    if i.isalnum():
        alnum +=1
    if i.isalpha():
        alpha += 1
    if i.isdigit():
        digit += 1
    if i.islower():
        lower += 1
    if i.isupper():
        upper += 1
print(alnum>=1)
print(alpha>=1)
print(digit>=1)
print(lower>=1)
print(upper>=1)