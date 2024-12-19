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
    for p in patterns:
        if goal == p:
            return True
        if goal.startswith(p):
            possibilities.append((goal[len(p):], patterns))
    for p in possibilities:
        if solvable(p[0], p[1]):
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
