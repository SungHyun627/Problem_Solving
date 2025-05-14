### P1806 부분합
from sys import stdin
stdin = open('./input.txt', 'r')

n, s = map(int, stdin.readline().split())
arr = [0]+list(map(int ,stdin.readline().split()))

for i in range(1, n+1):
  arr[i] += arr[i-1]

ans = n
start, end = 1, 1

while True:
  total = arr[end] - arr[start-1]
  if (start == n):
    if (total >= s):
      ans = min(ans, end-start+1)  
    break
  if (end == n and total < s): break
  if (total >= s):
    ans = min(ans, end-start+1)
    if (end-start+1) == 1: break
    start += 1
  else:
    end +=1
  
print(0 if arr[n] < s else ans)
