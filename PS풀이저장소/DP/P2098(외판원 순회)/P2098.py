## P2098. 외판원 순회
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
w = [list(map(int, stdin.readline().split())) for _ in range(n)]
size = 1 << n

INF = float('inf')
## dp[visited][city]
dp = [[INF] * n for _ in range(size)]
dp[1<<0][0] = 0
ans = float('inf')

for visited in range(size):
  for last in range(n):
    ### last가 포함되지 않았을 때
    if not (visited & (1 << last)):
      continue
    for next in range(n):
      ### next를 이미 방문했을 때
      if (visited & (1 << next)):
        continue
      ### last -> next 경로가 없을 때
      if w[last][next] == 0:
        continue
      n_visited = visited | (1 << next)
      dp[n_visited][next] = min(dp[n_visited][next], dp[visited][last] + w[last][next])

for i in range(n):
  ### i에서 0으로 가는 경로가 없을 때
  if w[i][0] == 0:
    continue
  ans = min(ans, dp[size -1][i] + w[i][0])

print(ans)