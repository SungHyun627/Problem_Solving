from itertools import combinations, product
from collections import Counter
from bisect import bisect_left


def solution(dice):
    n = len(dice)
    max_win = 0
    answer = []
    
          
#   주사위 n // 2 개씩 나누기
    cases = list(combinations([i for i in range(1, n+1)], n // 2))
    
    for case in cases:
        result = 0
        dice_a = list(case)
        dice_b = list(set([i for i in range(1, n+1)]) - set(dice_a))       
        a1, a2 = 0, 0
        b1, b2 = 0, 0
        
        sum_a = [sum(t) for t in list(product(*[dice[i-1] for i in dice_a]))]
        sum_b = [sum(t) for t in list(product(*[dice[i-1] for i in dice_b]))]
        
        length = len(sum_a)
        a = Counter(sum_a)
                
        ## b 합계 정렬
        sum_b.sort()
            
        for t in a.keys():
            result += bisect_left(sum_b, t) * a[t]
        
        
        ## max_win 갱신
        if max_win < result:
            max_win = result
            answer = dice_a
    
    return answer