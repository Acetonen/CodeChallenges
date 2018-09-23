'''
MERSENNE PRIME

A Mersenne prime is a prime number that is one less than a pover of two.
It is a prime number of the from 2^n - 1 for some integer n.
Write a program to check if the user input is a prime number or not.

Bonus: Print all the Mersinne primes in a given range.
'''

# Enter numbers
print("Enter the range of numbers.")
bottomNumber = int(input("Enter bottom line of numbers: "))
upperNumber = int(input("Enter upper line of numbers: "))
# First counter from bottom to upper
for counter in range(bottomNumber, upperNumber + 1):
    # Check if it prime number
    for counter2 in range(2, counter):
        if counter % counter2 == 0:
            break
        elif counter2 == counter - 1:
            # Check if it Mersenne
            for i in range(2, int((counter + 1) / 2 + 1)):
                if 2 ** i == counter + 1:
                    print(counter)
                    break
