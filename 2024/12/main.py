data = open('input.txt').read().splitlines()
width, height = len(data[0]), len(data)

visited = set()

add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def get_score(r, c, ch):
  if (r, c) in visited:
    return (0, 0)
  visited.add((r, c))

  score = (1, 0)  # (area, perimeter)
  for r2, c2 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
    if r2 in (-1, height) or c2 in (-1, width) or data[r2][c2] != ch:
      score = add(score, (0, 1))
    else:
      score = add(score, get_score(r2, c2, ch))
  return score

s = 0
for r, row in enumerate(data):
  for c, ch in enumerate(row):
    if (r, c) in visited:
      continue

    score = get_score(r, c, ch)
    s += score[0] * score[1]
print(s)
