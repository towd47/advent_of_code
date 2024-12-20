from readInput import yieldLines
import sys

def solve(filename='19'):
    lines = yieldLines(filename)
    line = next(lines)
    patterns = set([pattern for pattern in line.strip().split(', ')])
    
    next(lines)
    goals = [line.strip() for line in lines]
    
    possible = 0
    tot = 0
    for goal in goals:
        poss = solvable(goal, patterns)
        if poss > 0:
            possible += 1
        tot += poss
    print(possible)
    print(tot)

def solvable(goal, patterns):
    possibilities = []
    poses = dict()
    poses[0] = 1
    for i, _ in enumerate(goal):
        if i not in poses:
            continue

        for p in patterns:
            if goal[i:].startswith(p):
                newPos = i + len(p)
                if newPos in poses:
                    poses[newPos] += poses[i]
                else:
                    poses[newPos] = poses[i]
    if len(goal) in poses:
        return poses[len(goal)]
    return 0

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
