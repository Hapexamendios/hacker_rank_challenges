if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

scores = []
# initialize scores list

for item in arr:
# for each item in array, perform the following
 
    scores.append(item)
    # add the item to the scores list

scores.sort(reverse=True)
# sort the scores list from highest to lowest

i=0
j=1
# Set list locations to 0 and 1

topVal=scores[i]
secVal=scores[j]
# identify first(0) and second(1) list items

while topVal==secVal:
# as long as first and second list items are equal, do the following. This is to ensure we don't just return the second value in case of a tie for the two highest values. We want the next highest following the tie.

    i=i+1
    j=j+1
    # increase list locations by one

    topVal=scores[i]
    secVal=scores[j]
    # identify list items

print(scores[j])
# print the second list item