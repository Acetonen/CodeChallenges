"""
Kapreka's constant

The number 6174 is known as Kapreka's constant. It is the ultimate convergence
point of the Kaprekar's routine, an algorithm thought up by Indian
mathematician D.R. Kaprekar in 1949.

The routine as follows:
1. Take any four-digit number (at least two different digits must be used).
2. Arrange the digits in descending and then in ascending order to get two
four-digit numbers.
3. Substract the smaller number from the larger number and ger result.
4. Repeat steps 2-4 with the new number.

After a few iterations, the algorithm converges to a fixed point and starts to
result in the same number - 6174 - the so-called Kaprekar's constant.
"""


def make_one_routine(number):
    """
    Arrange the digits in descending and then in ascending order to get two
    four-digit numbers.
    Substract the smaller number from the larger number and ger result.
    """
    sorted_number = sorted(list(number))
    ascending_list = int(''.join(sorted_number))
    descending_list = int(''.join(sorted_number[::-1]))
    result = descending_list - ascending_list
    print("{} - {} = {}".format(descending_list, ascending_list, result))
    if result == 0:
        print("It isn't Kapreka's constant, try different input.")
    return str(result)


if __name__ == '__main__':
    NUMBER = input(
        "Input any number\n"
        "If three-digit number have repetitive digits or\n"
        "if four-digit number haven't at least two different digits,"
        "result'll be ZERO\n")
    KAPREKAR_CONSTANT = NUMBER
    RESULT_LIST = []
    while KAPREKAR_CONSTANT not in ['6174', '0', '495']:
        KAPREKAR_CONSTANT = make_one_routine(KAPREKAR_CONSTANT)
        if KAPREKAR_CONSTANT in RESULT_LIST:
            print("Infinity cycle found.")
            break
        RESULT_LIST.append(KAPREKAR_CONSTANT)
