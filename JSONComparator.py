'''
JSON Comparator
Write a program that takes two strings in JSON format and compares them.
The program shoud output the difference between those JSON strings.
Example input:
{"a": 2, "b": 3}
{"a": 2, "b": 4}

{"a": "hello", "b": {"c": 3}, "c": 2}
{"a": "hello", "b": {"c": 11}, "c": 2}
'''

firstSt = list(map(str, input("Input first JSON string: ").split(",")))
secondSt = list(map(str, input("Input second JSON string: ").split(",")))

for counter in range(len(firstSt)):
    if firstSt[counter] != secondSt[counter]:
        print(f"{firstSt[counter]}\n{secondSt[counter]}")
