def dfs(x):
    group.add(x)
    if not adj_wire[x]:
        return
    for i in adj_wire[x]:
        if i not in group:
            dfs(i)
    
def solution(n, wires):
    global group, adj_wire
    answer = 5050
    adj_wire = [[] for _ in range(n+1)]
    
    for wire in wires:
        a, b = wire
        adj_wire[a].append(b)
        adj_wire[b].append(a)
    
    for t in wires:
        group = set()
        a, b = t
        adj_wire[a].remove(b)
        adj_wire[b].remove(a)
        if not adj_wire[1]:
            answer = min(answer, n-2)
        else:
            dfs(1)
            # print(group)
            answer = min(answer, abs(n-2*len(group)))
        adj_wire[a].append(b)
        adj_wire[b].append(a)
        
    return answer