from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

#대나무 숲의 크기
n = int(stdin.readline())
#대나무 숲
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

#상, 하, 좌, 우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

#dp table
dp = [[0] * n for _ in range(n)]

move_max = 1

#각 지점에 대하여 DFS
def DFS(x, y):
    global move_max

    if dp[x][y] != 0:
        return dp[x][y]
        
    dp[x][y] = 1
    move_count = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        #범위를 벗어났을 때
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue

        if graph[nx][ny] > graph[x][y]:
            move_count = max(move_count, DFS(nx, ny))
    dp[x][y] += move_count
    
    move_max = max(move_max, dp[x][y])
    return dp[x][y]
    
for i in range(n):
    for j in range(n):
        DFS(i, j)

print(move_max)