from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    while sum_q1 != sum_q2:
        if sum_q1 > sum_q2:
            a = q1.popleft()
            sum_q1 -= a
            q2.append(a)
            sum_q2 += a
        else:
            a = q2.popleft()
            sum_q2 -= a
            q1.append(a)
            sum_q1 += a
        answer += 1
        if answer > 3 * (len(queue1)):
            return -1
    return answer