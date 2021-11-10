#P2583 영역 구하기
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

m, n, k = map(int, stdin.readline().split())
board = [[0] * n for _ in range(m)]
result = []
count = 0
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

for _ in range(k):
    a, b, c, d = map(int, stdin.readline().split())
    b = m - b - 1 
    c -= 1
    d = m - d
    for i in range(d, b+1):
        for j in range(a, c+1):
            board[i][j] = 1

def bfs(i, j):
    area = 1
    queue = deque()
    board[i][j] = 1
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue
            area += 1
            board[nx][ny] = 1
            queue.append((nx, ny))
    return area
                


for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            count += 1
            result.append(bfs(i, j))
result.sort()
print(count)
print(*result)
