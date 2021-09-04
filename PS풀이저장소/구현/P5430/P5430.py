from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

#테스트 케이스 수
t = int(stdin.readline())


#AC언어 연산
def AC_Calculate(funcs, array):
    # print(array)
    is_reverse = False
    for i in funcs:
        if i == 'R':
            is_reverse = not(is_reverse)
        else:
            if array:
                if is_reverse:
                    array.pop()
                else:
                    array.popleft()
            else:
                return 'error'
    if is_reverse:
        array.reverse()
    array_string = ",".join(list(array))
    new_array_string = f'[{array_string}]'
    return new_array_string

        
for _ in range(t):
    funcs = stdin.readline().rstrip()
    number = int(stdin.readline())
    elements_string = (stdin.readline().rstrip())[1:-1]
    # print(elements_string)
    if elements_string:
        elements = deque(list(elements_string.split(',')))
    else:
        if 'D' in funcs:
            print('error')
        else:
            print('[]')
        continue
    print(AC_Calculate(funcs, elements))