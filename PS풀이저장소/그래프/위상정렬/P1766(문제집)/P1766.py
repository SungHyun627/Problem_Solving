#P1766 문제집
from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
arr = []
indegree = [0] * (n+1)
priority = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    priority[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if not indegree[i]:
        heapq.heappush(arr, i)

while arr:
    # print(arr)
    k = heapq.heappop(arr)
    for t in priority[k]:
        indegree[t] -= 1
        if not indegree[t]:
            heapq.heappush(arr, t)
    result.append(k)
print(*result)