from sys import setrecursionlimit
setrecursionlimit(10**6)
n = int(input())

# Initialize arrays with n+1 size to match 1-based indexing
t = [0] * (n + 1)
a = [0] * (n + 1)
children = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for i in range(2, n + 1):
    t[i], a[i], p = map(int, input().split())
    children[p].append(i)
    dp[i] = a[i] if t[i] == 1 else -a[i]

def dfs(x):
    for node in children[x]:
        dfs(node)
    
    for node in children[x]:
        if dp[node] > 0:
            dp[x] += dp[node]
    
dfs(1)
print(dp[1])