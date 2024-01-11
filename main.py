sk = input("How many Grades did you get? ")
def gradeCalculator (sk):
    i = 1
    sum=0
    while i <= int(sk):
     print("Enter Grade", i,": ")
     grade = input()
     sum = sum + int(grade)
     i += 1
    global rez
    rez = sum / int(sk)

gradeCalculator(sk)

def checkRez (rez):

    if (rez >= 5):
       print("Passed!")
    else:
       print("Failed")

    print(rez)

checkRez(rez)