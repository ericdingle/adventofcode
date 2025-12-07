import sys
import itertools

# Part 1.
ranges, invalid = open(sys.argv[1], 'r').read().split(','), 0
for r in ranges:
  left, right = map(int, r.split('-'))
  for i in range(left, right + 1):
    s = str(i)
    l = len(s)
    if s[:l//2] == s[l//2:]:
      invalid += i
print(invalid)

# Part 2.
ranges, invalid = open(sys.argv[1], 'r').read().split(','), set()
for r in ranges:
  left, right = map(int, r.split('-'))
  for i in range(left, right + 1):
    s = str(i)
    l = len(s)
    for size in range(1, l):
      if len(set([s[k:k+size] for k in range(0, l, size)])) == 1:
        invalid.add(i)
print(sum(invalid))
