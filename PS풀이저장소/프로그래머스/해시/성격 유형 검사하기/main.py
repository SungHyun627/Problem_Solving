def solution(survey, choices):
    answer = ''
    type_pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    survey_num = len(survey)
    scores = dict.fromkeys(['A', 'N', 'C', 'F', 'M', 'J', 'R', 'T'], 0)
    choice_score = [3, 2, 1, 0, 1, 2, 3]
    
    for i in range(survey_num):
        choice = choices[i]
        if choice <= 4:
            scores[survey[i][0]] += choice_score[choice - 1]
        else:
            scores[survey[i][1]] += choice_score[choice - 1]
    
    for i in range(4):
        a, b = type_pairs[i]
        if scores[a] >= scores[b]:
            answer += a
        else:
            answer += b
    return answer