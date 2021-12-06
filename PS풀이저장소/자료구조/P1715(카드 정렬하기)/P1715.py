#P1715 카드 정렬하기
from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = []
for _ in range(n):
    a = int(stdin.readline())
    heapq.heappush(arr, a)
result = 0

if len(arr) == 1:
    print(0)
else:
    while True:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)
        result += (x+y)
        if not arr:
            break
        heapq.heappush(arr, x+y)
    print(result)