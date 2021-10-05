from sys import stdin

##PyPy로 통과
stdin = open('./input.txt', 'r')

max_len = 0
str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
    if max_len < max(dp[i]):
        max_len = max(dp[i])

print(max_len)