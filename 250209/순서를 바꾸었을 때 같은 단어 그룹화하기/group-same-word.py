from collections import defaultdict
n = int(input())
words = [input() for _ in range(n)]
cases = defaultdict(int)

for word in words:
    s = ''
    record = defaultdict(int) 
    for c in word:
        record[c] += 1
    keys = list(record.keys())
    keys.sort()
    for key in keys:
        s+=(record[key]*key)
    cases[s] += 1
print(max(cases.values()))