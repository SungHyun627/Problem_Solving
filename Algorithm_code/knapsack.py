## 코드 (2차원 DP)
N, K = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(K + 1):
        if w < weights[i-1]:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])

print(dp[N][K])  # 최대 가치

## 1차원 DP, 뒤에서부터 업데이트
dp = [0] * (K + 1)

for i in range(N):
    for w in range(K, weights[i] - 1, -1):  # 역순 루프
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

print(dp[K])