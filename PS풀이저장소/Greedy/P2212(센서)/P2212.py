#P2212 센서
from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
k = int(stdin.readline())
answer = 0
arr = list(map(int, stdin.readline().split()))
diff = []

if n <= k:
  answer = 0
else:
  arr.sort()
  for i in range(n-1):
    diff.append(arr[i+1]- arr[i])
  diff.sort()
  answer = sum(diff[:n-k])
    
print(answer)