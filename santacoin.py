key = 'yzbqklnj'

from hashlib import md5

i = 0
found = False

while 1:
    hsh = md5()
    hsh.update(key + str(i))
    print "\r", i,
    if not found and hsh.hexdigest().startswith('00000'):
        print
        found = True
    if hsh.hexdigest().startswith('000000'):
        break
    i += 1
