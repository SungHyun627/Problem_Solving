from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

n = int(stdin.readline())

# 간선
edges = []
# 컴퓨터를 연결하기 위해 필요한 랜선의 길이
lineLength = 0
# 전체 랜선의 길이
sumLength = 0

for i in range(1, n+1):
    temp = list(map(ord, stdin.readline().rstrip()))
    for j in range(n):
        if 97 <= temp[j] <= 122:
            temp[j] = temp[j] - 96
        elif 65 <= temp[j] <= 90:
            temp[j] = temp[j] - 38
        else:
            temp[j] = 0
        if temp[j] != 0:
            edges.append((temp[j], i, j+1))
    sumLength += sum(temp)

# edges를 길이에 따라 정렬
edges.sort()

# 각 컴퓨터의 root를 기록하는 parent table
parent = [i for i in range(n + 1)]

# root를 찾는 함수
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

# 두 node(컴퓨터)의 root를 union 하는 함수
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for edge in edges:
    line, a, b = edge
    if a == b:
        continue
    # 만약 동일한 집합에 a, b가 속해있지 않다면
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        lineLength += line

# 모든 edge에 대한 연산을 마친 후, 각 node의 parent를 찾는다.
for i in range(1, n+1):
    findParent(parent, i)
    
if parent.count(1) == n:
    print(sumLength - lineLength)
else:
    print(-1)