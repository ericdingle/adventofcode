import functools
import itertools
import sys

# Part 1.
lines = open(sys.argv[1], 'r').read().splitlines()
data = [tuple(map(int, line.split(','))) for line in lines]

result = 0
for l, r in itertools.combinations(data, 2):
  result = max(result, (abs(l[0] - r[0]) + 1) * (abs(l[1] - r[1]) + 1))
print(result)

# Part 2.
lines = open(sys.argv[1], 'r').read().splitlines()
data = [tuple(map(int, line.split(','))) for line in lines]

xs = [(key, sorted(x[1] for x in group)) for key, group in itertools.groupby(sorted(data), key=lambda x: x[0])]
ys = [(key, sorted(x[0] for x in group)) for key, group in itertools.groupby(sorted(data, key=lambda x: x[1]), key=lambda x: x[1])]
print(xs)
print(ys)
