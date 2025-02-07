n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

graph = [[0] for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]
graph[0].extend([0]*n)

for i in range(1, n+1):
    graph[i].extend(grid[i-1])

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(grid[i-1][j-1], min(dp[i][j-1], dp[i-1][j]))

print(dp[n][n])


