import csv
import random

words: set[str] = set([])

with open('data/cards.csv', mode='r', encoding='utf-8', newline='\n') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    names = [row[0] for row in reader]

temp = []
for name in names:
    temp += name.split(' ')

words = set([x.capitalize() for x in temp if x.isascii() and x.isalpha() and 5 < len(x) < 10])
with open('seed_word_tbl.py', 'w') as f:
    f.write(f'word_tbl = {list(words)}')

test = ''.join(random.choices(list(words), k=3))
print(test)