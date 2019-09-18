n = input()
ITERATIONS = int(n)
l = []
print(l)
iteration=1
for item in range(ITERATIONS):
    print("this is action:",iteration)
    iteration=iteration+1
    n=input()
    expression = n.split()
    print(expression)
    if expression[0] == "insert":
        eval(l.expression[0](expression[1],expression[2]))
    print(l)