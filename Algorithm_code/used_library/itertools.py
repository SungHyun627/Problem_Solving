from itertools import combinations, permutations, product

a = [1, 2, 3, 4, 5]
b = [3, 4, 5]
# 조합
print(list(combinations(a, 2)))
# 순열
print(list(permutations(a, 2)))
# 곱집합
print(list(product(a, b)))