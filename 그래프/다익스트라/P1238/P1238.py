from sys import stdin
import heapq
INF = int(1e6)

stdin = open('./input.txt', 'r')


# n : 학생 수, m : 도로 수, x : 파티 장소
n, m, x = map(int, stdin.readline().split())

# 마을 사이의 소요 시간 
graph = [[] for _ in range(n + 1)]
# 다른 정점으로부터 X까지의 최단시간을 구하기 위해 간선의 방향 reverse
graph_reverse = [[] for _ in range(n + 1)]
# 각 도로의 시작점, 끝점, 소요시간 입력
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph_reverse[b].append((a, c))

# x에서 다른 정점까지 최소 시간
tfromX = [INF] * (n+1)
# 다른 정점에서 X까지의 최소 시간
ttoX = [INF] * (n+1)

def dijkstra(start, graph, t):
    # 우선순위 큐 리스트
    queue = []
    t[start] = 0
    heapq.heappush(queue, (0, start))
    
    # 큐가 빌 때까지 실행
    while queue:
        # 마을, 시간
        time, town = heapq.heappop(queue)
        # 이전에 처리된 마을(사람)이라면
        if t[town] < time:
            continue
        
        # 연결된 마을에 대하여 최단시간 갱신
        for i in graph[town]:
            new_time = time + i[1]
            if new_time < t[i[0]]:
                t[i[0]] = new_time
                heapq.heappush(queue, (t[i[0]], i[0]))

# X로부터 각 정점까지의 최소 거리
dijkstra(x, graph, tfromX)
# 각 정점으로부터 X까지의 최소 거리
dijkstra(x, graph_reverse, ttoX)

# X까지 오고 가는데 가장 오래 걸린 학생의 소요시간
print(max([ttoX[i] + tfromX[i] for i in range(1, n+1)]))