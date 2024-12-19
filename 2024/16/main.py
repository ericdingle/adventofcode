from heapq import heappush, heappop

add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def get_score(filename):
  data = open(filename).read().splitlines()

  grid = {}
  for r, row in enumerate(data):
    for c, ch in enumerate(row):
      grid[(r, c)] = ch

  start = next(k for k, v in grid.items() if v == 'S')

  heap = []
  heappush(heap, (0, start, (0, 1)))  # score, pos, facing
  visited = {(start, (0, 1)): (1, {start})}  # (pos, facing): (min_score, set(tiles))

  while len(heap) != 0:
    score, pos, facing = heappop(heap)
    tiles = visited[(pos, facing)][1]

    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      new_pos = add(pos, dir)
      new_score = score + 1 + (0 if dir == facing else 1000)

      if (new_pos, dir) in visited:
        min_score, old_tiles = visited[(new_pos, dir)]
        if new_score == min_score:
          visited[(new_pos, dir)] = (min_score, old_tiles | tiles)
      elif grid[new_pos] != '#':
        visited[(new_pos, dir)] = (new_score, tiles | {new_pos})
        if grid[new_pos] != 'E':
          heappush(heap, (new_score, new_pos, dir))

  end = next(k for k, v in grid.items() if v == 'E')
  score, tiles = sorted(v for (pos, _), v in visited.items() if pos == end)[0]
  return score, len(tiles)

print(get_score('input.txt'))
print(get_score('input2.txt'))
#print(get_score('input3.txt'))
