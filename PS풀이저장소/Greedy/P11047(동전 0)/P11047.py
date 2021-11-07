#P11047 동전 0
from sys import stdin

stdin = open('./input.txt', 'r')

n, total = map(int, stdin.readline().split())
result = 0
coins = list(int(stdin.readline()) for _ in range(n))

for i in range(n-1, -1, -1):
    result += (total // coins[i])
    total %= coins[i]
    if total == 0:
        break
print(result)