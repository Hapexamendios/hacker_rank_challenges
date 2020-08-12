def print_rangoli(size):
    # first iteration of the alphabet rangoli problem
    # acknowledged this is total spaghetti


    givenNumber=size
    number=givenNumber
    row=1
    totalRows=givenNumber*2-1
    maxDashes=(givenNumber-1)*2
    maxLength=maxDashes*2+1
    #print(maxLength)
    letterCounter=givenNumber
    letter=1
    min_flag=0
    #print(17/2)
    for i in range(1,totalRows+1):
        charsToPrint=maxLength-abs((number-i))*4
        #print(charsToPrint)
        print(abs(givenNumber-i)*2*"-",end="")
        printed=(abs(givenNumber-i)*2)

        #print(value,end="")
        while charsToPrint>0:
            if charsToPrint==1:
                print(chr(ord('`')+number),end="")
                charsToPrint-=1
                min_flag=1
                printed+=1
            if charsToPrint>1 and min_flag==0:
                print(chr(ord('`')+number)+"-",end="")
                charsToPrint-=2
                number-=1
                if number==1:
                    min_flag=1;
                printed+=2
                if printed>maxLength/2:
                    min_flag=1
                    number+=2
            if charsToPrint>1 and min_flag==1:
                print(chr(ord('`')+number)+"-",end="")
                charsToPrint-=2
                number+=1
                printed+=2
            #if printed>maxLength/2:
            #    min_flag=1
            #    number+=1
        print(abs(givenNumber-i)*2*"-")
        printed=printed+abs(givenNumber-i)*2
        #print(printed)

        row+=1
        number=givenNumber
        min_flag=0
if __name__ == '__main__':