clouds1 = [0, 0, 1, 0, 0, 1, 0]
# test array

location = 0
destination = len(clouds1)-1
jumps = 0
# initialize variables

while location < destination:

    if location == destination - 1:
        location += 1
        jumps += 1
    # If 1 space from destination, jump 1 location

    elif location == destination - 2:
        location += 2
        jumps += 1
    # If 2 spaces from destination, jump 2 locations

    else:
        if clouds1[location+1] == 1:
            location += 2
            jumps += 1
        # If adjacent to a "1" cloud, jump 2 locations

        elif clouds1[location+2]:
            location += 1
            jumps += 1
        # If 2 locations away there is a "1" cloud, jump
        # 1 location

        else:
            location += 2
            jumps +=1
        # Otherwise jump 2 locations


print(location)
print(jumps)
# Print statements, replace w/ return in HR