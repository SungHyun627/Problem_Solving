### P9184 신나는 함수 실행
from sys import stdin
stdin = open('./input.txt', 'r')

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]


for i in range(21):
  for j in range(21):
    dp[0][i][j] = 1
    dp[i][0][j] = 1
    dp[i][j][0] = 1

for i in range(1, 21):
  for j in range(1, 21):
    for k in range(1, 21):
      if i < j and j < k:
        dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
      else:
        dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
        


def w(a, b, c):
  if a <= 0 or b <=0 or c <=0:
    return 1
  if a > 20 or b > 20 or c > 20:
    return dp[20][20][20]
  return dp[a][b][c]


while 1:
  a, b, c = map(int, stdin.readline().split())
  if a == -1 and b == -1 and c == -1:
    break
  result = w(a, b, c)
  print('w({}, {}, {}) = {}'.format(a, b, c, result))
