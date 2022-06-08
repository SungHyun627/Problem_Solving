#P1068 트리
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
answer = 0

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

erase_node = int(stdin.readline())

for key in tree.keys():
  if erase_node in tree[key].children:
    tree[key].children.remove(erase_node)

def erase(x):
  for i in tree[x].children:
    erase(i)
  del tree[x]

erase(erase_node)

for key in tree.keys():
  if not (tree[key].children):
    answer += 1
print(answer)