def read_input(filename):
  a, b, c, _, program = open(filename).read().splitlines()

  a = int(a.split()[-1])
  b = int(b.split()[-1])
  c = int(c.split()[-1])
  program = [*map(int, program.split()[1].split(','))]

  return a, b, c, program

def run(a, b, c, program):
  def combo(operand):
    if 0 <= operand <= 3:
      return operand
    elif operand == 4:
      return a
    elif operand == 5:
      return b
    elif operand == 6:
      return c
    raise Exception('Invalid operand: %d' % operand)

  pc = 0
  out = []

  while pc < len(program):
    opcode, operand = program[pc:pc+2]

    if opcode == 0:  # adv
      a = a >> combo(operand)
    elif opcode == 1:  # bxl
      b = b ^ operand
    elif opcode == 2:  # bst
      b = combo(operand) % 8
    elif opcode == 3:  # jnz
      pc = pc + 2 if a == 0 else operand
    elif opcode == 4:  # bxc
      b = b ^ c
    elif opcode == 5:  # out
      out.append(combo(operand) % 8)
    elif opcode == 6:  # bdv
      b = a >> combo(operand)
    elif opcode == 7:  # cdv
      c = a >> combo(operand)
    else:
      raise Exception('Unknown opcode: %d' % opcode)

    if opcode != 3:  # jnz
      pc += 2

  return out

def part1(filename):
  a, b, c, program = read_input(filename)
  out = run(a, b, c, program)
  return ','.join([*map(str, out)])

print(part1('input.txt'))
#print(part1('input3.txt'))

def part2(filename):
  _, b, c, program = read_input(filename)
  l = len(program)

  def traverse(a, depth):
    if depth == l:
      return a

    a = a << 3
    for i in range(8):
      out = run(a + i, b, c, program)
      if out == program[l - depth - 1:]:
        a2 = traverse(a + i, depth + 1)
        if a2 != -1:
          return a2

    return -1

  return traverse(0, 0)

print(part2('input2.txt'))
#print(part2('input3.txt'))
