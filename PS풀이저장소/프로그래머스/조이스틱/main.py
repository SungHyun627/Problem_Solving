def cal_horizontal_count(x, y, name_len):
    front_dist = x-1
    back_dist = name_len-1-y
    if x == 0:
        return 2 * back_dist
    min_dist = min(front_dist, back_dist)
    
    if min_dist == front_dist:
        total_dist = 2 * front_dist + back_dist
    else:
        total_dist = front_dist + 2 * back_dist       
    return total_dist if total_dist < name_len - 1 else name_len - 1    

def solution(name):
    answer = 0
    a_region = []
    a_start, a_end = -1, -1
    for x in name:
        k = ord(x) - ord('A')
        if k <= 13:
            answer += k
        else:
            answer += (26-k)
    
#    연속적인 A의 개수와 위치
    for i in range(len(name)):
#         해당 알파벳이 'A'일때
        if name[i] == 'A':
#         첫 'A'일때
            if a_start == -1:
                a_start = i
            a_end = i
#             마지막 문자라면
            if i == len(name) - 1:
                a_region.append((a_start, a_end))
        else:
            if a_start != -1:
                a_region.append((a_start, a_end))
                a_start, a_end = -1, -1   
    if a_region:
        a_region.sort(key = lambda x: cal_horizontal_count(x[0], x[1], len(name)))
        answer += cal_horizontal_count(a_region[0][0], a_region[0][1], len(name))
    else:
#         A가 없는 경우
        answer += len(name) - 1
    return answer