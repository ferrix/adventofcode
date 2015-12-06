with open('wrapping.txt') as lines:
    presents = lines.readlines()

presents = [sorted(map(int, x.strip().split('x'))) for x in presents]
areas = [sorted([x[0] * x[1], x[1] * x[2], x[0] * x[2]]) for x in presents]
area = [2 * sum(x) + min(x) / 2 for x in areas]
print sum(area)

ribbon = [[x[0] * x[1] * x[2], 2 * x[0] + 2 * x[1]] for x in presents]
print sum((sum(x) for x in ribbon))
