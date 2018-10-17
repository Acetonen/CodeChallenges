#!/usr/bin/python3.6
"""
Caesar Cipher
The Caesar Cipher is a type of subatitution cipher in which each letter in the
plain text is shifted to a certain number of dlaces down the alphabet.
"""

def cription(shift, string):
    """Function that encript and decript string"""
    symbols = [' ', ',', '.', '-', '!', '&', '?']
    result = ''
    for c in string:
        if c in symbols:
            result = result + c
        else:
            result = result + chr(ord(c)+shift)
    return result

while True:
    string = input("Input string: ")
    choise = input("Input 'enc' for encription, \
'dec' for decription, 'ex' for exit: ")
    if choise == 'enc':
        print(cription(1, string))
    elif choise == 'dec':
        print(cription(-1, string))
    elif choise == 'ex':
        break
    else: print('wrong input')
