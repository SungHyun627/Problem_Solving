#P10830 행렬 제곱
from sys import stdin
from math import log2
from copy import deepcopy

stdin = open('./input.txt', 'r')

n, b = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
power_of_two = {}
power_of_two[0] = matrix

t = 2
idx = 1

while (t < int(10e12)):
    temp_result = [[0] * n for _ in range(n)]
    temp_matrix = power_of_two[int(log2(t) - 1)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp_result[i][j] += temp_matrix[i][k] * temp_matrix[k][j]
    for i in range(n):
        for j in range(n):
            temp_result[i][j] %= 1000
    power_of_two[idx] = temp_result
    t *= 2
    idx += 1

def mutlply_matrix(k):
    if k == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    else:
        multiply_index = []
        temp_result = [[0] * n for _ in range(n)]

        for i in range(40):
            if k & (1 << i):
                multiply_index.append(i)
            

        for i in range(len(multiply_index)):
            temp_matrix = [[0] * n for _ in range(n)]
            if i == 0:
                for p in range(n):
                    for q in range(n):
                        temp_matrix[p][q] = power_of_two[multiply_index[0]][p][q]
            else:
                for p in range(n):
                    for q in range(n):
                        for t in range(n):
                            temp_matrix[p][q] += temp_result[p][t] * power_of_two[multiply_index[i]][t][q]
                        temp_matrix[p][q] %= 1000
            
            temp_result = deepcopy(temp_matrix)
        return temp_matrix

result = mutlply_matrix(b)
for i in range(n):
    print(*result[i])