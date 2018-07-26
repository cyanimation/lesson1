"""
Write a program that does the following:
    create a variable for each class you want to include (biology, geometry, etc)
    create variables storing the credits for each grade
    a = 4
    a_minus = 3.7
    ...
    ask the user what letter grade they received for each class you chose to include
    calculate the points for each grade by multiplying the user's provided value with the credits associated with that letter grade

    if (biology == 'a-'):
        biology_points = a_minus * biology ...
    keep track of the total points and the total credits
    calculate the GPA: total_points / total_credits
    print your cumulative GPA
"""
import time
classList = []
while True:
    className = input('\nEnter the name of the class or enter quit to quit: ')
    if (className == "quit" or className == "Quit"):
        print("\n\n")
        break
    else:
        while True:
            try:
                print("\nEnter your grade in points between 0 and 4 for {}: ".format(className))
                classGrade = float(input())
                if (classGrade >= 0 and classGrade <= 4):
                    break
                else:
                    print("Enter  a number between 0 and 4 for real this time")
            except:
                print ("Please try again with an actual digit number")

        while True:
            try:
                classCredits = float(input('\nEnter the amount of credits for {}: '.format(className)))
                break
            except:
                print ("Oh why did college ever release you...")

        classList.append([className,classGrade,classCredits])

        print("With the following classes:")


totalPoints = 0
totalCredits = 0
for i in classList:
    print("In {} class you earned {} points and it had {} credits".format(*i) )
    totalPoints += i[1]*i[2]
    totalCredits += i[2]


print("\n\nNow calculating......beep....boop....yo mamma...old pizza\n\n")
time.sleep(2)
print("Done calcumalating:")
time.sleep(.5)

GPA = (totalPoints/(totalCredits*4))*4
print("Your total GPA is " + str(round(GPA,2)))



