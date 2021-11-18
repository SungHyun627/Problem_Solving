# P7569 토마토
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

# h : 상자의 수, m : 상자의 가로 칸 수, n : 상자의 세로 칸수
m, n, h = map(int, stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]

def is_all_riped(arr):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] != -1 and not arr[i][j][k]:
                    return False
    return True
    

def bfs(q, visited):
    dh, dx, dy =  [0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]
        
    while q:
        z, x, y, count = q.popleft()
        for i in range(6):
            nz = z + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nz >= h or nx >= n or ny >= m or nz < 0 or nx < 0 or ny < 0:
                continue
            if visited[nz][nx][ny]:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            queue.append((nz, nx, ny, count + 1))
            visited[nz][nx][ny] = True
    if is_all_riped(visited):
        return count
    else:
        return -1
            
queue = deque()
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k, 0))
                visited[i][j][k] = True

print(bfs(queue, visited))