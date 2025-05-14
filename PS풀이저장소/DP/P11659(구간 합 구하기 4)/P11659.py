### P11659 구간합 구하기
from sys import stdin
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
arr = [0] + list(map(int, stdin.readline().split()))

for i in range(1, n+1):
  arr[i] += arr[i-1]

for _ in range(m):
  a, b = map(int, stdin.readline().split())
  print(arr[b] - arr[a-1])