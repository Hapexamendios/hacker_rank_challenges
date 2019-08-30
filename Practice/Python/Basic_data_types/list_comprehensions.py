if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

solution=[]
# initialize empty solution list

x_line = list(range(0,x+1))
y_line = list(range(0,y+1))
z_line = list(range(0,z+1))
# create a list of integers along each dimension


for i in x_line:
# perform the following for each item in the x_line list

    for j in y_line:
    # perform the following for each item in the y_line list

        for k in z_line:
        # perform the following for each item in the z_line list. These three for-loops will iterate through all points in all three lists. For example, if our end coordinates are 3,3,3, it will iterate over 0,0,0, 0,0,1, 0,0,2, 0,0,3, 0,1,0 0,1,1 etc.
            coordinate = [x_line[i],y_line[j],z_line[k]]
            # create a list with the current coordinates in it

            if (coordinate[0]+coordinate[1]+coordinate[2]) != n:
            # check if the sum of the values of the cooridnate don't equal n

                solution.append(coordinate)
                # add the list containing the coordinate points to the list of coordinates that don't have a value sum of n

print(solution)
# output the list of acceptable coordinate points