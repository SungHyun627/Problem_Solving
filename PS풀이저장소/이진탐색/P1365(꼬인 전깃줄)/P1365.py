#P1365 꼬인 전깃줄
from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')

#전선의 수
n = int(stdin.readline())
#연결된 전선의 배열
arr = list(map(int, stdin.readline().split()))

dp = [arr[0]]
end = 0

for i in range(1, n):
    #다음 올 수가 dp에 저장된 맨 마지막 수보다 크다면
    if dp[end] < arr[i]:
        dp.append(arr[i])
        end += 1
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]

#연결할 수 있는 최대 전선 수 => end + 1
print(n - (end + 1))