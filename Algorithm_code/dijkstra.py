from sys import stdin
import heapq

# 1. 다익스트라 
# 간단 : O(V^2), 복잡 : O(ElogV)
# 1차원 distance table


# 1-1. 간단 but 느린 방법

"""
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않는 노드 중 최단거리가 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3 ~ 4 반복
"""
stdin = open('./input.txt', 'r')

# 무한대
INF = int(1e9)

# v : 노드의 개수, 간선의 개수 : e
n, m = map(int, stdin.readline().rstrip().split())

# start node
start_node = int(stdin.readline().rstrip())

# 간선 정보를 담는 리스트
graph = [[] for _ in range(n+1)]

# 최단 경로 리스트
distance = [INF] * (n+1)

# 방문 기록 리스트
visited = [False] * (n+1)

for _ in range(m):
    a, b, c = map(int, stdin.readline().rstrip().split())
    graph[a].append((b, c))

def find_smallest_distance_node():
    min_distance = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i]:
            if distance[i] < min_distance:
                min_distance = distance[i]
                index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for node in graph[start]:
        distance[node[0]] = node[1]
    
    for _ in range(n-1):
        next_node = find_smallest_distance_node()
        visited[next_node] = True
        for node in graph[next_node]:
            temp_dist = distance[next_node] + node[1]
            if temp_dist < distance[node[0]]:
                distance[node[0]] = temp_dist

dijkstra(start_node)
print(distance[1:])

# 1-2. heapq를 이용하여 최단 거리가 가장 작은 노드를 택하는 방법
# 시간 복잡도 : O(ElogV)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for next_node in graph[node]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))
                
dijkstra(start_node)
print(distance[1:])

