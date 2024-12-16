from readInput import yieldLines
import sys
import re
from sympy import Eq, symbols 
from sympy import solve as solveEq
from sympy import Integer as symInt

def solve(filename='13'):
    machines = []

    lines = yieldLines(filename)
    
    machine = []
    for line in lines:
        if line != "\n":
            machine.append(re.findall(r'(\d+)', line))
        else:
            machine = [[int(x) for x in p] for p in machine]
            machines.append(machine)
            machine = []
    if machine:
        machine = [[int(x) for x in p] for p in machine]
        machines.append(machine)

    tot = 0
    for machine in machines:
        res = solveMachine(machine)
        if res:
            tot += 3 * res[0] + res[1]
    print(tot)

    tot = 0
    for machine in machines:
        machine[2] = [machine[2][0] + 10000000000000, machine[2][1] + 10000000000000]
        res = solveMachine(machine)
        if res:
            tot += 3 * res[0] + res[1]
    print(tot)

def solveMachine(m):
    x, y = symbols('x y')
    eq1 = Eq(m[0][0] * x + m[1][0] * y, m[2][0])
    eq2 = Eq(m[0][1] * x + m[1][1] * y, m[2][1])
    res = solveEq((eq1, eq2), (x, y))
    if not res or type(res[x]) != symInt or type(res[y]) != symInt:
        return None
    return res[x], res[y]

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
