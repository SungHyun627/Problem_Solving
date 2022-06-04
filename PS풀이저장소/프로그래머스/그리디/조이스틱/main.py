def solution(name):
    answer = 0
    # 수평으로 이동하는 횟수
    temp1 = len(name)
    name_len = len(name)

    for x in name:
        k = ord(x) - ord('A')
        if k <= 13:
            answer += k
        else:
            answer += (26-k)
    for k in range(len(name)):
      # k+1부터 시작하여 처음으로 문자가 'A'가 아닌 경우, 해당 문자의 index
      not_A_idx = k+1
      while not_A_idx < name_len:
        if name[not_A_idx] != 'A':
          break
        not_A_idx += 1
      temp1 = min(temp1, 2*k + name_len - not_A_idx, k + 2 * (name_len - not_A_idx))
    answer += temp1
    return answer