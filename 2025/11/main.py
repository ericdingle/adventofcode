import functools
import itertools
import sys

# Part 1.
lines = open(sys.argv[1], 'r').read().splitlines()
lines = [line.split(': ') for line in lines]
data = {k: v.split(' ') for k, v in lines}

@functools.cache
def func(start, end):
  if start == end:
    return 1
  return sum(func(v, end) for v in data.get(start, []))

print(func(sys.argv[2], sys.argv[-1]))

# Part 2.
lines = open(sys.argv[1], 'r').read().splitlines()
lines = [line.split(': ') for line in lines]
data = {k: v.split(' ') for k, v in lines}

ops = [func(start, end) for start, end in itertools.pairwise(sys.argv[2:])]
print(functools.reduce(lambda x, y: x * y, ops, 1))
