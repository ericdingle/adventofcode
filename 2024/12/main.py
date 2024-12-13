from collections import defaultdict

data = open('input.txt').read().splitlines()
width, height = len(data[0]), len(data)

visited = set()

add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sub = lambda a, b: (a[0] - b[0], a[1] - b[1])

def get_score(r, c, ch):
  if (r, c) in visited:
    return (0, [])
  visited.add((r, c))

  score = (1, [])  # (area, edges/coords)
  for r2, c2 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
    if r2 in (-1, height) or c2 in (-1, width) or data[r2][c2] != ch:
      edge = sub((r2, c2), (r, c))
      coord = (c, r) if edge[0] == 0 else (r, c)
      score = add(score, (0, [(*edge, *coord)]))
    else:
      score = add(score, get_score(r2, c2, ch))
  return score

def get_num_edges(edges):
  d = defaultdict(list)
  for e1, e2, i, j in edges:
    d[(e1, e2, i)].append(j)

  s = 0
  for vals in d.values():
    vals = sorted(vals)
    s += [y - x > 1 for x, y in zip(vals, vals[1:])].count(True) + 1
  return s

s, s2 = 0, 0
for r, row in enumerate(data):
  for c, ch in enumerate(row):
    if (r, c) in visited:
      continue

    score = get_score(r, c, ch)
    s += score[0] * len(score[1])
    s2 += score[0] * get_num_edges(score[1])
print(s)
print(s2)
