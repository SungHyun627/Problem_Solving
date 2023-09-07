#P11000 강의실 배정
from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
q = []
arr = []
cnt = 1

for _ in range(n):
  arr.append(list(map(int, stdin.readline().split())))

arr.sort()
heapq.heappush(q, arr[0][1])

for i in range(1, n):
  if arr[i][0] >= q[0]:
    heapq.heappop(q)
  else:
    cnt += 1
  heapq.heappush(q, arr[i][1])
print(cnt)