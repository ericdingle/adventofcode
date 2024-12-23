from collections import deque

add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def get_num_steps(filename, width, height, num_bytes):
  lines = open(filename).read().splitlines()[:num_bytes]
  bad_coords = [*map(lambda line: eval('(%s)' % line), lines)]

  q = deque([((0, 0), 0)])  # (x, y), steps
  visited = set()
  visited.update(bad_coords)
  while len(q):
    coord, steps = q.popleft()
    if coord == (width - 1, height - 1):
      return steps
    elif coord in visited or not (0 <= coord[0] < width and 0 <= coord[1] < height):
      continue
    visited.add(coord)

    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      q.append((add(coord, dir), steps + 1))

print(get_num_steps('input.txt', 7, 7, 12))
#print(get_num_steps('input2.txt', 71, 71, 1024))
