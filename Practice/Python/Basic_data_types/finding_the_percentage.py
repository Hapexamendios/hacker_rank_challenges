numStudents = int(input())
#print(numStudents)
increment = 0
studentDict = {}
grades = []
for item in range(0,numStudents):
    increment += 1
    #print(increment)
    nameAndGrades = input()
    #print(nameAndGrades)
    nameAndGrades = nameAndGrades.split()
    #print(nameAndGrades)
    grades = [float(nameAndGrades[1]),float(nameAndGrades[2]),float(nameAndGrades[3])]
    studentDict.update({nameAndGrades[0]:grades})
#print(studentDict)
studentToAverage=input()
#print(studentToAverage)
scoresToAverage=studentDict[studentToAverage]
#print(scoresToAverage)
average = (scoresToAverage[0]+scoresToAverage[1]+scoresToAverage[2])/3
print("{:.2f}".format(average))