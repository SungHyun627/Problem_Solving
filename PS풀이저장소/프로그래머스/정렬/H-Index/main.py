def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(citations[0], 0 , -1):
        num = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                num += 1
            else:
                break
        if num >= i:
            answer = i
            break    
    return answer