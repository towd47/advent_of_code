import readInput

def p1(lines):
    return sum(map(possibleArrangements, lines))

def p2(lines):
    return sum(map(possibleArrangements2, lines))

def possibleArrangements(line):
    springs, broken = line.split()
    broken = [int(x) for x in broken.split(",")]
    springs = springs.strip(".")
    springs = ".".join([x for x in springs.split(".") if x])
    val = allPossibilities(springs, broken)
    return val

def possibleArrangements2(line):
    springs, broken = line.split()
    broken = [int(x) for x in broken.split(",")]
    broken = broken * 5
    newsprings = list(springs)
    for _ in range(4):
        newsprings.append("?")
        newsprings.extend(springs)
    newsprings = "".join(newsprings)
    val = allPossibilities(newsprings, broken)
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

    counts = countPossibilitiesV2(ranges, broken, brokenposes)
    _, x = list(zip(*counts))
    total = sum(x)

    return total

def countPossibilitiesV2(ranges, broken, brokenposes):
    if len(ranges) == 1:
        return list(zip(ranges[0], [1] * len(ranges[0])))
    
    prev_poss = countPossibilitiesV2(ranges[1:], broken[1:], brokenposes)
    counts = []
    for x in ranges[0]:
        b = broken[0]
        tot = 0
        for p in prev_poss:
            if x + b >= p[0]:
                continue
            valid = True
            for bp in brokenposes:
                if bp >= x + b and bp < p[0]:
                    valid = False
                    break
            if not valid:
                break
            tot += p[1]
        counts.append(tot)
    return list(zip(ranges[0], counts))

def countPossibilities(start, ranges, broken, brokenposes):
    total = 0
    for x in ranges[0]:
        if len(ranges) == 1:
            if checkValid(start + [x], broken, brokenposes):
                total += 1
        else:
            total += countPossibilities(start + [x], ranges[1:], broken, brokenposes)
    return total
    
    
def checkValid(possibility, broken, brokenposes):
    for i in range(len(possibility) - 1):
        if possibility[i] + broken[i] >= possibility[i+1]:
            return False
    for x in brokenposes:
        found = False
        for a, b in zip(possibility, broken):
            if x >= a and x < a + b:
                found = True
                break
        if not found:
            return False
    return True


if __name__ == "__main__":
    lines = readInput.linesToList("12")
    print(p1(lines))
    print(p2(lines))