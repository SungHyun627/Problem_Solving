from itertools import combinations_with_replacement, permutations

"""
n개의 이모티콘에 대해 각각 10, 20, 30, 40의 할인율 일때
서비스 가입자 및 이모티콘 판매액 계산
4**7*100
"""

def solution(users, emoticons):
    ratio = [10, 20, 30, 40]
    n = len(emoticons)
    cases = []
    max_register, max_amount = 0, 0
    
    for x in combinations_with_replacement(ratio, n):
        cases += list(set(permutations(x, n)))
    
    for case in cases:
        x_register, x_amount = 0, 0
        
        for i in range(len(users)):
            amount = 0
            for j in range(n):
                if case[j] < users[i][0]:
                    continue
                amount += (100 - case[j]) * emoticons[j] // 100
                if amount >= users[i][1]:
                    x_register += 1
                    amount = 0
                    break
            x_amount += amount
        if x_register < max_register:
            continue
        if x_register == max_register and max_amount > x_amount:
            continue
            
        max_register = x_register
        max_amount = x_amount
    
    answer = [max_register, max_amount]
    return answer