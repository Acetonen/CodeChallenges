'''
STRANGE ROOT
A number has a strange root if its square and square root
share any digit.
'''

import math
startNumber = int(input("Enter the number: "))
power = str(startNumber ** 2)

#convert root to string and round 4 number after point
root = str(round(math.sqrt(startNumber), 4))
if len(root) > 3:
    root = root[:-1]

noRoots = True
print(f"Power = {power}\nRoot = {root}")
for char in range(len(power)):
    if power[char] in root:
        print(f"Your number has a Strange Root {power[char]}")
        noRoots = False
if noRoots:
    print("There is no Strange Root")
