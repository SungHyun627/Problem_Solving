#P10942 팰린드롬?
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = [0] + list(map(int, stdin.readline().split()))
#테스트 케이스 수
t = int(stdin.readline())

#2차원 dp 리스트
dp = [[False] * (n+1) for _ in range(n+1)]


for i in range(1, n+1):
    dp[i][i] = True

for interval in range(1, n):
    for i in range(1, n-interval+1):
        if arr[i] != arr[i+interval]:
            continue
        if interval == 1:
            dp[i][i+interval] = True
        if dp[i+1][i+interval-1]:
            dp[i][i+interval] = True

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    print(1) if dp[a][b] else print(0)