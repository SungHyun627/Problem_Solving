from sys import stdin
from sys import setrecursionlimit

stdin = open('./input.txt', 'r')

# 재귀한도 설정
setrecursionlimit(10000)

def DFS(x, y):
    # 탐색 노드 방문 처리
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 방문하지 않았다면
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 상, 하, 좌, 우 노드에 대하여 재귀적으로 호출
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True
    return False

# t : 테스트 케이스의 개수 
t = int(stdin.readline())

for _ in range(t):
    # m : 가로, n : 세로, k : 배추의 위치 개수
    m, n, k = map(int, stdin.readline().rstrip().split())
    graph = [[0] * m for _ in range(n)]

    # 필요한 지렁이 수 
    result = 0
    # 배추밭 입력 값
    for _ in range(k):
        # x : 세로, y : 가로
        y, x = map(int, stdin.readline().rstrip().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if DFS(i, j) == True:
                result += 1
    
    print(result)