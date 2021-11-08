#P1912 연속합
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [i for i in arr]

for i in range(1, n):
    if dp[i-1] >= 0:
        dp[i] += dp[i-1]
print(max(dp))