from sys import stdin
#pypy로 통과
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
# print(graph)
shape = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
         [(1, 0), (0, 1), (1, 1)],
         [(0, -1), (-1, -1), (-2, -1)], [(-1, 0), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (1, -1), (1, -2)],
         [(0, 1), (-1, 1), (-2, 1)], [(-1, 0), (-1, -1), (-1, -2)], [(0, -1), (1, -1), (2, -1)], [(1, 0), (1, 1), (1, 2)],
         [(1, 0), (1, 1), (2, 1)], [(0, 1), (-1, 1), (-1, 2)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],
         [(-1, 0), (-1, 1), (-1, -1)], [(0, 1), (-1, 1), (1, 1)], [(1, 0), (1, -1), (1, 1)], [(0, -1), (-1, -1), (1, -1)]        
         ]

max_sum = 0

for i in range(n):
    for j in range(m):
        for k in range(19):
            temp_sum = graph[i][j]
            is_break = False
            for t in range(3):
                x = i + shape[k][t][0]
                y = j + shape[k][t][1]
                if x < 0 or y < 0 or x >= n or y >= m:
                    is_break = True
                    break
                temp_sum += graph[x][y]
            
            if is_break:
                continue
            
            if temp_sum > max_sum:
                max_sum = temp_sum

print(max_sum)