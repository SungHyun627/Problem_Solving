def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        new_array = sorted(array[i-1:j])
        answer.append(new_array[k-1])
    return answer