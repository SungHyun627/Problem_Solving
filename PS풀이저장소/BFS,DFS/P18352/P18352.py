from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

## n: 도시의 개수, m: 도로의 개수, k: 거리 정보, x: 출발 도시 번호
n, m, k, x = map(int, stdin.readline().split())

# 연결 리스트
graph = [[] for _ in range(n+1)]
# 방문 리스트
visited = [False]*(n+1)
# 특정 node로부터 거리 리스트
distance = [0] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

# BFS
def bfs(graph, v, visited, distance):
    queue = deque([])
    queue.append(v)
    # 방문 처리
    visited[v] = True

    while queue:
        t = queue.popleft()
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[t] + 1

bfs(graph, x, visited, distance)

if distance.count(k) == 0:
    print(-1)
else:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)