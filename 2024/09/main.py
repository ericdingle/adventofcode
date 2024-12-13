data = open('input.txt').read()[:-1]
data = [*map(int, list(data))]

def get_disk():
  disk = []
  for i, val in enumerate(data):
    if i % 2 == 0:
      disk.extend([i // 2] * val)
    else:
      disk.extend([-1] * val)
  return disk

# Part 1
disk = get_disk()

start = disk.index(-1)
end = len(disk) - 1

while start < end:
  disk[start] = disk[end]
  disk[end] = -1

  start = disk.index(-1, start + 1)
  while disk[end] == -1:
    end -= 1

print(sum(i * val for i, val in enumerate(disk) if val != -1))

# Part 2
disk = get_disk()

def find_seq(val, start, step):
  i = start
  while disk[i] != val:
    i += step
  start = i
  while disk[i] == val:
    i += step
    if not (0 <= i < len(disk)):
      return (-1, 0)
  return (min(start, i+1), abs(i - start))

val = disk[-1]
end = len(disk) - 1

while val >= 0:
  end, len2 = find_seq(val, end, -1)

  start, len1 = 0, 0
  while True:
    start, len1 = find_seq(-1, start + len1, 1)
    if start == -1 or len1 >= len2:
      break

  if start != -1 and start < end:
    for i in range(len2):
      disk[start + i] = disk[end + i]
      disk[end + i] = -1

  val -= 1

print(sum(i * val for i, val in enumerate(disk) if val != -1))
