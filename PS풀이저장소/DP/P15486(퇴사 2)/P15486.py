#P15486 퇴사 2
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = []
#dp[i]는 i번째 일에 얻을 수 있는 최대 이익
dp = [0] * (n+1)

for _ in range(n):
  arr.append(list(map(int, stdin.readline().split())))

for i in range(n):
  idx = i + arr[i][0]
  if (idx) < n+1:
      dp[idx] = max(dp[idx], dp[i] + arr[i][1])
  dp[i+1] = max(dp[i], dp[i+1])
print(dp[n])