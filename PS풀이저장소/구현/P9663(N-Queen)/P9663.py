#P9663 N-Queen (PyPy로 채점)
from sys import stdin
stdin = open('./input.txt', 'r')

#체스판의 길이
n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
#퀸을 놓는 방법의 수
count = 0

#오른쪽 아래로 향하는 대각선 방향에 퀸을 놓을 수 있는지 체크
checked1 = [False] * (2*(n-1) + 1)
#왼쪽 아래로 향하는 대각선 방향에 퀸을 놓을 수 있는지 체크
checked2 = [False] * (2*(n-1) + 1)
#특정 열에 퀸을 놓을 수 있는지 check
checked3 = [False] * (n)

def backtrack(cur):
    global count
    if cur == n:
        count += 1
        return
    
    for i in range(n):
        if checked1[cur-i+n-1] or checked2[cur+i] or checked3[i ]:
            continue
        checked1[cur-i+n-1] = True
        checked2[cur+i] = True
        checked3[i] = True
        backtrack(cur + 1)
        checked1[cur-i+n-1] = False
        checked2[cur+i] = False
        checked3[i] = False

backtrack(0)
print(count)