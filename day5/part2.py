with open('smallinput') as f:
  instructions = [int(p.strip()) for p in f.readlines()]

n = 0
i = instructions[0]

while i < len(instructions):
  prev_i = i
  i += instructions[i]
  if instructions[prev_i] > 2:
    instructions[prev_i] -= 1 
  else:
    instructions[prev_i] += 1 
  n += 1

print(n)
