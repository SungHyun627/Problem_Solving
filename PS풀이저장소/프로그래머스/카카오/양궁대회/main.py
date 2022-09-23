def DFS(arrow_num, target, lion, apeach, info, arrow_state):
    global answer, max_gap 
    if arrow_num == 0:
        gap = lion - apeach
        if gap > max_gap:
            max_gap = gap
            answer = [i for i in arrow_state]
            print(answer, lion, apeach)
            
        elif gap == max_gap and max_gap != 0:
            for j in range(10, -1, -1):
                if answer[j] == arrow_state[j]:
                    continue
                elif answer[j] > arrow_state[j]:
                    break
                else:
                    answer = [i for i in arrow_state]
                    break
                    print(answer, lion, apeach)
        else:
        	pass
        return

    else:
        for k in range(target, 11):
            if arrow_num > info[k]:
                arrow_state[k] = info[k] + 1
                if info[k]:
                	DFS(arrow_num - arrow_state[k], k+1, lion+10-k, apeach-10+k, info, arrow_state)
                else:   
                    DFS(arrow_num - arrow_state[k], k+1, lion+10-k, apeach, info, arrow_state)
                arrow_state[k] = 0
            else:
                if k == 10:
                    arrow_state[10] = arrow_num
                    DFS(0, k+1, lion, apeach+10-k, info, arrow_state)
                    arrow_state[10] = 0
                else:
                    DFS(arrow_num, k+1, lion, apeach, info, arrow_state)
               
def solution(n, info):
    global answer, max_gap
    apeach = 0
    max_gap = 0
    answer = [0] * 11
    for i in range(11):
        if info[i] > 0:
            apeach += (10-i)
    DFS(n, 0, 0, apeach, info, [0] * 11)
    if max_gap == 0:
        answer = [-1]
    return answer