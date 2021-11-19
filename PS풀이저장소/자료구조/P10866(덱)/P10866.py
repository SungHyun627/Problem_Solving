#P10866 덱
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n = int(stdin.readline())

q = deque()

for _ in range(n):
    a = list(stdin.readline().split())
    if a[0] == 'push_front':
        q.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        q.append(int(a[1]))
    elif a[0] == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif a[0] == 'pop_back':
        print(q.pop()) if q else print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        print(1) if not q else print(0)
    elif a[0] == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)