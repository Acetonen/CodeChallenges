"""
Longest Sequence

Given a series of numbers, find the longest sequence in the series.
A sequence could be one of the following: ascending, descending, equal.
"""
import operator # import module with operators (.eq ==; .lt <; .gt >)
sequence = list(map(int, input("Input sequence of numbers: ")))

# def universal function to find all 3 sequenses
def search(op): # as arguments we use our operators
    temp_rezult = [sequence[0]]
    rezult = []
    for i in range(len(sequence)-1): # search in digits
        if op(sequence[i], sequence[i+1]):
            temp_rezult.append(sequence[i+1])
            if len(temp_rezult) > len(rezult): # if find longest seq, mind it
                rezult = temp_rezult
        else: temp_rezult = [sequence[i+1]]
    return rezult # return rezult

print(f"Longest equal {search(operator.eq)}")
print(f"Longest ascending {search(operator.lt)}")
print(f"Longest descending {search(operator.gt)}")
