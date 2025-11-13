##P5639. 이진 검색 트리
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')
preorder = []
cnt = 0

while True:
  cnt += 1
  x = stdin.readline().rstrip()
  if not x:
    break
  preorder.append(int(x))

n = len(preorder)

def postorder(start, end):
  if start > end:
    return
  root = preorder[start]
  idx = start + 1
  while idx <= end and preorder[idx] < root:
    idx += 1
  postorder(start+1, idx-1)
  postorder(idx, end)
  print(root)

postorder(0, n-1)