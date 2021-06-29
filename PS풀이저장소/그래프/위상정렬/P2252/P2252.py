from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

# n : 학생 수, m : 키를 비교한 횟수
n, m = map(int, stdin.readline().split())

# 정렬된 순서를 담기 위한 리스트
result = []
# 각 학생별 본인보다 키가 큰 학생을 저장하는 리스트
graph = [[] for _ in range(n+1)]
# 각 학생별 진입차수를 저장하는 리스트
indegree = [0] * (n+1)

# 키를 비교한 정보 입력
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topologySort():
    # 큐 생성
    queue = deque()
    # 진입차수가 0인 node를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    # 큐가 빌때까지 실행
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                # 진입차수가 0이면 큐에 추가
                queue.append(i)

topologySort()

print(*result)