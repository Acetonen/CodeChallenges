'''
Owl Matrix

An Owl matrix is a symmetric matrix that coud be "folded" vertically and
horizontally in the middle and would generate four eqyal pieces.

For Example:
x x x x    a b b a
x x x x    c c c c
x x x x    c c c c
x x x x    a b b a
'''
from sys import exit

# input matrix
print("You must insert SYMMETRIC matrix with ODD numbers of rows/columns.")
rows = int(input("Iput ODD number of rows: "))
print("input row by row, split values by spases:")
matrix = []
for i in range(rows):
    matrix.append(list(input("").split(' ')))

# ful protection
if (len(matrix) != len(matrix[0])) or (rows % 2 or len(matrix[0]) % 2 != 0):
    exit("You must enter SYMMETRIC matrix with ODD numbers of rows/columns, goodbye.")

# search in rows
for i in range(rows):
    for j in range(int(rows / 2)):
        if matrix[i][j] != matrix[i][-1-j]:
            exit("Youre matrix doesn't Owl Matrix")
            
# search in columns
for j in range(rows):
    for i in range(int(rows / 2)):
        if matrix[i][j] != matrix[-1-i][j]:
            exit("Youre matrix doesn't Owl Matrix")

print("CONGRATULATIONS! Youre matrix is Owl Matrix")
