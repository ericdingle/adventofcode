from collections import defaultdict
import copy

def get_num_moves(grid):
  height = len(grid)
  width = len(grid[0])
  visited = defaultdict(set)

  guard = (0, 0)
  for r, row in enumerate(grid):
    c = next((i for i in range(width) if row[i] == '^'), -1)
    if c != -1:
      guard = (r, c)
      break

  while True:
    r, c = guard
    ch = grid[r][c]

    if ch in visited[guard]:
      return -1
    visited[guard].add(ch)

    if ch == '^':
      r2 = next((i for i in range(r-1, -1, -1) if grid[i][c] == '#'), -1)
      for i in range(r2+1, r+1):
        grid[i][c] = 'X'
      if r2 == -1:
        break
      grid[r2+1][c] = '>'
      guard = (r2+1, c)

    elif ch == '>':
      c2 = next((i for i in range(c+1, width) if grid[r][i] == '#'), width)
      for i in range(c, c2):
        grid[r][i] = 'X'
      if c2 == width:
        break
      grid[r][c2-1] = 'v'
      guard = (r, c2-1)

    elif ch == 'v':
      r2 = next((i for i in range(r+1, height) if grid[i][c] == '#'), height)
      for i in range(r, r2):
        grid[i][c] = 'X'
      if r2 == height:
        break
      grid[r2-1][c] = '<'
      guard = (r2-1, c)

    elif ch == '<':
      c2 = next((i for i in range(c-1, -1, -1) if grid[r][i] == '#'), -1)
      for i in range(c2+1, c+1):
        grid[r][i] = 'X'
      if c2 == -1:
        break
      grid[r][c2+1] = '^'
      guard = (r, c2+1)

  return sum(row.count('X') for row in grid)

data = open('input.txt').read().splitlines()
data = [*map(list, data)]

print(get_num_moves(data))

data = open('input.txt').read().splitlines()
data = [*map(list, data)]

s = 0
for r in range(len(data)):
  for c in range(len(data[0])):
    if data[r][c] in ('#', '^'):
      continue
    data_copy = copy.deepcopy(data)
    data_copy[r][c] = '#'
    if get_num_moves(data_copy) == -1:
      s += 1
print(s)
