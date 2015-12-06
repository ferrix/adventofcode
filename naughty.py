import os


def debug(text):
    if 'DEBUG' in os.environ:
        print text

with open('naughty.txt') as n:
    words = [x.strip() for x in n.readlines()]

nice = []
renice = []

for w in words:
    if 'ab' in w or 'cd' in w or 'pq' in w or 'xy' in w:
        continue

    if ((w.count('a') + w.count('e') + w.count('i') + w.count('o') +
         w.count('u')) < 3):
        continue

    prev = w[0]

    for l in w[1:]:
        if l == prev:
            nice.append(w)
            break
        prev = l

print len(nice)

for w in words:
    pairs = set([w[i - 1] + w[i] for i in range(1, len(w))])
    twice = False
    for pair in pairs:
        if pair in w.replace(pair, '_', 1):
            debug(pair + ' ' + w.replace(pair, '_' + pair + '_'))
            twice = True

    if not twice:
        continue

    prev = w[1]
    pprev = w[0]

    for l in w[2:]:
        if l == pprev:
            debug('{}{}{} '.format(l, prev, pprev) +
                  w.replace('{}{}{}'.format(l, prev, pprev),
                            '_{}{}{}_'.format(l, prev, pprev)))
            renice.append(w)
            break
        pprev = prev
        prev = l

print len(renice)
