def convert_table_to_set(table):

    ni = len(table)
    nj = len(table[0])

    s = set()
    for i in range(ni):
      for j in range(nj):
        if table[i][j] == 1:
          s.add((i,j))

    return s

def convert_set_to_table(s):

  if not set:
    mi = mj = ni = nj = 0
  else:
    mi = min(map(lambda x: x[0], s))
    mj = min(map(lambda x: x[1], s))
    ni = max(map(lambda x: x[0], s))
    nj = max(map(lambda x: x[1], s))

  table = [[0 for j in range(nj-mj+1)] for i in range(ni-mi+1)]

  for (i,j) in s:
    table[i-mi][j-mj] = 1

  return table

  from itertools import product

def get_generation(cells, generations):

  cells = convert_set_to_dict(cells)

  for n in range(generations):

    cells_neigh = set()
    cells_new = set()

    for (i,j) in cells:
      for (di, dj) in product((-1,0,1), (-1,0,1)):
        cells_neigh.add((i+di,j+dj))

    for (i,j) in cells_neigh:
      neighbours = 0
      for (di, dj) in product((-1,0,1), (-1,0,1)):
        if (i+di,j+dj) in cells and (di,dj) != (0,0):
          neighbours += 1

      if neighbours == 3:
        cells_new.add((i,j))
      elif neighbours == 2 and (i,j) in cells:
        cells_new.add((i,j))

    cells = cells_new

  return convert_set_to_table(cells)
