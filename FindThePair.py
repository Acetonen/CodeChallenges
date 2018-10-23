"""
Find the pair.
You have a collection of numbers, where you want to find it there exists a pair
whose sum is equal to the user's input.
"""

from itertools import combinations

user_input = input("Input collection of number, splittin by spaces: ")
collections = list(map(int, user_input.split(' ')))
target_number = int(input("Input target number: "))
for i in combinations(collections, 2):
    if target_number == sum(i):
        print(f"True, {i}")
