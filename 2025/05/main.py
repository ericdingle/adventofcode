import sys

# Part 1.
data = open(sys.argv[1], 'r').read()
ranges, nums = data.split('\n\n')

ranges = [tuple(map(int, range.split('-'))) for range in ranges.splitlines()]
nums = list(map(int, nums.splitlines()))

x = set()
for num in nums:
  for l, r in ranges:
    if l <= num <= r:
      x.add(num)
print(len(x))

# Part 2.
data = open(sys.argv[1], 'r').read()
ranges, _ = data.split('\n\n')

ranges = [tuple(map(int, range.split('-'))) for range in ranges.splitlines()]
ranges.sort(key=lambda x: x[0])

i = 0
merged = []
while i < len(ranges):
  l1, r1 = ranges[i]

  for j in range(i+1, len(ranges)):
    l2, r2 = ranges[j]
    if r1 >= l2:
      i += 1
      r1 = max(r1, r2)
    else:
      break

  i += 1
  merged.append((l1, r1))

print(sum(r - l + 1 for l, r in merged))
