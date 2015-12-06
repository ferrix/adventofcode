with open('floors.txt') as fl:
    floors = fl.read().strip()

pos = 0
basement = None

for i, f in enumerate(floors):
    if f == '(':
        pos += 1
    elif f == ')':
        pos -= 1
    else:
        continue

    if basement is None and pos == -1:
        basement = i + 1

print pos
print basement
