#P12100 2048(Easy)
from sys import stdin
from copy import deepcopy
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
initial_board = list(list(map(int, stdin.readline().split())) for _ in range(n))
dir = ["left", "right", "up", "down"]
#만들 수 있는 최대 숫자
max_num = 0

def move(board, direction):
    #수평으로 옮기기
    if direction == "right" or direction == "left":
        for i in range(n):
            new_row = []
            num_zero = 0
            for j in board[i]:
                if j:
                    new_row.append(j)
                else:
                    num_zero += 1
            if direction == 'right':
                for _ in range(num_zero):
                    new_row.insert(0, 0)
            else:
                for _ in range(num_zero):
                    new_row.append(0)
            board[i] = new_row
        #계산
        for i in range(n):
            if direction == 'right':
                for j in range(n-1, 0, -1):
                    if board[i][j] == 0:
                        break
                    if board[i][j] == board[i][j-1]:
                        board[i][j] *=2
                        del board[i][j-1]
                        board[i].insert(0, 0)
            else:
                for j in range(n-1):
                    if board[i][j] == 0:
                        break
                    if board[i][j] == board[i][j+1]:
                        board[i][j] *=2
                        del board[i][j+1]
                        board[i].append(0)
    #수직으로 옮기기
    else:
        new_board = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[i][j] = board[j][i]

        for i in range(n):
            new_row = []
            num_zero = 0
            for j in new_board[i]:
                if j:
                    new_row.append(j)
                else:
                    num_zero += 1
            if direction == "down":
                for _ in range(num_zero):
                    new_row.insert(0, 0)
            else:
                for _ in range(num_zero):
                    new_row.append(0)
            new_board[i] = new_row
        
        #계산
        for i in range(n):
            if direction == "down":
                for j in range(n-1, 0, -1):
                    if new_board[i][j] == 0:
                        break
                    if new_board[i][j] == new_board[i][j-1]:
                        new_board[i][j] *=2
                        del new_board[i][j-1]
                        new_board[i].insert(0, 0)
            else:
                for j in range(n-1):
                    if new_board[i][j] == 0:
                        break
                    if new_board[i][j] == new_board[i][j+1]:
                        new_board[i][j] *=2
                        del new_board[i][j+1]
                        new_board[i].append(0)
        
        for i in range(n):
            for j in range(n):
                board[i][j] = new_board[j][i]
    return board

for a in range(4):
    direction_case = []
    direction_case.append(dir[a])
    for b in range(4):
        direction_case.append(dir[b])
        for c in range(4):
            direction_case.append(dir[c])
            for d in range(4):
                direction_case.append(dir[d])
                for e in range(4):
                    direction_case.append(dir[e])
                    board = deepcopy(initial_board)
                    max_num_board = 0
                    for i in range(5):
                        board = move(board, direction_case[i])
                    for i in range(n):
                        max_num_board = max(max_num_board, max(board[i]))
                    max_num = max(max_num, max_num_board)
                    direction_case.pop()
                direction_case.pop()
            direction_case.pop()
        direction_case.pop()
    direction_case.pop()
print(max_num)