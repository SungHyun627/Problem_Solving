def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    already_lend = set()
    
    for i in new_lost:
#         왼쪽부터 확인
        if i != 1 and (i-1) in new_reserve and (i-1) not in already_lend:
            already_lend.add((i-1))
            continue
        else:
            if i != n and (i+1) in new_reserve and (i+1) not in already_lend:
                already_lend.add(i+1)
    answer = n - len(new_lost) + len(already_lend)
    return answer