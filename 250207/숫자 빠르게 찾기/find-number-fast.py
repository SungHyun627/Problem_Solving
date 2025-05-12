n, m = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid + 1
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return -1

for _ in range(m):
    x = int(input())
    print(binary_search(x))