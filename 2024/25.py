from readInput import yieldLines

def solve():
    lines = yieldLines('25')
    keys = []
    locks = []
    obj = []
    for line in lines:
        line = line.strip()
        if not line:
            isLock = obj[0][0] == '#'
            obj = list(zip(*obj))
            vals = []
            for l in obj:
                vals.append(len([c for c in l if c == '#']) - 1)
            if isLock:
                locks.append(vals)
            else:
                keys.append(vals)
            obj = []
        else:
            obj.append(line)
    isLock = obj[0][0] == '#'
    obj = list(zip(*obj))
    vals = []
    for l in obj:
        vals.append(len([c for c in l if c == '#']) - 1)
    if isLock:
        locks.append(vals)
    else:
        keys.append(vals)

    combos = 0
    for lock in locks:
        for key in keys:
            if checkKey(key, lock):
                combos += 1
    print(combos)

def checkKey(key, lock):
    for (k, l) in zip(key, lock):
        if k+l > 5:
            return False
    return True


if __name__ == '__main__':
    solve()
