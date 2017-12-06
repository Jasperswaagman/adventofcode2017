import sys, time
sys.setrecursionlimit(30000)
mem = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
seen = [mem]
cycles = 0

def malloc(mem, cycles):
  if seen.count(seen[-1]) > 1: return cycles
  m = list(mem); h = m.index(max(m)) # Get index of highest mem bank
  # Set index to +1 or jump back to index 0
  i = 0 if h == (len(m) - 1) else (h + 1)
  blocks = max(m)
  m[h] = 0
  while blocks > 0:
    m[i] += 1
    i += 1
    if (i == len(m)): i = 0
    blocks -= 1
  cycles += 1
  seen.append(m)
  return malloc(seen[-1], cycles)

print(malloc(mem, cycles))
