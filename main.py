#P1135 뉴스 전기
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())

tree = {}
class Node:
  def __init__(self, data):
    self.data = data
    self.children = set()

for i in range(n):
  tree[i] = Node(i)

parents = list(map(int, stdin.readline().split()))

for i in range(n):
  if parents[i] == - 1:
    continue
  tree[parents[i]].children.add(i)

def dfs(x):
  temp = 0
  if not tree[x].children:
    return 1
  for i in tree[x].children:
    temp += dfs(i)
  print(x, temp)
  return temp

dfs(0)
# print(result)