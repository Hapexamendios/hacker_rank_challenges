n = input()
# collect the number of inputs

ITERATIONS = int(n)
# set the number of iterations to the integer value of the input

l = []
# initialize the list

for item in range(ITERATIONS):
# for each object in the range from 1 to the number of iterations, do the following:

    n=input()
    # request / collect input

    expression = n.split()
    # split the input into a list at spaces

    if expression[0] == "insert":
    # if the first item in the input list is insert, do the following

        l.insert(int(expression[1]),int(expression[2]))
        # insert the third input list item at the location specified in the second input list item

    elif expression[0]=="print":
    # if the first item in the input list is print, do the following

        print(l)
        # print the list

    elif expression[0]=="remove":
    # if the first item in the input list is remove, do the following

        l.remove(int(expression[1]))
        # remove the first appearance of the input from the list

    elif expression[0]=="append":
    # if the first item in the input list is append, do the following

        l.append(int(expression[1]))
        # append the second input list item to the list

    elif expression[0]=="sort":
    # if the first item in the input list is sort, do the following

        l.sort()
        # sort the list

    elif expression[0]=="pop":
    # if the first item in the input list is pop, do the following

        l.pop()
        # remove the last item from the list

    elif expression[0]=="reverse":
    # if the first item in the input list is reverse, do the following

        l.reverse()
        # reverse the order of the list