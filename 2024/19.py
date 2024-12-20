from readInput import yieldLines
import sys

def solve(filename='19'):
    lines = yieldLines(filename)
    line = next(lines)
    patterns = set([pattern for pattern in line.strip().split(', ')])
    
    next(lines)
    goals = [line.strip() for line in lines]
    
    print(sum([solvable(goal, patterns) for goal in goals]))

def solvable(goal, patterns):
    possibilities = []
    poses = set()
    poses.add(0)
    for i, _ in enumerate(goal):
        if i not in poses:
            continue

        for p in patterns:
            if goal[i:] == p:
                return True
            if goal[i:].startswith(p):
                poses.add(i + len(p))
    return False

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
