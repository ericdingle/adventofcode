from heapq import heappush, heappop

add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def get_score(filename):
  data = open(filename).read().splitlines()

  grid = {}
  for r, row in enumerate(data):
    for c, ch in enumerate(row):
      grid[(r, c)] = ch

  start = next(k for k, v in grid.items() if v == 'S')

  visited = {start}
  h = []
  heappush(h, (0, start, (0, 1)))  # score, pos, facing

  while len(h) != 0:
    score, pos, facing = heappop(h)
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      neighbor = add(pos, dir)
      if not neighbor in visited and grid[neighbor] != '#':
        visited.add(neighbor)
        score2 = score + 1 + (0 if dir == facing else 1000)
        if grid[neighbor] == 'E':
          return score2
        heappush(h, (score2, neighbor, dir))

print(get_score('input.txt'))
print(get_score('input2.txt'))
#print(get_score('input3.txt'))
