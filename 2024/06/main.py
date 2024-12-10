data = open('input.txt').read().splitlines()
data = [*map(list, data)]
height = len(data)
width = len(data[0])

guard = (0, 0)
for r, row in enumerate(data):
  c = next((i for i in range(width) if row[i] == '^'), -1)
  if c != -1:
    guard = (r, c)
    break

while True:
  r, c = guard
  ch = data[r][c]

  if ch == '^':
    r2 = next((i for i in range(r-1, -1, -1) if data[i][c] == '#'), -1)
    for i in range(r2+1, r+1):
      data[i][c] = 'X'
    if r2 == -1:
      break
    data[r2+1][c+1] = '>'
    guard = (r2+1, c+1)

  elif ch == '>':
    c2 = next((i for i in range(c+1, width) if data[r][i] == '#'), width)
    for i in range(c, c2):
      data[r][i] = 'X'
    if c2 == width:
      break
    data[r+1][c2-1] = 'v'
    guard = (r+1, c2-1)

  elif ch == 'v':
    r2 = next((i for i in range(r+1, height) if data[i][c] == '#'), height)
    for i in range(r, r2):
      data[i][c] = 'X'
    if r2 == height:
      break
    data[r2-1][c-1] = '<'
    guard = (r2-1, c-1)

  elif ch == '<':
    c2 = next((i for i in range(c-1, -1, -1) if data[r][i] == '#'), -1)
    for i in range(c2+1, c+1):
      data[r][i] = 'X'
    if c2 == -1:
      break
    data[r-1][c2+1] = '^'
    guard = (r-1, c2+1)

print(sum(row.count('X') for row in data))
