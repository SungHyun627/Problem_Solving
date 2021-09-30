from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

# n : 세로, m : 가로
n, m = map(int, stdin.readline().split())

graph = [list(stdin.readline().rstrip()) for _ in range(n)]

#각 지점에서 이동할 수 있는 칸의 개수를 저장하는 2차원 리스트
move = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            move[i][j] = 1

#방문 배열
visited = [[False] * m for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(x, y):
    
    #방문한 칸의 수
    count = 1
    queue = deque()

    #마주친 벽 set
    walls = set()

    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if (not visited[nx][ny]) and graph[nx][ny] == '0':
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
            if graph[nx][ny] == '1':
                if (nx, ny) not in walls:
                    walls.add((nx, ny))
    #print(walls, count)
    for wall in walls:
        move[wall[0]][wall[1]] += count

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            move[i][j] %= 10
    print(''.join(map(str, move[i])))