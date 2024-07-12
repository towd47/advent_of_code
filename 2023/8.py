import readInput
import math

def part1(turns, nodes):
    currentNode = "AAA"
    steps = 0
    while currentNode != "ZZZ":
        instruction = turns[steps % len(turns)]
        if instruction == "L":
            currentNode = nodes[currentNode][0]
        else:
            currentNode = nodes[currentNode][1]
        steps += 1
    print(steps)

def part2(turns, nodes, startNodes):
<<<<<<< HEAD
    return


lines = readInput.yieldLines("8")
=======
    zs = []
    for cn in startNodes:
        z = findPattern(turns, nodes, cn)
        zs.append(z)
    print(math.lcm(*zs))
>>>>>>> 65135535f46716d7ac010ebe3ecfd179ff2fadd4


def findPattern(turns, nodes, cn):
    steps = 0
    while cn[-1] != "Z":
        instruction = turns[steps % len(turns)]
        if instruction == "L":
            cn = nodes[cn][0]
        else:
            cn = nodes[cn][1]
        steps += 1
    return steps

def solve():

    lines = readInput.yieldLines("8")

    turns = next(lines).strip()
    next(lines)

    nodes = dict()
    p2StartNodes = []
    for line in lines:
        line = line.strip()
        node, nextNodes = line.split(" = ")
        next1, next2 = nextNodes.split(", ")
        next1 = next1.lstrip("(")
        next2 = next2.rstrip(")")

        nodes[node] = (next1, next2)
        if node[-1] == "A":
            p2StartNodes.append(node)

    part1(turns, nodes)
    part2(turns, nodes, p2StartNodes)

if __name__ == "__main__":
    solve()
