from sys import stdin
stdin = open('./input.txt', 'r')

t = int(stdin.readline())

def student_have_team(n, arr):
    #팀을 구성하는 학생들을 담는 리스트
    person_in_team = []
    #해당 학생들이 체크 되었는 지를 표시하는 리스트
    is_checked = [False] * (n+1)

    #해당 학생이 선택한 학생을 표시하는 리스트
    parent = [i for i in range(n+1)]

    for i in range(1, len(arr)):
        if arr[i] == i:
            is_checked[i] = True
            person_in_team.append(i)
            continue
        parent[i] = arr[i]
    
    for i in range(1, len(arr)):
        # 팀을 구성하지 않는 학생에 대하여
        if not is_checked[i]:
            not_make_team = False
            # i를 포함하는 팀(key), 순서(값)
            team = {}
            team[i] = 0
            temp = 1
            team_student = [i]
            while True:
                if parent[i] != i:
                    if is_checked[parent[i]]:
                        not_make_team = True
                        break
                    if parent[i] in team:
                        target = team[parent[i]]
                        break
                    team[parent[i]] = temp
                    team_student.append(parent[i])
                    i = parent[i]
                    temp += 1

            #팀을 구성하지 못하는 경우
            if not_make_team:
                #체크
                for k in range(temp):
                    is_checked[team_student[k]] = True
                continue
            
            #팀을 구성한 경우
            for k in range(temp):                
                is_checked[team_student[k]] = True
                if k >= target:
                    person_in_team.append(k)
    # print(parent, is_checked)
    return len(person_in_team)

for _ in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    arr = [0] + arr
    num = student_have_team(n, arr)
    print(n - num)