"""
  - 각 privacie 만료일 구하기
  - 만만료된 privacy 찾기
  - 오름차순 정렬
    32
"""

def calc_due_date(year, month, date, term):
    dy, dm, dd = -1, -1, date
    
    if (month + term) > 12:
        x, y = (month + term) // 12, (month+term) % 12
        if y == 0:
            dm = 12
            dy = year + x - 1
        else:
            dm = y
            dy = year + x
    else:
        dy, dm = year, (month + term)
    print(dy, dm, dd)
    if dd == 1:
        dd = 28
        if dm == 1:
            dy -= 1
            dm = 12
        else:
            dm -= 1
    else:
        dd -= 1
    return dy, dm, dd

def solution(today, terms, privacies):
    
    answer = []
        
    ty, tm, td = map(int, today.split('.'))
    dues = dict()
    
    for term in terms:
        name, period = term.split(' ')
        dues[name] = int(period)
        
    for i in range(len(privacies)):
        p_date, name = privacies[i].split(' ')
        py, pm, pd = map(int, p_date.split('.'))
        pdy, pdm, pdd = calc_due_date(py, pm, pd, dues[name])
        print(ty, tm, td, pdy, pdm, pdd)
        
        if (pdy > ty):
            continue
        
        if (pdy == ty and pdm > tm):
            continue
        
        if (pdy == ty and pdm == tm and pdd >= td):
            continue

        answer.append(i+1)
    answer.sort()
    
    return answer