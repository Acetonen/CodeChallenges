"""
Number Spiral

Write a program which will take a number as input and print a spiral
from 1 till the square of the number.

For eXample:
Input: 3
Output:
9 8 7
2 1 6
3 4 5

Input instruction for SoloLearn playground:
first string: input number
second string: input 'c' for clockwise direction; 'a' for anticlockwise.
"""

import itertools


def get_start_position_coordinates(number, direction):
    """Get spiral start point"""
    x_coordinate = 0
    y_coordinate = 0
    if (number+1) % 2 == 0:
        x_coordinate = y_coordinate = (number-1) // 2
    else:
        x_coordinate = number // 2 - 1
        if direction == 'c':
            y_coordinate = x_coordinate
        elif direction == 'a':
            y_coordinate = x_coordinate + 1
    start_position = {'x': x_coordinate, 'y': y_coordinate}
    return start_position


def move(direction):
    """Move in different direction on spiral"""
    CURENT_POSITION['x'] += DIRECTION_COORDINATES[direction][0]
    CURENT_POSITION['y'] += DIRECTION_COORDINATES[direction][1]


def look(direction):
    """Look in future move direction to understand if it free"""
    look_x = CURENT_POSITION['x'] + DIRECTION_COORDINATES[direction][0]
    look_y = CURENT_POSITION['y'] + DIRECTION_COORDINATES[direction][1]
    return MATRIX[look_x][look_y]


def choosing_direction(direction):
    """Choose between clockwise and anticlockwise directions"""
    direction_list = {'c': ['right', 'down', 'left', 'up'],
                      'a': ['left', 'down', 'right', 'up']}
    return direction_list[direction]


def print_matrix(matrix):
    """Pretty matrix output"""
    max_number_length = len(str(NUMBER**2))
    for row in matrix:
        for number in row:
            number = str(number)
            string_number = number + (max_number_length-len(number))*' '
            print(string_number, end=' ')
        print()


if __name__ == '__main__':
    NUMBER = int(input("Input number: "))
    DIRECTION = input("Input spiral direction.\n"
                      "For clockwise input - c\n"
                      "For anticlockwise input - a\n")
    CURENT_POSITION = get_start_position_coordinates(NUMBER, DIRECTION)
    # Create zero-matrix.
    MATRIX = [[0 for X in range(1, NUMBER+1)] for Y in range(1, NUMBER+1)]

    DIRECTION_NAMES = choosing_direction(DIRECTION)
    DIRECTION_COORDINATES = {'left': (0, -1),
                             'right': (0, 1),
                             'down': (1, 0),
                             'up': (-1, 0)}

    MOVE_CYCLE = itertools.cycle(DIRECTION_NAMES)
    TURN = DIRECTION_NAMES[3]
    NEXT_TURN = next(MOVE_CYCLE)

    for digit in range(1, (NUMBER**2 + 1)):
        MATRIX[CURENT_POSITION['x']][CURENT_POSITION['y']] = digit
        if look(NEXT_TURN) != 0:
            move(TURN)
        else:
            move(NEXT_TURN)
            TURN = NEXT_TURN
            NEXT_TURN = next(MOVE_CYCLE)

    print_matrix(MATRIX)
