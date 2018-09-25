"""
Anty-Lychel Number

An anti-lychel numner is a number that forms a
palindrome through the iterative process of reversing its
digits and adding the resulting numbers. For example, 56 becomes polindromic
after one iteration: 56 + 65 = 121. If the number doesn't become palindromic
after 30 iterations, then it is not anti-Lychen number.
"""

numberRange = list(map(int, input("Input your range of numbers \
separate by '-': ").split("-")))

#check palindrome
def palindrome(k):
    x = True
    for i in range(len(k) // 2):
        if k[i] != k[len(k) - 1 - i]:
            x = False
            break
    return x

#reverse number
def reverse(y):
    rev = ''
    for i in range(len(y)):
        rev += y[len(y) - 1 - i]
    IntRev = int(rev)
    return IntRev

#search a-Ln in range
for i in range(numberRange[0], numberRange[1] + 1):
    counter = i
    for l in range(1, 31):
        counter += reverse(str(counter))
        if palindrome(str(counter)):
            print(f"{i} is Anty-Lychrel number after {l} iteration it reach \
palindrome {counter}")
            break
