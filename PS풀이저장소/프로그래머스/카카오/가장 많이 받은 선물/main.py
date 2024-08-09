from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    records = defaultdict(dict)
    result = defaultdict(int)
    answer = 0   
    
    for friend in friends:
        records[friend] = dict()
        records[friend]['get'] = defaultdict(int)
        records[friend]['give'] = defaultdict(int) 
    
    for gift in gifts:
        a, b = gift.split(' ')
        records[a]['give'][b] += 1
        records[b]['get'][a] += 1
    
    pair = list(combinations(friends, 2))
    
    # print(records)
    
    for x, y in pair:
        ## 개수
        x_give = records[x]['give'][y]
        x_get = records[x]['get'][y]
        
        if x_give > x_get:
            result[x] += 1
            continue
        if x_give < x_get:
            result[y] += 1
            continue
        
        x_idx = sum(records[x]['give'].values()) - sum(records[x]['get'].values())
        y_idx = sum(records[y]['give'].values()) - sum(records[y]['get'].values())
        
        if x_idx > y_idx:
            result[x] += 1
            continue
        
        if x_idx < y_idx:
            result[y] += 1
            continue
    
    
    return max(result.values()) if len(result.values()) != 0 else 0