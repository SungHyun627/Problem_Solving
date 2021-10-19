from sys import stdin
from itertools import combinations
from bisect import bisect_right, bisect_left

stdin = open('./input.txt', 'r')

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

#두 부분으로 나누기
arr1 = arr[:n//2]
arr2 = arr[n//2:]
case1 = list(tuple(j) for i in range(1, n//2 + 1) for j in combinations(arr1, i))
case2 = list(tuple(j) for i in range(1, n + 1 - n//2) for j in combinations(arr2, i))

sum1 = [sum(i) for i in case1]
sum2 = [sum(i) for i in case2]

#오름차순 정렬
sum2.sort()

#합이 s가 되는 부분수열의 개수
count = 0

#각 부분합 리스트에서 s를 만족하는 경우 count
count = sum1.count(s) + sum2.count(s)

for i in range(2 ** (n//2) - 1):
    count += (bisect_right(sum2, s - sum1[i]) - bisect_left(sum2, s-sum1[i]))

print(count)