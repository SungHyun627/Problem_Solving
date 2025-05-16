## P1182. 부분수열의 합
from sys import stdin
stdin = open('./input.txt', 'r')

n, s = map(int, stdin.readline().split())
lis = list(map(int, stdin.readline().split()))
ans = 0

def backtrack(idx, total, num):
  global ans
  if idx == n:
    if total == s and num != 0:
      ans += 1  
    return
  backtrack(idx+1, total+lis[idx], num+1)
  backtrack(idx+1, total, num)

backtrack(0, 0, 0)
print(ans)