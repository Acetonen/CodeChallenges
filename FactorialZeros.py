"""
Factorial Zeros

The factorial of non-negative integer n, denoted by n! is the
product of all positive integers less than or equal to n. For
example, 5!= 5x4x3x2x1 =120.

Write a program to calculate the number of traling zeros in n!
Where n is any positive number less than 10^7
"""

number = int(input("Input your number: "))
factorial = 1
# sesrching factorial
for i in range(2, number + 1):
    factorial *= i
stringF = str(factorial)
# searching zeros
for k in range(1, len(stringF)):
    print
    if stringF[len(stringF) - k] != '0':
        break
print(f"Output: {k - 1} ({number}! = {factorial} has {k - 1} \
trailing zeroes)")
