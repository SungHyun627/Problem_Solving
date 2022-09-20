#P2230 수 고르기
from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')
ans = 2 * int(1e9) + 1
n, m = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(n)]

# 정렬
arr.sort()
end = 0
for start in range(n):
  while(end < n and arr[end] - arr[start] < m):
    end += 1
  if end == n:
    break
  ans = min(ans, arr[end] - arr[start])

print(ans)