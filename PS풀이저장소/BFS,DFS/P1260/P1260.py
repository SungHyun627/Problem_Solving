from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

def BFS(graph, v, visited):
    # 큐 생성
    queue = deque([v])
    visited[v] = True

    while queue:
        # 큐에서 하나의 원소를 꺼낸 후
        v = queue.popleft()
        print(v, end = " ")

        # graph에 v와 인접한 노드 중 방문되지 않는 노드를 queue에 append
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def DFS(graph, v, visited):
    # 탐색 노드 방문 처리
    visited[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

# 노드의 개수, 간선의 개수, 시작 노드
n, e, s = map(int, stdin.readline().rstrip().split())
graph = [[0] for _ in range(n + 1)]
DFS_visited = [False] * (n + 1)
BFS_visited = [False] * (n + 1)
DFS_visited[0] = True
BFS_visited[0] = True

for _ in range(e):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드에 연결되어 있는 노드를 정렬
for i in graph:
    i.sort()

DFS(graph, s , DFS_visited)
print()
BFS(graph, s, BFS_visited)