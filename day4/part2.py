from itertools import permutations
with open('input', 'r') as f:
  passphrases = f.readlines()

passphrases = [r.strip() for r in passphrases]
n = 0

def has_double(s):
  seen = set()
  for w in s:
    if w in seen: return True
    seen.add(w)

def has_anagram(s):
  if s:
    perms = [''.join(p) for p in permutations(s[0])]
    for _ in perms:
      if _ in s[1:]: 
        return True
    return has_anagram(s[1:]) 

for l in passphrases:
  l = l.split()
  if not has_double(l): 
    if not has_anagram(l): n += 1

print(n)
