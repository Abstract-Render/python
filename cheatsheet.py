#Running totals
i = 1
while i < 6:
  print(i)
  i += 1
#For loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#functions
pi = 3.14

def showAreaOfCircle(radius):
    area = pi * radius * radius
    print('Area: ' + str(area))

def updatePi(newPi):
    global pi
    pi = newPi

showAreaOfCircle(10)

updatePi(3.141)

showAreaOfCircle(10)
###
def FahrtoCel(variable):
        '''
        Function that converts Fahrenheit to Celsius and displays them side by side in steps of 10
        using the range function, it takes in one parameter up to and not including that number.
        '''
        print('F        C')
        F = []
        for i in range(variable):
                if i % 10 == 0:
                        F.append(i)
        C=[]
        for j in F:
                cel = ((j-32)*5/9)
                C.append(cel)
        for Fah,Cel in zip(F,C):
                print(Fah,'     ',Cel)

FahrtoCel(101)

# Write a program that calculates your current grade in a course with 5 categories of assignments: Quizzes, Projects, Activities, Attendance, Exams

studentName = input("Enter student's name: ")
courseName = input("Enter course name: ")
studentWeights = []
studentAverages = [] 

category = ["quizzes","projects","activities","attendance","exams"]
for item in category:
    print("Enter ", item, "weight")
    weight = float( input())
    studentWeights.append(weight)
    
for item in category:
    print("Enter ", item, "average.")
    averages = float( input())
    studentAverages.append(averages)
studentPercent = [a*b for a,b in zip(studentWeights,studentAverages)]

print(studentPercent)
print(studentPercent)
for item in studentPercent:
    total = sum(studentPercent)*100
print(total)
print("Hi", studentName, "You have a ",total,"% in your ",courseName," course.")