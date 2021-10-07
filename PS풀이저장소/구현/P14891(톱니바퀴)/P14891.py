from sys import stdin

stdin = open('./input.txt', 'r')

teeth = []

for _ in range(4):
    teeth.append(list(map(int, stdin.readline().rstrip())))

#check_point

rotate_num = 0 
rotate_num = int(stdin.readline())
score = 0

def rotate_task(num, dir, count):
    global score
    rotate_dir = [0, 0, 0, 0]
    is_same_pole = [teeth[0][2]==teeth[1][6], teeth[1][2]==teeth[2][6], teeth[2][2]==teeth[3][6]]
    rotate_dir[num] = dir
    
    if num == 0:
        for i in range(3):
            if is_same_pole[i]:
                break
            else:
                rotate_dir[i+1] = -rotate_dir[i]
    elif num == 3:
        for i in range(2, -1, -1):
            if is_same_pole[i]:
                break
            else:
                rotate_dir[i] = -rotate_dir[i+1]
    elif num == 1:
        if not is_same_pole[0]:
            rotate_dir[0] = - rotate_dir[num]
        
        if not is_same_pole[1]:
            rotate_dir[2] = - rotate_dir[num]
            if not is_same_pole[2]:
                rotate_dir[3] = - rotate_dir[2]
    else:
        if not is_same_pole[2]:
            rotate_dir[3] = - rotate_dir[num]
        
        if not is_same_pole[1]:
            rotate_dir[1] = - rotate_dir[num]
            if not is_same_pole[0]:
                rotate_dir[0] = - rotate_dir[1]

    for i in range(4):
        if not rotate_dir[i]:
            continue
        elif rotate_dir[i] == 1:
            teeth[i].insert(0, teeth[i].pop())
        else:
            teeth[i].append(teeth[i].pop(0))
        
    
    if count == rotate_num - 1:
        for i in range(4):
            if teeth[i][0] == 1:
                score += (2 ** i)
    # print(teeth)

for i in range(rotate_num):
    a, b = map(int, stdin.readline().rstrip().split())
    rotate_task(a-1, b, i)

print(score)