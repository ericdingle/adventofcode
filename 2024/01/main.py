f = open('input.txt', 'r')

lhs, rhs = zip(*[map(int, line.split()) for line in f])

lhs, rhs = sorted(lhs), sorted(rhs)

print(sum(abs(l - r) for l, r in zip(lhs, rhs)))

print(sum(i * rhs.count(i) for i in lhs))
