with open('lights.txt') as f:
    lights = [l.strip() for l in f.readlines()]


grid = [[0 for x in range(0, 1000)] for y in range(0, 1000)]
newgrid = [[0 for x in range(0, 1000)] for y in range(0, 1000)]


def direction(value):
    if value == 'on':
        return 1
    if value == 'off':
        return -1
    return 0


def instruction(value):
    result = {}
    value = value.replace('turn ', '')
    x, start, _, end = value.split(' ')
    result['direction'] = direction(x)
    result['start'] = map(int, start.split(','))
    result['end'] = map(int, end.split(','))
    return result


instructions = map(instruction, lights)

for n in instructions:
    for x in range(n['start'][0], n['end'][0] + 1):
        for y in range(n['start'][1], n['end'][1] + 1):
            if n['direction'] == 0:
                grid[x][y] = (grid[x][y] + 1) % 2
                newgrid[x][y] += 2
            if n['direction'] == 1:
                grid[x][y] = True
                newgrid[x][y] += 1
            if n['direction'] == -1:
                grid[x][y] = False
                if newgrid[x][y] > 0:
                    newgrid[x][y] -= 1

print sum(map(sum, grid))
print sum(map(sum, newgrid))
