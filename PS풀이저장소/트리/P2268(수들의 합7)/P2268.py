#P2268 수들의 합7. PyPy로 채점
from sys import stdin
from math import ceil, log2

stdin = open('./input.txt', 'r')

#n : 수의 개수, q : 명령의 개수
n, q = map(int, stdin.readline().split())

arr = [0] * n
height = ceil(log2(n))
tree = [0] * (2 ** (height + 1) -1)

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    else:
        mid = (start + end) // 2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2 + 1]

#업데이트
def update(node, start, end, index, diff):
    if start > index or end < index:
        return 
    
    tree[node] += diff
    if start == end:
        return
    
    mid = (start + end) // 2
    update(node*2, start, mid, index, diff)
    update(node*2 + 1, mid+1, end, index, diff)


#구간 합 구하기
def find_interval_sum(node, start, end, left, right):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return find_interval_sum(node*2, start, mid, left, right) + find_interval_sum(node*2 +1, mid+1, end, left, right)

for _ in range(q):
    a, b, c = map(int, stdin.readline().split())
    if a == 0:
        if b > c:
            b, c = c, b
        print(find_interval_sum(1, 0, n-1, b-1, c-1))
    else:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, n-1, b-1, diff)