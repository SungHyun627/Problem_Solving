from itertools import permutations

def solution(n, weak, dist):
    #원형을 직선형으로
    weak_len = len(weak)
    dist_len = len(dist)
    answer = dist_len + 1
    
    for i in range(weak_len):
        weak.append(weak[i] + n)
    dist_seqs = list(permutations(dist, dist_len))
    
    for start in range(weak_len):
        for dist_seq in dist_seqs:
            count = 1
            #친구의 이동 위치
            pos = weak[start] + dist_seq[count-1]
            
            for idx in range(start, start+weak_len):
                if pos < weak[idx]:
                    count += 1
                    if count > dist_len:
                        break
                    pos = weak[idx] + dist_seq[count-1]
            answer = min(answer, count)
    if answer == (dist_len + 1):
        return -1                     
    
    return answer