from readInput import yieldLines
import sys

def solve(filename='24'):
    lines = yieldLines(filename)

    vals = {}
    while (line := next(lines)) != '\n':
        line = line.strip()
        wire, val = line.split(': ')
        vals[wire] = int(val)

    gates = []
    for line in lines:
        line = line.strip()
        ins, out = line.split(' -> ')
        ins = ins.split()
        gates.append((ins, out))

    p1(vals, gates)

def p1(vals, gates):
    while gates:
        gate = gates.pop(0)
        ins, out = gate
        if ins[0] in vals and ins[2] in vals:
            vals[out] = doOp(ins, vals)
        else:
            gates.append(gate)

    zVals = [v for v in vals if v.startswith('z')]
    zVals.sort()
    zVals.reverse()
    b = ''.join([str(vals[v]) for v in zVals])
    print(int(b, 2))

def doOp(ins, vals):
    v1 = ins[0]
    v2 = ins[2]
    match ins[1]:
        case 'OR':
            return vals[v1] or vals[v2]
        case 'AND':
            return vals[v1] and vals[v2]
        case 'XOR':
            return vals[v1] ^ vals[v2]

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
