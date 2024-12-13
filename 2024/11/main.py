data = [*map(int, open('input.txt').read().split())]

def run(data):
  out = []
  for i in data:
    if i == 0:
      out.append(1)
    elif len(s := str(i)) % 2 == 0:
      j = len(s) // 2
      out.extend([int(s[:j]), int(s[j:])])
    else:
      out.append(i * 2024)
  return out

for i in range(25):
  data = run(data)

print(len(data))
