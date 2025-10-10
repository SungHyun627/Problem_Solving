from itertools import product
inputs = [[[7, 42, 5]], [[63, 111, 95]]]

### 포화 이진 트리 길이 맞추기
def getFullBtlength(length):
  full_length = 1
  while full_length < length:
    full_length = 2*full_length +1
  return full_length

### 완전 이진 포화 트리가 가능한지
def is_possible(tree):
  
  if len(tree) == 1:
    return True
  mid = len(tree) // 2
  root = tree[mid]
  left = tree[:mid]
  right = tree[mid+1:]

  if root == '0' and ('1' in left or '1' in right):
    return False
  return is_possible(left) and is_possible(right)


def solution(numbers):
  answer = []

  for number in numbers:
    binStr = bin(number)[2:]
    full_length = getFullBtlength(len(binStr))
    binStr = binStr.zfill(full_length)

    answer.append(1 if is_possible(binStr) else 0)
  
  return answer

for input in inputs:
  print(solution(*input))