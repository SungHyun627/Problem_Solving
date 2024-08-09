from collections import defaultdict

def solution(edges):
    inEdge = defaultdict(set)
    outEdge = defaultdict(set)
    nodes = set()
    max_num = 0
    start = -1
    total, line, donut, eight = 0, 0, 0, 0
    
    for edge in edges:
        a, b = edge
        inEdge[b].add(a)
        outEdge[a].add(b)
        nodes.add(a)
        nodes.add(b)
        max_num = max(max_num, a, b)
    
    ### 시작 정점
    for v in range(1, max_num+1):
        if len(inEdge[v]) == 0 and len(outEdge[v]) >= 2:
            start = v
            break
            
    ## 전체 그래프 개수
    total = len(outEdge[start])
    
    ## 시작 정점에 연결된 edge 제거
    for v in outEdge[start]:
        inEdge[v].remove(start)
        
    ## 팔자형 그래프
    for v in range(1, max_num + 1):
        ## outEdge와 inEdge의 개수가 2개씩인 정점 탐색
        if len(outEdge[v]) == 2 and len(inEdge[v]) == 2:
            eight += 1
            
    ## 막대 그래프
    for v in range(1, max_num + 1):
        ## outEdge가 0인 정점 탐색, 해당 node가 존재하는 지 확인
        if len(outEdge[v]) == 0 and v in nodes:
            line += 1
    
    ## 도넛 그래프
    donut = total - line - eight
        
    answer = [start, donut, line, eight]
    return answer