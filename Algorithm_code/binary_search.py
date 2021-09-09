# 데이터가 정렬되어 있다는 전제조건
# 탐색범위가 2000만을 넘어가면 이진 탐색 생각, 
from sys import stdin

stdin = open('./input.txt', 'r')
n, target = map(int, stdin.readline().rstrip().split())
array = list(map(int, stdin.readline().rstrip().split()))

# 1. 재귀
def binary_search1(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return None

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search1(array, target, start, mid-1)
    else: 
        return binary_search1(array, target, mid+1, end)

print(binary_search1(array, target, 0, n-1) + 1)

#2. 반복문
def binary_search2(array, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else: 
            start = mid + 1
    return None

print(binary_search2(array, target, 0, n-1) + 1)

