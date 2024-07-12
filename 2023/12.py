import readInput

def p1(lines):
    return sum(map(possibleArrangements, lines))

def possibleArrangements(line):
    springs, broken = line.split()
    broken = [int(x) for x in broken.split(",")]
    springs = springs.strip(".")
    springs = ".".join([x for x in springs.split(".") if x])
    val = allPossibilities(springs, broken)
    print(springs, broken, val)
    return val

def allPossibilities(springs, broken):
    ranges = []
    for i, e in enumerate(broken):
        if i == 0:
            start = 0
        else:
            start = sum(broken[:i]) + i
        if i == len(broken) - 1:
            end = len(springs)
        else:
            end = len(springs) - sum(broken[i+1:]) - len(broken[i+1:])
        
        vals = []
        for j in range(start, end + 1 - e):
            if not '.' in springs[j:j+e] and (j == 0 or springs[j-1] != '#') and (j + e >= len(springs) or springs[j+e] != '#'):
                vals.append(j)
        ranges.append(vals)

    firstBroken = springs.find("#")
    lastBroken = springs.rfind("#")

    brokenposes = []
    for i, e in enumerate(springs):
        if e == '#':
            brokenposes.append(i)
            
    if firstBroken != -1:
        newranges = [x for x in ranges[0] if x <= firstBroken]
        ranges[0] = newranges
        newranges = [x for x in ranges[-1] if x + broken[-1] > lastBroken]
        ranges[-1] = newranges

    return 1

def countPossibilities(r, prev):
    if prev == None:
        return


if __name__ == "__main__":
    lines = readInput.linesToList("tests")
    print(p1(lines))