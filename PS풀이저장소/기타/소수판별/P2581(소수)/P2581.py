#P2581 소수
from sys import stdin

stdin = open('./input.txt', 'r')

m = int(stdin.readline())
n = int(stdin.readline())

result = []
is_prime = [True] * (n+1)

for i in range(2, int(n ** 0.5) + 1):
    j = 2
    while i*j <= n:
        if is_prime[i*j]:
            is_prime[i*j] = False
        j += 1

for i in range(2, n+1):
    if is_prime[i] and i >= m:
        result.append(i)

print(-1) if not result else print(sum(result), result[0], sep='\n')