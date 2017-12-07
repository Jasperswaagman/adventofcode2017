with open('smallinput') as f:
  program = [l.strip() for l in f.readlines()]
  t = [p.split() for p in program]

n, m = [], []
for x in t:
  n.append(x[:2])
  m.append(x[0]) # How does one get list by value

for _ in n:
  _[1] = int(_[1][1:-1])

for _, p in enumerate(t):
  if len(p) > 2: 
    for i in p[3:]:
      # get index of found value
      index = m.index(i.rstrip(','))
      n[_].append(n[index])

for _ in n:
  print(_) 

# TODO: learn the shit about iterators, generators, yield and itertools.
