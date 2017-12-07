with open('input') as f:
  program = [l.strip() for l in f.readlines()]
  t = [p.split() for p in program]

# we don't need the weight for now
for _ in t:
  del _[1]

n = []
for x in t:
  n.append(x[0])

for _ in t:
  if len(_) > 1:
    for p in _[2:]:
      n.remove(p.rstrip(','))

print(n[0])
