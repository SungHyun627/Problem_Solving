from sys import stdin
#음수 간선이 존재할 때 사용가능

#거리 무한대
INF = int(1e9)
#노드, 간선의 개수
n, m = map(int, stdin.readline().split())

#모든 간선 대한 정보를 담는 리스트
edges = []
#최단 거리 테이블
dist = [INF] * (n+1)

#간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    #a -> b 비용이 c
    edges.append((a, b, c))

def bellman_ford(start):
    #시작노드에서 초기화
    dist[start] = 0
    #전체 n번의 round 반복
    for i in range(n):
        #매 반복마다 "모든 간선"확인
        for j in range(m):
            cur, next_node, cost= edges[j]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                #n반쩨 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False
    
#Start node가 1일때
neg_cycle = bellman_ford(1)

if neg_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])