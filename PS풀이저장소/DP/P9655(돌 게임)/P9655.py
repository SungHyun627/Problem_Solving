#P9655 돌 게임
#마지막으로 돌을 가져가는 사람이 이기는 게임
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())

dp = [False] * (1001)
dp[1], dp[2], dp[3] = True, False, True

for i in range(4, 1001):
    dp[i] = (not dp[i-1] and not dp[i-3])
    
print("SK") if dp[n] else print("CY")