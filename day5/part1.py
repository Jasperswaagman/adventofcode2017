with open('input') as f:
  instructions = [int(p.strip()) for p in f.readlines()]

steps, i = 0, 0

while i < len(instructions):
  prev_i = i
  i += instructions[i]
  instructions[prev_i] += 1 
  steps += 1

print(steps)
