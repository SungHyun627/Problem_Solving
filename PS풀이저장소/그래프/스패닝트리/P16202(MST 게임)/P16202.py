#P16202 MST 게임
from sys import stdin

stdin = open('./input.txt', 'r')
n, m, k = map(int, stdin.readline().split())
edges = [0] * (m+1)
isUsed = [False] * (m+1)
parents = [i for i in range(n+1)]
result = []
lines = []
cost = 0
cycle = False

def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union_parent(x, y):
  a = find_parent(x)
  b = find_parent(y)
  if a > b:
    parents[a] = b
  else:
    parents[b] = a

for i in range(1, m+1):
  x, y = map(int, stdin.readline().split())
  edges[i] = (x, y)


for i in range(k):
  if cycle:
    result.append(0)
    continue
  
  lines.sort()
  
  if i != 0:
    cost -= lines[0]
    lines = lines[1:]
    parents = [i for i in range(n+1)]
    for t in range(n-2):
      x, y  = edges[lines[t]]
      if find_parent(x) != find_parent(y):
        union_parent(x, y)
    
  for j in range(1, m+1):
    if not isUsed[j]:
      x, y = edges[j]
      if find_parent(x) != find_parent(y):
        union_parent(x, y)
        cost += j
        lines.append(j)
        isUsed[j] = True
  for line in lines:
    x, y = edges[line]
    if find_parent(x) != find_parent(y):
      union_parent(x, y)
   
  if len(set(parents[1:])) != 1:
    cycle = True
    result.append(0)
    continue
  result.append(cost) 

print(' '.join(map(str,result)))