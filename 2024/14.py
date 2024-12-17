from readInput import yieldLines
import sys
import re

def solve(filename='14'):
    bots = []
    for line in yieldLines(filename):
        bot = [int(v) for v in re.findall(r'(-?\d+)', line)]
        bots.append(bot)

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    xmid = 50
    ymid = 51
    # xmid = 5
    # ymid = 3
    for bot in bots:
        x, y = calcPos(bot, 100)
        if x < xmid:
            if y < ymid:
                q1 += 1
            elif y > ymid:
                q2 += 1
        elif x > xmid:
            if y < ymid:
                q3 += 1
            elif y > ymid:
                q4 += 1
    print(q1*q2*q3*q4)

    steps = 0
    while True:
        bots = doStep(bots)
        steps += 1
        bottomHalf = set()
        leftHalf = set()
        for bot in bots:
            if bot[1] > 51:
                bottomHalf.add((bot[0], bot[1]))
            if bot[0] < 50:
                leftHalf.add((bot[0], bot[1]))
        if len(bottomHalf) < len(bots) / 3 and len(leftHalf) < len(bots) / 3:
            printBots(bots)
            print(steps)
            break

def printBots(bots):
    line = ['.' for _ in range(101)] 
    grid = [line.copy() for _ in range(103)] 
    for bot in bots:
        grid[bot[1]][bot[0]] = '#'
    for line in grid:
        print("".join(line))

def doStep(bots):
    for bot in bots:
        x, y = calcPos(bot, 1)
        bot[0] = x
        bot[1] = y
    return bots

def calcPosA(bot, steps):
    xpos = (bot[0] + bot[2] * steps) % 11
    ypos = (bot[1] + bot[3] * steps) % 7
    if xpos < 0:
        xpos = 11 + xpos
    if ypos < 0:
        ypos = 7 + ypos
    return xpos, ypos

def calcPos(bot, steps):
    xpos = (bot[0] + bot[2] * steps) % 101
    ypos = (bot[1] + bot[3] * steps) % 103
    if xpos < 0:
        xpos = 101 + xpos
    if ypos < 0:
        ypos = 103 + ypos
    return xpos, ypos



if __name__ == '__main__':
    solve()
