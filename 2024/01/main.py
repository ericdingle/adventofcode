f = open('input.txt', 'r')

lhs, rhs = zip(*[map(int, line.split('   ')) for line in f])

lhs, rhs = sorted(lhs), sorted(rhs)

print(sum([abs(lhs[i] - rhs[i]) for i in range(len(lhs))]))

print(sum([i * rhs.count(i) for i in lhs]))
