with open('input') as f:
  instructions = [int(p.strip()) for p in f.readlines()]

n, i = 0, 0

while i < len(instructions):
  prev_i = i
  i += instructions[i]
  if instructions[prev_i] >= 3:
    instructions[prev_i] -= 1 
  else:
    instructions[prev_i] += 1 
  n += 1

print(n)
