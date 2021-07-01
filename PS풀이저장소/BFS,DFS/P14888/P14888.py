from sys import stdin
from itertools import permutations
stdin = open('./input.txt', 'r')
n = int(stdin.readline().rstrip())
numbers = list(map(int, stdin.readline().rstrip().split()))
# 0 : +, 1 : -, 2 : *, 3 : /
operator_number = list(map(int, stdin.readline().rstrip().split()))
operator = []
min_result = ""
max_result = ""

for i in range(4):
    for _ in range(operator_number[i]):
        operator.append(i)

operator_seqs = set(list(permutations(operator, len(operator))))

for operator_seq in operator_seqs:
    temp_result = numbers[0]
    for i in range(n-1):
        if operator_seq[i] == 0:  
            temp_result += numbers[i+1]
        elif operator_seq[i] == 1:
            temp_result -= numbers[i+1]
        elif operator_seq[i] == 2:
            temp_result *= numbers[i+1]
        else:
            temp_result = int(temp_result / numbers[i+1])
    #     print(temp_result)
    # print(temp_result, operator_seq)
    if max_result == "" and min_result == "":
        max_result = temp_result
        min_result = temp_result
    max_result = max(max_result, temp_result)
    min_result = min(min_result, temp_result)
print(max_result, min_result, sep = '\n')