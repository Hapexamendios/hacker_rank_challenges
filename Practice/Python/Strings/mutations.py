def mutate_string(string, position, character):
    inputString = string
    stringToList = list(inputString)
    stringToList[position] = character
    modifiedString = "".join(stringToList)
    return modifiedString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)