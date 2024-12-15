import re

pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

def get_robots(filename):
  robots = []
  for line in open(filename).read().splitlines():
    match = re.search(pattern, line)
    robots.append([*map(int, match.group(1, 2, 3, 4))])
  return robots

def get_grid(robots, width, height):
  grid = [[0] * width for i in range(height)]
  for x, y, _, _ in robots:
    grid[y][x] += 1
  return grid

def get_factor(filename, width, height):
  robots = get_robots(filename)

  for i in range(100):
    for robot in robots:
      x, y, vx, vy = robot
      x = (x + vx) % width
      y = (y + vy) % height
      robot[0], robot[1] = x, y

  grid = get_grid(robots, width, height)

  p = 1
  for x1, x2 in [(0, width//2), (width//2+1, width)]:
    for y1, y2 in [(0, height//2), (height//2+1, height)]:
      p *= sum(sum(slice[x1:x2]) for slice in grid[y1:y2])
  return p

print(get_factor('input.txt', 11, 7))
#print(get_factor('input2.txt', 101, 103))
