#P11722 가장 긴 감소하는 부분 수열
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [1] * (n)

for i in range(1, n):
  for j in range(i):
    if arr[i] < arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))