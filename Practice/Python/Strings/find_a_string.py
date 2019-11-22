# Count how many times a substring exists within a string

def count_substring(string, sub_string):
    searchable = string
    sub = sub_string
    length = len(searchable)
    result = 0
    while length > 0:
        #print("performing find")
        index = searchable.find(sub)
        if index == 0:
            #print("found at index 0, popping at 0")
            searchable = list(searchable)
            searchable.pop(0)
            searchable = "".join(searchable)
            #print(searchable)
            result += 1
        elif index > 0:
            #print("found at non-zero index, starting pop loop")
            counter = 0
            while counter <= index:
                searchable = list(searchable)
                searchable.pop(0)
                searchable = "".join(searchable)
                #print(searchable)
                counter+=1
            result += 1
        elif index == -1:
            #print("no longer found")
            return result
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)