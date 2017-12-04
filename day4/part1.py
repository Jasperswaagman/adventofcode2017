with open('input', 'r') as f:
  passphrases = f.readlines()

passphrases = [r.strip() for r in passphrases]
n = 0

def double(s):
  global n
  seen = set()
  for w in s.split():
    if w in seen: return
    seen.add(w)

  n += 1 

for l in passphrases:
  double(l)

print(n)
