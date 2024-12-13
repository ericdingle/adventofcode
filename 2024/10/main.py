from time import time

data = open('input.txt').read().splitlines()
data = [*map(lambda row: [*map(int, list(row))], data)]
width, height = len(data[0]), len(data)

def score(r, c, distinct):
  i = data[r][c]
  if i == 9:
    return {(r, c, time())} if distinct else {(r, c)}

  s = set()
  for r2, c2 in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
    if 0 <= r2 < height and 0 <= c2 < width and data[r2][c2] == i + 1:
      s.update(score(r2, c2, distinct))
  return s

def run(distinct):
  s = 0
  for r, row in enumerate(data):
    for c, i in enumerate(row):
      if i == 0:
        s += len(score(r, c, distinct))
  return s

print(run(False))
print(run(True))
