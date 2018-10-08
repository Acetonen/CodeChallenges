"""
Permutable Prime
A permutable prime is a prime number of two or more digits that remains prime
with every possible rearrangment of the digits.
"""

from itertools import permutations # give all possible rearrangment

def prime(numb):
# Function that check if the number is prime.

    flag = True
    for i in range(2, numb):
        if numb % i == 0:
            flag = False
            break
    return flag


range_of_numb = list(map(int, input("Input range \
of numbers splitting by '-': ").split('-')))
# input range of numbers, splitting by '-'

for numb in range(range_of_numb[0], range_of_numb[1]):
    list_of_primes = [] # collect variations of digits for output
    main_flag = True
    for i in permutations(str(numb)): # result of permutation is 'typlets'
        res = int("".join(list(i))) # create integer for permutations output
        if prime(int(res)):
            list_of_primes.append(res)
        else:
            main_flag = False
            break
    if main_flag: print(f"{numb} is a Permuteble Prime {list_of_primes}")
