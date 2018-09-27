'''
Complex Number Calc

A complex number can be epressed as (a, b) or as a + bi. a is called the numbers
real part, and the b is called immaginary part. i is defined by i x i = -1.
'''

# input coefficients
print("Input coefficients (a1, b1, a2, b2) of Compplex numbers \
(separate by spases):")
a, b, c, d = map(int, (input().split(' ')))

# choose tho operation
operation = input("input operation ('*' or '/'): ")
if operation == '*':
    print(f"Result of multiplication is:\n\t{a*c-b*d} + {b*c + a*d}i")
if operation == '/':
    print(f"Result of division is:\n\t{(a*c+b*d)/(c**2+d**2)} \
+ {(b*c-a*d)/(c**2+d**2)}i")
