inputs = [["2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]], ["2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]]]

def isExpired(today, dueDate):
  return today[0] > dueDate[0] or (today[0] == dueDate[0] and today[1] > dueDate[1]) or (today[0] == dueDate[0] and today[1] == dueDate[1] and today[2] > dueDate[2])

def getYMD(date):
  return list(map(int, date.split('.')))

def calcExpiredDate(date, period):
  year, month, day = date
  nm = (month + period) % 12 if (month + period) % 12 != 0 else 12
  ny = year + (month + period) // 12 if (month + period) % 12 != 0 else year + (month + period) // 12 -1
  nd = day-1
  if nd == 0:
    nd = 28
    nm -= 1
    if nm == 0:
      nm = 12
      ny -= 1
  return [ny, nm, nd]


def solution(today, terms, privacies):
  result = []
  term = dict()
  for t in terms:
    x, y = t.split()
    term[x] = int(y)

  tymd = getYMD(today)

  for i in range(len(privacies)):
    d, t = privacies[i].split()
    pymd = getYMD(d)
    period = term[t]
    expiredymd = calcExpiredDate(pymd, period)
    
    if isExpired(tymd, expiredymd):
      result.append(i+1)  
  return result

for input in inputs:
  print(solution(*input))