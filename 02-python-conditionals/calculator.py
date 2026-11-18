# Create a simple calculator supporting +, -, *, /.

a = 10
b = 5
char = input("Enter the character: ")

if (char == "+"):
    print(a + b)
elif (char == "-"):
    print(a - b)
elif (char == "*"):
    print(a * b)
elif (char == "/"):
    print(a / b)
else:
    print("Invalid Character")