#P7576 토마토
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

def is_all_ripe(arr):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not arr[i][j]:
                return False
    return True

def bfs():
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j, 0))
                visited[i][j] = True
    while queue:
        # print(queue)
        x, y, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if visited[nx][ny] or graph[nx][ny] == -1:
                continue
            
            if graph[nx][ny] == 1:
                queue.append((nx, ny, count))
            else:
                queue.append((nx, ny, count + 1))
            visited[nx][ny] = True
    if is_all_ripe(visited):
        return count
    else:
        return -1

print(bfs())