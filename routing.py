current = [0, 0]
coord = [(0, 0)]
twocurrent = [[0, 0], [0, 0]]
twocoord = [(0, 0), (0, 0)]

with open('routing.txt') as inp:
    directions = inp.read().strip()

for i, d in enumerate(directions):
    bcur = twocurrent[i % 2]
    if d == 'v':
        current[0] += 1
        bcur[0] += 1
    elif d == '^':
        current[0] -= 1
        bcur[0] -= 1
    elif d == '<':
        current[1] -= 1
        bcur[1] -= 1
    elif d == '>':
        current[1] += 1
        bcur[1] += 1
    else:
        continue

    coord.append(tuple(current))
    twocoord.append(tuple(bcur))

print len(set(coord))
print len(set(twocoord))
