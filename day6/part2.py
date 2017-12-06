mem = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
seen = []
seen.append(mem)
cycles, first_cycle = 0, 0

def malloc(mem):
  m = list(mem)
  i = m.index(max(m)) + 1
  if i == len(m): i = 0 
  blocks = max(m)
  m[m.index(max(m))] = 0
  while blocks > 0:
    m[i] += 1
    i += 1
    if (i == len(m)): i = 0
    blocks -= 1
  return m

while True:
  seen.append(malloc(seen[-1]))
  cycles += 1
  if seen.count(seen[-1]) > 2: break
  if seen.count(seen[-1]) == 2 and not first_cycle: first_cycle = cycles

print(cycles-first_cycle)
