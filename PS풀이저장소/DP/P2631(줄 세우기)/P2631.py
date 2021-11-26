#P2631 줄세우기
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

# 증가하는 부분 수열의 개수
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n-max(dp))