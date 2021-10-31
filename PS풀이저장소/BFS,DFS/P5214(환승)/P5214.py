#P5214 환승
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

#n : 역의 수, k : 하이퍼 튜브가 서로 연결하는 역의 수, m : 하이퍼튜브의 수
n, k, m = map(int, stdin.readline().split())

#1번부터 시작 하여 각각의 0까지 도달할 때 드는 비용
cost = [0] * (n+m+1)

#각 역에 연결된 하이퍼튜브, 하이퍼튜브에 연결된 역의 정보를 저장하는 리스트
#역-하이퍼튜브-역 경로
#역은 1~n, 하이퍼 튜브는 n+1~n+m
connected_tube_station = [[] for _ in range(n+m+1)]

for i in range(1, m+1):
    arr = list(map(int, stdin.readline().split()))
    for j in range(k):
        connected_tube_station[arr[j]].append(n+i)
        connected_tube_station[n+i].append(arr[j])
# print(connected_tube_station)
def bfs():
    queue = deque()
    cost[1] = 1
    queue.append(1)
    while queue:
        # print(queue)
        station_num = queue.popleft()
        if station_num == n:
            return cost[n]
        
        for i in connected_tube_station[station_num]:
            #방문한 적이 없다면
            if not cost[i]:
                #하이퍼 튜브에 도달하면
                if i > n:
                    cost[i] = cost[station_num]
                else:
                    cost[i] = cost[station_num] + 1
                queue.append(i)

    return -1

print(bfs())