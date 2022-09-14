def passed_words_num(t, k):
    temp = 0
    for i in range(k):
        temp += (5 ** i)
    return t * temp + 1

def solution(word):
    answer = 0
    alphabets = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    cnt = 5
    for c in word:
        answer += passed_words_num(alphabets[c], cnt)
        cnt -= 1
    return answer