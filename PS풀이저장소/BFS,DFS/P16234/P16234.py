from sys import stdin
from collections import deque

"""
#변수
- graph, group, time

1. 입력값 입력
2. 국경선 그룹핑
3. 인구 이동
2-3 반복

"""
stdin = open('./input.txt', 'r')

n, l, r = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
# print(graph)

visited = [[False] * n for _ in range(n)]
# print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def open_gate(graph):
    groups = []
    visited = [[False] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            group = []
            if not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))
                
                while queue:
                    x, y = queue.popleft()
                    group.append((graph[x][y], x, y))

                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if visited[nx][ny]:
                            continue

                        diff = graph[x][y] - graph[nx][ny]
                        # print(x, y, nx, ny, graph[x][y], graph[nx][ny], diff)
                        if l <= abs(diff) <= r:
                            # print(x, y, nx, ny)
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                # print(group)
                if not (len(group) == 1):
                    groups.append(group)
    return groups

def move_people(groups, graph):
    for group in groups:
        people_num = 0
        for city in group:
            people_num += city[0]
        after_move_people_num = int(people_num / len(group))
        for city in group:
            graph[city[1]][city[2]] = after_move_people_num

num = 0

while True:
    grouping_result = open_gate(graph)
    if not grouping_result:
        break
    move_people(grouping_result, graph)
    # print(graph)
    num += 1
print(num)