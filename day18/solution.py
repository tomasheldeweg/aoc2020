import re
from functools import reduce
from operator import mul, add

with open('day18/input.txt') as f:
    data = f.read().split('\n')

def eval_operation_lr(equation):
    operation_map = {
        '+': add,
        '*': mul
    }
    equation = equation.replace(' ', '')
    numbers = [int(d) for d in re.findall(r'\d+', equation)]
    operations = (operation_map[op] for op in re.findall(r'[+*]', equation))

    total = reduce(
        lambda x, y: next(operations)(x, y),
        numbers
    )
    return str(total)

def eval_operation_add_mul(equation):
    equation = equation.replace(' ', '')
    while '+' in equation:
        new = re.sub(
            r'(\d+)\+(\d+)',
            lambda m: str(int(m.group(1)) + int(m.group(2))),
            equation
        )
        equation = new
    return eval_operation_lr(equation)

def recurse_brackets(equation, precedence=eval_operation_lr):
    stack = []

    for ind, char in enumerate(equation):
        if char == '(':
            stack.append(ind)
        if char == ')':
            op = stack.pop()
            cl = ind + 1
            equation = equation.replace(
                equation[op:cl],
                precedence(equation[op:cl])
            )
            break

    if '(' in equation:
        return recurse_brackets(equation, precedence)
    else:
        return precedence(equation)

# Solve 1
total = sum(int(recurse_brackets(eq)) for eq in data)
print(total)

# Solve 2
total = sum(int(recurse_brackets(eq, eval_operation_add_mul)) for eq in data)
print(total)
