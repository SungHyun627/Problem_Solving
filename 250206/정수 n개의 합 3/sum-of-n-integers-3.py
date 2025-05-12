n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0] * (n+1) for _ in range(n+1)]
ans = 0

for i in range(1, n+1):
    prefix_sum[i] = [0] + [t for t in arr[i-1]]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

for i in range(k, n+1):
    for j in range(k, n+1):
        ans = max(ans, prefix_sum[i][j] - prefix_sum[i-k][j] - prefix_sum[i][j-k] + prefix_sum[i-k][j-k])

print(ans)