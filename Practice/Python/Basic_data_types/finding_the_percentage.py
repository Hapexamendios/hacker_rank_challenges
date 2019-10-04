numStudents = int(input())
# Obtain the number of students - the number of times to add to the dictionary

studentDict = {}
# Initialize the dictionary that will hold students and their grades

grades = []
# Initialize the list that will hold grades

for item in range(0,numStudents):
# Perform the following the number of times there are students (first input)

    nameAndGrades = input()
    # Obtain student name and grades

    nameAndGrades = nameAndGrades.split()
    # Split name and grades apart into a list

    grades = [float(nameAndGrades[1]),float(nameAndGrades[2]),float(nameAndGrades[3])]
    # Set the grades list equal to the scores, and convert scores to floats from strings

    studentDict.update({nameAndGrades[0]:grades})
    # Create a dictionary item with the name string as they key and a list containing grades as the associated value

studentToAverage=input()
# Accept input for the student whos average to find

scoresToAverage=studentDict[studentToAverage]
# Obtain the scores of the student in question

average = (scoresToAverage[0]+scoresToAverage[1]+scoresToAverage[2])/3
# Obtain the average of the three scores of the student in question

print("{:.2f}".format(average))
# Format the average to be 2 decimal points and output it