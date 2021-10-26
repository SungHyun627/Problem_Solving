#P2239, 스도쿠
from sys import stdin

stdin = open('./input.txt', 'r')
board = []
rows = [[False] * 10 for _ in range(10)]
columns = [[False] * 10 for _ in range(10)]
is_finished = False

areas = {
    (0, 0) : [False] * 10, (0, 1) : [False] * 10, (0, 2) : [False] * 10,
    (1, 0) : [False] * 10, (1, 1) : [False] * 10, (1, 2) : [False] * 10,
    (2, 0) : [False] * 10, (2, 1) : [False] * 10, (2, 2) : [False] * 10
        } 

for i in range(9):
    a = stdin.readline().rstrip()
    for j in range(9):
        b = int(a[j])
        board.append(b)
        rows[i][b] = True
        columns[j][b] = True
        areas[((i // 3), (j // 3))][b] = True

def fill_board(num):
    # print(num)
    global is_finished
    #모든 스토쿠가 다 채워 졌다면
    if is_finished:
        return
    if num == 81 and not is_finished:
        is_finished = True
        s = ''
        for i in range(1, 82):
            s += str(board[i-1])
            if i % 9 == 0:
                print(s)
                s = ''
    #해당 숫자가 0이 아닐 때
    elif board[num]:
        fill_board(num+1)
        return
    else:
        p = num // 9
        q = num % 9
        for i in range(1, 10):
            if not rows[(p)][i] and not columns[(q)][i] and not areas[(((p) // 3), ((q) // 3))][i]:
                rows[(p)][i] = True
                columns[(q)][i] = True
                areas[(((p) // 3), ((q) // 3))][i] = True
                #해당 값을 i로 채우기
                board[num] = i
                #다음 공간 채우기
                fill_board(num + 1)

                rows[(p)][i] = False
                columns[(q)][i] = False
                areas[(((p) // 3), ((q) // 3))][i] = False
                board[num] = 0
        return
fill_board(0)