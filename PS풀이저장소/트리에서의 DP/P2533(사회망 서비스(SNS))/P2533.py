#P2533 사회망 서비스(SNS)
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

#정점의 수
n = int(stdin.readline())
#dp[i][0] : i가 얼리어답터일 때 얼리어답터의 수, dp[i][1]: i가 얼리어답터가 아닐 때 얼리어답터의 수
dp = [[0, 0] for _ in range(n+1)]

# 각 정점에 대하여 연결된 정점을 저장하는 리스트
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

# 방문 체크 리스트
visited = [False] * (n+1)

def DFS(x):
  visited[x] = True
  dp[x][0] = 1
  for i in tree[x]:
    if not visited[i]:
      DFS(i)
      # x가 얼리어답터일 때
      dp[x][0] += min(dp[i])
      # x가 얼리어답터가 아닐때
      dp[x][1] += dp[i][0]

DFS(1)
print(min(dp[1]))
