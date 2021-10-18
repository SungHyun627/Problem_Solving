from sys import stdin
from itertools import combinations

stdin = open('./input.txt', 'r')

t = int(stdin.readline())
    

for _ in range(t):
    n = int(stdin.readline())
    arr = []
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        arr.append((a, b))

    all_pairs = list(combinations(arr, n // 2))
    # print(*all_pairs, sep='\n')
    all_pairs_x_sum = sum(map(lambda x: x[0], arr))
    all_pairs_y_sum = sum(map(lambda x: x[1], arr))
    result = int(1e9)

    #백터에서 plus할 쌍
    for pairs in all_pairs[:len(all_pairs) // 2]:
        plus_x = sum(map(lambda x: x[0], pairs))
        plus_y = sum(map(lambda x: x[1], pairs))

        vector_sum =  ((2 * plus_x - all_pairs_x_sum) ** 2 + (2 * plus_y - all_pairs_y_sum) ** 2) ** 0.5

        if vector_sum < result:
            result = vector_sum

    print(result)