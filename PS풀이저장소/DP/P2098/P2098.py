from sys import stdin

#비트마스킹을 이용한 dp

stdin = open('./input.txt', 'r')


# 도시의 수
n = int(stdin.readline())

# 비용 행렬
cost_matrix = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

# size
size = 2 ** (n-1)

# dp 2차원 배열 생성, dp[i][route] : i에서 route경로를 거쳐 0에 도달하는 최소비용
dp = [[0] * (size) for _ in range(n)]


def determine_min(n, path, k):
    min_dist = float('inf')
    for i in range(1, n):
        if path & (1 << i - 1) != 0:
            before_path = path & ~(1 << i - 1)
            dist = cost_matrix[k][i] + dp[i][before_path]
            if min_dist > dist:
                min_dist = dist
    return min_dist



def find_all_min_cost(n):
    for i in range(n):
        for j in range(n):
            if not cost_matrix[i][j]:
                cost_matrix[i][j] = float('inf')
    
    #0번 도시에 바로 도달할 수 있는 비용 기록
    for i in range(1, n):
        dp[i][0] = cost_matrix[i][0]

    #경로에 있는 도시가 1~(n-2)개일 때를 고려하여 dp 테이블 갱신
    for i in range(1, n-1):
        for path in range(1, size):
            cities_in_path = 0
            for j in range(1, n):
                if path & (1 << j - 1) != 0:
                    cities_in_path += 1
            if cities_in_path == i:
                for k in range(1, n):
                    if not(path & (1 << k - 1)):
                        dp[k][path] = determine_min(n, path, k)
    
    print(determine_min(n, size-1, 0))

find_all_min_cost(n)