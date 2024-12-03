lhs, rhs = zip(*[map(int, line.split()) for line in open('input.txt')])

lhs, rhs = sorted(lhs), sorted(rhs)

print(sum(abs(l - r) for l, r in zip(lhs, rhs)))

print(sum(i * rhs.count(i) for i in lhs))
