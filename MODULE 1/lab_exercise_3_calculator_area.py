# Lab Exercise 3: Simple Calculator and Area Calculations

print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

print("\nArea Calculations")
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
print("Area of rectangle:", length * width)

radius = float(input("Enter circle radius: "))
pi = 3.14159
print("Area of circle:", pi * radius * radius)
