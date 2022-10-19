ar = [1,2,1,2,1,3,2]
# test array

d = {}
# declare an empty dictionary

for item in ar:
    if item in d:
        d[item] = d[item]+1
    else:
        d[item] = 1
# For each item in the array, test if it's a key in the dict
# yet. If it is, increment its value by one. If it isn't,
# create a new key and set its value to one

pairs = 0
# Initialize an empty pairs variable

for item in d:
    pairs = pairs + d[item]//2
# Perform floor division to determine how many times 2 goes
# into the value associated with each key

print(pairs)
# Print the value we will return in HackerRank