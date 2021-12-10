#P2589 보물섬
# PyPy로 채점
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')
max_dist = 0

n, m = map(int, stdin.readline().split())
board = list(list(stdin.readline()) for _ in range(n))
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(s_x, s_y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    visited[s_x][s_y] = True
    queue.append((s_x, s_y, 0))

    while queue:
        x, y, dist = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] or board[nx][ny] == 'W':
                continue
            queue.append((nx, ny, dist+1))
            visited[nx][ny] = True
    return dist

for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            max_dist = max(max_dist, bfs(i, j))
print(max_dist)