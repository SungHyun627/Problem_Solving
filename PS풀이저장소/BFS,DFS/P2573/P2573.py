from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10 ** 4)

stdin = open('./input.txt', 'r')

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 얼음에서 바닷물으로 되는 위치를 저장하는 dictionary
ice_to_water = {}

def melting_ice(ice_map):
    # 동, 남, 서, 북 네 방향 중 바다인 부분 count
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice_map[i][j] == 0:
                continue
            # 주변에 있는 바닷물 칸의 수
            count = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni >= n or ni < 0 or nj >= m or nj < 0:
                    continue
                if ice_map[ni][nj] == 0 and (ni, nj) not in ice_to_water:
                    count += 1
            if ice_map[i][j] <= count:
                ice_to_water[((i, j))] = 1
            ice_map[i][j] = max(ice_map[i][j] - count, 0)
    ice_to_water.clear()

def DFS(x, y, ice_map, visited):
    # 범위를 벗어나거나, 바닷물일 때
    if x < 0 or y < 0 or x >= n or y >= m or ice_map[x][y] == 0:
        return False
    
    # 방문한 적이 없을 때
    if visited[x][y] == 0:
        # 방문 체크
        visited[x][y] = 1
        for i in range(4):
            DFS(x+dx[i], y+dy[i], ice_map, visited)
        return True
    return False
            
# n : 세로, m : 가로
n, m = map(int, stdin.readline().split())
# 현시점에서 ice_map
ice_map = [list(map(int, stdin.readline().split())) for _ in range(n)]

# 빙산이 최초로 분리되는 시간
result = 0

while True:
    # 빙산 덩어리의 개수
    partition = 0
    # 방문 이력
    visited = [[0] * m for _ in range(n)]

    # 빙산이 녹는 과정
    melting_ice(ice_map)
    
    # DFS를 통한 빙산의 개수 계산
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice_map[i][j] == 0:
                continue
            if DFS(i, j, ice_map, visited):
                partition += 1
    result += 1

    # 빙산이 분리 되었다면 
    if partition > 1:
        break
    # 분리되지 않고 모두 녹아버렸다면
    if ice_map == [[0] * m for _ in range(n)]:
        result = 0
        break
print(result)