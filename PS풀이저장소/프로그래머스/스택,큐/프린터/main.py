from collections import deque

def solution(priorities, location):
    queue = deque([])
    doc_dict = {}
    answer = 0
    target_value = priorities[location] 

    for i in range(len(priorities)):
        if i == location:
            queue.append('target')
            dict_key = target_value
        else:
            queue.append(priorities[i])
            dict_key = priorities[i]
        
        if dict_key in doc_dict:
            doc_dict[dict_key] += 1
        else:
            doc_dict[dict_key] = 1
    
    while queue:
        is_exist = False
        value = queue.popleft()

        if value == 'target':
            temp = target_value
        else: 
            temp = value

        for i in range(temp + 1, 10):
            if i in doc_dict:
                queue.append(value)
                is_exist = True
                break
        
        if not is_exist:
            if value == 'target':
                answer += 1
                break
            else:
                if doc_dict[value] != 1:
                    doc_dict[value] -= 1
                else:
                    del doc_dict[value]
                answer += 1
    return answer