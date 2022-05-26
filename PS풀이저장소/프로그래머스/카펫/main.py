import math

def solution(brown, yellow):
    mul = brown + yellow
    plus = (brown + 4) // 2
    height = 0
    width = 0
    
    for i in range(1, int(math.sqrt(mul)) + 1):
        if mul % i == 0:
            if (mul // i) + i == plus:
                height = i
                width = (mul // i)
                print(height, width)
                break
    answer = [width, height]
    print(answer)
    return answer