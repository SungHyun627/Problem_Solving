def solution(s):
    answer = True
    s_len = len(s)
    left_num = 0
    
    for i in range(s_len):
        if s[i] == '(':
            left_num += 1
        else:
            if left_num == 0:
                return False
            left_num -= 1
    
    return True if not left_num else False