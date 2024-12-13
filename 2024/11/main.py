from functools import cache

data = [*map(int, open('input.txt').read().split())]

@cache
def func(input, depth):
  if depth == 0:
    return 1

  if input == 0:
    return func(1, depth - 1)
  elif len(s := str(input)) % 2 == 0:
    j = len(s) // 2
    return func(int(s[:j]), depth - 1) + func(int(s[j:]), depth - 1)
  else:
    return func(input * 2024, depth - 1)

print(sum(func(i, 6) for i in data))
print(sum(func(i, 25) for i in data))
print(sum(func(i, 75) for i in data))
