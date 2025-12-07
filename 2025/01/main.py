import sys

# Part 1.
pos, zeroes = 50, 0
for line in open(sys.argv[1], 'r'):
  dir, dist = line[0], int(line[1:])
  pos += -dist if dir == 'L' else dist
  pos %= 100
  if pos == 0:
    zeroes += 1
print(zeroes)

# Part 2.
pos, zeroes = 50, 0
for line in open(sys.argv[1], 'r'):
  dir, dist = line[0], int(line[1:])

  dist_to_zero = 100 if pos == 0 else (pos if dir == 'L' else 100 - pos)

  pos += -dist if dir == 'L' else dist
  pos %= 100

  if dist >= dist_to_zero:
    zeroes += 1
    dist -= dist_to_zero
    zeroes += dist // 100
print(zeroes)
