from sys import stdin

stdin = open('./input.txt', 'r')

dp = [0]*1000001
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 1000001):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= 1000000009

#테스트 케이스 수
t = int(stdin.readline())

for _ in range(t):
    print(dp[int(stdin.readline())])