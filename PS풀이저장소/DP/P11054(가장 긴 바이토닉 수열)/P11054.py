#P11054 가장 긴 바이토닉 부분 수열
from sys import stdin
stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
max_length = 0

# 해당 원소를 포함하여 이전 수열 중 가장 긴 증가 부분 수열의 길이를 저장하는 dp
dp1 = [1] * n 
# 해당 원소를 포함한 이후 수열 중 가장 긴 증가 부분 수열의 길이를 저장하는 dp
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] <= arr[j]:
            continue
        dp1[i] = max(dp1[j] + 1, dp1[i])

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] <= arr[j]:
            continue
        dp2[i] = max(dp2[j]+ 1, dp2[i])

for i in range(n):
    max_length = max(max_length, dp1[i] + dp2[i])
print(max_length - 1)