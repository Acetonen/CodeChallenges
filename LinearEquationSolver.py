"""
Linear Equation Solver
A linear equation is an equation that may be put in the form a*x + b = c,
where x is the variable, a, b, c are the coefficients, which are often
real numbers.
Example inputs:
2x - 3 = 1
3 = 1 + 2x
"""

string = input('Input equation, separate numbers and operators by spaces \
(example: 2x - 3 = 1): ')
# Creating list: ['2x', '-', '3', '=', '1']
eq = list(string.split(' '))
# Join '-' operators to number: ['2x', '-', '-3', '=', '1']
for i in range(len(eq)):
    if eq[i] == '-':
        eq[i+1] = eq[i] + eq[i+1]
# Find index of '='.
sep = eq.index('=')
# Creating list of coefficients [a, b, c]: [2, -3, 1]
# Move all coefficients without 'x' on right side of '=', and with 'x' on left.
coeff = []
for i in range(0, len(eq), 2):
    try:
        if i < sep:
            coeff.append(-int(eq[i]))
        else:
            coeff.append(int(eq[i]))
    # Catch number with 'x'
    except:
        if i > sep:
            coeff.insert(0, -int(eq[i][:-1]))
        else:
            coeff.insert(0, int(eq[i][:-1]))
# Count x.
x = (coeff[1]+coeff[2]) / coeff[0]
print('x = ', x)
