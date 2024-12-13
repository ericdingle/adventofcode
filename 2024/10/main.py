data = open('input2.txt').read().splitlines()
data = [*map(lambda row: [*map(int, list(row))], data)]
width, height = len(data[0]), len(data)

def score(r, c):
  i = data[r][c]
  if i == 9:
    return {(r, c)}

  s = set()
  for r2, c2 in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
    if 0 <= r2 < height and 0 <= c2 < width and data[r2][c2] == i + 1:
      s.update(score(r2, c2))
  return s

s = 0
for r, row in enumerate(data):
  for c, i in enumerate(row):
    if i == 0:
      s += len(score(r, c))
print(s)
