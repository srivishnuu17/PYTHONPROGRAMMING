# Lab Exercise 2: Variables, Operators, and Input/Output

name = input("Enter your name: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_result = a + b
difference = a - b
product = a * b

print(f"Hello, {name}!")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")
