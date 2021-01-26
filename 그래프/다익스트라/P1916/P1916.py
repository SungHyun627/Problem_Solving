from sys import stdin
import heapq
INF = int(1e9)

stdin = open('./input.txt', 'r')
# n : 도시의 수
n = int(stdin.readline())
# m : 버스의 수
m = int(stdin.readline())

# 버스의 노선
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))

# 출발점, 도착점
startPoint, endPoint = map(int, stdin.readline().split())

# 최단 거리 리스트 
d = [INF] * (n + 1)

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
dijkstra(startPoint)

print(d[endPoint])