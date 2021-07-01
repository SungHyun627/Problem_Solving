from sys import stdin
from collections import deque
from itertools import product, combinations

stdin = open('./input.txt', 'r')
n, m  = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
new_graph = [[0] * m for _ in range(n)]
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(new_graph, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if new_graph[nx][ny] != 1 and new_graph[nx][ny] != 2:
                    new_graph[nx][ny] = 2
                    queue.append((nx, ny))

for walls in list(combinations(list(product([i for i in range(n)], [j for j in range(m)])), 3)):
    stop = False
    temp_result = 0
    for i in range(n):
        for j in range(m):
            new_graph[i][j] = graph[i][j]

    for wall in walls:
        x, y = wall
        if new_graph[x][y] != 0:
            stop = True
            break
        new_graph[x][y] = 1

    if stop == True:
        continue

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                bfs(new_graph, i, j)
    
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                temp_result += 1
    result = max(result, temp_result)    

print(result)