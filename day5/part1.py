with open('smallinput') as f:
  instructions = [int(p.strip()) for p in f.readlines()]

n = 0
i = instructions[0]

while i < len(instructions):
  prev_i = i
  i += instructions[i]
  instructions[prev_i] += 1 
  print(instructions)
  n += 1

print(n)
