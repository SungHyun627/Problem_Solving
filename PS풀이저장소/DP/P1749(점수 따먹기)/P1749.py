#P1749. 점수따먹기
from sys import stdin
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = -10000 * 200 * 200

for r1 in range(n):
  temp = [0] * (m)
  for r2 in range(r1, n):
    for c in range(m):
      temp[c] += arr[r2][c]
    max_sum = temp[0]
    cur_sum = temp[0]
    for i in range(1, m):
      cur_sum = max(cur_sum + temp[i], temp[i])
      max_sum = max(max_sum,cur_sum)
    ans = max(ans, max_sum)
  
print(ans)