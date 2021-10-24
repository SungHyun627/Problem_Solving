#P11049. 행렬 곱셈 순서
from sys import stdin

stdin = open('./input.txt', 'r')

#테스트 케이스
t = int(stdin.readline())
INF = 500 ** 4

#행렬 리스트
arr = [list(map(int, stdin.readline().split())) for _ in range(t)]


dp = [[0] * t for _ in range(t)]

#dp[a][b] = min(dp[a][b], dp[a][i] + dp[i+1][b] + dp[a][0]*dp[i][1]*dp[b][1])
for i in range(1, t):
    for j in range(t-i):
        if (j+i) == 1:
            dp[j][j+i] = arr[j][0] * arr[i+j][0] *arr[j+i][1]
            continue
        dp[j][j+i] = INF
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1]*arr[j+i][1])
print(dp[0][t-1])