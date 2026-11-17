# Write a program to grade students based on marks.

marks = int(input("Enter marks: "))

if (marks >= 90) :
    print("A")
elif (marks < 90 and marks >= 80) :
    print("B")
elif (marks < 80 and marks >= 70 ):
    print("C")
elif (marks < 70):
    print("D")
else:
    print("Not a valid input")