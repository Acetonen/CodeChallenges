"""
The Crypto-Cube

Imagine a cube, which can contain characters at its vertices. Each vertex can
contain a single character.

For example, we can store the string "SoloLearn" in a cube.
'S' will be stored at the position (0, 0, 0), 'o' at (0, 1, 0),
'l' at (1, 1, 0), 'o' at (1, 0, 0), 'L' at (0, 0, 1), 'e' at (0, 1, 1),
'a' at (1, 1, 1), 'r' at (1, 0, 1).

As each cube has only 8 vertices, we will need another cube to store the last
character. A string of 100 characters will require 100/8: 13 cubes to store
all the characters.

Reading from and writing to a cube is done in the sequence: (0, 0, 0),
(0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1).

Each cube can be rotated left, right, up and down. After each rotation, the
characters move from their vertices to corresponding neighbor vertices.

Let's consider the example from above: the first cube contains "SoloLear"
and the second cube contains the leftover "n".
If we rotate the first cube to the right once we will get:

Reading the rotated cube will result in "LeoSralo".
We can rotate as many times as we want.

TASK:
Write a program that encrypts a given string by randomly rotating the
corresponding cubes, as well as decrypts the string, given the encrypted string
and the rotation sequence.

For instance, for the text "I love coding and SoloLearn" you will need 4 cubes
and here's a random sample of rotations:
0:U:U:L:R,1:U,2:D:R,3:U:R
0, 1, 2 or 3 are the numbers of the cubes, U, L R D are the rotation directions
(Up, Left, Right, Down). Cube rotations are comma-separated. Each cube can have
multiple rotations, separated by colons.

So, 0:U:U:L:R means that the first cube is rotated up, then again up, to the
left, and finally to the right.
"""

import random

global cubes, dir_list
cubes = [] # List of all cubes.
dir_list = ['U', 'D', 'L', 'R'] # Directory of rotations.

def string_form():
    """Count cube number and extend string to fill all cubes"""
    global cube_number
    string = input("Input string: ")
    # Count the numbers of cubes.
    if len(string) % 4 != 0:
        cube_number = len(string) // 8 + 1
        # Extend input string with empty chars to fill all cubes.
        string = string + ' ' * (cube_number * 8 - len(string))
    else:
        # If number of chars exactly = number of vertexes.
        cube_number = len(string) // 8
    return string

def cube_in(string):
    """Input string in cubes"""
    ind = 0 # Index of char in input string.
    out = ''
    for i in range(cube_number):
        cube = {} # Fill each cube.
        for z in (0, 1):
            for x in (0, 1):
                for y in (abs(0-x), abs(1-x)):
                    cube[(x, y, z)] = string[ind]
                    ind += 1
        cubes.append(cube)

def cube_out():
    """Output string from cubes"""
    out = ''
    for i in range(cube_number):
        for z in (0, 1):
            for x in (0, 1):
                for y in (abs(0-x), abs(1-x)):
                    out = out + cubes[i][(x, y, z)]
    return out

def rotate(n, direction):
    """
    Rotate cube in different directions. Input number of cube 'n' and
    direction of rotation 'direction'.
    """
    temp_cube = {}
    for z in (0, 1):
        for y in (0, 1):
            for x in (0, 1):
                if direction == 'U': # Up direction.
                    temp_cube[(x, abs(z-1), y)] = cubes[n][(x, y, z)]
                elif direction == 'D': # Down direction.
                    temp_cube[(x, z, abs(y-1))] = cubes[n][(x, y, z)]
                elif direction == 'L': # Left direction.
                    temp_cube[(z, y, abs(x-1))] = cubes[n][(x, y, z)]
                elif direction == 'R': # Right direction.
                    temp_cube[(abs(z-1), y, x)] = cubes[n][(x, y, z)]
    cubes[n] = temp_cube

def encription():
    """Random encription with random rotating cubes."""
    rotate_key = '' # Decription key.
    for cube in range(len(cubes)):
        rotate_key = rotate_key + str(cube) + ':'
        # Choose random count for rotation operations.
        for i in range(random.randint(1, 5)):
            # Choose random rotation.
            dir = random.choice(dir_list)
            rotate(cube, dir)
            rotate_key = rotate_key + dir + ':'
        rotate_key =  rotate_key[:-1] + ','
    rotate_key = rotate_key[:-1]
    return rotate_key

def decription(key, string):
    """Decript string with input key"""
    # Decription list is opposit for encription direction list.
    decript_list = ['D', 'U', 'R', 'L']
    # Create list of lists with cube rotetions from keys:[['U','D'], ['L', 'R']]
    key_list = [x.split(':')[:0 :-1] for x in list(map(str, key.split(',')))]
    # Decript string by opposit cubes rotations.
    for cube in range(len(key_list)):
        for dir in key_list[cube]:
            # Make opposit rotation command.
            dec = decript_list[dir_list.index(dir)]
            rotate(cube, dec)


if __name__ == '__main__':
    string = string_form()
    cube_in(string)
    choise = input("For encription input 'enc', for decription input 'dec': ")
    if choise == 'enc':
        print(f"Key: {encription()}; crypto string: '{cube_out()}'; ")
    elif choise == 'dec':
        key = input("Input decription key: ")
        decription(key, string)
        print(f"Decripted string: {cube_out()}")
