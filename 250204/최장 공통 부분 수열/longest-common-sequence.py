a = input()
b = input()

x = len(a)
y = len(b)

dp = [[0] * (y+1) for _ in range(x+1)]


for i in range(1, x+1):
    for j in range(1, y+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[x][y])
