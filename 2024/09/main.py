data = open('input.txt').read()[:-1]
data = [*map(int, list(data))]

disk = []
for i, val in enumerate(data):
  if i % 2 == 0:
    disk.extend([i // 2] * val)
  else:
    disk.extend([-1] * val)

start = disk.index(-1)
end = len(disk) - 1

while start < end:
  disk[start] = disk[end]
  disk[end] = -1

  start = disk.index(-1, start + 1)
  while disk[end] == -1:
    end -= 1

print(sum(i * val for i, val in enumerate(disk) if val != -1))
