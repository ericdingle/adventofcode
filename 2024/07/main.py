from itertools import combinations

lines = open('input.txt').read().splitlines()
tests = [*map(lambda x: x.split(': '), lines)]
tests = [*map(lambda x: (int(x[0]), [*map(int, x[1].split(' '))]), tests)]

def run(pipe_operator):
  s = 0
  for value, operands in tests:
    t = [operands[0]]
    for operand in operands[1:]:
      t = (
        [x + operand for x in t] +
        [x * operand for x in t] +
        ([int(str(x) + str(operand)) for x in t] if pipe_operator else [])
      )
    if value in t:
      s += value
  return s

print(run(False))
print(run(True))
