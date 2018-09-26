'''
Lab Numbers

A lab number is a number if it has AT LEAST one prime divisor and ALL of the
squares of it's prime divisors sre still it's divisors.
'''

# Function that check if the number is prime
def Prime(k):
    flag = True
    for i in range(2, k):
        if k % i == 0:
            flag = False
            break
    return flag

# input range of number
numRange = list(map(int, input("Input range of numbers \
split by '-'").split('-')))

# check all numbers in range
for num in range(numRange[0], numRange[1] + 1):
    # make list of all prime divisors for each number in range
    primeDivs = []
    for div in range(2, num):
        if (num % div == 0) and Prime(div):
            primeDivs.append(div)
    # if number has at least one prime divisor check it square
    if len(primeDivs) > 0:
        mainFlag = True
        for i in range(len(primeDivs)):
            if num % (primeDivs[i] ** 2) != 0:
                mainFlag = False
                break
        # print if we find Lab Number
        if mainFlag:
            print(f"{num} is a Lab Number, divisors are: {primeDivs}")
