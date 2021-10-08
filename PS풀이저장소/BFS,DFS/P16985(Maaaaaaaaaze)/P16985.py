from sys import stdin
from collections import deque
from itertools import permutations

stdin = open('./input.txt', 'r')

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

case1 = []
case2 = []
case3 = []
case4 = []
case5 = []

def rotate_board(graph, case):
    new_graph1 = [[0] * 5 for _ in range(5)]
    new_graph2 = [[0] * 5 for _ in range(5)]
    new_graph3 = [[0] * 5 for _ in range(5)]

    new_x = 0
    new_y = 0
    #original
    case.append(graph)

    #270 degree
    for i in range(5):
        for j in range(5):
            new_x = j-2
            new_y = -i+2
            new_x, new_y = -new_y, new_x
            new_x += 2
            new_y -= 2
            new_x, new_y = abs(new_y), new_x
            # print(new_x, new_y)
            new_graph1[new_x][new_y] = graph[i][j]
    case.append(new_graph1)

    #180 degree
    for i in range(5):
        for j in range(5):
            new_x = j-2
            new_y = -i+2
            new_x, new_y = -new_x, -new_y
            new_x += 2
            new_y -= 2
            new_x, new_y = abs(new_y), new_x
            # print(new_x, new_y)
            new_graph2[new_x][new_y] = graph[i][j]
    case.append(new_graph2)

    #90 degree
    for i in range(5):
        for j in range(5):
            new_x = j-2
            new_y = -i+2
            new_x, new_y = new_y, -new_x
            new_x += 2
            new_y -= 2
            new_x, new_y = abs(new_y), new_x
            # print(new_x, new_y)
            new_graph3[new_x][new_y] = graph[i][j]
    case.append(new_graph3)

for i in range(5):
    graph_2d = []
    for _ in range(5):
        graph_2d.append(list(map(int, stdin.readline().split())))
    
    if i == 0:
        rotate_board(graph_2d, case1)
    elif i == 1:
        rotate_board(graph_2d, case2)
    elif i == 2:
        rotate_board(graph_2d, case3)
    elif i == 3:
        rotate_board(graph_2d, case4)
    else:
        rotate_board(graph_2d, case5)

def bfs():
    queue = deque()
    if graph_3d[0][0][0] == 0 or graph_3d[4][4][4] == 0:
        return 125
    queue.append((0, 0, 0, 0))
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    

    while queue:
        x, y, z, count = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0  or nx >= 5 or ny >= 5 or nz >= 5:
                continue

            if not visited[nx][ny][nz] and graph_3d[nx][ny][nz]:
                if nx == 4 and ny == 4 and nz == 4:
                    return count + 1
                else:
                    queue.append((nx, ny, nz, count+1))
                    visited[nx][ny][nz] = True
    return 125

min_count = 125
graph_3d = [0, 0, 0, 0, 0]
t = list(permutations(range(5)))
# print(t)
for seq in t:
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        graph_3d[seq[0]] = case1[i]
                        graph_3d[seq[1]] = case2[j]
                        graph_3d[seq[2]] = case3[k]
                        graph_3d[seq[3]] = case4[l]
                        graph_3d[seq[4]] = case5[m]
                        if graph_3d == [[[1] * 5 for _ in range(5)] for _ in range(5)]:
                            min_count = min(12, min_count)
                        else:
                            min_count = min(bfs(), min_count)
print(min_count) if min_count != 125 else print(-1)