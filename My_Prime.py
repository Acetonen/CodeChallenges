# Function that check if the number is prime
def Prime(k):
    flag = True
    for i in range(2, k):
        if k % i == 0:
            flag = False
            break
    return flag
