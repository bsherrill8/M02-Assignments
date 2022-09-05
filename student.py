# Student.py
# by: Brian Sherrill
# 09/05/2022
# Purpose: Get student name and GPA and check for Dean's List qualification

while True:
    lName = input("Enter student's last name or ZZZ to quit: ")
    if lName == "ZZZ":
        break

    fName = input("Enter student's first name: ")
    GPA = float(input("Enter student's GPA: "))

    if GPA >= 3.25:
        print( fName, lName, "has made the Honor Roll")
    if GPA >= 3.5:
        print("and the Dean's List")
    
    print(" ")
    
