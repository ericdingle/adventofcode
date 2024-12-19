def run(filename):
  a, b, c, _, program = open(filename).read().splitlines()

  a = int(a.split()[-1])
  b = int(b.split()[-1])
  c = int(c.split()[-1])
  program = [*map(int, program.split()[1].split(','))]

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
      num = a
      den = pow(2, combo(operand))
      a = num // den
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
      num = a
      den = pow(2, combo(operand))
      b = num // den
    elif opcode == 7:  # cdv
      num = a
      den = pow(2, combo(operand))
      c = num // den
    else:
      raise Exception('Unknown opcode: %d' % opcode)

    if opcode != 3:  # jnz
      pc += 2

  return ','.join([*map(str, out)])

print(run('input.txt'))
#print(run('input2.txt'))
