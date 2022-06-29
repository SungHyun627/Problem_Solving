#P1966 프린터 큐
from sys import stdin 
from collections import deque

stdin = open('./input.txt', 'r')
t = int(stdin.readline())
for _ in range(t):
  cnt = 0
  n, m = map(int, stdin.readline().split())
  a = list(map(int, stdin.readline().split()))
  b = [i for i in range(n)]
  q1 = deque(a)
  q2 = deque(b)
  while True:
    if q1[0] == max(q1):
      x, y = q1.popleft(), q2.popleft()
      if y == m:
        print(cnt + 1)
        break
      cnt += 1
    else:
      q1.append(q1.popleft())
      q2.append(q2.popleft())
      
