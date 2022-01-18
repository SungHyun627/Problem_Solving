# P4963 섬의 개수
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

def bfs(sx, sy):
    queue = deque()
    count = 0
    board = list(list(map(int, stdin.readline().split())) for _ in range(sx))
    visited = [[False] * sy for _ in range(sx)]
    for i in range(sx):
        for j in range(sy):
            if board[i][j] and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= sx or ny >= sy:
                            continue
                        if not board[nx][ny] or visited[nx][ny]:
                            continue
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                count += 1
    print(count)

while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    bfs(b, a)
