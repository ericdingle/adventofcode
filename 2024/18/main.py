from collections import deque

add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def get_num_steps(bad_coords, width, height):
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

def part1(filename, width, height, num_bytes):
  lines = open(filename).read().splitlines()[:num_bytes]
  bad_coords = [*map(lambda line: eval('(%s)' % line), lines)]
  return get_num_steps(bad_coords, width, height)

print(part1('input.txt', 7, 7, 12))
#print(part1('input2.txt', 71, 71, 1024))

def part2(filename, width, height):
  lines = open(filename).read().splitlines()
  bad_coords = [*map(lambda line: eval('(%s)' % line), lines)]

  l, r = 0, len(bad_coords) - 1
  while True:
    m = (l + r) // 2
    steps1 = get_num_steps(bad_coords[:m], width, height)
    steps2 = get_num_steps(bad_coords[:m+1], width, height)
    if steps1 and steps2:
      l = m + 1
    elif steps1:
      return bad_coords[m]
    else:
      r = m

print(part2('input.txt', 7, 7))
#print(part2('input2.txt', 71, 71))
