n = int(input())

left = [0] * 26
right = [0] * 26

for _ in range(n):
    x, l, r = input().split()
    left[ord(x) - ord("A")] = l
    right[ord(x) - ord("A")] = r

def preorder(x):
    idx = ord(x) - ord("A")
    print(x, end="")
    if left[idx] != '.':
        preorder(left[idx])
    if right[idx] != '.':
        preorder(right[idx])


def inorder(x):
    idx = ord(x) - ord("A")
    if left[idx] != '.':
        inorder(left[idx])
    print(x, end="")
    if right[idx] != '.':
        inorder(right[idx])

def postorder(x):
    idx = ord(x) - ord("A")
    if left[idx] != '.':
        postorder(left[idx])
    if right[idx] != '.':
        postorder(right[idx])
    print(x, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')