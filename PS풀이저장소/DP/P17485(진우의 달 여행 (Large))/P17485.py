#P17485 진우의 달 여행 (Large)
from sys import stdin

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
universe = [[0]*m] + [list(map(int, stdin.readline().split())) for _ in range(n)]

# dp[i][j][k] : i번째 줄에서 j번째 열에 있는 위치에 k방향으로 도달할 경우의 수
# k가 0: 왼쪽 아래 방향, 1: 아래 방향, 2: 오른쪽 아래 방향
dp = [[[int(1e8)] * 3 for _ in range(m)] for _ in range(n+1)]

# 답
result = int(1e8)

for i in range(m):
    for j in range(3):
        dp[1][i][j] = universe[1][i]
    

for i in range(2, n+1) :
    for j in range(m):
        if j == 0:
            dp[i][0][0] = min(dp[i-1][1][1], dp[i-1][1][2]) + universe[i][0]
            dp[i][0][1] = dp[i-1][0][0] + universe[i][0]
            
        elif j == m-1:
            dp[i][m-1][1] = dp[i-1][m-1][2] + universe[i][m-1]
            dp[i][m-1][2] = min(dp[i-1][m-2][0], dp[i-1][m-2][1]) + universe[i][m-1]
        else:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + universe[i][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + universe[i][j]
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + universe[i][j]

# print(dp)
for i in range(m):
    if result > min(dp[n][i]):
        result = min(dp[n][i])

print(result)