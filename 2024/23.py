from readInput import yieldLines
import sys

def solve(filename='23'):
    lines = yieldLines(filename)
    comps = {}
    for line in lines:
        line = line.strip()
        c1, c2 = line.split('-')
        if c1 in comps:
            comps[c1].add(c2)
        else:
            comps[c1] = set([c2])
        if c2 in comps:
            comps[c2].add(c1)
        else:
            comps[c2] = set([c1])

    p1(comps)
    p2(comps)

def p1(comps):
    trios = set()
    for comp in comps:
        connected = comps[comp]
        for c in connected:
            con2 = comps[c]
            for c2 in con2:
                if comp in comps[c2]:
                    trio = [comp, c, c2]
                    trio.sort()
                    trios.add(tuple(trio))

    print(sum([trioHasT(trio) for trio in trios]))

def p2(comps):
    sets = set()
    keys = list(comps.keys())
    tested = set()
    foundSets = set()
    for key in keys:
        tested.add(key)
        foundSets.update(generateSets(key, set([key]), tested, foundSets, comps))
    longest = set()
    for s in foundSets:
        if len(s) > len(longest):
            longest = s
    longest = list(longest)
    longest.sort()
    print(",".join(longest))

def generateSets(c, s, tested, foundSets, comps):
    sets = set()
    for con in comps[c]:
        if con in s:
            continue
        valid = True
        for val in s:
            if val not in comps[con]:
                valid = False
                break
        if valid:
            cs = s.copy()
            if frozenset(cs) not in foundSets:
                foundSets.add(frozenset(cs))
                cs.add(con)
                sets.update(generateSets(con, cs, tested, foundSets, comps))
    if not sets:
        sets.add(frozenset(s))
    return sets

def trioHasT(trio):
    for c in trio:
        if c.startswith('t'):
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
