import re

pattern = re.compile(r'X[+=](\d+), Y[+=](\d+)')

lines = open('input.txt').read().splitlines() + ['']
entries = []
for line1, line2, line3, _ in (lines[i:i+4] for i in range(0, len(lines), 4)):
  n = []
  for line in (line1, line2, line3):
    n.extend([*re.search(pattern, line).group(1, 2)])
  n = [*map(int, n)]
  entries.append(n)

def get_score(add_to_prize):
  s = 0
  for x1, y1, x2, y2, x3, y3 in entries:
    # x1*a + x2*b = x3
    # y1*a + y2*b = y3

    x3, y3 = x3 + add_to_prize, y3 + add_to_prize

    num = (x3 * y1 - x1 * y3)
    den = (x2 * y1 - x1 * y2)
    if num % den == 0:
      b = num // den
      a = (x3 - x2 * b) // x1
      s += 3 * a + b
  return s

print(get_score(0))
print(get_score(10000000000000))
