import re, itertools
with open ('input', 'r') as f:
  spreadsheet = f.readlines()

spreadsheet = [r.strip().split() for r in spreadsheet]
total = 0

for r in spreadsheet:
  r = list(map(int,r)) 
  for x,y in itertools.combinations(r, 2):
    if (x % y == 0 or y % x == 0):
      total += max(x,y)//(min(x,y))

print(total)
