#P14442 벽 부수고 이동하기 2
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n, m, k = map(int, stdin.readline().split())
dist = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
board = list(list(map(int, stdin.readline().rstrip())) for _ in range(n))

def bfs():
    # board가 1X1이라면
    if n == 1 and m == 1:
        return 1
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    queue = deque()
    dist[0][0][0] = 1
    queue.append((0, 0, 0))
    
    while queue:
        x, y, t = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if dist[nx][ny][t]:
                continue
            if t == k and board[nx][ny]:
                continue
            if nx == n-1 and ny == m-1:
                return dist[x][y][t] + 1
            
            if board[nx][ny]:
                queue.append((nx, ny, t+1))
                dist[nx][ny][t+1] = dist[x][y][t] + 1
            else:
                queue.append((nx, ny, t))
                dist[nx][ny][t] = dist[x][y][t] + 1
    return -1

print(bfs())