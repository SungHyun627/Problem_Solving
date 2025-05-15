# P2075. N번째 큰 수
from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

n = int(stdin.readline())

q = []

for i in map(int, stdin.readline().split()):
  heapq.heappush(q, i)

for i in range(1, n):
  for j in map(int, stdin.readline().split()):
    if q[0] < j:
      heapq.heappop(q)
      heapq.heappush(q, j)

print(q[0])