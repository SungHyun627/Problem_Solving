from collections import defaultdict
from itertools import combinations

friends_list = [["muzi", "ryan", "frodo", "neo"], ["joy", "brad", "alessandro", "conan", "david"], ["a", "b", "c"]]
gifts_list = [["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"],["a b", "b a", "c a", "a c", "a c", "c a"]]

## 1. A > B -> B => A 
## 2. 선물지수 큰 = 준선문 - 받은 선물


def solution(friends, gifts):
  give = defaultdict(dict)
  take = defaultdict(dict)
  result = defaultdict(int)

  for gift in gifts:
    a, b = gift.split()
    if b in give[a]:
      give[a][b] += 1
    else:
      give[a][b] = 1
    if a in take[b]:
      take[b][a] += 1
    else:
      take[b][a] = 1
    
    
  for x, y in combinations(friends, 2):
    g1 = give[x][y] if y in give[x] else 0
    g2 = give[y][x] if x in give[y] else 0
    if g1 > g2:
      result[x] += 1
    elif g1 < g2:
      result[y] += 1
    else:
      s1 = sum(give[x].values()) - sum(take[x].values())
      s2 = sum(give[y].values()) - sum(take[y].values())
      if s1 == s2:
        continue
      if s1 > s2:
        result[x] += 1
      else:
        result[y] += 1
  return max(result.values()) if result else 0

for i in range(len(friends_list)):
  print(solution(friends_list[i], gifts_list[i]))