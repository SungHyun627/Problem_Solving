#P1275 커피숍2
from sys import stdin
from math import ceil, log2
stdin = open('./input.txt', 'r')

#n: 수의 개수, q: 턴의 개수
n, q = map(int, stdin.readline().split())

#수를 담을 리스트
arr = list(map(int, stdin.readline().split()))

#트리의 높이
h = ceil(log2(n))

#트리를 담는 리스트
tree = [0] * (2 ** (h+1))

#트리 초기화
def init(node, start, end):
    # print(tree, node, start, end)
    if start == end:
        tree[node] = arr[start]
        return 
    
    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2 +1]

#트리 업데이트
def update(node, start, end, index, value):
    # print(node, start, end)
    if (index < start) or (index > end):
        return

    if start == end:
        tree[node] = value
        return

    if (start != end):
        mid = (start+end) // 2
        update(node*2, start, mid, index, value)
        update(node*2 + 1, mid+1, end, index, value)
        tree[node] = tree[node * 2] + tree[node*2 + 1]
        

#구간 합 구하기
def find_interval_sum(node, start, end, left, right):
    if (left > end) or (right < start):
        return 0
    
    #구간 합이 노드의 범위를 포함할 때
    if (left <= start) and (right >= end):
        return tree[node]
    
    mid = (start + end) // 2
    return (find_interval_sum(node*2, start, mid, left, right) + find_interval_sum(node*2 + 1, mid+1, end, left, right))

#트리 초기화
init(1, 0, n-1)

for _ in range(q):
    a, b, c, d = map(int, stdin.readline().split())
    if a > b:
        a, b = b, a
    print(find_interval_sum(1, 0, n-1, a-1, b-1))
    update(1, 0, n-1, c-1, d)