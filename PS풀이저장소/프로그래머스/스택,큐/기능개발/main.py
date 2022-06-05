from collections import deque

def solution(progresses, speeds):
    queue1 = deque(progresses)
    queue2 = deque(speeds)
    answer = []
    while queue1:
        function_number = 0
        for i in range(len(queue1)):
            queue1[i] += queue2[i]

        for i in range(len(queue1)):
            if queue1[i] < 100:
                break
            function_number += 1

        if function_number != 0:
            for _ in range(function_number):
                queue1.popleft()
                queue2.popleft()
            answer.append(function_number)
    return answer