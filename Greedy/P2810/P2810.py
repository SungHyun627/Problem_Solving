from sys import stdin

stdin = open('./input.txt', 'r')

# 전체 좌석 수
seat_num = int(stdin.readline().rstrip())
# 좌석 리스트
seat_list = stdin.readline().rstrip()
# 커플 좌석의 수
couple_seat_num = seat_list.count('LL')
# 컵을 놓을 수 있는 사람의 수


# 커플 석이 없는 경우
if couple_seat_num == 0:
    canuse_people_num = seat_num
else:
    canuse_people_num = seat_num + 1 - couple_seat_num

print(canuse_people_num)