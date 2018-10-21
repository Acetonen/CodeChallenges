"""
Goldbach's Conjective
Is a rule in math that states the following: every even number grater than
two csn be expressed as the sum of two prime numbersself.

Write a progrsm that finds evvery possible pair of prime numbers, whose sum
equals the given number or set of numbers within s range.
"""

def prime(number):
    """Function that check if number is prime"""
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    return flag

# Input range of numbers.
num_range = list(map(
    int, input("Input range of numbers (>2) splitting by '-'").split('-')))
for num in range(num_range[0], num_range[1] + 1):
    # Check only even numbers in range.
    if num % 2 == 0:
        # Compily listt of result. Check only in range num//2 to num-i to avoid
        # dublicate results (3+5 and 5+3) and avoid '1' (17+1).
        res_list = ([(x, num-x) for x in range(num // 2, num - 1)
                        if prime(x) and prime(num-x)])
        # Print list of results.
        if res_list:
            print('\n', num, end=': ')
            for pair in res_list:
                print(f"{pair[0]} + {pair[1]}", end='; ')
