from itertools import combinations, product
from bisect import bisect_left
dice1 = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
dice2 = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
dice3 = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
dices = [dice1, dice2, dice3]

def solution(dice):
  n = len(dice)
  dice_idx = [i for i in range(n)]
  ans = []
  maxCnt = 0
  for a in combinations(dice_idx, n // 2):
    b = tuple(set(dice_idx) - set(a))
    winCnt = 0
    sumA = [sum(x) for x in product(*[dice[i] for i in a])]
    sumB = [sum(x) for x in product(*[dice[i] for i in b])]
    sumB.sort()
    for x in sumA:
      winCnt += bisect_left(sumB, x)
    if winCnt > maxCnt:
      maxCnt = winCnt
      ans = [i+1 for i in a]
  return ans

for dice in dices:
  print(solution(dice))