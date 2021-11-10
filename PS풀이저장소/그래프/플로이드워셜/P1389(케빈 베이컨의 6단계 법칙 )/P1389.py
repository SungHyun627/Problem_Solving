#P1389 케빈 베이컨의 6단계 법칙 
from sys import stdin

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
dp = [[100] * (n+1) for _ in range(n+1)]
min_num = 100 * 5000
result = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    dp[a][b] = 1
    dp[b][a] = 1

for i in range(1, n+1):
    dp[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1):
    temp_sum = sum(dp[i][1:])
    if min_num > temp_sum:
        min_num = temp_sum
        result = i
print(result)