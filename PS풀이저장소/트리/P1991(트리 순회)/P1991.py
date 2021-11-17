# P1991 트리 순회
from sys import stdin

stdin = open('./input.txt', 'r')

tree = {}

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
    
def preorder(node):
    print(tree[node].data, end='')
    if tree[node].left_node != '.':
        preorder(tree[node].left_node)
    if tree[node].right_node != '.':
        preorder(tree[node].right_node)

def inorder(node):
    if tree[node].left_node != '.':
        inorder(tree[node].left_node)
    print(tree[node].data, end='')
    if tree[node].right_node != '.':
        inorder(tree[node].right_node)

def postorder(node):
    if tree[node].left_node != '.':
        postorder(tree[node].left_node)
    if tree[node].right_node != '.':
        postorder(tree[node].right_node)
    print(tree[node].data, end ="")

n = int(stdin.readline())
for _ in range(n):
    a, b, c = stdin.readline().rstrip().split()
    tree[a] = Node(a, b, c)
preorder('A')
print()
inorder('A')
print()
postorder('A')