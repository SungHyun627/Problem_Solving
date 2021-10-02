from sys import stdin

stdin = open('./input.txt', 'r')

#집의 수
n = int(stdin.readline())

arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n-1]))