import math
from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
            
def solution(numbers):
    answer = 0
    number = list(numbers)
    number_set = set()
    for i in range(1, len(number) + 1):
        for x in permutations(number, i):
            number_set.add(int(''.join(x)))   
    for num in number_set:
        if is_prime(num):
            answer += 1
            print(num, answer)
    return answer