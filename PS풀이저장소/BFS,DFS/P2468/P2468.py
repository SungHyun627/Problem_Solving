from sys import stdin
from sys import setrecursionlimit

stdin = open('input.txt', 'r')
n = int(stdin.readline().rstrip())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
# #print(graph)

# # recursion 한도 설정
setrecursionlimit(10000)

# move direction(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, k):
    # Out of map
    if x >= n or y >=n or x < 0 or y < 0:
        return False

    if visited[x][y] == 1:
        return False

    if graph[x][y] <= k:
        visited[x][y] = 1
        return False
    
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny, k)
    return True


max_rain = 0 

for i in range(n):
    max_rain = max(max_rain, max(graph[i]))

result = 0
for t in range(1, max_rain + 1):
    visited = [[0] * n for _ in range(n)] 
    temp_result = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, t) == True:
                temp_result += 1
    # print(result, temp_result)
    result = max(temp_result, result)
print(result if result != 0 else 1, end = '')