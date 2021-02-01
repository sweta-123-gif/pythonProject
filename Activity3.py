# Sweta kc
# ISQA 3900
# 01/31/2021
# Getting the format letter grades and number grades for class.


#This is a display title for this assignment.
def display_title():
    print("Welcome to the Grade Calculator")


#Here I ask for the input from 1-1000 points, by using repetition stucture and if else statement.
def get_totalPoints():
    while True:
        point = float(input("Enter the total score(0-1000): "))
        if point >= 0 and point <= 1000:
            return point

        else:
            print("You must enter integer values >= 0 and <= 1000. Try again.")


#Here I ask points and get the return letter grades.
def get_LetterGrades(grade):
    if grade >= 92:
        return "A"
    elif grade >= 88 and grade <= 91.99:
        return "B+"
    elif grade >= 82 and grade <= 87.99:
        return "B"
    elif grade >= 78 and grade <= 81.99:
        return "C+"
    elif grade >= 70 and grade <= 77.99:
        return "C"
    elif grade >= 60 and grade <= 69.99:
        return "D"
    elif grade < 60:
        return "F"


# Here is the main body part where the loop repeats and ask again if the points is invalid.
def main():
    display_title()

    while True:

        totalPoints = get_totalPoints()
        letterGrades = get_LetterGrades((totalPoints / 1000) * 100)
        print(
            "You earned an average of  %.02f. Letter grade of grade earned: %s" % ((totalPoints / 1000) * 100, letterGrades))
        val = input("Would you like to enter another score (y/n)?")
        if (val != 'y'):
            break


if __name__ == "__main__":
    main()
