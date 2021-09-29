#DFS + DP
from sys import stdin, setrecursionlimit
from collections import deque

stdin = open('./input.txt', 'r')

setrecursionlimit(10**6)

#세로 : m, 가로 : n
m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(m)]


#이동하는 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dp = [[-1] *n for _ in range(m)]

def dfs(x, y):
    # print(x, y)
    #도착 지점인 경우 1 return
    if x == m-1 and y == n-1:
        return 1
    
    #방문하지 않은 경우
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]


print(dfs(0, 0))
# print(dp)