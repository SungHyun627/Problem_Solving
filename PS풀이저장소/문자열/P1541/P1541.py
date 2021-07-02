from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

equation = stdin.readline().rstrip()
stack = []
minus_flag = False
number = ''
for i in range(len(equation)):

    if equation[i] != '-' and equation[i] != '+':
        number += equation[i]
        if i == len(equation) - 1:
            stack.append(str(int(number)))
            if minus_flag:
                stack.append(')')

    elif equation[i] == '-':
        stack.append(str(int(number)))
        number = ''

        if not minus_flag:
            minus_flag = True
            stack.append('-')
            stack.append('(')
        else:
            stack.append(')')
            stack.append('-')
            stack.append('(')
    else:
        stack.append(str(int(number)))
        number = ''
        stack.append('+')

# print(stack)
print(eval(''.join(stack)))