#P18258 큐 2
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
q = deque([])

for _ in range(n):
  s = stdin.readline().split()
  if len(s) == 2:
    q.append(int(s[1]))
    continue
  c = s[0]
  
  if c == 'front':
    print(q[0] if q else -1)
  elif c == 'pop':
    print(q.popleft() if q else -1)
  elif c == 'empty':
    print(0 if q else 1)
  elif c == 'back':
    print(q[-1] if q else -1)
  else:
    print(len(q))
