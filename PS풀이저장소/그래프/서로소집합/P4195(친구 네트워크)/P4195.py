#P4195 친구 네트워크
from sys import stdin
stdin = open('./input.txt', 'r')

t = int(stdin.readline())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b, group):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return group[a]
    elif a > b:
        parent[a] = b        
    else:
        parent[b] = a
    group[a] += group[b]
    group[b] = group[a]
    return group[a]

def calculate_network_pepole(relation_num):
    group_people = [1] * (2 * relation_num + 1)
    people = {}
    index = 1
    parent = [i for i in range(2 * relation_num + 1)]
    for _ in range(relation_num):
        a, b = stdin.readline().rstrip().split()
        if a not in people:
            people[a] = index
            index += 1
        if b not in people:
            people[b] = index
            index += 1
        print(union_parent(parent, people[a], people[b], group_people))

for _ in range(t):
    n = int(stdin.readline())
    calculate_network_pepole(n)