with open('input') as f:
  program = [l.strip() for l in f.readlines()]

[print(p) for p in program]

# we put every program in a long list: A dict with the program name and weight
# Then we go through the list again and for every name we see that is ontop of another program we add that one to the dict of the program below it
