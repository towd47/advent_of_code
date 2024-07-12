import readInput

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
    return


lines = readInput.yieldLines("8")

turns = next(lines)
turns = turns.strip()
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
    if node[2] == "A":
        p2StartNodes.append(node)

part1(turns, nodes)