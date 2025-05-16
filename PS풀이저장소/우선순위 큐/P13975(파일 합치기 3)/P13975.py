#P13975 파일 합치기 3
from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

t = int(stdin.readline())

for _ in range(t):
  n = int(stdin.readline())
  result = 0
  q = list(map(int, stdin.readline().split()))
  heapq.heapify(q)
  
  while True:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    result += (x+y)
    if not q:
      break
    heapq.heappush(q, x+y)
  print(result)

  
