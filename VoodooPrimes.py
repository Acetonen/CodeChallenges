'''
Voodoo Primes

A Voodoo Prime is a prime number whose reciprocal (in decimal) has the same
number in its digits. For examle, 7 is vodoo prime because its reciprocal
1/7=0.14285714285 contains 7.
'''
# Function that check if the number is prime
def Prime(k):
    flag = True
    for i in range(2, k):
        if k % i == 0:
            flag = False
            break
    return flag

numberStr = list(map(int, input("Input range of numbers split by '-': ").split("-")))
for number in range(numberStr[0], numberStr[1] + 1):
    if Prime(number):
        rezult = str(1 / number)
        if str(number) in rezult:
            print(f"{number} is a Voodoo prime, reciprocal - {rezult}")
