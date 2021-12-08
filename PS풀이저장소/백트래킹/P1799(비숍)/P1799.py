#P1799 비숍
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
max_num = 0
# 오른쪽 아래 방향
visited1 = [False] * (2*n - 1)
# 왼쪽 아래 방향
visited2 = [False] * (2*n - 1)
# 놓은 비숍의 개수
count = 0

def backtrack(num):
    is_all_one = True
    global max_num
    global count
    if num == (2*n - 1):
        # print(count, visited1, visited2)
        if max_num < count:
            max_num = count
        return
    
    if num <= n-1:
        for i in range(num+1):
            if board[i][num-i] and not visited1[num] and not visited2[i-(num-i) + n - 1]:
                is_all_one = False
                visited1[num] = True
                visited2[i-(num-i) + n - 1] = True
                count += 1
                backtrack(num + 1)
                visited1[num] = False
                visited2[i-(num-i) + n - 1] = False
                count -= 1
        if is_all_one:
            backtrack(num+1)
    else:
        for i in range(num-(n-1), n):
            if board[i][num-i] and not visited1[num] and not visited2[i-(num-i) + n - 1]:
                is_all_one = False
                visited1[num] = True
                visited2[i-(num-i) + n - 1] = True
                count += 1
                backtrack(num + 1)
                visited1[num] = False
                visited2[i-(num-i) + n - 1] = False
                count -= 1
        if is_all_one:
            backtrack(num+1)

backtrack(0)
print(max_num)