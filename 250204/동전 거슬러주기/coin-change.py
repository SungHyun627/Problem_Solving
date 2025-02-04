n, m = map(int, input().split())
coin = list(map(int, input().split()))

dp = [m] * (m+1)
dp[0] = 0


for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)

print(dp[m])
