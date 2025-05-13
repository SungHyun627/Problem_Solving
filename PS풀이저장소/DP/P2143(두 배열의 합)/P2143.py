### P2143. 두 배열의 합
from sys import stdin
from bisect import bisect_left, bisect_right
stdin = open('./input.txt', 'r')

t = int(stdin.readline())
n = int(stdin.readline())
arr1 = [0] + list(map(int, stdin.readline().split()))
m = int(stdin.readline())
arr2 = [0] + list(map(int, stdin.readline().split()))
result = 0

a = []
b = []

for i in range(1, n+1):
  arr1[i] += arr1[i-1]

for i in range(1, m+1):
  arr2[i] += arr2[i-1]

for i in range(n):
   for j in range(i+1, n+1):
      a.append(arr1[j] - arr1[i])

for i in range(m):
   for j in range(i+1, m+1):
      b.append(arr2[j] - arr2[i])
a.sort()

for i in range(len(b)):
  k = t - b[i]
  result += (bisect_right(a, k)-bisect_left(a, k))

print(result)