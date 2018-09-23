"""
Howling Prime

A Howling Prime is a prime number if the sum of
its digits is also prime number
"""

numbers = list(map(int, input("Inter the range of numbers. \
separate by spaces: ").split(" ")))

# Function that check if the number is prime
def Prime(k):
    flag = True
    for i in range(2, k):
        if k % i == 0:
            flag = False
            break
    return flag

# Search numbers in our range
for mainCounter in range(numbers[0], numbers[1] + 1):
    
    # Sum the digits of number
    sum = 0
    main = str(mainCounter)
    if Prime(mainCounter):
        for i in range(len(main)):
            sum += int(main[i])
        if Prime(sum):
            print(f"{mainCounter} is Howling Prime")
