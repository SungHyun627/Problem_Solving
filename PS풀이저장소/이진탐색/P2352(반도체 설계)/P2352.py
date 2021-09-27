from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')

#n개의 연결
n = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))

dp = [arr[0]]
end = 0

for i in range(1, n):
    if dp[end] < arr[i]:
        dp.append(arr[i])
        end += 1
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
print(end+1)