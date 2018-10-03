"""
Disarium Number

A number is called a Disarium number if the sum of the povers of its digits
equals the number itself. The digits are powered to their positions in the
number.
"""

# input the range of numbers
rangeList = list(map(int, input("Input the numbers (>10) range (split by '-'): ").split('-')))
# search Disarium number in range
for i in range(rangeList[0], rangeList[1] + 1):
    # create a list with digits of our number
    num = list(map(int, str(i)))
    # check if the sum of the povers of its digits equals the number itself
    if i == sum(list(i**(num.index(i)+1) for i in num)):
        # print rezult
        print(f"{i} is Disarium number (power of its digits: \
{list(i**(num.index(i)+1) for i in num)})")
