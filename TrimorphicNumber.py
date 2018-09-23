'''
Trimorphic Number
A trimorphic number is a number whorse cube ends in the number itself.
'''
numberRange = list(map(int, input("Input range of numbers separete \
by \"-\" (ex: 45-56): ").split("-")))
noTrimorphic = True
for number in range(numberRange[0],numberRange[1] + 1):
    stNumber = str(number)
    stCube = str(number ** 3)
    flag = True
    for i in range(1, len(stNumber) + 1):
        if stNumber[len(stNumber) - i] != stCube[len(stCube) - i]:
            flag = False
            break
    if flag:
        noTrimorphic = False
        print(f"{stNumber} is a trimorphic number, it's cube: {stCube}")
if noTrimorphic:
    print("There is no trimorphic number in this range")
