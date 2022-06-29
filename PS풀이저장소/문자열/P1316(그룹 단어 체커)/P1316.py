from sys import stdin 

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
answer = 0

def is_group_word(s):
  t = set()
  prev_char = ''
  for i in range(len(s)):
    if not prev_char:
      t.add(s[i])
      prev_char = s[i]
    else:
      if prev_char == s[i]:
        continue
      else:
        if s[i] in t:
          return False
        else:
          t.add(s[i])
          prev_char = s[i]
  return True

for _ in range(n):
  a = stdin.readline().rstrip()
  if is_group_word(a):
    answer += 1
print(answer)