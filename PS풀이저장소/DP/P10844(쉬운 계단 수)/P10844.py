from sys import stdin

stdin = open('./input.txt', 'r')

# n : 자리 수
n = int(stdin.readline())

#세로 : 자릿 수 , 가로 : 맨 앞에 오는 숫자
dp = [[0] * (10) for _ in range(n+1)]

for i in range(10):
    dp[0][i] = 0
    if i == 0:
        dp[1][i] = 0
    else:
        dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 0
            continue
        if j == 1:
            if i == 2:
                dp[i][j] = dp[i-1][j+1] + 1
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-2][j]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)