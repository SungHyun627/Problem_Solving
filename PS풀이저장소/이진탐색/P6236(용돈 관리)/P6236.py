### P6236 용돈 관리
from sys import stdin
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
arr = [int(stdin.readline().rstrip()) for _ in range(n)]
ans = n
start, end = max(arr), sum(arr)

while (start <= end):
  mid = (start + end) // 2
  
  cnt = 0
  remainder = 0
  for i in range(n):
    if (remainder < arr[i]):
      remainder = mid
      cnt +=1
    remainder -= arr[i]

  if m >= cnt:
    ans = mid
    end = mid - 1
    
  else:
    start = mid + 1
print(ans)

