from sys import stdin
import heapq

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().split())
start = int(stdin.readline())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, stdin.readline().split())
  graph[a].append((b, c))

def dijk(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
dijk(start)
print(distance)
