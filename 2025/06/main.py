from functools import reduce
import sys

# Part 1.
data = open(sys.argv[1], 'r').read().splitlines()

nums = [*map(lambda row: [*map(int, row.split())], data[:-1])]
ops = data[-1].split()

total = 0
for i, op in enumerate(ops):
  operands = [row[i] for row in nums]
  total += sum(operands) if op == '+' else reduce(lambda x, y: x * y, operands, 1)
print(total)

# Part 2.
data = open(sys.argv[1], 'r').read().splitlines()
nums = data[:-1]
ops = data[-1]

op, cur, total = '', 0, 0
for i in range(len(ops)+1):
  try:
    operand = int(''.join(str(row[i]) for row in nums))
  except:
    total += cur
    continue

  if ops[i] != ' ':
    op = ops[i]
    cur = operand
  else:
    cur = cur + operand if op == '+' else cur * operand
print(total)
