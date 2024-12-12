from collections import defaultdict
from itertools import combinations

add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
in_grid = lambda a, w, h: 0 <= a[0] < h and 0 <= a[1] < w

data = open('input.txt').read().splitlines()

coords_map = defaultdict(set)
for r in range(len(data)):
  for c, ch in enumerate(data[r]):
    if ch != '.':
      coords_map[ch].add((r, c))

nodes = set()
for ch, coords  in coords_map.items():
  for a, b in combinations(coords, 2):
    dist = sub(a, b)
    for coord in (add(a, dist), sub(b, dist)):
      if in_grid(coord, len(data), len(data[0])):
        nodes.add(coord)
print(len(nodes))
