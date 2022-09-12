from collections import deque

def compare_word(a, b, l):
    different_char_num = 0
    
    for i in range(l):
        if a[i] != b[i]:
            different_char_num += 1
    return different_char_num
    
def solution(begin, target, words):
    #target이 words에 없을 때
    if target not in words:
        return 0
    
    #words 개수
    words_num = len(words)
    #word길이
    word_length = len(words[0])
    #방문 리스트
    visited = [False] * words_num
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        print(q)
        t_word, num = q.popleft()
        for i in range(words_num):
            if visited[i]:
                continue
            if compare_word(t_word, words[i], word_length) == 1:
                if words[i] == target:
                    return num + 1
                else:
                    q.append((words[i], num + 1))
                    visited[i] = True
    
    return 0