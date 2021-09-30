from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())

dp = [0] * (n+1)

count = 0
    
for i in range(1, n+1):
    if i == 1:
        dp[i] = 0
        continue
    
    if i % 2 == 0:
        if i % 3 == 0:
            dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
        else:
            dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        if i % 3 == 0:
            dp[i] = min(dp[i-1], dp[i//3]) + 1
        else:
            dp[i] = dp[i-1] + 1

print(dp[n])

while True:
    print(n, end = ' ')
    if n == 1:
        break
    if n % 2 == 0:
        if n % 3 == 0:
            min_n = min(dp[n-1], dp[n//2], dp[n//3])
            if min_n == dp[n-1]:
                n -= 1
                continue
            elif min_n == dp[n//2]:
                n //=2
                continue
            else:
                n //=3
                continue
        else:
            min_n = min(dp[n-1], dp[n//2])
            if min_n == dp[n-1]:
                n -= 1
                continue
            else:
                n //=2
                continue
    else:
        if n % 3 == 0:
            min_n = min(dp[n-1], dp[n//3])
            if min_n == dp[n-1]:
                n -= 1
                continue
            else:
                n //= 3
        else:
            n -= 1