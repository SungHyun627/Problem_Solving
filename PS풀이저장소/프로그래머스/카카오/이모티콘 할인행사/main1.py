from itertools import product
inputs = [[[[40, 10000], [25, 10000]], [7000, 9000]], [[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900], ]]

def solution(users, emoticons):
  answer = [0, 0]
  n = len(emoticons)
  discountRates = [10, 20, 30, 40]
  
  for x in product(discountRates, repeat = n):
    membercnt, amount = 0, 0
    for user in users:
      uamount = 0
      ur, limit = user
      for i in range(n):
        cost = emoticons[i]
        if ur <= x[i]:
          uamount += int(cost * (100 - x[i]) // 100)
        if uamount > limit:
          break
      if uamount >= limit:
        membercnt += 1
      else:
        amount += uamount
    if membercnt < answer[0]:
      continue
    elif membercnt == answer[0]:
      if answer[1] < amount:
        answer[1] = amount
    else:
      answer[0], answer[1] = membercnt, amount
  return answer

for input in inputs:
  print(solution(*input))