from sys import stdin
#카탈란 수

stdin = open('./input.txt', 'r')

dp = [0] * 31
dp[0] = 1

for i in range(1, 31):
    for j in range(i):
        dp[i] += dp[j]*dp[i-1-j]

while True:
    n = int(stdin.readline())
    if not n:
        break
    print(dp[n])