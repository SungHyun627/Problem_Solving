from collections import deque

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    prior_exist = [[False] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        prior_exist[i][i] = True
        prior_exist[i][0] = True
        
    for result in results:
        a, b = result
        graph[b].append(a)
    
    for i in range(1, n+1):
        q = deque()
        for j in graph[i]:
            prior_exist[i][j] = True
            prior_exist[j][i] = True
            q.append(j)
        
        while q:
            x = q.popleft()
            for k in graph[x]:
                if not prior_exist[i][k]:
                    prior_exist[i][k] = True
                    prior_exist[k][i] = True
                    q.append(k)
    
    for i in range(1, n+1):
        if all(prior_exist[i]):
            answer += 1
    return answer