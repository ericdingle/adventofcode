from collections import defaultdict
import re

first, second = open('input.txt').read().split('\n\n')

first = [*map(int, re.split('\||\n', first))]

deps = defaultdict(list)
for a, b in [*zip(first[0::2], first[1::2])]:
  deps[b].append(a)

def topo_sort(nodes: set):
  ordered, visited, visiting = [], set(), set()
  def visit(node):
    if node in visited:
      return
    if node in visiting:
      raise Exception('cycle')

    visiting.add(node)

    for dep in deps[node]:
      if dep in nodes:
        visit(dep)

    visiting.remove(node)
    visited.add(node)
    ordered.append(node)
  for node in nodes:
    visit(node)
  return ordered

tests = [*map(lambda x: [*map(int, x.split(','))], second.splitlines())]

s1, s2 = 0, 0
for test in tests:
  ordered = topo_sort(set(test))
  if all(ordered.index(a) < ordered.index(b) for a, b in zip(test, test[1:])):
    s1 += test[len(test)//2]
  else:
    s2 += ordered[len(ordered)//2]
print(s1)
print(s2)
