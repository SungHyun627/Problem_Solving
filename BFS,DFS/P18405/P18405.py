from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

# n: 시험관의 가로, 세로 길이,, k: 바이러스 종류
n, k = map(int, stdin.readline().split())

# 시험관
graph = []

# 방향 리스트(동, 서, 남, 북)
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

graph = [list(map(int, stdin.readline().split())) for _ in range(n)]    

# s: 경과 시간, sx, sy : s초 후 살펴볼 좌표의 위치
s, sx, sy = map(int, stdin.readline().split())

def bfs():
    # 큐 생성 
    queue = deque()
    # 바이러스가 있는 공간의 바이러스 종료, 위치를 저장하는 리스트
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                virus.append((graph[i][j], i, j))

    for _ in range(s):
        if len(virus) == n ** 2:
            break
        virus.sort()
        queue.extend(virus)
        while queue:
            number, x, y, = queue.popleft()    
            for i in range(4):
                # 주위 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = number
                    virus.append((number, nx, ny))
                
bfs()
print(graph[sx-1][sy-1])