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
    
    print(len(track))
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
    print('Finished track')

    adjDict = {}
    for i, p in enumerate(trackOrder):
        adjDict[p] = []
        dist2 = p.coordsAtDist(2)
        for c in dist2:
            if c in track:
                distSaved = trackOrder.index(c) - i - 2
                if distSaved > 0:
                    adjDict[p].append((c, distSaved))

    cheatsFor100Plus = 0
    for p in adjDict:
        for cheat in adjDict[p]:
            if cheat[1] >= 100:
                cheatsFor100Plus += 1

    print(cheatsFor100Plus)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
