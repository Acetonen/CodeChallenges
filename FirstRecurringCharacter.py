"""
First Recurring Char
Write a program that tkes a string as input and returns the first recuring
character as the output.
"""

string = input("Input string of char: ")
control_string = []
for char in string:
    if char in control_string:
        print(f"Find! - {char}"); break
    else: control_string.append(char)
