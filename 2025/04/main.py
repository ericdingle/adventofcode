import sys

# Part 1.
data = open(sys.argv[1], 'r').read().splitlines()
w, h = len(data[0]), len(data)

data.insert(0, [''] * w)
data.append([''] * w)
data = [[0] + list(map(lambda c: 1 if c == '@' else 0, row)) + [0] for row in data]

total = 0
for r in range(1, h+1):
  for c in range(1, w+1):
    if data[r][c] == 1 and sum(data[r-1][c-1:c+2]) + data[r][c-1] + data[r][c+1] + sum(data[r+1][c-1:c+2]) < 4:
      total += 1
print(total)

# Part 1.
data = open(sys.argv[1], 'r').read().splitlines()
w, h = len(data[0]), len(data)

data.insert(0, [''] * w)
data.append([''] * w)
data = [[0] + list(map(lambda c: 1 if c == '@' else 0, row)) + [0] for row in data]

total = 0
while True:
  coords = set([])
  for r in range(1, h+1):
    for c in range(1, w+1):
      if data[r][c] == 1 and sum(data[r-1][c-1:c+2]) + data[r][c-1] + data[r][c+1] + sum(data[r+1][c-1:c+2]) < 4:
        total += 1
        coords.add((r, c))
  if not len(coords):
    break
  for (r, c) in coords:
    data[r][c] = 0
print(total)
