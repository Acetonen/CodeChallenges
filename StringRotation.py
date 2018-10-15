"""
String Rotation
Create a function that accepts a string argument and returns an array
of strings, which are shifted varsions of the argument string.
Sample input:
"Hello"
Sample output:
["elloH", "lloHe", "loHel", "oHell", "Hello"]
"""

string = input("Input string: ")

def rotation(string):
    """Function, that rotate strings"""
    result = []
    for i in range(len(string)):
        word = string[1:] + string[0]
        result.append(word)
        string = word[:]
    return result

print(rotation(string))
