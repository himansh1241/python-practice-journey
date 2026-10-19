# Q4. Basic Calculator

# Take two numbers from the user and calculate:

# Addition
# Subtraction
# Multiplication
# Division

num1 = int(input("Enter first no: "))
num2 = int(input("Enter second no: "))

print("Addition: ",(num1 + num2))
print("Subtraction: ",(num1 - num2))
print("Multiplication: ",(num1 * num2))

if num2 != 0:
    print("Division: ",(num1 / num2))
else:
    print("Division isn't possible")