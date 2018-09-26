'''
Empire Number

An empir is a prime number that results in different prime when its decimal
digits are reversed.
'''

# input range of numbers
numberStr = list(input("Input range of numbers split by '-': ").split("-"))

# check if prime
def Prime(k):
    flag = True
    for i in range(2, k):
        if k % i == 0:
            flag = False
            break
    return flag

for num in range(int(numberStr[0]), int(numberStr[1])+1):
    # reverse number
    check = str(num)[::-1]
    # compare number and reversed
    if Prime(num) and Prime(int(check)):
        print(f"{num} and {check} are prime numbers")
