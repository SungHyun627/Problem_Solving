#P5575 1학년
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = [0] + list(map(int, stdin.readline().split()))

# dp[i][j] => i개의 숫자를 계산했을 대 j의 값을 가지게 되는 경우의 수
dp = [[0]*21 for _ in range(n+1)]

# 첫번째 수를 계산했을 때의 경우의 수는 1
dp[1][arr[1]] = 1

for i in range(2, n):
    for j in range(21):
        # i-1번째까지 계산한 결과가 j이고
        if dp[i-1][j] > 0:
            # j+arr[i]가 20이하 일때
            if j+arr[i] <= 20:
                dp[i][j+arr[i]] += dp[i-1][j]
            # j-arr[i]가 0이상일 때
            if j-arr[i] >= 0:
                dp[i][j-arr[i]] += dp[i-1][j]

# print(dp)
print(dp[n-1][arr[n]])