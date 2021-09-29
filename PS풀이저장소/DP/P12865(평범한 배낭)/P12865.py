#P12865(평범한 배낭)
from sys import stdin

stdin = open('./input.txt', 'r')

#n : 물품의 수, k: 버틸 수 있는 무게
n, k = map(int, stdin.readline().split())

values = [(0, 0)]
for _ in range(n):
    values.append(tuple(map(int, stdin.readline().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        #해당 제품의 무게가 허용가능한 무게보다 크다면
        if values[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            # 해당 제품을 포함하는 경우 / 포함하지 않은 경우 중 max
            dp[i][j] = max(values[i][1] + dp[i-1][j-values[i][0]], dp[i-1][j])

print(dp[n][k])