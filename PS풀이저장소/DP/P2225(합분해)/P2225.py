from sys import stdin
from math import factorial

stdin = open('./input.txt', 'r')
n, k = map(int, stdin.readline().split())

#중복 조합 
print((factorial(n+k-1) // (factorial(n) * factorial(k-1))) % int(1e9))

#dp 풀이
#dp[i][k] = dp[i-1][k] + dp[i][k-1]
dp = [0] * (n+1)
dp[0] = 1

for _ in range(1, k+1):
    for i in range(1, n+1):
        dp[i] = (dp[i] + dp[i-1])%int(1e9)
print(dp[n])