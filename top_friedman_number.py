"""
Friedman Number
Friedman Number is a integer, which the result of an expression using all
its digits in combination with any of the basic arithmetic operators (+,-,*,/),
addictive inverses, parentheses, and exponentiationself.
"""

from operator import add, sub, mul, truediv, pow
from itertools import permutations

symb_operators = ['+', '-', '*', '/', '^', 'r/', 'r^']
operators = [add, sub, mul, truediv, pow, 'reverse_div', 'reverse_pow']
''' To not use parentheses in my code, I add two new operators:
reverse_div (r/) and reverse_pow (r^).
They work in such way:
(6-2)r^5 == 5^(6-2) or (5+6)r/8 == 8/(5+6)
Because my program working with operators ONLY from LEFT to RIGTH, i need
this operators to not use the parentheses. This operators work only if sum or
sub was done before them.'''

def counter_add(array, system):
    """
    Function that add one to counter. This program use two different counters
    one in binary system and one in seventh system (by numbers of differents
    operators in list)
    """
    i = 0
    while i < len(array):
        if array[i] < (system - 1):
            array[i] += 1
            break
        else:
            array[i] = 0
            i += 1
    return array

def number_of_variations(counter, system):
    """
    Counting number of variations by translate maximum number from
    counter system to decimal system
    """
    summa = 0
    for i in range(len(counter)):
        summa += system ** i * (system - 1)
    return summa

def parentheses(rev_op):
    """ Remove all "reverse operators" and put parentheses to output"""
    global op_counter, temp_number, symb_operators
    if rev_op in op_counter:
        ind = op_counter.index(rev_op)
        flag = False
        if ((0 in op_counter[:ind]) or
            (1 in op_counter[:ind])): flag = True
        op_counter.remove(rev_op)
        op_counter.insert(0, (rev_op-2))
        temp_number.insert(0, temp_number[ind+1])
        del temp_number[ind+2]
        if flag:
            temp_number[1] = '(' + str(temp_number[1])
            temp_number[ind+1] = str(temp_number[ind+1]) + ')'


# User input range of numbers, splitting by '-'.
num_list = list(map(int, input("Input range (split '-'): ").split('-')))
fried_number_collector = [] # list of founded FN

# Search number thrue the inpunt range.
for totall in range(num_list[0], (num_list[1] + 1)):
    num = str(totall)
    # Create tuplets of all variation of number in range.
    for tup in permutations(num):
        number = list(map(int, tup)) # creating list of int from tuplet
        # Creating counter of different possible variation of joints in number.
        # For ex.: num = 3457, joints: 3 4 5 7, 34 5 7, 3 45 7, 3 457, e.t.c
        join_counter = [0 for x in number][:-1]

        # Number of variants different joints.
        join_summa = number_of_variations(join_counter, 2)

        # All variants of joints.
        for j in range(join_summa + 1):
            temp_number = number[:]
            # Curent joint. Doing that:
            # number = 3 4 5 6
            # joint = x 34 5 6
            # remove 'x' => joint number = 34 5 6
            for i in range(len(join_counter)):
                if join_counter[i] == 1:
                    temp_number[i+1] = int(str(temp_number[i])
                                         + str(temp_number[i+1]))
                    temp_number[i] = 'x'
            temp_number = [x for x in temp_number if x != 'x']
            join_counter = counter_add(join_counter, 2) # add 1 to joint count.

            # Creating counter of all possible variants operators in our number
            # For ex.: number = 3 4 5 6,
            #          variants: 3+4+5+6; 3^4+5-6; e.t.c
            op_counter = [0 for x in temp_number][:-1]

            # Number of variants different operators combibations.
            summa = number_of_variations(op_counter, 7)

            # Results for every combination of operators.
            for j in range(summa + 1):
                result = temp_number[0]

                # Count result of current combination.
                for i in range(len(op_counter)):
                    try: # catch zerro div error
                        if (operators[op_counter[i]] == 'reverse_div' or
                            operators[op_counter[i]] == 'reverse_pow'):
                            if ((4 not in op_counter[:i]) and
                                (6 not in op_counter[:i])):
                                result = operators[op_counter[i]-2](
                                                   temp_number[i+1],
                                                   result)
                        else:
                            result = operators[op_counter[i]](
                                               result,
                                               temp_number[i+1])
                    except: result = None

                # If we find Friedman Number, print it.
                if result == totall:
                    if result in fried_number_collector: break
                    print('Friedman Number: ', totall, end=' = ')
                    parentheses(6) # remove r^ from output
                    parentheses(5) # remove r/ from output
                    for i in range(len(temp_number)):
                        print(temp_number[i], end=' ')
                        try: print(symb_operators[op_counter[i]], end=' ')
                        except: print('')
                    # Add result in collection.
                    fried_number_collector.append(totall)

                op_counter = counter_add(op_counter, 7) # add 1 to op. count.
