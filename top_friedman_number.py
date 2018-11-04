"""
Friedman Number
Friedman Number is a integer, which the result of an expression using all
its digits in combination with any of the basic arithmetic
OPERATORS (+,-,*,/),
addictive inverses, simulate_parentheses, and exponentiationself.
"""

from operator import add, sub, mul, truediv
from itertools import permutations

SYMB_OPERATORS = ['+', '-', '*', '/', '^', 'r/', 'r^']
OPERATORS = [add, sub, mul, truediv, pow, 'reverse_div', 'reverse_pow']
''' To not use simulate_parentheses in my code, I add two new OPERATORS:
reverse_div (r/) and reverse_pow (r^).
They work in such way:
(6-2)r^5 == 5^(6-2) or (5+6)r/8 == 8/(5+6)
Because my program working with OPERATORS ONLY from LEFT to RIGTH, i need
this OPERATORS to not use the simulate_parentheses. This OPERATORS work only if
sum or sub was done before them.'''


def add_one_to_counter(counter, counter_system):
    """
    Function that add one to counter. This program use two different counters
    one in binary system and one in seventh system
    (by numbers of differents OPERATORS in list)
    """
    position = 0
    while position < len(counter):
        if counter[position] < (counter_system - 1):
            counter[position] += 1
            break
        else:
            counter[position] = 0
            position += 1
    return counter


def count_variants_of_counter(counter, counter_sys):
    """
    Counting number of variations by translate maximum number from
    counter system to decimal system
    """
    number_of_variants = 0
    for digit in range(len(counter)):
        number_of_variants += counter_sys ** digit * (counter_sys - 1)
    return number_of_variants


def create_list_of_joints(number_to_joint, counter):
    """Create list of different digits joints"""
    joint_list = []
    join_variant = 0
    while join_variant < joint_summa:
        temp_number = number_to_joint[:]
        for digit, counter_digit in enumerate(counter):
            if counter_digit == 1:
                previous_digit = str(temp_number[digit])
                next_digit = str(temp_number[digit+1])
                temp_number[digit+1] = int(previous_digit + next_digit)
                temp_number[digit] = 'x'
        temp_number = [x for x in temp_number if x != 'x']
        counter = add_one_to_counter(counter, 2)
        joint_list.append(temp_number)
        join_variant += 1
    return joint_list


def cath_zero_division(current_item, next_item):
    """Catching ZeroDivisionError"""
    cached_result = False
    rev_div_on_zero = current_operator == 'reverse_div' and current_item == 0
    div_on_zero = current_operator == truediv and next_item == 0
    zero_in_minus_pow = (current_operator == pow and
                         current_item == 0 and
                         next_item < 0)
    rev_zero_in_minus_pow = (current_operator == 'reverse_pow' and
                             current_item < 0 and
                             next_item == 0)
    if (rev_div_on_zero or div_on_zero or
            zero_in_minus_pow or rev_zero_in_minus_pow):
        cached_result = True
    return cached_result


def make_normal_from_reverse(position):
    """Make standart operator from reverse."""
    normal_operator = OPERATORS[OPERATOR_COUNTER[position]-2]
    return normal_operator


def is_reverse(cheking_operator):
    """Check if it reverse operator"""
    it_reverse = False
    if cheking_operator in ['reverse_div', 'reverse_pow']:
        it_reverse = True
    return it_reverse


def is_repetition_before(position):
    """Check repetition of reverse operator before."""
    it_repeat = False
    if 4 in OPERATOR_COUNTER[:position] or 6 in OPERATOR_COUNTER[:position]:
        it_repeat = True
    return it_repeat


def output_friedman_number():
    """Print Friedman number on screen."""
    print('Friedman Number: {}'.format(CHECKING_NUMBER), end=' = ')
    remove_reverse_pow = simulate_parentheses(6, JOINT_VARIANT)
    remove_reverse_div = simulate_parentheses(5, remove_reverse_pow)
    for ind, num in enumerate(remove_reverse_div):
        print(num, end=' ')
        if ind > len(OPERATOR_COUNTER)-1:
            print()
            break
        print(SYMB_OPERATORS[OPERATOR_COUNTER[ind]], end=' ')


def simulate_parentheses(reverse_operator, list_to_simulate):
    """ Remove all "reverse operators" and put parentheses to output"""
    output_list = list_to_simulate[:]
    if reverse_operator in OPERATOR_COUNTER:
        ind = OPERATOR_COUNTER.index(reverse_operator)
        flag = False
        if (0 in OPERATOR_COUNTER[:ind]) or (1 in OPERATOR_COUNTER[:ind]):
            flag = True
        OPERATOR_COUNTER.remove(reverse_operator)
        OPERATOR_COUNTER.insert(0, (reverse_operator-2))
        output_list.insert(0, output_list[ind+1])
        del output_list[ind+2]
        if flag:
            output_list[1] = '(' + str(output_list[1])
            output_list[ind+1] = str(output_list[ind+1]) + ')'
    return output_list


if __name__ == '__main__':
    INPUT_RANGE = input("Input range (split '-'): ").split('-')
    NUM_LIST = [int(x) for x in INPUT_RANGE]
    FRIEDMAN_NUMBER_COLLECTOR = []
    CHECKING_NUMBER = 0
    JOINT_VARIANT = 0
    OPERATOR_COUNTER = []
    JOINT_COUNTER = []

    for CHECKING_NUMBER in range(NUM_LIST[0], (NUM_LIST[1] + 1)):

        for variation in permutations(str(CHECKING_NUMBER)):
            number = [int(x) for x in variation]
            JOINT_COUNTER = [0 for x in number][:-1]
            joint_summa = count_variants_of_counter(JOINT_COUNTER, 2)
            list_of_joints = create_list_of_joints(number, JOINT_COUNTER)

            for JOINT_VARIANT in list_of_joints:
                OPERATOR_COUNTER = [0 for x in JOINT_VARIANT][:-1]
                summa = count_variants_of_counter(OPERATOR_COUNTER, 7)

                # Results for every combination of OPERATORS.
                for j in range(summa + 1):
                    current_number = JOINT_VARIANT[0]
                    result = current_number

                    # Count result of current combination.
                    for index, operator in enumerate(OPERATOR_COUNTER):
                        next_number = JOINT_VARIANT[index+1]
                        current_operator = OPERATORS[operator]

                        if is_reverse(current_operator):
                            current_operator = make_normal_from_reverse(index)
                            current_number = next_number
                            next_number = result
                            if is_repetition_before(index):
                                break

                        if cath_zero_division(current_number, next_number):
                            result = None
                            break

                        result = current_operator(current_number, next_number)
                        current_number = result

                    if result == CHECKING_NUMBER:
                        if result in FRIEDMAN_NUMBER_COLLECTOR:
                            break
                        output_friedman_number()
                        FRIEDMAN_NUMBER_COLLECTOR.append(CHECKING_NUMBER)

                    OPERATOR_COUNTER = add_one_to_counter(OPERATOR_COUNTER, 7)
