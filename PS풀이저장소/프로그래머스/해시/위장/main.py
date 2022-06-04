def solution(clothes):
    clothe_type = {}
    answer = 1
    for clothe in clothes:
        if clothe[1] in clothe_type:
            clothe_type[clothe[1]] += 1 
        else:
            clothe_type[clothe[1]] = 1
    each_clothe_number = list(clothe_type.values())
    for i in each_clothe_number:
        answer *= (i + 1)     
    return answer - 1