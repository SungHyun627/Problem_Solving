#P1003 피보나치 함수
from sys import stdin

stdin = open('./input.txt', 'r')

t = int(stdin.readline())
zero_count = 0
one_count = 0

dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(t):
    n = int(stdin.readline())
    print(*dp[n])