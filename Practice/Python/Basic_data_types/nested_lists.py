if __name__ == '__main__':
    scores=[]
    # initialize scores

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score=[name,score]
        # create a list that contains a name and a score
        scores.append(student_score)
        # create a list containing all the name-score lists

y=0
# initialize iterator
for item in range(0,len(scores)-1):
    y=y+1
    # iterate 1 less time than the number of items in the list

    x=0
    # initialize iterator

    while x<len(scores)-1:
        #Perform the following once for each item in the list of scores

        if scores[x][1]<scores[x+1][1]:
            # identify if the left item is smaller than the right item

            storage=scores[x+1]
            scores[x+1]=scores[x]
            scores[x]=storage
            # if so, swap the left and right items

        x=x+1
        #increase the increment by one

i=1
# initialize the counter at 1

lowest=scores[len(scores)-i][1]
secLowest=scores[len(scores)-(i+1)][1]
# find the rightmost and second rightmost scores

while lowest==secLowest:
# if the rightmost and second rightmost scores are equal, do the following

    i=i+1
    # increment the counter by one

    lowest=scores[len(scores)-i][1]
    secLowest=scores[len(scores)-(i+1)][1]
    # review the two scores one space to the left

x=0
# initialize the counter at zero

resultNames=[]
# initialize the result names list

while x<len(scores)-1:
# if the counter is less than the length of scores minus one do the following

    if scores[x][1]==secLowest:
        # if the score is equal to the identified second lowest, do the following

        resultNames.append(scores[x][0])
        # add the name to the result Names list

    x=x+1
    # incrememnt the counter by one

resultNames.sort()
# alphabetize the name list

x=0
# set the counter to zero

while x<len(resultNames):
# while the counter is less than the number of items in result names, do the following

    print(resultNames[x])
    # Print the name the result names list is currently on

    x=x+1
    # increment the counter