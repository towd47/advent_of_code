from readInput import yieldLines
from coord import Coord
import sys

def solve(filename = '20'):
    track = set()

    lines = yieldLines(filename)
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == '.':
                track.add(Coord(row, col))
            elif val == 'S':
                track.add(Coord(row, col))
                startpt = Coord(row, col)
            elif val == 'E':
                track.add(Coord(row, col))
                endpt = Coord(row, col)
    
    trackOrder = [startpt]
    trackSoFar = set()
    pt = startpt
    while pt != endpt:
        trackSoFar.add(pt)
        adj = pt.adjacent()
        for a in adj:
            if a in track and a not in trackSoFar:
                trackOrder.append(a)
                pt = a
                break

    print(countCheats(trackOrder, 2, 100))
    print(countCheats(trackOrder, 20, 100))
    
def countCheats(trackOrder, cheatDist, cheatMin):
    cheats = 0
    trackIndex = dict()
    for i, p in enumerate(trackOrder):
        trackIndex[p] = i

    for i, p in enumerate(trackOrder[:-100]):
        for j, p2 in enumerate(trackOrder[i+100:]):
            dist = p.mDist(p2)
            cutLen = trackIndex[p2] - i - dist
            if dist <= cheatDist and cutLen >= cheatMin:
                cheats += 1

    return cheats

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
