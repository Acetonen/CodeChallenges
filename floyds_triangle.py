"""
Floyd's triangle

Floyds's triangle is a right ungled triangular array of natural numbers,
used to computer science aducation.
It is defined by filling the rows of the triangle with consecutive numberes,
starting with a 1 at the top left corner:
1
2 3
4 5 6
7 8 9 10
"""


def creating_triangle_array(number_of_rows):
    """Creating list of digit rows for make triangle"""
    list_of_digits = []
    last_number = 0
    for number in range(number_of_rows):
        row = [str(x) for x in range(last_number+1, last_number+number+2)]
        last_number = int(row[-1])
        list_of_digits.append(row)
    return list_of_digits


if __name__ == '__main__':
    NUMBER_OF_ROWS_INPUT = int(input("Input number of rows: "))
    STYLE = input("Iput style, for strict - 's', for reversed - 'r': ")
    if STYLE == 's':
        print("Floyd's triangle:")
        for roww in creating_triangle_array(NUMBER_OF_ROWS_INPUT):
            print(' '.join(roww))
    elif STYLE == 'r':
        print("Reversed Floyd's triangle:")
        for roww in reversed(creating_triangle_array(NUMBER_OF_ROWS_INPUT)):
            print(' '.join(reversed(roww)))
