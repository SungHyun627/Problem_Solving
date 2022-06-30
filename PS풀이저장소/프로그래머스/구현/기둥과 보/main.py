def check_build(ans):
    for frame in ans:
        x, y, a = frame
        if a == 0:
            if y == 0 or [x, y-1, 0] in ans or [x-1, y, 1] in ans or [x, y, 1] in ans:
                continue
            return False
        else:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            answer.append([x, y, a])
            if not check_build(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check_build(answer):
                answer.append([x, y, a])
    
    answer.sort()
    
    return answer