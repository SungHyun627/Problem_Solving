from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n = int(stdin.readline())

#방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#일반인
graph1 = [[] for _ in range(n)]
#적록색약
graph2 = [[] for _ in range(n)]

for i in range(n):
    arr = list(stdin.readline().rstrip())
    for j in range(n):
        if arr[j] == 'G':
            graph2[i].append('R')
        else:
            graph2[i].append(arr[j])
        graph1[i].append(arr[j])

def bfs(graph):
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    region = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue.append((i, j, graph[i][j]))
                visited[i][j] = True

                while queue:
                    x, y, color = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx >= n or ny >= n or nx < 0 or ny < 0:
                            continue
                        if not visited[nx][ny] and graph[nx][ny] == color:
                            queue.append((nx, ny, graph[nx][ny]))
                            visited[nx][ny] = True
                region += 1
    return region

print(bfs(graph1), bfs(graph2))