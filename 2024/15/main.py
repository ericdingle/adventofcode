def index_of(haystack, needle, start, end, step):
  for i in range(start, end, step):
    if haystack[i] == needle:
      return i
  return -1

def get_score(filename):
  grid, moves = open(filename).read().split('\n\n')

  grid = grid.splitlines()
  grid = [*map(list, grid)]
  width, height = len(grid[0]), len(grid)

  moves = ''.join(moves.split('\n'))

  for move in moves:
    r, c = next((r, row.index('@')) for r, row in enumerate(grid) if '@' in row)
    row = grid[r]
    col = [row[c] for row in grid]

    if move == '<':
      wall = index_of(row, '#', c, -1, -1)
      empty = index_of(row, '.', c, wall, -1)
      if empty == -1:
        continue
      for i in range(empty, c):
        grid[r][i] = grid[r][i+1]
      grid[r][c] = '.'

    elif move == '>':
      wall = index_of(row, '#', c, width, 1)
      empty = index_of(row, '.', c, wall, 1)
      if empty == -1:
        continue
      for i in range(empty, c, -1):
        grid[r][i] = grid[r][i-1]
      grid[r][c] = '.'

    elif move == '^':
      wall = index_of(col, '#', r, -1, -1)
      empty = index_of(col, '.', r, wall, -1)
      if empty == -1:
        continue
      for i in range(empty, r):
        grid[i][c] = grid[i+1][c]
      grid[r][c] = '.'

    elif move == 'v':
      wall = index_of(col, '#', r, height, 1)
      empty = index_of(col, '.', r, wall, 1)
      if empty == -1:
        continue
      for i in range(empty, r, -1):
        grid[i][c] = grid[i-1][c]
      grid[r][c] = '.'

  s = 0
  for r, row in enumerate(grid):
    for c, ch in enumerate(row):
      if ch == 'O':
        s += 100 * r + c
  return s

print(get_score('input.txt'))
print(get_score('input2.txt'))
#print(get_score('input3.txt'))
