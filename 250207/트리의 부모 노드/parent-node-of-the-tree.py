n = int(input())

parent = [-1] * (n+1)
parent[1] = 0

pairs = [tuple(map(int, input().split())) for _ in range(n-1)]

def find_children(t):
    nodes = [i for i in pairs if t in i]
    for node in nodes:
        a, b = node
        if parent[a] != -1 and parent[b] != -1:
            continue    
        if parent[b] != -1:
            parent[a] = b
            find_children(a)
        else:
            parent[b] = a
            find_children(b)

find_children(1)
print(*parent[2:], sep="\n")
