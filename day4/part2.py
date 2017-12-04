from itertools import permutations
with open('smallinput', 'r') as f:
  passphrases = f.readlines()

passphrases = [r.strip() for r in passphrases]

def has_double(s):
  seen = set()
  for w in s:
    if w in seen: return
    seen.add(w)

def has_anagram(s):
  if s:
    perms = [''.join(p) for p in permutations(s[0])]
    for _ in perms:
      if _ in s[1:]: print('DAFUQ is dit'); return 1
    has_anagram(s[1:]) 

for l in passphrases:
  if not has_double(l.split()):
    print(has_anagram(l.split()))

