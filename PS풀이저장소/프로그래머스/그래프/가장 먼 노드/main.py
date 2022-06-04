import heapq

#무한대 설정
INF = int(1e9)

def solution(n, edge):
    # 1번에서 각 노드까지의 거리
    distance = [INF] * (n+1)
    distance[0] = -1
    
    #인접 리스트
    graph = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        
        for x in graph[node]:
            if (dist + 1) < distance[x]:
                distance[x] = (dist + 1)
                heapq.heappush(q, (dist+1, x))
    max_distance = max(distance)
    
        
    answer = distance.count(max_distance)
    return answer