from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().rstrip().split()))
#dp 방법 : O(n^2)
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))