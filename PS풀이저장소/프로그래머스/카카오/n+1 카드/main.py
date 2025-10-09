inputs = [[4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]],[3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]], [2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]], [10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]]

def matching(cards, target):
  for i in range(len(cards)):
    if (target - cards[i]) in cards:
      return cards[i], target-cards[i]
  return -1, -1

def solution(coin, cards):
  n = len(cards)
  idx = n//3
  a, b = [*cards[:(n//3)]], []
  round = 1
  while idx < n:
    c1, c2 = cards[idx: idx+2]
    p1, p2 = matching(a, n+1)
    ## a에 이미 짝이 있을 때
    if p1 != -1:
      a.remove(p1)
      a.remove(p2)
      b.append(c1)
      b.append(c2)
      round += 1
      idx += 2
      continue
    ## 코인이 없을 때 
    if coin == 0:
      break
    b.append(c1)
    b.append(c2)
    ## a에 있는 카드와 b에 있는 카드가 pair일 때 
    p3, p4 = -1, -1
    for i in a:
      if (n+1 - i) in b:
        p3, p4 = i, n+1-i
        break
      
    if p3 != -1:
      coin -=1
      a.remove(p3)
      b.remove(p4)
      round += 1
      idx += 2
      continue

    if coin < 2:
      break
    p5, p6 = matching(b, n+1)
    if p5 == -1 or coin < 2:
      break
    coin -=2
    b.remove(p5)
    b.remove(p6)
    round += 1
    idx += 2    
  return round

for input in inputs:
  print(solution(input[0], input[1]))