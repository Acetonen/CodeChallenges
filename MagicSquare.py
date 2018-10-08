"""
Magic Square

A magic square is a square matrix of distinct numbers in which the sum of
the numbers in each row, column and diagonal is equal. THa sum is caled the
magic sum.
"""
import sys

matrix = [] # create matrix
print("Input symmetric matrix row by row (separate digits by space):")
first_row = list(map(int, input().split(' ')))
# Input first row separately to count numbers of rows for cycle.
matrix.append(first_row)
for i in range (len(first_row) - 1):
    row = list(map(int, input().split(' ')))
    if len(row) != len(first_row):
        print("you must input SYMMETRIC matrix!")
        sys.exit()
    matrix.append(row)
# Now we have matrix as list of lists (rows).

def no_magic():
    # If there is no magic sum.
    print("There is no magic!)")

def rows_sum():
    # Check sum in all rows.
    for i in range(1, len(matrix)):
        if sum(matrix[i]) != sum(matrix[i-1]):
            no_magic() # output "No magic"
            sys.exit() # exit program
    return sum(matrix[i])

def columns_sum():
    # Check sum in all columns.
    sum_list = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        sum_list.append(sum)
    if sum_list.count(sum_list[0]) != len(sum_list):
    # We create list of columns sums and check if they are the same.
        no_magic()
        sys.exit()
    return sum_list[0]

def diagonal_sum():
    # Check sum in diagonals.
    first_diagonal = 0
    second_diagonal = 0
    for i in range(len(matrix)):
        first_diagonal += matrix[i][i]
        second_diagonal += matrix[i][len(matrix)-1-i]
    if first_diagonal != second_diagonal:
        no_magic()
        sys.exit()
    return first_diagonal

if rows_sum() == columns_sum() == diagonal_sum():
    print("We found magic square! Magic sum =", rows_sum())
