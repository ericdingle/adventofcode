import itertools

diff_pairs = lambda row: [y - x for x, y in itertools.pairwise(row)]

all_pos = lambda row: all(map(lambda x: x > 0, row))
all_neg = lambda row: all(map(lambda x: x < 0, row))
all_le3 = lambda row: all(map(lambda x: abs(x) <= 3, row))

is_safe = lambda row: all_le3(row) and (all_pos(row) or all_neg(row))


data = [map(int, line.split()) for line in open('input.txt')]
data = [*map(diff_pairs, data)]
print([is_safe(row) for row in data].count(True))


def row_subsets(row):
  rows = [row]
  for i in range(len(row)):
    rows.append(row[:i] + row[i+1:])
  return rows

data = [list(map(int, line.split())) for line in open('input.txt')]
data = [*map(row_subsets, data)]
data = [(diff_pairs(row) for row in rows) for rows in data]
data = [(is_safe(row) for row in rows) for rows in data]
print([any(row) for row in data].count(True))
