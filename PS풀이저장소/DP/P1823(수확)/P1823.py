#P1823 수확
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = list(int(stdin.readline()) for _ in range(n))

# dp[i][j] : i부터 j까지의 벼가 남았을 때, n-(j-i)번째 벼를 수확할 때의 최대 이익
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = arr[i] * n

for k in range(1, n):
    for i in range(n-k):
        dp[i][i+k] = max(dp[i][i+k-1] + arr[i+k]*(n-k), dp[i+1][i+k] + arr[i]*(n-k))

print(dp[0][n-1])