#플로이드 워셜 알고리즘
"""
1. 2차원 인접 행렬 생성
2. 간선 정보 입력 및 자기 자신으로 가는 값 0으로 초기화
3. 3중 for문
"""


#인접 행렬 이용
from sys import stdin
stdin = open('./input.txt', 'r')
# 무한대
INF = int(1e9)
# n : 노드의 개수, m : 간선의 개수 
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

#입력 받기
for _ in range(m):
    a, b, c = map(int, stdin.readline().rstrip().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph[1:])