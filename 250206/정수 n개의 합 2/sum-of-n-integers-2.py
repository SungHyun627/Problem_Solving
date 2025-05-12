n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n+1)
prefix_sum[1] = arr[1]
ans = -100*k

for i in range(2, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for i in range(k, n+1):
    ans = max(ans, prefix_sum[i] - prefix_sum[i-k])
print(ans)