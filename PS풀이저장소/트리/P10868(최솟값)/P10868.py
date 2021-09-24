from sys import stdin
from math import log2, ceil
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
a = []

for _ in range(n):
    a.append(int(stdin.readline()))

tree = [0] * (2 ** (ceil(log2(n)) + 1) - 1)

def init(node, start, end):
    if start == end:
        tree[node] = a[start]
        return
    
    mid = (start + end) // 2
    init(node*2, start, mid)
    init(node*2 + 1, mid+1, end)
    tree[node] = min(tree[node*2], tree[node*2 + 1])

def find_interval_min(node, start, end, left, right):
    if right < start or left > end:
        return int(1e9)
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return min(find_interval_min(node*2, start, mid, left, right), find_interval_min(node*2+1, mid+1, end, left, right))

#트리 초기화
init(1, 0, n-1)

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    print(find_interval_min(1, 0, n-1, x-1, y-1))