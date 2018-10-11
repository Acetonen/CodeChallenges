"""
Scientific Notation
Scientific Notation is the way to handle very large nubers or very smal numbers.
It allows representing numbers in a smzller and readable way, using powers of 10
"""

def counter(num):
    """Function that count zeros and non-zero digits."""

    zeros = 0
    for digit in num:
        if digit == '0':
            zeros += 1
        else: break
    rezult = num[zeros:] # non zero digits
    return rezult, zeros


number = input("Input number: ")
if number[0] == '0':
    # Cut '0,' from number
    cut_number = number[2::]
    print(f"SN = {counter(cut_number)[0]}*10^-{len(cut_number)}")
else:
    inv_number = number[::-1]
    print(f"SN = {counter(inv_number)[0][::-1]}*10^{counter(inv_number)[1]}")
