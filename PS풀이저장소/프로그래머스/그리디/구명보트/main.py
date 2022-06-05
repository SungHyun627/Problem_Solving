def solution(people, limit):
    answer = 0
    if len(people) == 1:
        return 1
    people.sort()
#    print(people)
    start, end = 0, len(people) - 1
    temp_sum = 0
    while True:
        if (temp_sum + people[end]) > limit:
            #print('end', temp_sum, start, end)
            temp_sum = 0
            answer += 1        
            continue
        else:
            temp_sum += people[end]
            end -= 1
            if start > end:
                answer += 1
                break
            
        if (temp_sum + people[start]) > limit:
            #print('start', temp_sum, start, end)
            temp_sum = 0
            answer += 1
            continue
        else:
            temp_sum += people[start]
            start += 1
            if start > end:
                answer += 1
                break
    print(answer)
    return answer