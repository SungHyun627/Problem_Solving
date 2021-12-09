#P14890 경사로
from sys import stdin
stdin = open('./input.txt', 'r')

n, l = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = 0

def can_pass(road):
    temp = -1
    count = 0
    lower_height = False
    
    for i in range(n):
        # print(temp, count, lower_height)
        if i == 0:
            count = 1
            temp = road[i]
            continue

        if road[i] == temp:
            count += 1
            if lower_height and count == l:
                lower_height = False
                count = 0
        else:
            if abs(road[i]-temp) > 1:
                return 0
            # 더 높은 곳으로 이동한다면
            if (road[i] - temp) == 1:
                if count < l:
                    return 0
                temp = road[i]
                count = 1
                lower_height = False
            
            if (temp - road[i]) == 1:
                if lower_height:
                    if count < l:
                        return 0
                else:
                    if l == 1:
                        temp = road[i]
                        count = 0
                    else:
                        lower_height = True
                        temp = road[i]
                        count = 1
    if lower_height:
        if count < l:
            return 0
        return 1
    else:
        # print(road)
        return 1

# 행
for i in range(n):
    # print(i)
    col = []
    result += can_pass(board[i])
    for j in range(n):
        col.append(board[j][i])
    result += can_pass(col)
print(result)