from sys import stdin

stdin = open('./input.txt', 'r')
tree_type = {}
total = 0
while True:
    n = stdin.readline().rstrip()
    if not n:
        break
    total += 1
    if n not in tree_type:
        tree_type[n] = 1
    else:
        tree_type[n] += 1

tree_sort = list(tree_type.keys())
tree_sort.sort()
for tree in tree_sort:
    s = '{0} {1:.4f}'.format(tree, (tree_type[tree]) / total * 100)
    print(s)