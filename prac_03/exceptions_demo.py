"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur when the value input datatype is not as defined
2. When will a ZeroDivisionError occur?
It is when the values are being divided by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I could try
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Numbers cannot be divided by zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
