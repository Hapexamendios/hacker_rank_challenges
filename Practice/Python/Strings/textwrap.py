import textwrap

def wrap(string, max_width):
    output=""
    chars = list(string)
    length = len(chars)
    while length // max_width > 0:
        for i in range (0,max_width):
            output = output+chars.pop(0)
        output=output+"\n"
        length = length - max_width
    else:
        while len(chars) > 0:
            output = output+chars.pop(0)
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)