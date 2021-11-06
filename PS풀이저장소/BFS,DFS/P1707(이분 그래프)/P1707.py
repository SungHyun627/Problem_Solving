#P1707 이분그래프
from sys import stdin
from collections import deque, Counter

stdin = open('./input.txt', 'r')

k = int(stdin.readline())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def is_bipartite_graph(v, nodes, roots):
    for root in roots:
        # 처음 색깔 : 'W', 빨간색 : 'R', 파란색 : 'B'
        colors = ["W" for _ in range(v+1)]
        queue = deque()
        queue.append((root, 'R'))
        color_to_paint = ""
        while queue:
            number, color = queue.popleft()
            if color == "R":
                color_to_paint = "B"
            else:
                color_to_paint = "R"
            
            # if number doesn't have adjacent node,
            if number not in nodes:
                continue
            for node in nodes[number]:
                if colors[node] == 'W':
                    colors[node] = color_to_paint
                    queue.append((node, color_to_paint))
                else:
                    if colors[node] != color_to_paint:
                        return "NO"
        # print(colors)
    return "YES"

for _ in range(k):
    v, e = map(int, stdin.readline().split())
    parent = [i for i in range(v+1)]
    adjacent_nodes = {}
    
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        if b > a:
            if a not in adjacent_nodes:
                adjacent_nodes[a] = [b]
            else:
                adjacent_nodes[a].append(b)
        else:
            if b not in adjacent_nodes:
                adjacent_nodes[b] = [a]
            else:
                adjacent_nodes[b].append(a) 

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    set_of_root_node = list(Counter(parent[1:]).keys())
    # print(set_of_root_node)
    print(is_bipartite_graph(v, adjacent_nodes, set_of_root_node))