import heapq
import itertools
import math
import sys

# Part 1.
data = open(sys.argv[1], 'r').read().splitlines()
data = [*map(lambda x: tuple(map(int, x.split(','))), data)]

heap = []
for l, r in itertools.combinations(data, 2):
  dist = math.sqrt((l[0]-r[0])**2 + (l[1]-r[1])**2 + (l[2]-r[2])**2)
  heapq.heappush(heap, (dist, l, r))

m = {}
for i in range(int(sys.argv[2])):
  dist, l, r = heapq.heappop(heap)
  l_set = m.get(l, frozenset([l]))
  r_set = m.get(r, frozenset([r]))

  new_set = l_set | r_set
  for coord in new_set:
    m[coord] = new_set

a, b, c = heapq.nlargest(3, [len(x) for x in set(m.values())])
print(a * b * c)

# Part 2.
data = open(sys.argv[1], 'r').read().splitlines()
data = [*map(lambda x: tuple(map(int, x.split(','))), data)]

heap = []
for l, r in itertools.combinations(data, 2):
  dist = math.sqrt((l[0]-r[0])**2 + (l[1]-r[1])**2 + (l[2]-r[2])**2)
  heapq.heappush(heap, (dist, l, r))

m = {}
while True:
  dist, l, r = heapq.heappop(heap)
  l_set = m.get(l, frozenset([l]))
  r_set = m.get(r, frozenset([r]))

  new_set = l_set | r_set
  for coord in new_set:
    m[coord] = new_set

  if len(new_set) == len(data):
    print(l[0] * r[0])
    break
