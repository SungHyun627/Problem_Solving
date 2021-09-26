from bisect import bisect_left
from sys import stdin

stdin = open('./input.txt', 'r')

# O(n^2) 방법

#수열의 크기
n = int(stdin.readline())
#수열
arr = list(map(int, stdin.readline().split()))

#dp[i] : 0~i번째로 만들수 있는 LIS의 길이
dp = [1] * (n)

#최장 LIS
answer = []

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)

target_index = n
for i in range(max_length, 0, -1):
    for j in range(target_index-1,  -1, -1):
        if dp[j] == i:
            answer.append(arr[j])
            target_index = j
            break

#역순
answer.reverse()

print(max_length)
print(*answer)