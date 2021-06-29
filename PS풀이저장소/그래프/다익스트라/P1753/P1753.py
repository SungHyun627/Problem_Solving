from sys import stdin
import heapq
INF = int(1e9)

stdin = open('./input.txt', 'r')
# v : 정점의 수, e : 간선의 개수
v, e = map(int, stdin.readline().split())
# 시작 정점
startNode = int(stdin.readline())
# 방향그래프
graph = [[] for _ in range(v + 1)]
# 간선 정보 입력

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))

# 최단 거리 리스트 
d = [INF] * (v + 1)
# 우선순위 큐
qList = []

def dijkstra(start):
    d[start] = 0
    heapq.heappush(qList, (0, start))
    
    #우선순위 큐가 빌 때까지 실행
    while qList:
        distance, node = heapq.heappop(qList)
        # 처리된 노드는 제외
        if d[node] < distance:
            continue

        # 해당 노드와 연결되어 있는 노드에 대하여
        # 거리를 계산후 최단 거리 리스트 갱신
        for i in graph[node]:
            new_distance = distance + i[1]
            # 기존 최단거리 리스트에 있는 값보다 작을 경우 갱신
            if new_distance < d[i[0]]:
                d[i[0]] = new_distance
                # 큐에 추가
                heapq.heappush(qList, (new_distance, i[0]))

# 다익스트라 알고리즘 실행
dijkstra(startNode)

for i in range(1, v + 1):
    print(d[i]) if d[i] != INF else print('INF')