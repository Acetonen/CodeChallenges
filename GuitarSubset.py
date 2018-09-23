'''
GUITAR SUBSET
For list of integers S and a target number G, a subset oof S that adds up to
G is called a guitar subset. BONUS: find them all!)

MUSREAD: enter target number in first line, enter sequence in second line,
separate wiht ";" without any spaces!
'''

# making input
target = int(input("Enter the target G-number: "))
subset = list(map(int, input('Enter some lines of numbers, separeted by \
spaces (ex: 42 1 3;): ').split(" ")))

# creating a binar counter
binarCounter = list(map(lambda x: x*0, subset))
mainFlag = 0
while mainFlag < len(binarCounter):
    i = len(binarCounter) - 1
    while i >= 0:
        if binarCounter[i] == 0:
            binarCounter[i] += 1
            break
        else:
            binarCounter[i] = 0
            i -= 1
    mainFlag = sum(binarCounter)
    summa = 0
    # searching the subset
    result = ""
    for number in range(0, len(binarCounter)):
        if binarCounter[number] == 1:
            summa += subset[number]
            result += str(subset[number]) + " "
    if summa == target:
        print(result)
        print()
