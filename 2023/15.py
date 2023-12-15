import readInput

def readInitSeq(f):
    lines = readInput.yieldLines(f)
    line = next(lines)
    line = line.strip()
    steps = line.split(",")
    return steps

def p1(hashes):
    tot = 0
    for s in hashes:
        tot += hashStr(s)
    print(tot)

def hashStr(s):
    tot = 0
    for c in s:
        tot += ord(c)
        tot *= 17
        tot = tot % 256
    return tot

def p2(steps):
    boxes = dict()
    for x in steps:
        if x[-1] == "-":
            label = x[:-1]
            box = hashStr(label)
            if box in boxes:
                boxes[box] = [(x, _) for (x, _) in boxes[box] if x != label]
        else:
            label = x[:-2]
            box = hashStr(label)
            if box in boxes:
                replaced = False
                for i, e in enumerate(boxes[box]):
                    if e[0] == label:
                        boxes[box][i] = (label, int(x[-1]))
                        replaced = True
                        break
                if not replaced:
                    boxes[box].append((label, int(x[-1])))
            else:
                boxes[box] = [(label, int(x[-1]))]
    tot = 0
    for box in boxes:
        tot += findBoxFocusingPower(boxes[box], box)

    print(tot)

def findBoxFocusingPower(box, boxNum):
    tot = 0
    for i, e in enumerate(box, 1):
        tot += (boxNum + 1) * i * e[1]
    return tot

def solve():
    steps = readInitSeq("15")
    p1(steps)
    p2(steps)

if __name__ == "__main__":
    solve()