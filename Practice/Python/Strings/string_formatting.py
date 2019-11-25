def print_formatted(number):
    length = len(bin(number).replace("0b", ""))
    for i in range(1,number+1):
        octal = str(oct(i).replace("0o",""))
        #print("oct:",octal)
        hexal = str(hex(i).replace("0x","")).upper()
        #print("hex:",hexal)
        binary = str(bin(i).replace("0b", ""))
        #print("binary:",binary)
        i=str(i)
        print(i.rjust(length),octal.rjust(length),hexal.rjust(length),binary.rjust(length))
        i=int(i)
    return 0

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)