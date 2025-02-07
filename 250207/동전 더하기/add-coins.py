n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

ans = 0

for i in range(n-1, -1, -1):
    ans += k // coins[i]
    k %= coins[i]
    if k == 0:
        break

print(ans)