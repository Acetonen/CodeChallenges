"""
N-bonachi numbers

The fibonachi sequence is a set of numbers that starts with a one or a zero,
followwed by a one, and proceeds based on the rule thet each number is equal
to the sum of the preceding two numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

We can generalize thisto an N-bonacci sequences, where the sum of the preceding
N numbers from the next term.
For example, 3-bonacci sequence is the following:
0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81...
"""


def create_list(n_bonacci, term):
    """Create M-th terms of N-bonacci list"""
    for i in range(term - n_bonacci):
        next_item = sum(N_BONACCI_LIST[i:])
        N_BONACCI_LIST.append(next_item)


if __name__ == '__main__':
    N_BONACCI = int(input("Input N-bonacci number: "))
    TERM = int(input("Input M-th terrm: "))

    N_BONACCI_LIST = [0 for x in range(N_BONACCI-1)] + [1]

    create_list(N_BONACCI, TERM)
    print(N_BONACCI_LIST)
