from sys import stdin

stdin = open('./input.txt', 'r')

#테스트 케이스 수
t = int(stdin.readline())


def is_consistency(phone_list):
    phone_list.sort()
    # print(phone_list)
    for i in range(len(phone_list)-1):
        if len(phone_list[i]) <= len(phone_list[i+1]):
            if phone_list[i] == phone_list[i+1][:len(phone_list[i])]:
                return 'NO'
    return 'YES'

for _ in range(t):
    number = int(stdin.readline().rstrip())
    phone_list = []
    for _ in range(number):
        phone_list.append(stdin.readline().rstrip())
    print(is_consistency(phone_list))