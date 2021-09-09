# 위상 정렬
# 방향 그래프의 모든 노드를 방향성에 거스르지 않고 순서대로 나열하는 것
# 시간 복잡도 : O(V+E)
"""
1. 진입차수가 0인 node를 큐에 넣는다.
2. 다음 과정 반복
    2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 제거
    2-2. 진입차수가 0인 노드를 큐에 넣는다.
"""
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
#진입차수 저장 리스트
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    print(x, end = ' ')
    for i in graph[x]:
        indegree[i] -=1
        if indegree[i] == 0:
            queue.append(i)
print('\n', end ='')





