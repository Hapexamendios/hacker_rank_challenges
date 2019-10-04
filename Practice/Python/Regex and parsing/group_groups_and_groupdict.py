givenString=input()

length = len(givenString)

splitGiven = []
splitGiven = [char for char in givenString]

location = 0
while location < length-1:

    if splitGiven[location].isalnum():

        if splitGiven[location] == splitGiven[location+1]:

            print(splitGiven[location])

            exit()
        else: 
            location +=1

    else:
        location += 1

print("-1")