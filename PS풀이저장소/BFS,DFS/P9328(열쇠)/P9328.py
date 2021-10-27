#P9328 열쇠
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

#테스트 케이스 수
t = int(stdin.readline())

#방향(북, 동, 남, 서)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(startx, starty, state, keys, docs):
    queue = deque()
    start_keys = keys
    new_keys = 0
    #입구가 열쇠일 때
    if ord('a') <= ord(graph[startx][starty]) <= ord('z'):
        start_keys = (start_keys | (1 << (ord(graph[startx][starty]) - ord('a'))))
        if (startx, starty) not in state:
            state[(startx, starty)] = start_keys
        else:
            if state[(startx, starty)] < start_keys:
                state[(startx, starty)] = start_keys
        queue.append((startx, starty, start_keys))
                
        
    #입구가 문서일 때
    elif graph[startx][starty] == '$':
        docs.append((startx, starty))
        queue.append((startx, starty, start_keys))
        state[(startx, starty)] = start_keys
        graph[startx][starty] = '.'

    #입구가 문일 때
    elif ord('A') <= ord(graph[startx][starty]) <= ord('Z'):
        #해당 열쇠가 없으면 pass
        if not (start_keys & (1 << (ord(graph[startx][starty]) - ord('A')))):
            return start_keys
        state[(startx, starty)] = start_keys    
        queue.append((startx, starty, start_keys))
        graph[startx][starty] = '.'

    #입구가 빈 곳일 때
    else:
        if (startx, starty) not in state:
            state[(startx, starty)] = start_keys
            queue.append((startx, starty, start_keys))
        else:
            if state[(startx, starty)] < start_keys:
                queue.append((startx, starty, start_keys))
                state[(startx, starty)] = start_keys
            else:
                return start_keys

    while queue:
        # print(queue)
        x, y, n_keys = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            #해당 위치가 벽인 경우
            if graph[nx][ny] == '*':
                continue

            #해당 위치에 열쇠가 있는 경우
            elif ord('a') <= ord(graph[nx][ny]) <= ord('z'):                
                # 해당 열쇠를 가져오기
                n_keys = (n_keys | (1 << (ord(graph[nx][ny]) - ord('a'))))
                # print(graph[nx][ny], bin(n_keys))
                if (nx, ny) not in state:
                    state[(nx, ny)] = n_keys
                    queue.append((nx, ny, n_keys))
                else:
                    if state[(nx, ny)] < n_keys:
                        state[(nx, ny)] = n_keys
                        queue.append((nx, ny, n_keys))

            #해당 위치에 문이 있는 경우
            elif ord('A') <= ord(graph[nx][ny]) <= ord('Z'):
                #해당 열쇠가 없으면 pass
                if not (n_keys & (1 << (ord(graph[nx][ny]) - ord('A')))):
                    continue
                state[(nx, ny)] = n_keys
                queue.append((nx, ny, n_keys))
                graph[nx][ny] = '.'

            #해당 위치에 문서가 있는 경우
            elif graph[nx][ny] == '$':
                # print("find", nx, ny)
                docs.append((nx, ny))
                queue.append((nx, ny, n_keys))
                state[(nx, ny)] = n_keys
                graph[nx][ny] = '.'
            #비어 있는 경우                
            else:
                if (nx, ny) not in state:
                    state[(nx, ny)] = n_keys
                    queue.append((nx, ny, n_keys))
                else:
                    if state[(nx, ny)] < n_keys:
                        queue.append((nx, ny, n_keys))
                        state[(nx, ny)] = n_keys
        if not queue:
            new_keys = n_keys
    # print(startx, starty, x, y, bin(new_keys), len(docs))
    return new_keys
    

def find_max_docs(n, m, graph, keys):
    #문서
    docs = []
    #각 위치의 state를 저장하는 dict
    state = {}
    #가장자리 중 입구 리스트
    entracnes = []

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if graph[i][j] != '*':
                    entracnes.append((i, j))
    temp_keys = -1
    while(temp_keys != keys):
        temp_keys = keys
        for entrance in entracnes:
            keys = bfs(entrance[0], entrance[1], state, keys, docs)
    
    return len(docs)

for _ in range(t):
    n, m = map(int, stdin.readline().split())
    graph = list(list(stdin.readline()) for _ in range(n))
    #key 비트마스킹
    keys = 2 ** 26
    key_string = stdin.readline().rstrip()
    if not (key_string == '0'):
        for i in key_string:
            keys = (keys | (1 << (ord(i) - ord('a'))))
    
    print(find_max_docs(n, m, graph, keys))