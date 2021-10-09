from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

#테스트 케이스 수
t = int(stdin.readline())

def topology_sort(m, edges, indegree):
    strahler = [0] * (m+1)
    count = [0] * (m+1)
    checked = [False] * (m+1)
    
    queue = deque()

    for i in range(1, m+1):
        if indegree[i] == 0:
            strahler[i] = 1
            queue.append(i)
            checked[i] = True

    while queue:
        # print(strahler)
        # print('I', indegree)
        # print(queue)
        n = queue.popleft()
        for i in edges[n]:
            if strahler[i] < strahler[n]:
                strahler[i] = strahler[n]
                count[i] = 1
            elif strahler[i] == strahler[n]:
                count[i] += 1
                if count[i] == 2:
                    strahler[i] += 1
                    count[i] = 0
            else:
                pass
            indegree[i] -=1
            if indegree[i] == 0 and not checked[i]:
                queue.append(i)
    # print('I', indegree)
    # print(strahler)
    return max(strahler)

for _ in range(t):
    k, m, p = map(int, stdin.readline().split())
    edges = [[] for _ in range(m+1)]
    indegree = [0] * (m+1)

    for _ in range(p):
        a, b = map(int, stdin.readline().split())
        edges[a].append(b)
        indegree[b] += 1

    print(k, topology_sort(m, edges, indegree))