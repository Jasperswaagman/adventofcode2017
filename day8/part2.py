import operator
with open('input') as f:
  instructions = [r.strip() for r in f.readlines()]
  instructions = [ _.split() for _ in instructions]

max_register = 0
dinstructions = {}
for i in instructions:
  dinstructions[i[0]] = 0

ops = {
  '+': operator.add,
  'inc': operator.add,
  '-': operator.sub,
  'dec': operator.sub,
  '>': operator.gt,
  '>=': operator.ge,
  '<': operator.lt,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne }

for ins in instructions:
  if ops[str(ins[5])](dinstructions[str(ins[4])],int(ins[6])): 
    dinstructions[ins[0]] = ops[str(ins[1])](dinstructions[ins[0]],int(ins[2]))
  for _ in dinstructions:
    if dinstructions[_] > max_register: max_register = dinstructions[_]

print(max_register)
