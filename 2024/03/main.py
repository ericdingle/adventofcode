import re

pattern1 = re.compile(r'mul\((\d+),(\d+)\)')
matches = re.findall(pattern1, open('input.txt').read())
print(sum(int(a) * int(b) for (a, b) in matches))

pattern2 = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
matches = re.findall(pattern2, open('input.txt').read())

s, enabled = 0, True
for match in matches:
  if match == 'do()':
    enabled = True
  elif match == "don't()":
    enabled = False
  elif match[:3] == 'mul' and enabled:
    match2 = re.match(pattern1, match)
    s += int(match2.group(1)) * int(match2.group(2))
print(s)
