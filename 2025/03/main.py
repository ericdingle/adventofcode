import sys

# Part 1.
lines, s = open(sys.argv[1], 'r'), 0
for line in lines:
  digits = list(map(int, line[:-1]))
  max_l, max_r = 0, 0
  for i in range(0, len(digits) - 1):
    if digits[i] > max_l:
      max_l, max_r = digits[i], digits[i+1]
    elif digits[i+1] > max_r:
      max_r = digits[i+1]
  s += max_l * 10 + max_r
print(s)

# Part 2.
lines, s = open(sys.argv[1], 'r'), 0
for line in lines:
  digits = list(map(int, line[:-1]))
  max_n = [0] * 12
  for i in range(0, len(digits) - 11):
    for j in range(12):
      if digits[i+j] > max_n[j]:
        max_n[j:] = digits[i+j:i+12]
        print(i, j, max_n)
  print(max_n)
  s += int(''.join(map(str, max_n)))
print(s)
