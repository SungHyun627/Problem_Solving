#P14940 쉬운 최단거리
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
# 방향 벡터
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
startx, starty = -1, -1
board = [] 
dist_graph = [[-1] * m for _ in range(n)]

for i in range(n):
    a = list(map(int, stdin.readline().split()))
    for j in range(m):
        if startx == -1 and a[j] == 2:
            startx, starty = i, j
        if a[j] == 0:
            dist_graph[i][j] = 0
    board.append(a)

queue = deque()
dist_graph[startx][starty] = 0
queue.append((startx, starty, 0))

while queue:
    x, y, dist = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if dist_graph[nx][ny] != -1:
            continue
        dist_graph[nx][ny] = dist + 1
        queue.append((nx, ny, dist + 1))

for i in range(n):
    print(*dist_graph[i])