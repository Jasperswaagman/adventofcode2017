from itertools import cycle
mem_address = 347991
ram = [(0,0,1)]

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

def get_surrounding_coordinates(x,y):
  coords = [] 
  coords.append(go_l(x,y))
  coords.append(go_u(go_l(x,y)[0],go_l(x,y)[1]))
  coords.append(go_u(x,y))
  coords.append(go_u(go_r(x,y)[0],go_r(x,y)[1]))
  coords.append(go_r(x,y))
  coords.append(go_d(go_r(x,y)[0],go_r(x,y)[1]))
  coords.append(go_d(x,y))
  coords.append(go_d(go_l(x,y)[0],go_l(x,y)[1]))
  return coords

def init_ram(size):
  stepsize, n = 1, 1
  while True:
    for r in range(2):
      move = next(_moves)
      for _ in range(stepsize):
        ram.append(move(ram[-1][0],ram[-1][1]))
        surrounding_coords = get_surrounding_coordinates(ram[-1][0],ram[-1][1])
        value_sum = 0
        for s in surrounding_coords:
          true_surrounding_coords = [c for c in ram if c[0] == s[0] and c[1] == s[1]]
          if true_surrounding_coords: value_sum += true_surrounding_coords[0][2]
        print(value_sum)
        ram[-1] += (value_sum,)
        if value_sum >= mem_address:
          return
        n += 1
    stepsize += 1

init_ram(mem_address)
