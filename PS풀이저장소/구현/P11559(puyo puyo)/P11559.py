from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')
graph = [list(stdin.readline().rstrip()) for _ in range(12)]
chain = 0

# print(graph)
def check_chain():
    global chain
    visited = [[False] * 6 for _ in range(12)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    is_chain = False
    #1. 뿌요가 있는 부분에 대하여 bfs
    for i in range(12):
        for j in range(6):
            if not(graph[i][j] == '.') and not visited[i][j]:
                check_position = []
                queue = deque()
                
                type_puyo = graph[i][j]
                visited[i][j] = True
                queue.append((i, j))
                check_position.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        #범위를 벗어난 경우
                        if nx >= 12 or ny >= 6 or nx < 0 or ny < 0:
                            continue
                        #방문한 곳이거나, 뿌요가 없는 경우, 뿌요가 다른 경우
                        if visited[nx][ny] or graph[nx][ny] == '.' or graph[nx][ny] != type_puyo:
                            continue
                        
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        check_position.append((nx, ny))

                # print(check_position)
                if len(check_position) >= 4:
                    for x, y in check_position:
                        graph[x][y] = '.'
                    # print(type_puyo)
                    is_chain = True
    if is_chain:
        chain += 1


def relocation():
    for j in range(6):
        puyo_col = []
        for i in range(12):
            if not(graph[i][j] == '.'):
                # print(graph[i][j])
                puyo_col.append(graph[i][j])
                graph[i][j] = '.'
        
        y = 11
        # print(puyo_col)
        while puyo_col:
            graph[y][j] = puyo_col.pop()
            y -= 1

temp = 1
while temp != chain:
    temp = chain
    check_chain()
    relocation()
print(chain)    