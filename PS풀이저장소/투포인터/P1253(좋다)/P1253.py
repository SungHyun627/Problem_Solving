### P1253 좋다
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = list(map(int, stdin.readline().rstrip().split()))

arr.sort()
result = 0

for i in range(n):
  target = arr[i]
  start, end = 0, n-1

  while(start < end):
    sum = arr[start] + arr[end]
    if start == i:
      start += 1
      continue
    if end == i:
      end -= 1
      continue

    if sum == target:
      result += 1
      break
    if sum < target:
      start += 1
    else:
      end -= 1
print(result)
