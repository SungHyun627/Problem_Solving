from collections import deque
#로봇의 상태(가로: 1, 세로: 2), 이동 좌표 고려
#위, 아래로만 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def check_out_of_boundary(t, n):
    if t[0] < 0 or t[1] < 0 or t[0] >= n or t[1] >= n:
        return True
    return False
    
def solution(board):
    answer = 0
    n = len(board)
    visited = set()
    cur = ((0, 0), (0, 1), 1)
    q = deque([])
    q.append(((0, 0), (0, 1), 1, 0))
    visited.add(cur)
    
    while q:
#        print(q)
        pos1, pos2, state, count = q.popleft()
        for k in range(4):
            npos1 = (pos1[0] + dx[k], pos1[1] + dy[k])
            npos2 = (pos2[0] + dx[k], pos2[1] + dy[k])
            if check_out_of_boundary(npos1, n):
                continue
            if check_out_of_boundary(npos2, n):
                continue
			#벽과의 충돌
            if board[npos1[0]][npos1[1]] or board[npos2[0]][npos2[1]]:
                continue
			#방문기록이 있다면
            if (npos1, npos2, state) in visited:
                continue
			#끝에 도착했다면
            if npos2[0] == n-1 and npos2[1] == n-1:
                return count + 1
            q.append((npos1, npos2, state, count+1))
            visited.add((npos1, npos2, state))

        #가로 방향이라면
        if state == 1:
            #아래로 회전 가능하다면
            if (pos1[0] + 1) < n:
                #벽이 아니라면
                if not board[pos1[0]+1][pos1[1]] and not board[pos2[0]+1][pos2[1]]:
                    if not (pos1, (pos2[0]+1, pos2[1]-1), 2) in visited:
                        if (pos2[0]+1) == n-1 and (pos2[1]-1) == n-1:
                            return count + 1
                        q.append((pos1, (pos2[0]+1, pos2[1]-1), 2, count + 1))
                        visited.add((pos1, (pos2[0]+1, pos2[1]-1), 2))
                    if not (pos2, (pos1[0]+1, pos1[1]+1), 2) in visited:
                        if (pos1[0]+1) == n-1 and (pos1[1]+1) == n-1:
                            return count + 1
                        q.append((pos2, (pos1[0]+1, pos1[1]+1), 2, count + 1))
                        visited.add((pos2, (pos1[0]+1, pos1[1]+1), 2))
            #위로 회전 가능하다면
            if (pos1[0] - 1) >= 0:
                if not board[pos1[0]-1][pos1[1]] and not board[pos2[0]-1][pos2[1]]:
                    if not ((pos2[0]-1, pos2[1]-1), pos1, 2) in visited:
                        if pos1[0] == n-1 and pos1[1] == n-1:
                            return count + 1
                        q.append(((pos2[0]-1, pos2[1]-1), pos1, 2, count + 1))
                        visited.add(((pos2[0]-1, pos2[1]-1), pos1, 2))
                    if not ((pos1[0]-1, pos1[1]+1), pos2, 2) in visited:
                        if pos2[0] == n-1 and pos2[1] == n-1:
                            return count + 1
                        q.append(((pos1[0]-1, pos1[1]+1), pos2, 2, count + 1))
                        visited.add(((pos1[0]-1, pos1[1]+1), pos2, 2))
        else:
            #오른쪽으로 회전 가능하다면
            if (pos1[1] + 1) < n:
                #벽이 아니라면
                if not board[pos1[0]][pos1[1]+1] and not board[pos2[0]][pos2[1]+1]:
                    if not (pos1, (pos2[0]-1, pos2[1]+1), 1) in visited:
                        if (pos2[0]-1) == n-1 and (pos2[1]+1) == n-1:
                            return count + 1
                        q.append((pos1, (pos2[0]-1, pos2[1]+1), 1, count + 1))
                        visited.add((pos1, (pos2[0]-1, pos2[1]+1), 1))
                    if not (pos2, (pos1[0]+1, pos1[1]+1), 1) in visited:
                        if (pos1[0]+1) == n-1 and (pos1[1]+1) == n-1:
                            return count + 1
                        q.append((pos2, (pos1[0]+1, pos1[1]+1), 1, count + 1))
                        visited.add((pos2, (pos1[0]+1, pos1[1]+1), 1))
            #왼쪽으로 회전 가능하다면
            if (pos1[1] - 1) >= 0:
                if not board[pos1[0]][pos1[1]-1] and not board[pos2[0]][pos2[1]-1]:
                    if not ((pos2[0]-1, pos2[1]-1), pos1, 1) in visited:
                        if pos1[0] == n-1 and pos1[1] == n-1:
                            return count + 1
                        q.append(((pos2[0]-1, pos2[1]-1), pos1, 1, count + 1))
                        visited.add(((pos2[0]-1, pos2[1]-1), pos1, 1))
                    if not ((pos1[0]+1, pos1[1]-1), pos2, 1) in visited:
                        if pos2[0] == n-1 and pos2[1] == n-1:
                            return count + 1
                        q.append(((pos1[0]+1, pos1[1]-1), pos2, 1, count + 1))
                        visited.add(((pos1[0]+1, pos1[1]-1), pos2, 1))