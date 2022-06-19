def rotate(x, y, z):
    new_key = [[0] * y for _ in range(y)]
    if z == 0:
        for i in range(y):
            for j in range(y):
                new_key[i][j] = x[i][j]
    #90도
    elif z == 1:
        for i in range(y):
            for j in range(y):
                new_key[j][y-i-1] = x[i][j]
    #180도
    elif z == 2:
        for i in range(y):
            for j in range(y):
                new_key[y-i-1][y-j-1] = x[i][j]
	#270도
    else:
        for i in range(y):
            for j in range(y):
                new_key[y-j-1][i] = x[i][j]
    return new_key
        
def is_match(dx, dy, new_key, board, k_l, l_l, b_l):
    temp_board = [[0] * b_l for _ in range(b_l)]
    for i in range(b_l):
        for j in range(b_l):
            temp_board[i][j] = board[i][j]
            
    for i in range(k_l):
        n_x = i + dx
        #키가 자물쇠의 범위를 벗어난 경우
        if (n_x) < (k_l - 1) or (n_x) > (k_l + l_l - 2):
            continue
        for j in range(k_l):
            n_y = j + dy
            #키가 자물쇠의 범위를 벗어난 경우
            if (n_y) < (k_l - 1) or (n_y) > (k_l + l_l - 2):
                continue
            if new_key[i][j] == 0:
                continue
            else:
                #자물쇠: 홈, 열쇠 : 돌기인 경우
            	if temp_board[n_x][n_y] == 1:
                    return False
            	else:
                	temp_board[n_x][n_y] = 1
    #자물쇠가 다 돌기로 채워졌나 확인
    for i in range(k_l - 1, k_l + l_l - 1):
        for j in range(k_l - 1, k_l + l_l - 1):
            if temp_board[i][j] == 0:
                return False
    return True


def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)
    board_length = key_length * 2 - 2 + lock_length
    board = [[0] * board_length for _ in range(board_length)]
    for i in range(lock_length):
        for j in range(lock_length):
            board[i+key_length-1][j+key_length-1] = lock[i][j]
    for i in range(board_length-key_length+1):
        for j in range(board_length-key_length+1):
            for k in range(4):
                if is_match(i, j, rotate(key, key_length, k), board, key_length, lock_length, board_length):
#                    print(i, j, k)
                    return True
    return False