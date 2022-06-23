#P1302 베스트셀러
from sys import stdin
from collections import defaultdict

stdin = open('./input.txt', 'r')
max_book_title = ''
max_sold_book_num = 0
n = int(stdin.readline())
sold_books = defaultdict(int)
for _ in range(n):
  sold_books[stdin.readline().rstrip()] += 1

for key in sold_books:
  if max_sold_book_num > sold_books[key]:
    continue
  elif max_sold_book_num == sold_books[key]:
    if key < max_book_title:
      max_book_title = key
  else:
    max_sold_book_num = sold_books[key]
    max_book_title = key

print(max_book_title)
