import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges[a].append((b, cost))

INF = 1e9

dist = [INF] * (n+1)


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue

        for x in edges[node]:
            cost = d + x[1]
            if dist[x[0]] > cost:
                dist[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

dijkstra(1)

for i in range(2, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])