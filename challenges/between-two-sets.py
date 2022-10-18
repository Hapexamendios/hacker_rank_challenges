a = [1]
b = [48, 72]
# Test input

c = [*range(max(a),min(b)+1)]
# Create list containing all possibilities

d = []
# Create an empty list to store possibilities to remove

for i in a:
    for j in c:
        if j % i != 0:
            d.append(j)
# Test each possibility to see if every item in list a is a factor. If it
# isn't, put the possibility in list d for later removal

d = [*set(d)]
# dedupe list d

for i in d:
    c.remove(i)
# Remove things in d from the possibility list c

e = []
# Create another empty list to store possibilities to remove

for i in c:
    yes_factor = 0
    for j in b:
        if j % i == 0:
            yes_factor += 1
    if yes_factor != len(b):
        e.append(i)
# Test each possibility to see if it's a factor of all items in list
# b. Increment by 1 if it is. Test if the number of increments equals
# length of b. If not, add it to e to be later removed from possibilites

e = [*set(e)]
# Dedupe e

for i in e:
    c.remove(i)
# Remove things in e from c list of possibilites

return len(c)
# Return the number of items in c

