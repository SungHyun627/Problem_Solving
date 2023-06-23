#P17413 단어 뒤집기 2
from sys import stdin

stdin = open('./input.txt', 'r')
stack = []
tag = False
result = ''
x = stdin.readline().rstrip()

for i in range(len(x)):
  if x[i] == '<':
    tag = True
    stack.reverse()
    result += ''.join(stack)
    stack = [x[i]]
  elif x[i] == '>':
    tag = False
    result += (''.join(stack) + '>')
    stack.clear()
  elif x[i] == ' ' and '<' not in stack:
    stack.reverse()
    result += (''.join(stack) + ' ')
    stack.clear()
  else:
    stack.append(x[i])
result += ''.join(''.join(stack)[::-1])
print(result)