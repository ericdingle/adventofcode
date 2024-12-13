from collections import defaultdict
from itertools import combinations

add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
in_grid = lambda a, w, h: 0 <= a[0] < h and 0 <= a[1] < w

data = open('input.txt').read().splitlines()
width, height = len(data[0]), len(data)

coords_map = defaultdict(set)
for r in range(len(data)):
  for c, ch in enumerate(data[r]):
    if ch != '.':
      coords_map[ch].add((r, c))

def get_num_nodes(harmonics):
  nodes = set()
  for ch, coords  in coords_map.items():
    for a, b in combinations(coords, 2):
      dist = sub(a, b)

      candidates = [a, b] if harmonics else []
      num_iters = min(height // abs(dist[0]), width // abs(dist[1])) if harmonics else 1

      for candidate, func in ((a, add), (b, sub)):
        for i in range(num_iters):
          candidate = func(candidate, dist)
          candidates.append(candidate)

      for coord in candidates:
        if in_grid(coord, width, height):
          nodes.add(coord)
  return len(nodes)

print(get_num_nodes(False))
print(get_num_nodes(True))
