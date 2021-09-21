from sys import stdin

stdin = open('./input.txt', 'r')

#6*9 문자열 입력 받기
graph = list(list(stdin.readline().rstrip()) for _ in range(6))


#인접한 2개의 가로 줄에 있는 대문자 수/종류를 반환하는 함수
def check_adjacent_row(x):
    upper_char = [0] * 26
    for i in range(x, x+2):
        for j in range(9):
            upper_char[ord(graph[i][j])-ord('A')] += 1
    
    char_count = list(enumerate(upper_char))
    char_count.sort(key= lambda x: x[1], reverse = True)
    # print(char_count)
    return char_count


#인접한 3개의 세로 줄에 대해 대문자 수/종류를 반환하는 함수
def check_adjacent_col(y):
    upper_char = [0] * 26
    for i in range(6):
        for j in range(y, y+3):
            upper_char[ord(graph[i][j])-ord('A')] += 1
    
    char_count = list(enumerate(upper_char))
    char_count.sort(key= lambda x: x[1], reverse = True)
    # s
    return char_count


#가운데 색생과 다른 두줄의 색이 다름을 판별하여 바꿔야하는 최소 문자를 반환하는 함수
def check_not_same_color(x, y, z):
    i, j, k = 0, 0, 0
    while (x[i][0] == y[j][0] or y[j][0] == z[k][0]):
        if x[i][0] == y[j][0]:
            if (x[i+1][1] - x[i][1]) > (y[j+1][1] - y[j][1]):
                i += 1
            else:
                j += 1
        if y[j][0] == z[k][0]:
            if (y[j+1][1] - y[j][1]) > (z[k+1][1] - z[k][1]):
                j += 1
            else:
                k += 1
    
    return 54 - (x[i][1] + y[j][1]+ z[k][1])


#가로로 3등분(2*9 3개)했을 때 바꿔야 할 문자수를 구하는 함수
def check_horizontal():
    character_numbers = []
    for i in range(0, 6, 2):
        character_numbers.append(check_adjacent_row(i))
    
    a, b, c = character_numbers

    return check_not_same_color(a, b, c)


#세로로 3등분(3*6 3개)했을 때 바꿔야 할 문자수를 구하는 함수
def check_vertical():
    character_numbers = []
    for i in range(0, 9, 3):
        character_numbers.append(check_adjacent_col(i))
    
    a, b, c = character_numbers
    
    return check_not_same_color(a, b, c)

print(min(check_horizontal(), check_vertical()))
