from sys import stdin

stdin = open('./input.txt', 'r')

#테스트 케이스 수
t = int(stdin.readline())

def calculate_cases(n, arr, m):
    dp = [0] * (m+1)
    dp[0] = 1
    for i in range(n):
        for j in range(arr[i], m+1):
            dp[j] += dp[j-(arr[i])]
    return dp[m]

for k in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    print(calculate_cases(n, arr, m))