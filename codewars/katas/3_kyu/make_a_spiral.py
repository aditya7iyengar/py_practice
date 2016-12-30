def spiralize(size):
  if size == 0:
    return []
  elif size == 1:
    return [[1]]
  elif size == 2:
    return [[1,1],[0,1]]

  spr = [ [0 for x in range(size)] for y in range(size) ]

  x = y = 0

  dx, dy = 0, 1

  rotated = 0
  while rotated < 2:
    spr[x][y] = 1

    if moveable(spr, x, y, dx, dy):
      x += dx
      y += dy
      rotated = 0
    else:
      dx, dy = dy, -dx
      rotated += 1

  dx, dy = -dy, dx
  if spr[x + dx][y + dy] == 1:
      spr[x][y] = 0

  return spr

def moveable(map, x, y, dx, dy):
  n = len(map)
  x += dx
  y += dy

  if x < 0 or x >= n or y < 0 or y >= n:
    return False

  if map[x][y] == 1:
    return False

  x += dx
  y += dy

  if x < 0 or x >= n or y < 0 or y >= n:
    return True

  if map[x][y] == 1:
    return False

  return True
