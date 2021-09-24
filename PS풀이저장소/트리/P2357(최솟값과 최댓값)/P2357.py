from sys import stdin
from math import log2, ceil
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
a = []

for _ in range(n):
    a.append(int(stdin.readline()))

#[최솟값, 최댓값]
tree = [[int(1e9), 0] for _ in range((2 ** (ceil(log2(n)) + 1) - 1))]
def init(node, start, end):
    if start == end:
        tree[node][0] = a[start]
        tree[node][1] = a[start]
        return
    else:
        mid = (start + end) // 2
        init(node*2, start, mid)
        init(node*2 + 1, mid+1, end)
        tree[node][0] = min(tree[node*2][0], tree[node*2 + 1][0])
        tree[node][1] = max(tree[node*2][1], tree[node*2 + 1][1])

def find_interval_max_min(node, start, end, left, right):
    if right < start or left > end:
        # print(node)
        return [int(1e9), 0]
    
    if left <= start and right >= end:
        # print(node, tree[node])
        return tree[node]
    
    mid = (start + end) // 2
    t1 = find_interval_max_min(node*2, start, mid, left, right)
    t2 = find_interval_max_min(node*2+1, mid+1, end, left, right)
    # print(node, t1, t2)
    # print(min(t1[0], t2[0]), max(t1[1], t2[1]))
    return [min(t1[0], t2[0]), max(t1[1], t2[1])]

#트리 초기화
init(1, 0, n-1)
# print(tree)
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    print(*find_interval_max_min(1, 0, n-1, x-1, y-1))