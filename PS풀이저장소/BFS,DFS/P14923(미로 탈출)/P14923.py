#P14923 미로 탈출
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
hx, hy = map(int, stdin.readline().split())
hx -= 1
hy -= 1
ex, ey = map(int, stdin.readline().split())
ex -= 1
ey -= 1

board = [list(map(int, stdin.readline().split())) for _ in range(n)]
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    queue = deque()
    queue.append((hx, hy, 0))
    while queue:
        # print(queue)
        x, y, k = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if nx == hx and ny == hy:
                continue
            if nx == ex and ny == ey:
                return dist[x][y][k] + 1
            
            if board[nx][ny]:
                if k == 1:
                    continue
                else:
                    if dist[nx][ny][1]:
                        continue
                    else:
                        dist[nx][ny][1] = dist[x][y][0] + 1
                        queue.append((nx, ny, 1))
            else:
                if not dist[nx][ny][k]:
                    dist[nx][ny][k] = dist[x][y][k] + 1
                    queue.append((nx, ny, k))
    return -1

print(bfs())