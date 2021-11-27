#P2579 계단 오르기
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = [0]
for _ in range(n):
    arr.append(int(stdin.readline()))
    
# dp[x][0]은 x번째 계단에 위치했을 때 그 전계단을 밟았을 때의 경우의 수
# dp[x][1]은 x번째 계단에 위치했을 때 그 전계단을 밟지 않았을 때의 경우의 수
dp = [[0] * 2 for _ in range(n+1)]

dp[1][0], dp[1][1] = arr[1], arr[1]

for i in range(2, n+1):
    dp[i][0] = arr[i] + dp[i-1][1]
    dp[i][1] = arr[i] + max(dp[i-2])
print(max(dp[n]))