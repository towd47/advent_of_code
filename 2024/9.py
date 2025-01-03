from readInput import oneString
import sys

def solve(filename='9'):
    diskmap = oneString(filename)
    diskmap = [int(c) for c in diskmap.strip()]
    p1(diskmap)
    p2(diskmap)

def p1(diskmap):
    emptyposes = []
    existingposes = []
    diskvals = []

    for i, e in enumerate(diskmap):
        if i % 2 == 0:
            block = [int(i/2), e]
            diskvals.append(block)
            existingposes.append(i)
        else:
            diskvals.append([None,e])
            emptyposes.append(i)

    i = 0
    while i < len(diskvals):
        if diskvals[i][0] != None:
            i += 1
            continue

        met = False
        while not met and i < len(diskvals):
            last = diskvals[-1]
            if last[0] == None or last[1] == 0:
                diskvals.pop()
            elif last[1] >= diskvals[i][1]:
                diskvals[i][0] = last[0]
                diskvals[-1][1] -= diskvals[i][1]
                met = True
            else:
                diff = diskvals[i][1] - last[1]
                diskvals[i][1] = diff
                diskvals.insert(i, [last[0], last[1]])
                diskvals.pop()
                i += 1
        i += 1

    pos = 0
    tot = 0
    for i, e in enumerate(diskvals):
        tot += sum([e[0] * i for i in range(pos, pos + e[1])])
        pos += e[1]

    print(tot)

def p2(diskmap):
    emptyposes = []
    existingposes = []
    diskvals = []

    for i, e in enumerate(diskmap):
        if i % 2 == 0:
            block = [int(i/2), e]
            diskvals.append(block)
            existingposes.append(i)
        else:
            diskvals.append([None,e])
            emptyposes.append(i)

    existingposes.reverse()
    p = 0
    while p < len(existingposes):
        pos = existingposes[p]
        p += 1
        for i, epos in enumerate(emptyposes):
            if epos >= pos or epos >= len(diskvals):
                break
            diff = diskvals[epos][1] - diskvals[pos][1]
            if diff > 0:
                diskvals[epos][1] = diff
                movedVal = diskvals[pos]
                diskvals[pos] = [None, diskvals[pos][1]] 
                diskvals.insert(epos, movedVal)
                emptyposes = emptyposes[:i] + [x + 1 for x in emptyposes[i:]]
                existingposes = [x + 1 if x >= epos else x for x in existingposes]
                break
            elif diff == 0:
                diskvals[epos] = diskvals[pos]
                diskvals[pos] = [None, diskvals[pos][1]]
                del emptyposes[i]
                break
    
    pos = 0
    tot = 0
    for i, e in enumerate(diskvals):
        tot += sum([e[0] * i if e[0] != None else 0 for i in range(pos, pos + e[1])])
        pos += e[1]

    print(tot)

'''
    while (emptypos := emptyposes.pop(0)) and emptypos < existingposes[-1]:
        flag = True
        offset = 0
        while flag:
            lastpos = existingposes[-1]
            v1 = diskvals[emptypos + offset][1]
            if v1 >= diskvals[lastpos][1]:
                diskvals[emptypos + offset][1] = v1 - diskvals[lastpos+offset][1]
                if diskvals[emptypos + offset][1] == 0:
                    flag = False
                    diskvals[emptypos + offset] = diskvals[lastpos+offset]
                else:
                    diskvals.insert(emptypos + offset, diskvals[lastpos+offset])
                    offset += 1
                existingposes.pop()
            else:
                diskvals[emptypos + offset] = [diskvals[lastpos+offset][0], v1]
                diskvals[lastpos + offset][1] = diskvals[lastpos + offset][1] - v1
                flag = False

    tot = 0
    pos = 0
    print(diskvals[:10])
    for i, e in enumerate(diskvals):
        tot += sum([e[0] * i for i in range(pos, pos + e[1])])
        pos += e[1]

    print(tot)
'''



if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        solve(filename)
    else:
        solve()
