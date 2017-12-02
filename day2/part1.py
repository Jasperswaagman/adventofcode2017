import re
with open ('input', 'r') as f:
  spreadsheet = f.readlines()

spreadsheet = [r.strip() for r in spreadsheet]
spreadsheet = [re.split(r' +',c) for c in spreadsheet]
checksum = []

for r in spreadsheet:
  rows = list(map(int, r))
  checksum.append(max(rows) - min(rows))

print(sum(checksum))
