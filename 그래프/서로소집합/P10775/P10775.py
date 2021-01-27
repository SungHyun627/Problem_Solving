from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')
# 게이트 수
g = int(stdin.readline())
# 비행기 수
p = int(stdin.readline())

# 각 게이트의 parent를 나타내는 리스트
gate = [i for i in range(g+1)]

# 해당 gate의 root를 찾는 함수
def find_root(gate, x):
    if gate[x] != x:
        gate[x] = find_root(gate, gate[x])
    return gate[x]

# 해당 gate의 root와 root의 왼쪽에 있는 gate를 간선으로 이어 union 시킨다
def union(gate, x):
    root = find_root(gate, x)
    gate[root] = root-1

# 도킹시킬 수 있는 비행기 수
num = 0
for _ in range(p):
    g = int(stdin.readline())
    if find_root(gate, g) == 0:
        break
    union(gate, g)
    num += 1

print(num)