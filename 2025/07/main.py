import sys

# Part 1.
data = [*map(list, open(sys.argv[1], 'r').read().splitlines())]

s = data[0].index('S')
data[1][s] = '|'

total = 0
for r in range(2, len(data)-1, 2):
  for c in range(0, len(data[r])):
    if data[r-1][c] == '|':
      if data[r][c] == '^':
        total += 1
        data[r][c-1] = '|'
        data[r][c+1] = '|'
        data[r+1][c-1] = '|'
        data[r+1][c+1] = '|'
      else:
        data[r][c] = '|'
        data[r+1][c] = '|'
print(total)

# Part 2.
data = [*map(list, open(sys.argv[1], 'r').read().splitlines())]
data = [[*map(lambda c: 0 if c == '.' else c, row)] for row in data]

s = data[0].index('S')
data[1][s] = 1

for r in range(2, len(data)-1, 2):
  for c in range(0, len(data[r])):
    i = data[r-1][c]
    if type(i) is int and i > 0:
      if data[r][c] == '^':
        data[r][c-1] += i
        data[r][c+1] += i
        data[r+1][c-1] += i
        data[r+1][c+1] += i
      else:
        data[r][c] += i
        data[r+1][c] += i

print(sum(data[-1]))
