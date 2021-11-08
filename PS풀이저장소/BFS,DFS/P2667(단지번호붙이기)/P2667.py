from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
graph = list(list(map(int, stdin.readline().rstrip())) for _ in range(n))
result = []
visited = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            queue = deque()
            num = 1
            visited[i][j] = True
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if visited[nx][ny] or graph[nx][ny] == 0:
                        continue
                    visited[nx][ny] = True
                    num += 1
                    queue.append((nx, ny))
            result.append(num)

result.sort()
print(len(result), *result, sep='\n')