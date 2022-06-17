def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    #누적합 board
    cumulative_board = [[0] * (m+1) for _ in range(n+1)]
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        if t == 1:
            degree = -degree
        cumulative_board[r1][c1] += degree
        cumulative_board[r1][c2+1] -= degree
        cumulative_board[r2+1][c1] -= degree
        cumulative_board[r2+1][c2+1] += degree

    #행별(가로방향) 누적합 실행
    for i in range(n+1):
        for j in range(m):
            cumulative_board[i][j+1] += cumulative_board[i][j]
    #열별(세로방향) 누적합 실행
    for i in range(m+1):
        for j in range(n):
            cumulative_board[j+1][i] += cumulative_board[j][i]

    #board에 반영
    for i in range(n):
        for j in range(m):
            board[i][j] += cumulative_board[i][j]        
            if board[i][j] > 0:
                answer += 1 
    return answer