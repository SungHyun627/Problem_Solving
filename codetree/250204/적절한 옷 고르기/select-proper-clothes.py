n, m = map(int, input().split())
clothes = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]* n for _ in range(m+1)]

for i in range(2, m+1):
    for j in range(n):
        s, e, v = clothes[j]
        if s <= i <= e:
            for k in range(n):
                bs, be, bv = clothes[k]
                if bs <= i-1 <= be:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v-bv))
print(max(dp[m]))






# Write your code here!
