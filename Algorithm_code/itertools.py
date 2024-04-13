from sys import stdin
from collections import deque

arr = [1, 2, 3, 4]

## 1. 순열
visited = [False] * len(arr)
ans1 = []


def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        ans1.append(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False


permutations(2, [])
print(ans1)

## 2. 중복순열
ans2 = []

def product(n, new_arr):
    global arr
    # 순서 상관 0, 중복 0
    if len(new_arr) == n:
        ans2.append(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

product(2, [])
print(ans2)

## 3. 조합
ans3 = []

def combinations(n, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        ans3.append(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


combinations(2, [], 0)
print(ans3)


## 4. 중복조합
ans4 = []
def combinations_with_replacement(n, new_arr, c):
    # 순서 상관 X, 중복
    if len(new_arr) == n:
        ans4.append(new_arr)
        return
    for i in range(c, len(arr)):
        combinations_with_replacement(n, new_arr + [arr[i]], i)


combinations_with_replacement(2, [], 0)
print(ans4)





