
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n, l = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
#size가 최대 l인 deque
h = deque()
result = [0]*n

for i in range(n):
    #h의 마지막 element가 현재 인덱스의 원소와 비교보다 크면 계속해서 pop
    while h and h[-1][0] > arr[i]:
        h.pop()
    #h의 가장 있는 인덱스가 h의 크기(l)을 벗어난 경우 popleft
    while h and (i - h[0][1]) >= l:
        h.popleft()
    #현재 인덱스의 원소를 h에 append
    h.append((arr[i], i))
    #h의 가장 첫번째 원소가 최솟값
    result[i] = h[0][0]

print(*result)