# P11726 2 * n 타일링
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
dp = [0] * (n+1)
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n] % 10007)