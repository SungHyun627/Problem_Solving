#P1600 말이 되고픈 원숭이
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

k = int(stdin.readline())
w, h = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(h)]
dist = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]

def bfs():
    if h == 1 and w ==1:
        return 0
    dx, dy = [0, 0, -1, 1, -2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, 0, 0, -1, 1, 2, -2, 2, -2, 1, -1]
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        # print(queue)
        x, y, t = queue.popleft()
        for i in range(12):
            if t == k and i >= 4:
                break
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
                
            if board[nx][ny]:
                continue

            if i < 4:
                if dist[nx][ny][t] or (nx == 0 and ny == 0):
                    continue
                else:
                    if nx == h-1 and ny == w-1:
                        return dist[x][y][t] + 1
                    else:
                        dist[nx][ny][t] = dist[x][y][t] + 1
                        queue.append((nx, ny, t))
            else:
                if dist[nx][ny][t+1] or (nx == 0 and ny == 0):
                    continue
                else:
                    if nx == h-1 and ny == w-1:
                        return dist[x][y][t] + 1
                    else:
                        dist[nx][ny][t+1] = dist[x][y][t] + 1
                        queue.append((nx, ny, t+1))
    return -1

print(bfs())