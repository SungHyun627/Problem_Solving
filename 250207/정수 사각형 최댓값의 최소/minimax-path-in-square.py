n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n) for _ in range(n)]

dp[0] = [i for i in graph[0]]

for i in range(1, n):
    dp[i][0] = graph[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(graph[i][j], min(dp[i][j-1], dp[i-1][j]))

print(dp[n-1][n-1])


