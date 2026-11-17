# Write a program to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter 1st no: "))
num2 = int(input("Enter 2nd no: "))
num3 = int(input("Enter 3rd no: "))

if (num1 >= num2 and num1 >= num3):
    print(f"{num1} is the largest no")
elif (num2 >= num1 and num2 >= num3):
    print(f"{num2} is the largest no")
else:
    print(f"{num3} is the largest no.")