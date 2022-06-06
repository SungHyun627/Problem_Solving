#P2213 트리의 독립집합
from sys import stdin

stdin = open('./input.txt', 'r')

#정점의 수
n = int(stdin.readline())
#dp[i][0] : i가 포함되었을 때의 최대 독립집합 크기, dp[i][1]: i가 포함되었을 때의 최대 독립집합 크기
dp = [[0, 0] for _ in range(n+1)]

# 각 정점에 대하여 연결된 정점을 저장하는 리스트
tree = [[] for _ in range(n+1)]
# 각 정점의 가중치
node_weight = [0] + list(map(int, stdin.readline().split()))
# 최대독립 집합의 정점 리스트
result_nodes = []

for _ in range(n-1):
  a, b = map(int, stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

# 방문 체크 리스트
visited = [False] * (n+1)

def DFS(x):
  visited[x] = True
  dp[x][0] = node_weight[x]
  for i in tree[x]:
    if not visited[i]:
      DFS(i)
      # x가 포함되었을 때
      dp[x][0] += dp[i][1]
      # x가 포함되지 않았을 때
      dp[x][1] += max(dp[i])

visited_find = [False] * (n+1)

# 최대 독립집합의 정점을 찾는 함수
# 이전 노드가 포함이 된 경우는 0, 아니면 1
def find_node(x, y):
  visited_find[x] = True
  # 이전 노드가 포함이 되었다면
  if y == 0:
    for i in tree[x]:
      if not visited_find[i]:
        find_node(i, 1)
  else:
    # 이전 노드가 포함이 되었을 때
    # 현재 노드가 포함된 경우의 값이 더 큰 경우
    if dp[x][0] > dp[x][1]:
      result_nodes.append(x)
      for i in tree[x]:
        if not visited_find[i]:
          find_node(i, 0)
    else:
      for i in tree[x]:
        if not visited_find[i]:
          find_node(i, 1)
      

DFS(1)
find_node(1, 1)
# 오름차순 정렬
result_nodes.sort()

print(max(dp[1]))
print(*result_nodes)