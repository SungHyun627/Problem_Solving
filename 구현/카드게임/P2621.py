from sys import stdin

# stdin = open('./input.txt', 'r')

card_list = []

# data 입력 받기
for _ in range(5):
    a, b = stdin.readline().rstrip().split()
    card_list.append([a, int(b)])

# 카드가 큰 순서대로 정렬
card_list.sort(key = lambda x : x[1], reverse = True)

# 해당 색깔을 가지는 카드의 개수를 나타내는 list(빨, 파, 노, 녹)
color_list = [0] * 4

# 해당 숫자를 가지는 카드의 개수를 나타내는 list(1~9)
# number_list[0]은 0으로 고정시키고, i의 개수는 number_list[i]에 저장
number_list = [0] * 10

for x, y in card_list:
    # color_list에 기록
    if x == "R":
        color_list[0] += 1
    elif x == "B":
        color_list[1] += 1
    elif x == "Y":
        color_list[2] += 1
    else:
        color_list[3] += 1
    # number_list에 기록
    number_list[y] += 1

# 점수를 계산하는 함수
def calculate_score(card, color, number):
    # 5장의 카드가 같은 색이고 연속적일때
    if 5 in color and number[number.index(1): number.index(1) + 5] == [1, 1, 1, 1, 1]:
        score = 900 + card[0][1]
    # 4장의 숫자가 같은 경우
    elif 4 in number:
        score = 800 + number.index(4)
    # 3장의 숫자가 같고, 나머지 2장의 숫자가 같은 경우
    elif 3 in number and 2 in number:
        score = 700 + 10 * number.index(3) + number.index(2)
    # 5장의 카드 색깔이 모두 같은 경우
    elif 5 in color:
        score = 600 + card[0][1]
    # 5장의 숫자가 연속적인 경우
    elif number[number.index(1): number.index(1) + 5] == [1, 1, 1, 1, 1]:
        score = 500 + card[0][1]
    # 3장의 숫자가 같은 경우
    elif 3 in number:
        score = 400 + number.index(3)
    # 2장의 숫자가 같고, 다른 2장의 숫자가 같은 경우
    elif number.count(2) == 2:
        score = 300 + (9 - number[::-1].index(2)) * 10 + number.index(2)
    # 2장의 숫자가 같은 경우
    elif 2 in number:
        score = 200 + number.index(2)
    # 어떤 경우에도 해당되지 않을 때
    else:
        score = 100 + card[0][1]
    return score
card_score = calculate_score(card_list, color_list, number_list)
print(card_score)