#P20291 파일 정리
from sys import stdin
from collections import defaultdict

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
d = defaultdict(int)
for _ in range(n):
  x, y = stdin.readline().rstrip().split('.')
  d[y] += 1
keys = list(d.keys())
keys.sort()

for key in keys:
  print(f"{key} {d[key]}")
  