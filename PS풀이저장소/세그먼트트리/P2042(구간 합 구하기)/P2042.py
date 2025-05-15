# P2042(구간 합 구하기)
from sys import stdin
stdin = open('./input.txt', 'r')

n, m, k = map(int, stdin.readline().split())

arr = [int(stdin.readline()) for _ in range(n)]
tree = [1]*(4*n)

def init(node, start, end):
  if start == end:
    tree[node] = arr[start]
    return
  mid = (start + end) // 2
  init(node*2, start, mid)
  init(node*2+1, mid+1, end)
  tree[node] = (tree[node*2] + tree[node*2+1])

def update(node, start, end, idx, val):
  if idx < start or idx > end:
    return
  if start == end:
    tree[node] = val
    return
  mid = (start + end) // 2
  update(node*2, start, mid, idx, val)
  update(node*2 + 1, mid+1, end, idx, val)
  tree[node] = (tree[node*2] + tree[node*2+1])


def query(node, start, end, l, r):
  if start > r or end < l:
    return 0
  if r >= end and l <= start:
    return tree[node]
  mid = (start + end) // 2
  return (query(node*2, start, mid, l, r) + query(node*2 + 1, mid+1, end, l, r))

init(1, 0, n-1)

for _ in range(m+k):
  a, b, c = map(int, stdin.readline().split())
  if a == 1:
    update(1, 0, n-1, b-1, c)
  else:
    print(query(1, 0, n-1, b-1, c-1))