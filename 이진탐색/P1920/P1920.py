from sys import stdin

stdin = open('./input.txt', 'r')
# 수들의 개수
n = int(stdin.readline())
numArray = list(map(int, stdin.readline().rstrip().split()))
# 존재하는 지 확인해야 하는 수들의 개수
m = int(stdin.readline())
checkArray = list(map(int, stdin.readline().rstrip().split()))

numArray.sort()
def binary_search(array1, array2, n):
    for i in array2:
        start = 0
        end = n-1
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if array1[mid] == i:
                result = 1
                break
            elif array1[mid] > i:
                end = mid - 1
            else:
                start = mid + 1
        print(result)
binary_search(numArray, checkArray, n)