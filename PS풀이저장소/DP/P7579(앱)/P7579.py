#dp
from sys import stdin

stdin = open('./input.txt', 'r')

# n : 앱의 개수, m: 필요한 메모리
n, m = map(int, stdin.readline().split())
weights = list(map(int, stdin.readline().split()))
costs = list(map(int, stdin.readline().split()))

#최소 비용
min_cost = 10000

dp = [[0]*10001 for _ in range(n)]

for i in range(n):
    for j in range(10001):
        if costs[i] > j:
            if i == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if i == 0:
                dp[i][j] = weights[i]
            else:
                dp[i][j] = max(dp[i-1][j-costs[i]] + weights[i], dp[i-1][j])

for k in range(10001):
    if dp[n-1][k] >=m:
        print(dp[n-1][k])
        break