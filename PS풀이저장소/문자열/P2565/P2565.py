from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = [0] * (501)
for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split()) 
    arr[a] = b

dp = []
for i in range(501):
    if arr[i] != 0:
        dp.append(arr[i])
        break
end = 0

for i in range(1, 501):
    if arr[i] == 0:
        continue
    if dp[end] < arr[i]:
        dp.append(arr[i])
        end += 1
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
    # print(dp)
print(n - len(dp))