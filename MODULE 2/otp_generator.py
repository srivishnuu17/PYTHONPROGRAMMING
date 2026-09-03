# Mini Project: OTP Generator

import random

print("=" * 35)
print("          OTP GENERATOR")
print("=" * 35)

try:
    length = int(input("Enter OTP length (4-8): "))

    if 4 <= length <= 8:
        otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
        print(f"Your OTP is: {otp}")
        print("This OTP is valid for demonstration purposes only.")
    else:
        print("Please enter an OTP length between 4 and 8.")
except ValueError:
    print("Please enter a valid number.")
