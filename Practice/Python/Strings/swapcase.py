def swap_case(s):
    s=s.swapcase()
    # Set s equal to the swapped cases of s
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)