"""
Fisher Number.
A fiesher number is a integer whose multipliers are equal to the number's cube.
For example, 12 is a fisher number, because 12^3 = 2*3*4*6*12
"""

numbers_list = list(map(int, input("Input the range of number, splitting \
by '-': ").split('-')))
for number in range(numbers_list[0], numbers_list[1] + 1):
    mult_rezult = 1
    rezult_list = []
    for mult in range(1, number + 1):
        if number % mult == 0:
            mult_rezult *= mult
            rezult_list.append(mult)
    if number**3 == mult_rezult:
        print("{0} is Fisher Number, {0}^3 = \
multiply {1}".format(number, rezult_list))
