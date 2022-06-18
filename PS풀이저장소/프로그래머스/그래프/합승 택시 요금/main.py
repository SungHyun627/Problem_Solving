def solution(n, s, a, b, fares):
    INF = int(1e9)
    min_distance = int(1e9)
    
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0

    # print(graph)#

    for fare in fares:
        x, y, cost = fare
        graph[x][y] = cost
        graph[y][x] = cost
    
    #플로이드 와셜 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i==j:
                    continue
                if graph[i][j] > graph[i][k]+ graph[k][j]:
                    graph[i][j] = graph[i][k]+ graph[k][j]

    # print(graph)
    
    for i in range(1, n+1):
        min_distance = min(min_distance, graph[s][i] + graph[i][a] + graph[i][b])
    answer = min_distance
    return answer