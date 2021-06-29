from sys import stdin

stdin = open('./input.txt', 'r')
# 카드 리스트 길이
stdin.readline().rstrip()

card_list = list(map(int, stdin.readline().rstrip().split()))
# 서로 인접한 카드를 옮길 수 있는 횟수
can_move_num = 0
for i in range(len(card_list) - 1):
    if card_list[i] >= card_list[i+1]:
        can_move_num += 1

print(len(card_list) - can_move_num)