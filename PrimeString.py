"""
Prime strings.

A string is called prime if it can't be constructed by concentrsting multiply
(more than one) equal strins.
For example:
"abac" is prime, but "xyxy" is not ("xyxy" = "xy" + "xy").
"""

import sys

string = input('Input string: ')
# Odd string allways prime.
if len(string) % 2 !=0:
    print(f'"{string}" - prime.')
    sys.exit()
# Split string on multiply length mini-strings.
for i in range(1, len(string) // 2 + 1):
    # String must contain round number of mini-strings.
    if len(string) % i == 0:
        string_list =[]
        S = string[:]
        # Create list of separate mini-strings.
        for j in range(1, len(string) // i + 1):
            string_list.append(S[:i])
            S = string[i*j:]
        # Check if all mini-strings the sames (set - delete all doubles).
        if len(set(string_list)) == 1:
            print(f'"{string}" = {string_list} - not prime.')
            sys.exit()
print(f'"{string}" - prime.')
