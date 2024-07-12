import readInput

def calcDist(t, ttot):
    return t * (ttot - t)

def numWinning(race):
    t, d = race
    count = 0
    for i in range(t):
        if calcDist(i, t) > d:
            count += 1
    return count

def p1(races):
    numWays = 1
    for race in races:
        numWays = numWays * numWinning(race)
    return numWays

lines = readInput.yieldLines("6")

times = [int(x) for x in next(lines).split(":")[1].split()]
distances = [int(x) for x in next(lines).split(":")[1].split()]

t2 = int("".join([str(x) for x in times]))
d2 = int("".join([str(x) for x in distances]))

races = list(zip(times, distances))

print(p1(races))
print(p1([(t2, d2)]))
