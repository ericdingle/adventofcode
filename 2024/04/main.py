from collections import defaultdict
import re

pattern = re.compile('XMAS')

data = open('input.txt').read().splitlines()

data_trans = [*map(lambda x: ''.join(x), zip(*data))]

data_diag1 = defaultdict(str)
for r in range(len(data)):
  for c in range(len(data[r])):
    data_diag1[r + c] += data[r][c]

MIN = len(data)
data_diag2 = defaultdict(str)
for r in range(len(data)):
  for c in range(len(data[r])):
    data_diag2[r - c + MIN] += data[r][c]

total = 0
for d in [data, data_trans, data_diag1.values(), data_diag2.values()]:
  total += sum(len(re.findall(pattern, row)) for row in d)
  total += sum(len(re.findall(pattern, row[::-1])) for row in d)
print(total)


s = 0
for r in range(1, len(data) - 1):
  for c in range(1, len(data[r]) - 1):
    if data[r][c] == 'A':
      a = data[r-1][c-1] + data[r-1][c+1] + data[r+1][c+1] + data[r+1][c-1]
      if a in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
        s += 1
print(s)
