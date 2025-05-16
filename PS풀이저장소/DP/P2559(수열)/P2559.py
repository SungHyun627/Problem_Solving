## P2559. 수열
from sys import stdin
stdin = open('./input.txt', 'r')

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
ans = sum(arr[:k])
cur_sum = sum(arr[:k])

for i in range(k, n):
  cur_sum += (arr[i] - arr[i-k])
  ans = max(ans, cur_sum)
print(ans)