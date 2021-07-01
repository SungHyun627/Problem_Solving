from sys import stdin
from itertools import combinations, product

# 입력 값 받기
stdin = open('./input.txt', 'r')
n = int(stdin.readline().rstrip())
graph = []
vacants = []
teachers = []
students = []

for i in range(n):
    graph.append(list(stdin.readline().rstrip().split()))
    
    for j in range(n):
        if graph[i][j] == 'S':
            students.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))
        else:
            vacants.append((i, j))

def find_student(teacher_position):
    #동, 서, 남, 북으로 student가 보이는지 check
    x = teacher_position[0]
    y = teacher_position[1]

    # 1. 동
    while y < n:
        if graph[x][y] == 'S':
            return True
        elif graph[x][y] == 'O':
            break
        y += 1
    
    x = teacher_position[0]
    y = teacher_position[1]

    # 2. 서
    while y >= 0:
        if graph[x][y] == 'S':
            return True
        elif graph[x][y] == 'O':
            break
        y -= 1
    
    x = teacher_position[0]
    y = teacher_position[1]

    # 3. 남
    while x < n:
        if graph[x][y] == 'S':
            return True
        elif graph[x][y] == 'O':
            break
        x += 1
    
    x = teacher_position[0]
    y = teacher_position[1]

    # 4. 북
    while x >= 0:
        if graph[x][y] == 'S':
            return True
        elif graph[x][y] == 'O':
            break
        x -= 1
    
    return False


for walls in list(combinations(vacants , 3)):
    can_hide = False

    for wall in walls:
        x, y = wall
        #벽 세우기
        graph[x][y] = 'O'

    if not any(list(map(lambda x: find_student(x), teachers))):
        can_hide = True
        break

    for wall in walls:
        x, y = wall
        #벽 세우기
        graph[x][y] = 'X'
    
if can_hide:
    print('YES')
else:
    print('NO')