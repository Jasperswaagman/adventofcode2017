from itertools import cycle
mem_address = 347991

def go_r(x,y):
  return x+1,y

def go_u(x,y):
  return x,y+1

def go_l(x,y):
  return x-1,y

def go_d(x,y):
  return x,y-1

moves = [go_r, go_u, go_l, go_d]
_moves = cycle(moves)
ram = [[0,0],[0,0]]

def init_ram(size):
  stepsize, n = 1, 0
  while True:
    for r in range(2):
      move = next(_moves)
      for _ in range(stepsize):
        ram.append(move(ram[-1][0],ram[-1][1]))
        if n >= mem_address:
          return
        n += 1
    stepsize += 1

init_ram(mem_address)
print((abs(ram[mem_address][0]) - abs(ram[0][0])) + (abs(ram[mem_address][1]) - abs(ram[0][1])))
