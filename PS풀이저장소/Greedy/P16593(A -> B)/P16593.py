#P16953 A -> B
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')


def calculate_num(x, y):
  result = 1
  while (x < y):
    if not (y % 2):
      y = int(y //2)
    else:
      if y % 10 == 1:
        y = int(y//10)
      else:
        return -1
    result += 1
  
  if x == y:
    return result
  else:
    return -1


a, b = map(int, stdin.readline().split())
print(calculate_num(a, b))
