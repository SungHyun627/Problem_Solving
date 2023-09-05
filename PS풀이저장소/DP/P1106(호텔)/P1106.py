#P1106 호텔
from sys import stdin

stdin = open('./input.txt', 'r')
c, n = map(int, stdin.readline().split())
a = []
MAX_IDX = 100*1000 + 1
dp = [0]*(MAX_IDX)
isDone = False
answer = -1

for _ in range(n):
  a.append(tuple(map(int, stdin.readline().split())))

for i in range(1, MAX_IDX+1):
  for j in range(n):
    if (i - a[j][0] >= 0):
      dp[i] = max(dp[i], dp[i-a[j][0]] + a[j][1])
      if dp[i] >= c:
        isDone = True
        answer = i
        break
  if isDone: break

print(answer)
