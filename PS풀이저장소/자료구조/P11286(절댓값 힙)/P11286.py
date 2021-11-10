#P11286 절댓값 힙
from sys import stdin
import heapq

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
q = []

for _ in range(n):
    a = int(stdin.readline())
    if a:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q :
            print(0)
        else:
            print(heapq.heappop(q)[1])