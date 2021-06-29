from sys import stdin
from collections import Counter

stdin = open('./input.txt', 'r')
# 배열의 크기
n = int(stdin.readline())
# 인덱스
k = int(stdin.readline())

# 이진 탐색

start = 1
end = n ** 2

# mid가 n*n배열에 존재하지 않는 수 일수도 있기 때문에
# while문의 초기 조건에 의해 반복문이 종료되기 전까지
# total == k인 값이 존재하여도 break 시키지 않는다.
while start <= end:
    # mid의 값보다 같거나 작은 수의 개수
    total = 0
    mid = (start + end) // 2
    for i in range(1, n+1):
        total += min(n, mid // i)
        if mid // i == 0:
            break
    
    if total < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)