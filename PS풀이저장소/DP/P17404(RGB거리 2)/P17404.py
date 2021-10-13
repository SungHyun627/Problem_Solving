from sys import stdin
from itertools import permutations
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
def calculate_cost(case):
    dp = [[int(1e9)] * 3 for _ in range(n)]
    dp[0][case[0]] = arr[0][case[0]]
    for i in range(1, n-1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
    
    dp[n-1][case[1]] = min(dp[n-2][(case[1]+1) % 3], dp[n-2][(case[1]-1) % 3]) + arr[n-1][case[1]]
    return min(dp[n-1])
    
min_cost = int(1e9)
for i in list(permutations(range(3), 2)):
    min_cost = min(min_cost, calculate_cost(i))
print(min_cost)