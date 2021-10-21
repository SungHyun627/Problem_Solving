from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

t = int(stdin.readline())

def bfs(x1, y1, x2, y2, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x1, y1, 0))
    visited[x1][y1] = True
    
    while queue:
        x, y, count = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            if visited[nx][ny]:
                continue

            if nx == x2 and ny == y2:
                return count + 1
                
            if not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True
    return 0

for _ in range(t):
    n = int(stdin.readline())
    x1, y1 = map(int, stdin.readline().split())
    x2, y2 = map(int, stdin.readline().split())
    print(bfs(x1, y1, x2, y2, n))